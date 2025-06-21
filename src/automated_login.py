from datetime import datetime as dt
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def get_driver():
    #Options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def write_file(text):
    """Write input in text file"""
    filename = f"{dt.now().strftime('%Y-%m-d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def login_and_click():
    """Login, click and scrape a given text in find_element()"""
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    write_file(element.text)


print(login_and_click())
