# REPO:
https://github.com/eshut/Inject-Framework

# Inject / Context Feature

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