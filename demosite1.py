import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
baseUrl = "http://www.demo.guru99.com/V4/"


class Login():

    def tc01_login_success(self):
        
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys("mngr303123")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("gyrUdaj")

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("Test Case T01 Login success PASSED")
        else:
            print("Test Case T01 Login success FAILED")


    def login_username_maxim_char(self):
        
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys("mngr299418dadasdasdas")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("EnYjAqa")

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("Test Case Login MAX CHARACTERS PASS")
        else:
            print("Test Case Login MAX CHARACTERS FAILED")

    def login_NOK(self , usernameString, passwordString, testCase):
        
        driver.get(baseUrl)

        if usernameString != "":
            username = driver.find_element(By.NAME, "uid")
            username.send_keys(usernameString)


        if passwordString != "":
            password = driver.find_element(By.NAME, "password")
            password.send_keys(passwordString)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = None
        try:
            actualTitle = driver.title
        except:
            print("Test Case  " + testCase + " PASSED")

        if actualTitle is not None:
            print("Test Case " +  testCase + " FAILED")

        



test = Login()

test.tc01_login_success()
test.login_NOK("mngr303123" , "dadadsadas", "T02 Login correct user and wrong password" )
test.login_NOK("NOK" , "gyrUdaj", "T03 Login wrong password and correct user" )
test.login_NOK("NOK" , "NOK", "T04 Login wrong password and wrong user" )
test.login_NOK("" , "gyrUdaj", "T05 Login empty user  and correct password" )
test.login_NOK("" , "NOK", "T06 Login empty user  and wrong password" )
test.login_NOK("mngr303123" , "", "T07 Login correct user  and empty password" )
test.login_NOK("NOK" , "", "T08 Login invalid user  and empty password" )
test.login_NOK("" , "", "T09 Login empty user  and empty password" )



#test.login_username_maxim_char()  





driver.quit()    