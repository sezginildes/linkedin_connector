# Linkedin Connector

Automatically connect with people on LinkedIn by creating targeted notes using ChatGPT.

## Requirements
- LinkedIn account language must be in english
- Google Chrome
- Selenium chrome driver compatible with google chrome version you're using
- Selenium library
- Openai library
- Openai API key (If you want to use ChatGPT feature of the script)

## Installation
1. You can install this repo by cloning it (git clone https://github.com/talha002/linkedin_connector.git) or download it as zip file.
2. Install Google Chrome.
3. Chrome driver within repo is compatible with chrome version of 117. If you're using higher or lower chrome version you can check compatible chrome driver from [here](https://googlechromelabs.github.io/chrome-for-testing/).
4. You can install libraries by using requirement.txt (pip install -r requirements.txt)
5. For Openai API key, you can checkout how to get one from [here](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt).

## Usage

There are several function within linkedin_connector_functions.py but you can use connector_pipe_line function to connect with people. You can import the function by creating new python script within installed folder and import connector_pipe_line from linkedin_connector_functions.py.

### Parameters
- login_link: str (represents the single use login link required for the script to connect to your account. You can get one from sing-in page of LinkedIn or from [here](https://www.linkedin.com/ssr-login/request-otp-generation).)
- driver: Selenium WebDriver object (represents the web browser that you want to control and automate).
- PATH: str (represents the path to the Chrome WebDriver executable.)
- search_link: str (represents the LinkedIn page which consists of people you wish to connect)
- message (optional): str, optional, default False (Allows you to provide a custom message to send along with the connection request. If not provided, it defaults to False. If it's defined as chatgpt it will send a message based on the profile of target.)
- headless: boolean, default True (represents driver option. If True opens driver as background process, if False directly opens chrome browser and starts the process.)
- limit: int, default 50 (represents page limit. E.g. if it's 50 the script will send 50 pages of invitation)
- openai_key (optional): str, optional, default None (Needed api key for chatgpt function, needed for sending targeted notes while connecting by using chatgpt)
- my_informations (optional): str, optional, default None (Your Linkedin profile informations, needed for sending targeted notes while connecting by using chatgpt)

### Usage Example

<strong>Video</strong>: https://youtu.be/-iY9VB7XOh4

<strong>With chatgpt</strong>:

import linkedin_connector_functions as lcf

lcf.connector_pipe_line(
    <br>login_link=<login_link>,
    <br>search_link=<search_link>,
    <br>PATH='chromedriver.exe',
    <br>message='chatgpt', 
    <br>my_informations="\n- Working as Data Scientist\n- Doing masters at Big Data\n- Doing traineeship at BME\n- My name: Talha",
    <br>openai_key=<openai_api_key>,
    <br>limit=20,
    <br>headless=False)

<strong>Without chatgpt</strong>:

import linkedin_connector_functions as lcf

lcf.connector_pipe_line(
    <br>login_link=<login_link>,
    <br>search_link=<search_link>,
    <br>PATH='chromedriver.exe',
    <br>message='Hello, I work as a data scientist/AI developer in cyber security sector. I would like to connect with you.',
    <br>limit=20,
    <br>headless=False)
