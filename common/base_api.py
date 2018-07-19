#-*-coding:utf-8-*- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common.function import *
class Base():
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.poll=0.5
    # loctor 传元祖，如（"id","xx"）
    def findElement(self,loctor):
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*loctor))
        return element
    # loctor 传元祖，如（"id","xx"）返回list
    def findElements(self, loctor):
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements
    # 找到了返回element，没找到抛异常
    def findElementNew(self,loctor):
        elememt = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elememt
    # 找到了返回list, 没找到抛异常
    def findElementsNew(self,loctor):
        elememt = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elememt
    # 点击事件
    def clickElements(self,loctor,n=0):
        element=self.findElements()  #list
        if len(element)<1:
            print("没找到元素！！！")
        elif n >len(element):
            print("越界了！！！！！，最大值是：%s" % len(element))
        else:
            element[n].click()
    # 输入文本
    def sendKeys(self,loctor,text):
        ele=self.findElement(loctor)
        ele.send_keys(text)
    # 点击事件
    def to_click(self,loctor):
        ele=self.findElement(loctor)
        ele.click()
    # 清除事件
    def to_clear(self,loctor):
        ele=self.findElement(loctor)
        ele.clear()
    # 鼠标悬停事件
    def moveToElement(self,loctor):
        mos=self.findElement(loctor)
        ActionChains(self.driver).move_to_element(mos).perform()
    # 判断给定的text在这个元素的文本上要么返回true,要么返回false
    def is_text_in_element(self,loctor,text):
        try:
            result=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(loctor, text))
            return result
        except:
            return False
    # 判断给定的属性的value值在这个元素的文本上
    def is_value_in_element(self,locator,value):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False
    # 元素是否存在
    def is_element_exsits(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False
    # 如有alert, 返回的是alert对象，没有就返回False
    def is_alert_exsit(self,timeout=5):
        try:
            alert=WebDriverWait(self.driver,timeout,self.poll).until(EC.alert_is_present())
            return alert
        except:
            return False
    # 滚动到底部
    def js_scroll_end(self):
        js_heig="window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)
    # 屏幕聚焦元素
    def js_focus(self,loctor):
        target=self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    # 回到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    base = Base(driver)
    driver.get("https://www.baidu.com")

    # driver.get("http://www.cnblogs.com/yoyoketang/p/")
    # import time
    #
    # time.sleep(3)
    # base.js_scroll_end()  # 滚动到底部
    # plun_loc = ("xpath", "//h3[text()='最新评论']")
    # base.js_focus(plun_loc)
    input_id=("link text","新闻")
    base.moveToElement(input_id)
    inser_img(driver,'test')
    base.to_click(input_id)
