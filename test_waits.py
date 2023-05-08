import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest



def test_selecting_elements(driver):
    wait = WebDriverWait(driver,10)
    driver.get("http://demostore.supersqa.com/")

    nav_items = driver.find_elements(By.CSS_SELECTOR,"ul.nav-menu li")
    for item in nav_items:
        item_class = item.get_attribute('class')
        if 'current_page_item' in item_class:
            print(f'the selected tab is: {item.text}')

    products = driver.find_element(By.CSS_SELECTOR, 'li.product a')
    product_link = products.get_attribute('href')
    print(product_link)

def test_drop_down(driver):
    driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    dropdown = driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > select:nth-child(2)')
    dropdown_object = Select(dropdown)
    # dropdown_object.select_by_index(2)
    # dropdown_object.select_by_value('saab')
    all_options = dropdown_object.options
    for option in all_options:
        print(option.text)

def test_check_box(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    selected = "input[value='Bike']"
    my_choice = driver.find_element(By.CSS_SELECTOR,selected)
    assert my_choice.is_selected, "not selected"

    num = 2
    all_checkboxes = driver.find_elements(By.NAME,'vehicle')
    print("elements:",len(all_checkboxes),"\n")
    assert len(all_checkboxes) == num
    action = ActionChains(driver)
    
    ## not needed
    # action.move_to_element(my_choice).perform()
    # ActionChains.move_to_element(action,driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']")).perform()
    # driver.execute_script("window.scrollBy(0, 500)")

    for checkbox in all_checkboxes:
        WebDriverWait(driver,10).until(EC.visibility_of(checkbox))
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'vehicle')))
        value = checkbox.get_attribute('value')
        print(value)
        checkbox.click()
        print(checkbox.is_displayed(),checkbox.is_selected())
        assert checkbox.is_selected()
    
def test_radio_button(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    genders = driver.find_elements(By.NAME,'gender')
    assert len(genders) == 3
    expected_values = ['male','female','other']
    for radio_button, value in zip(genders, expected_values):
        if radio_button.get_attribute('type') == 'radio':
            radio_button.click()
            assert radio_button.is_selected()
            assert radio_button.get_attribute('value') == value, f"value: {value} not selected"
        else:raise Exception("radio button not selected")
            
def test_alert(driver):
    driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    alert_button = driver.find_element(By.CLASS_NAME, "styled-click-button")
    alert_button.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am an alert box!" # Check the alert message
    alert.accept() # Accept the alert

    prompt = driver.find_element(By.ID, "confirmexample")
    prompt.click()
    prompt= driver.switch_to.alert
    assert prompt.text == "I am a confirm alert" # Check the prompt message
    # prompt.accept() # Accept the prompt
    prompt.dismiss() # Dismiss the prompt

    
def test_prompt(driver):
    driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    prompt_box = driver.find_element(By.CSS_SELECTOR, "#promptexample")
    prompt_box.click()
    prompt_box= driver.switch_to.alert
    prompt_box.send_keys("I am a prompt box!")
    prompt_box.accept() # Accept the prompt
    text=driver.find_element(By.XPATH,"//p[@id='promptreturn']").text
    assert text == "I am a prompt box!" # Check the prompt message

    