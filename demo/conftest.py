import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome('../chromedirve78/chromedriver.exe')        #打开谷歌浏览器
    #调整浏览器大小最大化
    #driver.maximize_window()
    yield driver        #之后操作一下命令
    driver.close()      #关闭浏览器