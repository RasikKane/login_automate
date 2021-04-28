# Login Automation

python application to automate web-login using selenium

## Purpose

This PoC project creates a windows executable file to log into a web account. <br> **Motivation behind this automation
came from mundane task of claiming a daily leave in [breathehr](https://www.breathehr.com/en-gb/) portal due to COVID-19
remote working conditions.**

Example implementations perform following tasks optionally:

* log into breathehr account and fill out a leave requisition form
* Log into facebook account

## Requirements

* [Chrome driver](https://sites.google.com/chromium.org/driver/) is necessary to drive python automation script. After
  downloading stable version zip, extract folder and add chromedriver.exe file in same directory as of driver script **
  login_site.py**
* conda environment named webcrawl is used for development. Environment file [webcrawl_env.yml](yamls/webcrawl_env.yml)
  file is attached in directory [yamls](yamls) of repository. Some important libraries used are:
    * [selenimum](https://selenium-python.readthedocs.io/) python package used for web automation
    * [pyinstaller](https://pypi.org/project/pyinstaller/) generates a python executable file portable across devices

## Usage

Executable [login_site.exe](login_site.exe) is exposed through a windows batch
file [login_startup.bat](login_startup.bat). This ensures that opened webdriver is closed without fail when browser is
closed. Before running this batch file, users should:

#### Edit following yml files to get system working

* [constraints.yml](yamls/constraint.yml) Keep site to sign into and comment out unwanted site. This file also defines
  user permission, and browser to use. Implementation as of now strictly uses Chrome.
* [login_credentials.yml](yamls/login_credentials.yml) file stores login credentials. External file in production
  prevents exposing credentials in source code; which is often pulled by people visiting repo.
* [web_constants.yml](yamls/web_constants.yml) file stores:
    * html components required to identify fields in opened web session
    * input arguments passed in form data

#### Ensure that following files are at same directory level:

* chromedriver.exe
* login_site.exe

## Development

Logins for additional websites can be easily implemented with bare minimum knowledge of selenium and with reference of
existing [login_site.py](login_site.py).

#### Build executable file after implementing new site logins

* Implement new logins and automate forms for different websites of your choice.
* Make sure that anaconda environment with requirements stated in [webcrawl_env.yml](yamls/webcrawl_env.yml) is created.
* if environment is named other than "webcrawl"; make necessary changes while activating conda environment
  in [make_exe.bat](make_exe.bat) file.
* run [make_exe.bat](make_exe.bat) to create new [login_site.exe](login_site.exe)

#### Known Issues

* Users can log into only one of the implemented websites
* Tasks like logging in, form-data completion can be separated with some object-oriented programming.
* Creating strings to search with selenium's "find_element" can be assembled pythonically with object-oriented
  programming.
* A basic tkinter alike UI would help user than fiddling with yml files
* Need Test cases  




