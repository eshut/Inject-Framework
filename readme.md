# Python WebDriver Framework | Inject Framework {I}
```Python
This documentation needs to be updated, feel free to leave your issues-comments
```
This is a framework for web/api software automation. You can use this Toolset to build your web automation scripts for any website or API. You can find some examples at [Page-Object instructions](./framework_inject/pages/readme.md) (look for "Page Example" as most usual way to write automation scripts). Please also note that I developed this for the people who already know how to automate web, so this documentation may need to be updated slightly with more use cases. Anyway feel free to reach me out by creating issues or pull requests.
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
   [Page-Object instructions](./framework_inject/pages/readme.md)
3. Consider using `Context()` and `I = Inject()` described at [Context Feature](./framework_inject/base/readme.md)
4. Import the page and run your `autotest/code`

<!-- TAGS: a1qa, A1QA, Itransition, autotests, Framework,  PlayWright, Selenium, Automation, Python -->
<!-- TAGS-END -->
