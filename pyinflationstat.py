from selenium import webdriver
import traceback
import sys
import time
import csv

# Open a Specific @url with Selenium @driver
def open_url(driver, url):
    try:
        driver.get(url)

    except Exception:
        traceback.print_exc()
        driver.quit()

    finally:
        driver.quit()

# Initiate the Selenium Web Driver
def init_driver():
    try:
        driver = webdriver.Chrome(executable_path=".//chromedriver")
        return driver
    except:
        print("chromedriver not found, please place it on the root of the project's folder")
        sys.exit(1)        

# Print Usage 
def print_help():
    print('[USAGE]: pyinflationstat.py [PRODUCT_ID] [START_YEAR] [END_YEAR]\n')
    print('Example:\n$> pipenv run python3.6 pyinflationstat.py APU0000701111 2018 2019\n')
    print('Flags:\n')
    print('\t--help : Print Usage\n')

# Checking the formart of the product ID
def check_productID(productID):
    try:
        if (len(productID) != 13):
            print("Incorrect product format, Try : APU0000701111 ")
            sys.exit(1)

    except:
        sys.exit(1)

# Checking the format of the years
def check_years(starting_year, ending_year):

    try:
        if (int(starting_year) >= int(ending_year)):
            print('ERROR : Incorrect Starting or Ending year')
            sys.exit(1)
        elif (len(starting_year) != 4 or len(ending_year) != 4):
            print('ERROR : Incorrect year format\nExample: 2017')
            sys.exit(1)

    except:
        sys.exit(0)

# Check the argument given to the program
def check_arguments():
    argument_number = len(sys.argv) - 1
    arguments = []

    if (argument_number != 3):
        print("ERROR: Incorrect Number of argument\n")
        print_help()
        sys.exit(1)
    
    for argument in sys.argv:
        if (argument == '--help'):
            print_help()
            sys.exit(0)
        else:
            arguments.append(argument)
    arguments.pop(0)
    return arguments
    

def main():
    arguments = check_arguments()

    check_productID(arguments[0])
    check_years(arguments[1], arguments[2])
    #request_data_api(argument)
main()