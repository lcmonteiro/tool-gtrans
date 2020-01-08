# #################################################################################################
# -------------------------------------------------------------------------------------------------
# File:   google_browser.py
# Author: Luis Monteiro
#
# Created on jan 6, 2020, 22:00 PM
# -------------------------------------------------------------------------------------------------
# #################################################################################################
import chromedriver_binary
#
from selenium import webdriver
from time     import sleep, time
# -------------------------------------------------------------------------------------------------
# GoogleAPI 
# -------------------------------------------------------------------------------------------------
class GoogleBrowser:
    # TAGS
    __ENDL  = "<+++>"
    __ENDS  = "<###>"
    __IAREA = "source"
    __OAREA = "//span[contains(@class, 'tlid-translation')]"

    def __init__(self, to_lang='en', from_lang=None):
        self.__from   = from_lang if from_lang is not None else 'auto'
        self.__to     = to_lang 
        self.__engine = self.__engine(self.__from, self.__to)

    def __del__(self):
        self.__engine.close()

    def translate(self, data, timeout=10):
        # write on page
        self.__write(self.__serialize(data))
        # read
        timeout = time() + timeout
        while time() < timeout:
            sleep(1)
            translated = self.__unserialize(self.__read())
            if len(translated) == len(data):
                self.__clear()
                return translated
        self.__clear()
        raise TimeoutError()
    # -----------------------------------------------------------------------------------
    # private 
    # -----------------------------------------------------------------------------------
    def __engine(self, from_lang, to_lang):
        from os.path import dirname, join, realpath
        from random  import choice
        # load user agents
        with open(join(dirname(realpath(__file__)), 'uagents.txt')) as f:
            uagents = [ua.strip() for ua in f if ua.strip()]
        # driver options
        options = webdriver.chrome.options.Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument(f"user-agent={choice(uagents)}")
        # open driver
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.get(f'http://translate.google.com/#{from_lang}/{to_lang}/')
        return driver

    def __write(self, data):
        # input area
        iarea = self.__engine.find_element_by_id(self.__IAREA)
        iarea.send_keys(data)

    def __read(self):
        # output area
        oarea = self.__engine.find_element_by_xpath(self.__OAREA)
        text  = oarea.text.replace('\n','')
        return text if text else ' '.join(
                [e.text for e in oarea.find_elements_by_xpath('./span')]).replace('\n','')

    def __clear(self):
        self.__engine.find_element_by_id(self.__IAREA).clear()
        sleep(2)

    def __serialize(self, data):
        return f'\n{self.__ENDS}\n'.join([d.replace('\n', f'{self.__ENDL}') for d in data])

    def __unserialize(self, data):
        from re import split
        return [d.replace(f'{self.__ENDL}', '\n') for d in  split(f' ?{self.__ENDS} ?', data)]

# #################################################################################################
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------
###################################################################################################