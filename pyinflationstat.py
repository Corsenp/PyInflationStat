from selenium import webdriver
import traceback
import sys
import time

def open_url(driver, url):
    try:
        driver.get(url)

    except Exception:
        traceback.print_exc()
        driver.quit()

    finally:
        driver.quit()

def init_driver():
    try:
        driver = webdriver.Chrome(executable_path=".//chromedriver")
        return driver
    except:
        print("chromedriver not found, please place it on the root of the project's folder")
        sys.exit(1)        

def main():
    driver = init_driver()
    open_url(driver, 'https://www.programiz.com/python-programming/time')

main()