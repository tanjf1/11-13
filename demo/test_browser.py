from time import sleep

def test_browser(driver):

#打开网址 完整的url
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.get("http://www.jd.com")
    sleep(2)


    #后退
    driver.back()
    sleep(2)

    #前进
    driver.forward()
    sleep(2)

    #刷新
    driver.refresh()
    sleep(2)
