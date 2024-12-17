"""Framework: https://github.com/eshut/Inject-Framework"""

import http
import os

import requests
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from framework_inject.constants import DEFAULT_BROWSER_DEBUGGER_ADDRESS
from framework_inject.constants import DEFAULT_VIEWPORT_SIZE, PLAYWRIGHT_PAGE_DEFAULT_TIMEOUT_MS, BROWSERS, \
    CHROME_BROWSER, FIREFOX_BROWSER, REMOTE_CHROME_BROWSER, REMOTE_FIREFOX_BROWSER, PLAYWRIGHT_DEFAULT_LOCALE

load_dotenv()
log_level = os.getenv("LOG_LEVEL")
localization = os.getenv("LOCALIZATION")
browser = os.getenv("BROWSER")
save_dir = os.getenv("SAVE_DIR")
firefox_location = os.getenv("FIREFOX_LOCATION")


class DriverWebSocket:
    def __init__(self, host=DEFAULT_BROWSER_DEBUGGER_ADDRESS):
        self.debugger_address = f"{host}/json/version"

    def get_websocket_debugger_url(self):
        response = requests.get(self.debugger_address)
        if response.status_code == http.HTTPStatus.OK:
            data = response.json()
            web_socket_debugger_url = data.get("webSocketDebuggerUrl")

            if web_socket_debugger_url:
                return web_socket_debugger_url
            else:
                print("WebSocketDebuggerUrl not found.")  # todo: remove prints
        else:
            print(f"Failed to fetch debugger version. Status code: {response.status_code}")


class ChromeBrowser:
    def __init__(self):
        self.driver_ws_url = DriverWebSocket().get_websocket_debugger_url()
        self.playwright = None
        self.browser = None
        self.page = None

    def run_browser(self, locale=PLAYWRIGHT_DEFAULT_LOCALE):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        context = self.browser.new_context(locale=locale)
        self.page = context.new_page()
        self.page.set_default_timeout(PLAYWRIGHT_PAGE_DEFAULT_TIMEOUT_MS)
        self.page.set_viewport_size(DEFAULT_VIEWPORT_SIZE)
        return self.browser, self.page

    def run_remote_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.connect_over_cdp(self.driver_ws_url)
        context = self.browser.contexts[0]
        self.page = context.new_page()
        return self.browser, self.page

    def close_browser(self):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()


class FireFoxBrowser:
    def __init__(self):
        self.driver_ws_url = DriverWebSocket().get_websocket_debugger_url()
        self.playwright = None
        self.browser = None
        self.page = None

    def run_browser(self, locale=PLAYWRIGHT_DEFAULT_LOCALE):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=False)
        context = self.browser.new_context(locale=locale)
        self.page = context.new_page()
        self.page.set_default_timeout(PLAYWRIGHT_PAGE_DEFAULT_TIMEOUT_MS)
        self.page.set_viewport_size(DEFAULT_VIEWPORT_SIZE)
        return self.browser, self.page

    def run_remote_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.connect_over_cdp(self.driver_ws_url)
        context = self.browser.contexts[0]
        self.page = context.new_page()
        return self.browser, self.page

    def close_browser(self):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()



class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        try:
            del Singleton._instances[cls]
        except KeyError:
            pass


class BrowserFactory(metaclass=Singleton):
    @staticmethod
    def get_browser(browsertype):
        try:
            if browsertype == BROWSERS.index(FIREFOX_BROWSER):
                browser, page = FireFoxBrowser().run_browser(localization)
                return browser, page
            elif browsertype == BROWSERS.index(CHROME_BROWSER):
                browser, page = ChromeBrowser().run_browser(localization)
                return browser, page
            elif browsertype == BROWSERS.index(REMOTE_FIREFOX_BROWSER):
                browser, page = FireFoxBrowser().run_remote_browser()
                return browser, page
            elif browsertype == BROWSERS.index(REMOTE_CHROME_BROWSER):
                browser, page = ChromeBrowser().run_remote_browser()
                return browser, page
            raise AssertionError("Browser not found")
        except AssertionError as _e:
            print(_e)  # todo: change to logger


class RunBrowser(metaclass=Singleton):
    def __init__(self):
        if browser in BROWSERS:
            browser_index = BROWSERS.index(browser)
            self.browser, self.page = BrowserFactory.get_browser(browser_index)
        else:
            raise Exception("No Such Browser")

    def update_page(self, new_page):
        """Method to update the page globally."""
        self.page = new_page
