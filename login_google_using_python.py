from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self,uname,pword):
        #select browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #selct start page
        self.driver.get('https://accounts.google.com/v3/signin/identifier?checkedDomains=youtube&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ddm=0&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARZ0qKIi8gs70RthDwfyqsJriqo6mAHl0TY5pIxji2ozOex-3iCd_DoBgnyz1t9RXqX5qzlxQd1sFw&pstMsg=1&rip=1&service=mail&theme=mn&dsh=S889667319%3A1711837811439487')
        #select mail input field
        email_input = self.driver.find_element(By.XPATH, '//input[@type="email"]')
        #send mail
        email_input.send_keys(uname)
        #select button
        email_click = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]')
        #click button
        email_click.click()
        #delay time to load the page
        time.sleep(5)
        #select password input field
        pass_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        #send password
        pass_input.send_keys(pword)
        #select button
        pass_click = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]')
        #click button
        pass_click.click()
        #redirect the page you want to open next loged in with your mail 
        self.driver.get('https://www.youtube.com')
        time.sleep(10)
        
        self.driver.quit()

with open('#locate your file that contain mail','r',encoding='utf-8') as u:
    uname = u.read().strip()
with open('#locate your file that contain password','r',encoding='utf-8') as p:
    pword = p.read().strip()
#call the class
Login(uname, pword)