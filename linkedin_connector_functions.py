from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, e_mail, password):
    '''
    Function for loging linkedin.

    driver: Selenium WebDriver object (represents the web browser that you want to control and automate).
    e_mail: str (representing the email or username that you want to input into the login form.)
    password: str (representing the password that you want to input into the login form.)
    '''
    sign_in = driver.find_element(By.XPATH, '//a[text()="Sign in"]')
    sign_in.click()

    e_mail_input = driver.find_element(By.ID, "username")
    e_mail_input.send_keys(e_mail)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    password_input.submit()

def connect(driver, message=False):
    '''
    Function to send connection invite

    driver: Selenium WebDriver object (Represents the web browser that you want to control and automate.)
    message (optional): srt, optional (Allows you to provide a custom message to send along with the connection request. If not provided, it defaults to False.)
    '''
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[class="reusable-search__result-container"]')))
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.1)
    driver.execute_script(f"window.scrollTo(0, 0)")
    people = driver.find_elements(By.CSS_SELECTOR, 'li[class="reusable-search__result-container"]')

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Connect"]')))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Connect"]')))
    except:
        return

    for peep in people:
        connect_btn = peep.find_element(By.TAG_NAME, 'button')
        if connect_btn.text == "Connect":
            connect_btn.click()

            try:
                if message:
                    note_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Add a note"]')
                    note_btn.click()
                    text_area = driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"]')
                    text_area.send_keys(message)

                send_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label = "Send now"]')
                send_btn.click()

            except:
                close_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
                close_btn.click()

        else:
            continue

def next_page(driver):
    '''
    Function to go next page

    driver: Selenium WebDriver object (Represents the web browser that you want to control and automate.)
    '''
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Next"]')))
    next_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
    next_btn.click()

def connector_pipe_line(url, e_mail, password, PATH, message=False):
    '''
    Function to automates the process of logging in to LinkedIn, connecting with people, and navigating through search results or content pages.

    driver: Selenium WebDriver object (represents the web browser that you want to control and automate).
    PATH: str (represents the path to the Chrome WebDriver executable.)
    url: str (represents the LinkedIn page which consists of people you wish to connect)
    e_mail: str (representing the email or username that you want to input into the login form.)
    password: str (representing the password that you want to input into the login form.)
    message (optional): srt, optional (Allows you to provide a custom message to send along with the connection request. If not provided, it defaults to False.)
    '''
    # Options for selenium driver
    op = webdriver.ChromeOptions()
    #op.add_argument("--headless")

    linkedin_driver = webdriver.Chrome(PATH, options=op)
    linkedin_driver.get(url)

    login(linkedin_driver, e_mail, password)

    for i in range(1, 100):
        connect(linkedin_driver, message)
        next_page(linkedin_driver)