# Install package
You need Python 3.7 or higher to run this code.

To install dependencies, please use pip. Please find here below an example using Python virtualenv

## Install and open Python virtualenv
1. Run the command `pip install virtualenv`
2. Run the command `mkdir envdir` to create a folder for your virtual environment
3. Run the command `virtualenv envdir`, this will initiate a new Python virtual environment, without polluting everything in your system Python
4. Run the command `.\envdir\Scripts\activate` to actually enable the virtual environment

## Install dependencies/requirements
Run the command `pip install -r requirements.txt` to install the needed dependencies. Please do this **after** activating the virtualenv.

# Run the code
DicomDatabase is a class which crawls the given folder, and indexes all dicom files. This file can be used as a library, and implemented in code to handle/wrangle DICOM files while taking into account proper file referencing. For example, see [checkStructScan.py](checkStructScan.py) to see how it can be implemented.