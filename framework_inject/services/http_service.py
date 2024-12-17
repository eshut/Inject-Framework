"""Framework: https://github.com/eshut/Inject-Framework"""

import requests

from framework_inject.logger.logger import Logger


class API(Logger):
    def __init__(self, site, logger=__file__):
        super().__init__(logger)
        self.site = site

    def status(self, get):
        '''
        :return: request > request.status_code
        '''
        self.logger.debug("Trying to get status code")
        req = requests.get(self.site + get)
        result = req
        return result

    def get(self, get):
        self.logger.debug("Trying to get Json")
        req = requests.get(self.site + get)
        result = req.status_code
        try:
            json = req.json()
            return json
        except:
            return "NOT JSON!"

    def post(self, get, data):
        self.logger.debug("Trying to send POST data to: " + str(self.site + get) + " With data: " + str(data))
        result = requests.post(self.site + get, data=data)
        self.logger.debug("Got response: " + str(result) + "With data: " + str(result.text))
        return result
