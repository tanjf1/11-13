import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome('../chromedirve78/chromedriver.exe')
    #调整浏览器大小最大化
    #driver.maximize_window()
    yield driver
    driver.close()