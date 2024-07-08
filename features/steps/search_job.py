from behave import *
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


@given('the client got navigated to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    #context.driver.maximize_window()
    context.driver.get("https://www.alten.es/")
    wait = WebDriverWait(context.driver, 10)
    accept_buton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tarteaucitronPersonalize2"]'))).click()

@when('the client enter a valid job into the seach box field')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]'))
    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]/div[1]/form/div/div/div[1]/div/div/input').send_keys("INGENIERO")
    time.sleep(5)

@when('the client click on seach icon')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]/div[1]/form/div/div/div[1]/div/div/span/span').click()
    time.sleep(5)

@then('valid jobs should be displayed in search results')
def step_impl(context):
    value = context.driver.find_element(By.XPATH, '//*[@id="jobboard-jobboard-0"]/div/div/div[5]/div[1]/h3/span[1]').text
    assert("Jobs (" + value + ") should be 1 or more", int(value) >= 1)
    context.driver.quit()




@when('the client enter an invalid job into the seach box field')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]'))
    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]/div[1]/form/div/div/div[1]/div/div/input').send_keys("PANADERO")
    time.sleep(5)
   
@then('zero valid jobs should be displayed in search results')
def step_impl(context):
    value = context.driver.find_element(By.XPATH, '//*[@id="jobboard-jobboard-0"]/div/div/div[5]/div[1]/h3/span[1]').text
    assert("Jobs (" + value + ") should be zero", int(value) == 0)
    context.driver.quit()



@when('the client enter TELETRABAJO into the search box field')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]'))
    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[9]/div[1]/form/div/div/div[1]/div/div/input').send_keys("TELETRABAJO")
    time.sleep(5)