import allure
@allure.feature("一级分类")
@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http//baidu.com",'bug')
@allure.testcase("http//baidu.com",'用例')

def test_report(driver):
    url1="http://ui.yansl.com/#/checkbox"
    with allure.step("打开网页:{}".format(url1)):pass   #allure.step 测试步骤的标题  with插入   pass表示改行到此为止，下面无代码
    driver.get(url1)
    with allure.step("点击多选框:{}".format('//*[@id="form"]/form/div[1]/div/input[1]')):    #format  赋值到{}
        allure.attach(driver.get_screenshot_as_png(),'截图1',allure.attachment_type.PNG)    #（截图内容，'截图1' =截图名字，截图类型）
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[1]').click()
    with allure.step("点击多选框:{}".format('//*[@id="form"]/form/div[1]/div/input[2]')):
        allure.attach(driver.get_screenshot_as_png(),'截图2',allure.attachment_type.PNG)
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[2]').click()

