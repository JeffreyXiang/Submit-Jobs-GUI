import os
import sys
import csv
import re
import json

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_MainWindow import *

from submit import *

class ConfigManager:
    def __init__(self, parent=None):
        self.userdata_path = './userdata.json'

        self.cluster_info_title = ['Cluster name', 'VC', 'Total GPUs', 'Region', 'Subscription ID', 'Workspace Name', 'Resource Group', 'Compute']
        self.cluster_info = []
        self.cluster_select = 0
        self.cluster_gpus = 0

        self.singularity_virtual_cluster = 'msroctovc'
        self.singularity_instance_type = None
        self.singularity_sla_tier = 'Basic'

        self.storage_datastore_name = None
        self.storage_container_name = None
        self.storage_account_name = None
        self.storage_account_key = None

        self.environment_docker_image = None

        self.experiment_name = None
        self.experiment_workdir = None
        self.experiment_script = None

        self.load_userdata()

    def save_userdata(self, filename=None):
        if filename is None:
            filename = self.userdata_path
        userdata = {
            'cluster': {
                'info': self.cluster_info,
                'select': self.cluster_select,
                'gpus': self.cluster_gpus,
                'singularity': {
                    'virtual_cluster': self.singularity_virtual_cluster,
                    'instance_type': self.singularity_instance_type,
                    'sla_tier': self.singularity_sla_tier
                }
            },
            'storage': {
                'datastore_name': self.storage_datastore_name,
                'container_name': self.storage_container_name,
                'account_name': self.storage_account_name,
                'account_key': self.storage_account_key,
            },
            'environment': {
                'docker_image': self.environment_docker_image,
            },
            'experiment': {
                'name': self.experiment_name,
                'workdir': self.experiment_workdir,
                'script': self.experiment_script,
            }
        }

        with open(filename, 'w') as f:
            json.dump(userdata, f, indent=4)

    def load_userdata(self, filename=None):
        if filename is None:
            filename = self.userdata_path
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                userdata = json.load(f)
            if 'cluster' in userdata:
                if 'info' in userdata['cluster']:   self.cluster_info = userdata['cluster']['info']
                if 'select' in userdata['cluster']: self.cluster_select = userdata['cluster']['select']
                if 'gpus' in userdata['cluster']:   self.cluster_gpus = userdata['cluster']['gpus']

                if 'singularity' in userdata['cluster']:
                    if 'virtual_cluster' in userdata['cluster']['singularity']: self.singularity_virtual_cluster = userdata['cluster']['singularity']['virtual_cluster']
                    if 'instance_type' in userdata['cluster']['singularity']:   self.singularity_instance_type = userdata['cluster']['singularity']['instance_type']
                    if 'sla_tier' in userdata['cluster']['singularity']:        self.singularity_sla_tier = userdata['cluster']['singularity']['sla_tier']

            if 'storage' in userdata:
                if 'datastore_name' in userdata['storage']: self.storage_datastore_name = userdata['storage']['datastore_name']
                if 'container_name' in userdata['storage']: self.storage_container_name = userdata['storage']['container_name']
                if 'account_name' in userdata['storage']:   self.storage_account_name = userdata['storage']['account_name']
                if 'account_key' in userdata['storage']:    self.storage_account_key = userdata['storage']['account_key']
            
            if 'environment' in userdata:
                if 'docker_image' in userdata['environment']: self.environment_docker_image = userdata['environment']['docker_image']

            if 'experiment' in userdata:
                if 'name' in userdata['experiment']:    self.experiment_name = userdata['experiment']['name']
                if 'workdir' in userdata['experiment']: self.experiment_workdir = userdata['experiment']['workdir']
                if 'script' in userdata['experiment']:  self.experiment_script = userdata['experiment']['script']


    def load_cluster_list_from_file(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.cluster_info = []
        for record in data[2:]:
            raw = re.split('[/&]', record[9])
            subscriptions = raw[raw.index('subscriptions') + 1]
            resourcegroups = raw[raw.index('resourcegroups') + 1]
            workspaces = raw[raw.index('workspaces') + 1]
            compute = raw[raw.index('compute') + 1]
            self.cluster_info.append(
                [record[0], record[1], record[2], record[7], subscriptions, workspaces, resourcegroups, compute])

    def submit_ITP(self):
        submit_ITP(
            self.cluster_info[self.cluster_select][4], self.cluster_info[self.cluster_select][6], self.cluster_info[self.cluster_select][5], self.cluster_info[self.cluster_select][7], self.cluster_gpus,
            self.storage_datastore_name, self.storage_container_name, self.storage_account_name, self.storage_account_key,
            self.environment_docker_image,
            self.experiment_name, self.experiment_workdir, self.experiment_script
        )

    def submit_singularity(self):
        submit_singularity(
            self.storage_datastore_name, self.storage_container_name, self.storage_account_name, self.storage_account_key,
            self.singularity_virtual_cluster, self.singularity_instance_type, self.singularity_sla_tier, self.environment_docker_image,
            self.experiment_name, self.experiment_workdir, self.experiment_script
        )


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tableWidget_cluster.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_cluster.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget_cluster.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.actionSave_Config.triggered.connect(self.save_config_slot)
        self.actionLoad_Config.triggered.connect(self.load_config_slot)
        self.actionAuthor_Info.triggered.connect(self.about_this_slot)

        # ITP
        self.pushButton_clusterlist.clicked.connect(self.load_cluster_list_slot)
        self.comboBox_clustername.activated.connect(self.select_cluster_slot)
        self.spinBox_gpus.valueChanged.connect(self.set_gpus_slot)

        # Singularity
        self.comboBox_singularityvirtualcluster.activated.connect(self.set_singularity_virtual_cluster_slot)
        self.lineEdit_singularityinstancetype.textEdited.connect(self.set_singularity_instance_type_slot)
        self.comboBox_singularityslatier.activated.connect(self.set_singularity_sla_tier_slot)
        self.label_singularityhelp.linkActivated.connect(QDesktopServices.openUrl)

        self.lineEdit_accountname.textEdited.connect(self.set_account_name_slot)
        self.lineEdit_containername.textEdited.connect(self.set_container_name_slot)
        self.lineEdit_datastorename.textEdited.connect(self.set_datastore_name_slot)
        self.lineEdit_accountkey.textEdited.connect(self.set_account_key_slot)
        self.lineEdit_dockerimage.textEdited.connect(self.set_docker_image_slot)
        self.lineEdit_expname.textEdited.connect(self.set_expname_slot)
        self.lineEdit_workdir.textEdited.connect(self.set_workdir_slot)
        self.textEdit_script.textChanged.connect(self.set_script_slot)
        self.pushButton_submit.clicked.connect(self.submit_slot)

        self.config = ConfigManager()
        self.load_userdata()

        sys.stdout = self
        sys.stderr = self

    def write(self, text):
        self.textBrowser_output.insertPlainText(text)

    def closeEvent(self, event):
        self.save_userdata()

    def save_userdata(self, filename=None):
        self.config.save_userdata(filename)

    def load_userdata(self, filename=None):
        self.config.load_userdata(filename)
        self.show_cluster_list()
        self.comboBox_clustername.setCurrentIndex(self.config.cluster_select)
        self.spinBox_gpus.setValue(self.config.cluster_gpus)
        self.comboBox_singularityvirtualcluster.setCurrentText(self.config.singularity_virtual_cluster)
        self.lineEdit_singularityinstancetype.setText(self.config.singularity_instance_type)
        self.comboBox_singularityslatier.setCurrentText(self.config.singularity_sla_tier)
        self.lineEdit_accountname.setText(self.config.storage_account_name)
        self.lineEdit_containername.setText(self.config.storage_container_name)
        self.lineEdit_datastorename.setText(self.config.storage_datastore_name)
        self.lineEdit_accountkey.setText(self.config.storage_account_key)
        self.lineEdit_dockerimage.setText(self.config.environment_docker_image)
        self.lineEdit_expname.setText(self.config.experiment_name)
        self.lineEdit_workdir.setText(self.config.experiment_workdir)
        self.textEdit_script.setText(self.config.experiment_script)

    def show_cluster_list(self):
        self.tableWidget_cluster.clear()
        self.tableWidget_cluster.setRowCount(len(self.config.cluster_info))
        self.tableWidget_cluster.setColumnCount(len(self.config.cluster_info_title))
        self.tableWidget_cluster.setHorizontalHeaderLabels(self.config.cluster_info_title)
        self.comboBox_clustername.clear()
        for i in range(len(self.config.cluster_info)):
            item = self.config.cluster_info[i]
            self.comboBox_clustername.addItem(item[0])
            for j in range(len(item)):
                item = QTableWidgetItem(str(self.config.cluster_info[i][j]))
                self.tableWidget_cluster.setItem(i, j, item)

    def load_cluster_list_from_file(self, filename):
        self.config.load_cluster_list_from_file(filename)
        self.show_cluster_list()

    """=============== SLOTS ==============="""

    def save_config_slot(self):
        filename = QFileDialog.getSaveFileName(self, caption='Select a location to save the config', filter='JSON Files (*.json)')
        filename = filename[0]
        if filename != '':
            self.save_userdata(filename)

    def load_config_slot(self):
        filename = QFileDialog.getOpenFileName(self, caption='Select the config file', filter='JSON Files (*.json)')
        filename = filename[0]
        if filename != '':
            self.load_userdata(filename)

    def about_this_slot(self):
        QMessageBox.information(self, "About this", "Author: Jianfeng Xiang\nEmail: v-jxiang@microsoft.com", QMessageBox.Yes, QMessageBox.Yes)

    def load_cluster_list_slot(self):
        filename = QFileDialog.getOpenFileName(self, caption='Select the cluster list file', filter='CSV Files (*.csv)')
        filename = filename[0]
        if filename != '':
            self.load_cluster_list_from_file(filename)

    def select_cluster_slot(self):
        self.config.cluster_select = self.comboBox_clustername.currentIndex()

    def set_gpus_slot(self):
        self.config.cluster_gpus = self.spinBox_gpus.value()

    def set_singularity_virtual_cluster_slot(self):
        self.config.singularity_virtual_cluster = self.comboBox_singularityvirtualcluster.currentText()

    def set_singularity_instance_type_slot(self):
        self.config.singularity_instance_type = self.lineEdit_singularityinstancetype.text()
    
    def set_singularity_sla_tier_slot(self):
        self.config.singularity_sla_tier = self.comboBox_singularityslatier.currentText()

    def set_account_name_slot(self):
        self.config.storage_account_name = self.lineEdit_accountname.text()

    def set_container_name_slot(self):
        self.config.storage_container_name = self.lineEdit_containername.text()

    def set_datastore_name_slot(self):
        self.config.storage_datastore_name = self.lineEdit_datastorename.text()

    def set_account_key_slot(self):
        self.config.storage_account_key = self.lineEdit_accountkey.text()

    def set_docker_image_slot(self):
        self.config.environment_docker_image = self.lineEdit_dockerimage.text()

    def set_expname_slot(self):
        self.config.experiment_name = self.lineEdit_expname.text()

    def set_workdir_slot(self):
        self.config.experiment_workdir = self.lineEdit_workdir.text()

    def set_script_slot(self):
        self.config.experiment_script = self.textEdit_script.toPlainText()

    def submit_slot(self):
        self.pushButton_submit.setDisabled(True)
        try:
            if self.tabWidget_cluster.currentIndex() == 0:
                self.config.submit_ITP()
            elif self.tabWidget_cluster.currentIndex() == 1:
                self.config.submit_singularity()
        except:
            pass
        self.pushButton_submit.setEnabled(True)


if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QApplication(sys.argv)
        gui = MainWindow()
        gui.show()
        sys.exit(app.exec_())
    else:
        config = ConfigManager()
        config.experiment_script = sys.argv[2]
        if sys.argv[1] == 'itp':
            config.submit_ITP()
        elif sys.argv[1] == 'sing':
            config.submit_singularity()