# Submit Jobs GUI

This small application can let you easily submit ITP and Singularity jobs through a GUI. Try it now!

## How to use?
  1. You need a Windows or Linux machine equipped with conda environment.
  2. Run `setup.bat` (Windows) or `setup.sh` (Linux). This will create a new conda env named 'submit_jobs' to run the app.
  3. Run `run.bat` (Windows) or `run.sh` (Linux) to open the gui.
  4. Fill the form and push the 'Submit' button.

## Letting others submit jobs for you
  1. You need a machine without any identity information. (Like a local Linux server)
  2. Setup environment as in [How to use](#How-to-use).
  3. Modify the config as your need. You can either directly modify `userdata.json` (not recommended) or open a GUI to modify through VNC and close to save.
  4. SSH connect to the machine (through like PUTTY or VSCode). Run `python gui.py [TYPE] [SCRIPT]`. `TYPE` is one of `sing` and `itp`, determining what type of cluster to submit to. `SCRIPT` is the running command of the job.
  5. The command shall return a device code auth info like `To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code XXXXXXXXX to authenticate.`. Send it to others who would like to help you. After finishing the authentication, job will be submitted.
  6. The authentication info will last for a few hours. If you want to switch account, delete `~/.azureml/auth`. Then the service shall ask you the relogin.

## ChangeLog
- 2022/3/29
  - Migrate from Submit-ITP-Jobs. Add the ability to submit Singularity jobs. 
- 2022/4/27
  - Reformat `userdata.json` for readability.
  - Add default value for Singularity VC and SLA to avoid inconsistence between GUI and internal config.
  - Add a guidance on letting others submit jobs for you.