from time import sleep

#断言 assert
def test_text(driver):
    driver.get('http://ui.yansl.com/#/message')
    buttons=driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/button[1]/span')
    buttons.click()

    message=driver.find_element_by_xpath("//div[@role='alert']/p")
    text=message.text
    print(text)
    a="这是一条消息提示"
    assert a == text
    sleep(2)

#获取页面源代码
def test_page_scoe(driver):
    driver.get('http://ui.yansl.com/#/message')
    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/div').click()

    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/ul/li/ul/li[3]').click()

    scoure=driver.page_source
    print(scoure)

    assert "手工关闭提示" in scoure
    sleep(2)


def test_youxiang(driver):
    driver.get("https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=qq%E9%82%AE%E7%AE%B1%E7%99%BB%E5%BD%95&rsv_pq=a379385f0000509f&rsv_t=ed92SUc20Cc7wn9Y8hURt0Sjg6RSmreWb8yHJ4NOHJNTjGC3nXcqLrPtVlw&rqlang=cn&rsv_dl=ts_2&rsv_enter=1&rsv_sug3=11&rsv_sug1=7&rsv_sug7=101&rsv_sug2=1&prefixsug=qqyouxiang&rsp=2&inputT=6365&rsv_sug4=6857")
    driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()

    a=driver.window_handles
    print(a)
    sleep(3)
