#!python
import azureml.core
from azureml.core import Workspace
from azureml.core import Datastore
from azureml.core import Experiment
from azureml.core.compute import ComputeTarget
from azureml.contrib.core.compute.k8scompute import AksCompute
from azureml.train.estimator import Estimator
from azureml.contrib.core.k8srunconfig import K8sComputeConfiguration
from azureml.core import ScriptRunConfig
from azureml.contrib.aisc.aiscrunconfig import AISuperComputerConfiguration

import os
import sys
import pprint
import argparse

def submit_ITP(
        subscription_id, resource_group, workspace_name, cluster_name, gpus,
        blob_datastore_name, blob_container_name, blob_account_name, blob_account_key,
        custom_docker_image,
        experiment_name, workdir, script
    ):
    ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)

    for key, target in ws.compute_targets.items():
        if type(target) is AksCompute:
            print('Found compute target:{}\ttype:{}\tprovisioning_state:{}\tlocation:{}'.format(target.name, target.type, target.provisioning_state, target.location))

    ds = Datastore.register_azure_blob_container(workspace=ws,
                                                 datastore_name=blob_datastore_name,
                                                 container_name=blob_container_name,
                                                 account_name=blob_account_name,
                                                 account_key=blob_account_key,
                                                 create_if_not_exists=False)

    wandb_api = 'aeda6d52585d2c9faa77b95518f4ffc411a3418b'
    source_directory = "./entry-script"
    entry_script = "./entry-script.py"

    # Create estimator object.
    estimator = Estimator(
        compute_target=ComputeTarget(workspace=ws, name=cluster_name),
        custom_docker_image=custom_docker_image,
        use_gpu=True,
        user_managed=True,
        source_directory=source_directory,
        entry_script=entry_script,
        script_params={
        "--workdir": ds.path(workdir).as_mount(),
        "--script": script
        },
        node_count=1,
        process_count_per_node=1,
        environment_variables = {'WANDB_API_KEY':wandb_api}    # for recording experiments with WandB.
    )

    k8sconfig = K8sComputeConfiguration()
    k8s = dict()
    k8s['gpu_count'] = gpus

    k8sconfig.configuration = k8s
    estimator.run_config.cmk8scompute = k8sconfig

    experiment = Experiment(ws, name=experiment_name)
    run = experiment.submit(estimator)
    pprint.pprint(run)

    # uncomment next line to see the stdout in your main.py on local machine.
    # run.wait_for_completion(show_output=True)

virtual_cluster_dict = {
    'msroctovc': {'subscription_id': 'd4404794-ab5b-48de-b7c7-ec1fefb0a04e', 'resource_group': 'gcr-singularity-octo', 'workspace_name': 'msroctows'},
    'msrpilot': {'subscription_id': '46da6261-2167-4e71-8b0d-f4a45215ce61', 'resource_group': 'gcr-singularity', 'workspace_name': 'msrpilotws'},
    'msrresrchvc': {'subscription_id': '22da88f6-1210-4de2-a5a3-da4c7c2a1213', 'resource_group': 'gcr-singularity-resrch', 'workspace_name': 'msrresrchws'},
}

def submit_singularity(
        blob_datastore_name, blob_container_name, blob_account_name, blob_account_key,
        virtual_cluster, instance_type, sla_tier, image_version,
        experiment_name, workdir, script
    ):
    ws = Workspace(**virtual_cluster_dict[virtual_cluster])

    for key, target in ws.compute_targets.items():
        print('Found compute target:{}\ttype:{}\tprovisioning_state:{}\tlocation:{}'.format(target.name, target.type, target.provisioning_state, target.location))

    ds = Datastore.register_azure_blob_container(workspace=ws,
                                                datastore_name=blob_datastore_name,
                                                container_name=blob_container_name,
                                                account_name=blob_account_name,
                                                account_key=blob_account_key,
                                                create_if_not_exists=False)
    data_ref = ds.path(workdir).as_mount()

    source_directory = "./entry-script"
    entry_script = "./entry-script.py"

    target_vc = virtual_cluster
    armid = (
        f"/subscriptions/{ws.subscription_id}/"
        f"resourceGroups/{ws.resource_group}/"
        "providers/Microsoft.MachineLearningServices/"
        f"virtualclusters/{target_vc}"
    )

    src = ScriptRunConfig(source_directory=source_directory,
                            script=entry_script,
                            arguments=[
                                "--workdir", str(data_ref),
                                "--script", script
                            ],
                        )
    src.run_config.data_references = {data_ref.data_reference_name: data_ref.to_config()}
    src.run_config.target = "aisupercomputer"
    src.run_config.aisupercomputer = AISuperComputerConfiguration()
    src.run_config.aisupercomputer.instance_type = instance_type
    src.run_config.aisupercomputer.sla_tier = sla_tier
    src.run_config.aisupercomputer.image_version=image_version
    src.run_config.node_count = 1
    src.run_config.aisupercomputer.scale_policy.auto_scale_interval_in_sec = 36000
    src.run_config.aisupercomputer.scale_policy.max_instance_type_count = 1
    src.run_config.aisupercomputer.scale_policy.min_instance_type_count = 1
    src.run_config.aisupercomputer.virtual_cluster_arm_id = armid

    experiment = Experiment(ws, name=experiment_name)
    run = experiment.submit(src)
    pprint.pprint(run)
