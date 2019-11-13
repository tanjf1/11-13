from time import sleep

# 输入
import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_input(driver):
    driver.get('http://ui.yansl.com/#/input')    #打开url
    sleep(2)       #停顿2秒

    input = driver.find_element_by_xpath("//input[@name='t1']")     #找到需要操作的位置，放到input里

    # 清空
    input.clear()   #清空操作位置的内容

    # 输入
    input.send_keys("我是谁?我在哪?我该干什么?")   #输入内容"我是谁?我在哪?我该干什么?"
    sleep(2)    #停顿2秒


# 点击
def test_radio(driver):
    driver.get('http://ui.yansl.com/#/radio')
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@value='1']")

    # 清空
    # radio.clear()

    # 点击
    radio.click()   #点击对应的位子
    sleep(2)


# 判断属性值
def test_checkbox(driver):
    driver.get('http://ui.yansl.com/#/checkbox')
    sleep(2)

    checkbox = driver.find_element_by_xpath("(//span[@class='el-checkbox__inner'])[1]")

    attributtr = checkbox.get_attribute('class')    #判断属性值
    if not attributtr == 'el-checkbox__input is-checked':       #如果不满足条件
        checkbox.click()        #点击
        sleep(5)

    heckbox = driver.find_element_by_xpath("(//span[@class='el-checkbox__inner'])[1]")

    attributtr = checkbox.get_attribute('class')
    if not attributtr == 'el-checkbox__input is-checked':
        checkbox.click()
        sleep(5)


# 下拉框选择
def test_select(driver):
    driver.get('http://ui.yansl.com/#/select')
    sleep(2)

    select = driver.find_element_by_xpath("(//i[@class='el-select__caret el-input__icon el-icon-arrow-up'])[2]")

    # 点击
    select.click()
    sleep(2)

    option = driver.find_element_by_xpath('(//span[text()="龙须面"])[last()]')
    actions = ActionChains(driver)          #导入，鼠标键盘操作都有，键盘操作26个字母
    actions.move_to_element(option).perform()       #鼠标移动，命令组合，perform运行命令
    sleep(2)
    option.click()
    sleep(2)


# 设置时间
def test_time(driver):
    driver.get('http://ui.yansl.com/#/dateTime')
    sleep(2)

    t1 = driver.find_element_by_xpath("//input[@autocomplete='off' and @type='text' and @placeholder='选择时间']")

    # 清空
    t1.clear()

    # 输入
    t1.send_keys("14:17:17")        #输入内容（"14:17:17"）
    sleep(2)


# 上传图片
def test_upload(driver):
    driver.get('http://ui.yansl.com/#/upload')
    sleep(2)

    upload = driver.find_element_by_xpath(
        "//div[@class='el-form-item__content' and @style='margin-left: 100px;']/input")

    # 清空
    upload.clear()

    # 输入
    upload.send_keys("C:\\Users\\guoya\\Desktop\\微信图片_20191028085516.jpg")      #输入图片位置，路径单\改成\\（双\）
    sleep(2)


# 上传文件
def test_upload1(driver):
    driver.get('http://ui.yansl.com/#/upload')
    sleep(2)

    upload1 = driver.find_element_by_xpath('//*[@id="form"]/form/div[2]/div/div/div[1]/button/span')

    # 清空
    upload1.click()
    sleep(2)
#1
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoya\\Desktop\\微信图片_20191028085516.jpg")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(5)
#2      #1-#2 ，点击后通过windows路径 上传图片，内容仅需改变文件路径，其他固定格式，无需改动

def test_alert(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    button = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td[2]/input')
    button.click()
    sleep(2)
    alert=driver.switch_to.alert
    alert.send_keys("abcdefg")
    alert.accept()
    sleep(2)

#窗口切换
def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("京东"):
            break

