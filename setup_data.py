# This file follows along the instructions in the Data Collection notebook.
# Due to the notebook not displaying in gitpod, we have copied the commands here and exectued them.

import numpy
import os

current_dir = os.getcwd()
current_dir
print(current_dir)
os.chdir('/workspace/ci-malaria-walkthrough/WalkthroughProject01')
print("You set a new current directory")


current_dir = os.getcwd()
current_dir

os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

print(current_dir)