from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Edge()
driver.get(r"https://www.suning.com/")
a=driver.find_element_by_name('utf-8_homepagev8_126605238630_word01')
ac=ActionChains(driver)
ac.move_to_element(a).perform()
driver.find_element_by_name('utf-8_homepagev8_126605238630_word01').click()

# driver.find_element_by_id('searchKeywords').send_keys('巴黎世家')
# driver.find_element_by_id('searchSubmit').click()
# driver.find_element_by_xpath('/html/body/div[10]/div/ul/li[16]/div/div/div[1]').click()
# driver.find_element_by_xpath('//*[@id="J-TZM"]/dl[1]/dd/ul').click()
# try:
    # driver.find_element_by_xpath('//*[@id="J-TZM"]/dl[1]/dd/ul/li[6]/a/span').click()
    #
    #
    # driver.find_element_by_id('addCart').click()

# except:
#     print('111111')


# try:
#     a=driver.find_element_by_xpath("/html/body/div/div/fguioihgfgh")#把滑块打包
#     ac=ActionChains(driver)#把driver交给事件链执行
#     # ac来驱动鼠标  点住 滑块包. 从300滑倒0   .立即执行
#     ac.click_and_hold(a).move_by_offset(300,0).perform()#立即执行
# except:
#     driver.save_screenshot("a.png")





#跳转页面操作

# a=driver.window_handles#获取窗口的元素
# driver.switch_to.window(a[-1])#跳入指定窗口
# print(a)

# try:
#     # driver.find_element_by_id("kw").send_keys("迪迦")
#     # driver.find_element_by_id("su").click()
#     driver.find_element_by_id("go0000o")
# except:
#     print("找不到id为kw的元素")
# else:#execpt没出错
#     print("那没事了")
# finally:#有没有错我都执行
#     print("巴比Ql")

# try:
# driver.find_element_by_id("kw").send_keys("迪迦")
# driver.find_element_by_id("su").click()
#操作弹窗
# driver.find_element_by_id("confirm").click()#有个弹窗
# #driver.switch_to.alert.accept()#点击确定
# driver.switch_to.alert.dismiss()#点击取消
#

# time.sleep(1000)
# driver.quit()