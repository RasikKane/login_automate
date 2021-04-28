# IMPORTS

from datetime import date

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# CONSTRAINTS

# load yaml file for constraints
site, permission, browser = [None] * 3

CONSTRAINTS = yaml.load(open("yamls/constraint.yml"), Loader=yaml.FullLoader)

if CONSTRAINTS:
    site, permission, browser = CONSTRAINTS.values()

# load yaml file for login credentials
# LOGIN = yaml.load(open('login_credentials.yml'), Loader=yaml.FullLoader)
LOGIN_URL, USER_ID, PASSWORD = [None] * 3

LOGIN = yaml.load(open("yamls/login.yml"), Loader=yaml.FullLoader)

if LOGIN:
    LOGIN_URL, USER_ID, PASSWORD = LOGIN[permission][site].values()

# load yaml file for identifying web elements
COOKIE, USERNAME, PWD, LOGIN, RQ_LEAVE, LEAVE_TYPE, SEL_REASON, \
REASON, START_DATE, START_DATE_IN, END_DATE, END_DATE_IN, NOTE, NOTE_TEXT = [None] * 14

WEB = yaml.load(open("yamls/web_constants.yml"), Loader=yaml.FullLoader)

if WEB:
    if site == 'breathehr':
        USERNAME, PWD, LOGIN, RQ_LEAVE, LEAVE_TYPE, SEL_REASON, \
        REASON, START_DATE, START_DATE_IN, END_DATE, END_DATE_IN, NOTE, NOTE_TEXT = WEB[permission][site].values()
        if START_DATE_IN is not date:
            START_DATE_IN = date.today().strftime("%d/%m/%Y")
        if END_DATE_IN is not date:
            END_DATE_IN = date.today().strftime("%d/%m/%Y")
    if site == 'fb':
        COOKIE, USERNAME, PWD, LOGIN = WEB[permission][site].values()

# CONSTANTS
PRE = "//"
ELEM = "*["
ATTR = "@"
POSTFIX = "]"
drivers = {'Chrome': webdriver.Chrome()}


# driver function
def login(driver=None,
          url=None,
          cookie_element=None,
          username_element=None,
          username=None,
          password_element=None,
          password=None,
          login_button_element=None):
    if driver:  # open session
        driver.get(url)

    if cookie_element:  # accept cookies if any
        driver.find_element(By.XPATH, cookie_element).click()

    if username_element:  # send username
        driver.find_element(By.XPATH, username_element).send_keys(username)

    if password_element:  # send password
        driver.find_element(By.XPATH, password_element).send_keys(password)

    if login_button_element:  # click login
        driver.find_element(By.XPATH, login_button_element).click()

    return driver


def fill_form(sess=None, request_leave_element=None, leave_radio=None, select_reason=None, reason=None,
              start_date=None, start_date_in=None, end_date=None, end_date_in=None, note=None, note_txt=None):
    if request_leave_element:  # click request leave button to start form
        sess.find_element(By.XPATH, request_leave_element).click()

    if leave_radio:  # click radio button for leave type
        sess.find_element(By.XPATH, leave_radio).click()

    if select_reason and reason:  # Write reason for leave
        reasons = Select(sess.find_element(By.XPATH, select_reason))
        reasons.select_by_visible_text(reason)

    if start_date and end_date and start_date_in <= end_date_in:  # select range of leave days
        sess.find_element(By.XPATH, start_date).send_keys(start_date_in)
        sess.find_element(By.XPATH, end_date).send_keys(end_date_in)

    if note:  # set reason for leave in drop down
        sess.find_element(By.XPATH, note).send_keys(note_txt)

    return sess


# call driver function login()
if site == 'breathehr':
    # login to bretheHR
    session = login(drivers[browser],
                    LOGIN_URL,
                    None,
                    PRE + ELEM + ATTR + USERNAME + POSTFIX,
                    USER_ID,
                    PRE + ELEM + ATTR + PWD + POSTFIX,
                    PASSWORD,
                    PRE + ELEM + LOGIN + POSTFIX)

    # wait till login completes and new web elements are available to parse
    session.implicitly_wait(3)

    # open and fill the request leave form
    session = fill_form(session,
                        PRE + ELEM + RQ_LEAVE + POSTFIX,
                        PRE + ELEM + ATTR + LEAVE_TYPE + POSTFIX,
                        PRE + ELEM + ATTR + SEL_REASON + POSTFIX,
                        REASON,
                        PRE + ELEM + ATTR + START_DATE + POSTFIX,
                        START_DATE_IN,
                        PRE + ELEM + ATTR + END_DATE + POSTFIX,
                        END_DATE_IN,
                        PRE + ELEM + ATTR + NOTE + POSTFIX,
                        NOTE_TEXT)

# call driver function login() for fb
elif site == 'fb':
    session = login(drivers[browser],
                    LOGIN_URL,
                    PRE + ELEM + ATTR + COOKIE + POSTFIX,
                    PRE + ELEM + ATTR + USERNAME + POSTFIX,
                    USER_ID,
                    PRE + ELEM + ATTR + PWD + POSTFIX,
                    PASSWORD,
                    PRE + ELEM + ATTR + LOGIN + POSTFIX)
