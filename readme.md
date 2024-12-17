# Python WebDriver Framework | Inject Framework {I}
This project describes most common PlayWright webdriver and http API methods in useful way. 

### Remote Debugging Support

Framework support `CDP (Chrome DevTools Protocol)` connection, set in `.env.example` by default. 
In order to use it this way consider running chrome with command:
```python
google-chrome --remote-debugging-port=9222
```

Otherwise change .env value `BROWSER = RemoteChromeBrowser` to `BROWSER = ChromeBrowser`


### RUN:
1. `Create a virtual environment and install requirements`
    ```python
    python3 -m venv venv
    pip3 install -r "requirements.txt"
    ```

2. `[Page Object]` Describe required web pages as it mentioned at:
   [Page-Object instructions](./framework/pages/readme.md)
3. Consider using `Context()` and `I = Inject()` described at [Context Feature](./framework/base/readme.md)
4. Import the page and run your `autotest/code`

<!-- TAGS: a1qa, A1QA, Itransition, autotests, Framework,  PlayWright, Selenium, Automation, Python -->
<!-- TAGS-END -->