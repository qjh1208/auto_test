#自动化测试框架（面向对象）
#在shop中进行登陆，并核对用户信息，最后进行退出
#conding:utf-8

# from selenium  import webdriver
# import time
# def login(url,uname,pwd):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.maximize_window()
#     login = driver.find_element_by_xpath('//*[@id="login"]').click()
#     time.sleep(2)
#     loginFrame=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/iframe')
#     driver.switch_to.frame(loginFrame)
#     name =driver.find_element_by_name('username')
#     psw = driver.find_element_by_name('password')
#     loginbt=driver.find_element_by_xpath('//*[@id="loginBtn"]')
#     name.send_keys(uname)
#     psw.send_keys(pwd)
#     loginbt.click()
#     userid =driver.find_element_by_xpath('/html/body/header/nav/div/div/div[1]/ul/li[1]/a')
#     if userid.text == uname:
#         print('login ok')
#     else:
#         print('login fail')
#     driver.find_element_by_xpath('//*[@id="logout"]').click()
#     time.sleep(2)
#     driver.quit()
#
# login('https://www.shopex.cn/','17335802294','17335802294')



#class 类在面向对象编程中  类下面只是表示带公共属性得组合
from selenium  import webdriver
import time
class Login():
    def browsertart(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self,uname,pwd):
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        time.sleep(2)
        loginFrame=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/iframe')
        self.driver.switch_to.frame(loginFrame)
        name =self.driver.find_element_by_name('username')
        psw = self.driver.find_element_by_name('password')
        loginbt=self.driver.find_element_by_xpath('//*[@id="loginBtn"]')
        name.send_keys(uname)
        psw.send_keys(pwd)
        loginbt.click()
        userid =self.driver.find_element_by_xpath('/html/body/header/nav/div/div/div[1]/ul/li[1]/a')
        if userid.text == uname:
            print('login ok')
            self.logout()
        else:
            print('login fail')
            self.driver.quit()
    def logout(self):
        self.driver.find_element_by_xpath('//*[@id="logout"]').click()
        time.sleep(2)
        self.driver.quit()


t=Login()
t.browsertart('https://www.shopex.cn/')
t.login('17335802294','17335802294')#login函数中包含logout函数