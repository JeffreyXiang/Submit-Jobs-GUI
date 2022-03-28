# Author: Fangyun Wei
#
# This Python script works as the entry script of the AML job. Specifically,
# it will be uploaded by run.py, be executed on remote VM, set up necessary
# runtime environments, and then execute a designated user command.
#

import os
import argparse

parser = argparse.ArgumentParser(description="AML Generic Launcher")
parser.add_argument('--workdir', default="", help="The working directory.")
parser.add_argument('--script', default="", help="The running script.")
args, _ = parser.parse_known_args()

# start training
os.chdir(args.workdir)
os.system(f"WORKDIR={args.workdir} && {args.script}")
