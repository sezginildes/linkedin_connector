from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import openai
from openai.error import ServiceUnavailableError

def chat_with_chatgpt(messages, key):
    '''
    Function for sending prompt to chatgpt.

    key: str (representing the openai API key for sending requests to chatgpt.)
    messeges: str (representing the prompt sending to chatgpt)
    '''

    openai.api_key = key
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': messages}],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = completion['choices'][0]['message']['content']
    return answer

def anlyze_profile(driver, peep_element, informations, key):
    '''
    Function for analysing linkedin profiles and sending them to chatgpt.

    driver: Selenium WebDriver object (represents the web browser that you want to control and automate).
    peep_element: Selenium WebDriver object (represents the webdriver element which includes profile link).
    key: str (representing the openai API key for sending requests to chatgpt.)
    informations: str (representing the career information of user)
    '''

    peep_profile = peep_element.find_element(By.TAG_NAME, 'a').get_attribute("href")
    driver.execute_script("window.open(arguments[0])", peep_profile)
    driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pv-text-details__left-panel')))

    header = driver.find_element(By.CLASS_NAME, 'pv-text-details__left-panel').text
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//section[.//div[@id="about"]]')))
        about_section = driver.find_element(By.XPATH, '//section[.//div[@id="about"]]').text
    except TimeoutException:
        about_section = "None"
    try:
        experience = driver.find_element(By.XPATH, '//section[.//div[@id="experience"]]').text
    except:
        experience = "None"

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    prompt = f"I want to send an introduction message limited to 300 characters to a person from linkedin. Write me an introduction message in 300 characters based on the information I gave down below:\nMy information:{informations}\nInformation of the person:\nName&Summary\n{header}\n{about_section}\n{experience}\nDont Metnion: collabration, hashtags."

    while True:
        try:
            answer = chat_with_chatgpt(messages=prompt, key=key)
            break
        except ServiceUnavailableError:
            print('The Chatgpt server is overloaded or not ready yet. Tryin again in 5 seconds.')

    return answer

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

def connect(driver, message=False, openai_key="None", my_informations="None"):
    '''
    Function to send connection invite

    driver: Selenium WebDriver object (Represents the web browser that you want to control and automate.)
    message (optional): str, optional (Allows you to provide a custom message to send along with the connection request. If not provided, it defaults to False. If it's defined as chatgpt it will send a message based on the profile of target.)
    openai_key (optional): str, optional (Needed api key for chatgpt function.)
    my_informations (optional): str, optional (Your Linkedin profile informations, needed for sending targeted notes while connecting)
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
        try:
            connect_btn = peep.find_element(By.TAG_NAME, 'button')
            
            if connect_btn.text == "Connect":

                if message == "chatgpt":
                        answer = anlyze_profile(driver, peep, informations=my_informations, key=openai_key)

                message_bubbles = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Messaging"]')
                for bubble in message_bubbles:
                    close = bubble.find_element(By.TAG_NAME, "button")
                    close.click()

                connect_btn.click()

                try:
                    if message == "chatgpt":
                        note_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Add a note"]')
                        note_btn.click()
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[name="message"]')))
                        text_area = driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"]')
                        text_area.send_keys(answer)

                    elif message:
                        note_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Add a note"]')
                        note_btn.click()
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[name="message"]')))
                        text_area = driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"]')
                        text_area.send_keys(message)

                    send_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label = "Send now"]')
                    if 'disabled' not in send_btn.get_attribute('class'):
                        send_btn.click()
                    #TODO: If disabled make a new aswer with chatgpt. Rather than close the window.
                    else:
                        close_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
                        close_btn.click()

                except:
                    close_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
                    close_btn.click()

            else:
                continue

        except NoSuchElementException:
            continue

def next_page(driver):
    '''
    Function to go next page

    driver: Selenium WebDriver object (Represents the web browser that you want to control and automate.)
    '''
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Next"]')))
    next_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
    next_btn.click()

def connector_pipe_line(login_link, search_link, PATH, message=False, headless=True, limit=50, openai_key="None", my_informations="None"):
    '''
    Function to automates the process of logging in to LinkedIn, connecting with people, and navigating through search results or content pages.

    driver: Selenium WebDriver object (represents the web browser that you want to control and automate).
    PATH: str (represents the path to the Chrome WebDriver executable.)
    url: str (represents the LinkedIn page which consists of people you wish to connect)
    e_mail: str (representing the email or username that you want to input into the login form.)
    password: str (representing the password that you want to input into the login form.)
    message (optional): str, optional (Allows you to provide a custom message to send along with the connection request. If not provided, it defaults to False. If it's defined as chatgpt it will send a message based on the profile of target.)
    headless: boolean (represents driver option. If True opens driver in background)
    limit: int (represents page limit. E.g. if it's 5 the script will send 5 pages of invitation)
    openai_key (optional): str, optional (Needed api key for chatgpt function, needed for sending targeted notes while connecting by using chatgpt)
    my_informations (optional): str, optional (Your Linkedin profile informations, needed for sending targeted notes while connecting by using chatgpt)
    '''
    # Options for selenium driver
    service = Service(executable_path=rf'{PATH}')
    op = webdriver.ChromeOptions()
    if headless:
        op.add_argument("--headless")

    linkedin_driver = webdriver.Chrome(service=service, options=op)
    linkedin_driver.get(login_link)
    linkedin_driver.get(search_link)

    count = 0

    #TODO: Limit part will be updated
    while count <= limit:
        connect(linkedin_driver, message, openai_key, my_informations)
        next_page(linkedin_driver)
        count += 1
    
    print("Invitation progress completed!")

    linkedin_driver.close()