# Introduction
This project is designed to make the game 'Keep Talking and Nobody Explodes' easier.
This code may also be able to speed you up to complete the game quicker.

# Requirements
* Python 3.10
* Access to install python modules

# Setup
Run the startup script

```./setup_script.py```

# Testing
Run the Functional tests as follows

```.\env\Scripts\python.exe -m pytest```

# Running Pylint
Suggest running pylint every time before updating. Ideally this would be run through gitlabs or Jenkins as a CI/CD tool to pass/fail the code before it is merged into master.

```./env/Scripts/python.exe -m pylint .\tests\```

```./env/Scripts/python.exe -m pylint .\bombManual\```

example output:

```./env/Scripts/python.exe -m pylint .\tests\```

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)