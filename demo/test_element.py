from time import sleep

#输入
from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get('http://ui.yansl.com/#/input')
    sleep(2)

    input=driver.find_element_by_xpath("//input[@name='t1']")

    #清空
    input.clear()

    #输入
    input.send_keys("我是谁?我在哪?我该干什么?")
    sleep(2)

#点击
def test_radio(driver):
    driver.get('http://ui.yansl.com/#/radio')
    sleep(2)

    radio=driver.find_element_by_xpath("//input[@value='1']")

    #清空
    #radio.clear()

    #点击
    radio.click()
    sleep(2)

#判断属性值
def test_checkbox(driver):
    driver.get('http://ui.yansl.com/#/checkbox')
    sleep(2)

    checkbox=driver.find_element_by_xpath("(//span[@class='el-checkbox__inner'])[1]")

    attributtr=checkbox.get_attribute('class')
    if not attributtr=='el-checkbox__input is-checked':
        checkbox.click()
        sleep(5)

    heckbox=driver.find_element_by_xpath("(//span[@class='el-checkbox__inner'])[1]")

    attributtr=checkbox.get_attribute('class')
    if not attributtr=='el-checkbox__input is-checked':
        checkbox.click()
        sleep(5)

#下拉框选择
def test_select(driver):
    driver.get('http://ui.yansl.com/#/select')
    sleep(2)

    select=driver.find_element_by_xpath("(//i[@class='el-select__caret el-input__icon el-icon-arrow-up'])[2]")

    #点击
    select.click()
    sleep(2)

    option=driver.find_element_by_xpath('(//span[text()="龙须面"])[last()]')
    actions=ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)

#设置时间
def test_time(driver):
    driver.get('http://ui.yansl.com/#/dateTime')
    sleep(2)

    t1=driver.find_element_by_xpath("//input[@autocomplete='off' and @type='text' and @placeholder='选择时间']")

    #清空
    t1.clear()

    #输入
    t1.send_keys("14:17:17")
    sleep(2)

#上传图片
def test_upload(driver):
    driver.get('http://ui.yansl.com/#/upload')
    sleep(2)

    upload=driver.find_element_by_xpath("//div[@class='el-form-item__content' and @style='margin-left: 100px;']/input")

    #清空
    upload.clear()

    #输入
    upload.send_keys("C:\\Users\\guoya\\Desktop\\微信图片_20191028085516.jpg")
    sleep(2)
