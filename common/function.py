#-*-coding:utf-8-*- 
from selenium import webdriver
import os,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def inser_img(driver,filename):
    f_path = os.path.dirname(os.path.realpath(__file__))
    log_path = os.path.join(os.path.dirname(f_path), "test_report","img/")
    # 判断项目下是否有logs文件夹，没有就创建一个
    if not os.path.exists(log_path): os.makedirs(log_path)
    now =time.strftime('%Y-%m-%d-%H-%M-%S')
    inser_path=log_path+now+filename+'.jpg'
    driver.get_screenshot_as_file(inser_path)

def find_new_report(dir):
    lists=os.listdir(dir)
    lists.sort(key=lambda fn:os.path.getctime(dir+"\\"+fn))
    report=os.path.join(dir,lists[-1])
    return report

def send_report(report):
    f=open(report,'rb')
    email_body=f.read()
    f.close()

    msg=MIMEText(email_body,'html','utf-8')
    msg['Subject']=Header(u'测试报告','utf-8')
    msg['from']='hjunping@126.com'
    msg['to']='275769643@qq.com'

    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('hjunping@126.com','275769643aa')
    smtp.sendmail('hjunping@126.com','275769643@qq.com',msg.as_string())
    smtp.quit()
    print ("email has send out")

if __name__ == "__main__":
    driver = webdriver.Firefox()
    print(inser_img(driver))