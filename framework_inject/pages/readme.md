# REPO:
https://github.com/eshut/Inject-Framework

# PAGES
This directory should contain Page-Objects with described logic and locators for each page

### Structural Example:
```
/framework/website_1/
    - website_1_constants.py
/framework/website_1/pages/
    - login_page.py 
    - main_page.py

/framework/website_2/
    - website_2_constants.py
/framework/website_2/pages/
    - first_page.py 
    - second_page.py
```

# Inject Feature

Framework implements global singleton Context() that can be reached in any part of the code in order to get/set any values. 
By default `context["I"]` contains driver.page instance allowing to directly access base methods.

### Example Usage
```python
from framework_inject.base.context import Context
from framework_inject.base.base_page import BasePage

I = Context()["I"]

class TestPage(BasePage):
    def __init__(self):
        self.SELECTORS = {
            "TEST_BUTTON": "//button[@type='submit']",
        }
        
    def test_step(self):
        I.goto("https://url.com")
        I.wait_for_element("test")

```

Another option is to use `self.` instead of `I = Inject` 

### Page Example:
```python
import os

from framework_inject.base.base_page import BasePage
from framework_inject.website_1.website_1_constants import MAIN_PAGE
from framework_inject.constants import DEFAULT_WAIT_TIME_SEC
from framework_inject.utils.time_util import wait_time

email = os.getenv("EMAIL")
password = os.getenv("PASS")


class LoginPage(BasePage):
    def __init__(self, logger=__file__):
        super().__init__(logger)
        self.login_page = MAIN_PAGE
        self.SELECTORS = {
            "SUBMIT_BUTTON": "//button[@type='submit']",
            "LOGIN_INPUT": "//input[@id='email']",
            "PASSWORD_INPUT": "//input[@id='password']",
        }

    def login(self):
        self.logger.info("Checking Login page")
        self.goto(self.login_page)
        wait_time(1)
        if not self.wait_for_element_conditional(self.SELECTORS['SUBMIT_BUTTON']):
            self.logger.info("Already Logged In")
            return
        self.click_and_fill_text(self.SELECTORS["LOGIN_INPUT"], email)
        self.click_and_fill_text(self.SELECTORS["PASSWORD_INPUT"], password)
        wait_time(DEFAULT_WAIT_TIME_SEC)
        self.move_and_click(self.SELECTORS["SUBMIT_BUTTON"])
        self.logger.info("Finish Login")
        wait_time(DEFAULT_WAIT_TIME_SEC)


```