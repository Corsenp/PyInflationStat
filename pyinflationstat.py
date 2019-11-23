from selenium import webdriver
import traceback
import sys
import time
import requests
import json
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

# Checking the formart of the @productID
def check_productID(productID):
    try:
        if (len(productID) != 13):
            print("Incorrect product format, Try : APU0000701111 ")
            sys.exit(1)

    except:
        sys.exit(1)

# Checking the format of the @starting_year and the @ending_year
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

# Parsing the @data receive from the GET request according to the @dictionary
def parse_data(data, dictionary):
    values = []
    print("PARSE")
    try:
        for result in data:
            if int(result.get('year')) >= dictionary.get('start_year') and int(result.get('year')) <= dictionary.get('end_year'):
                result.pop('footnotes')
                result.pop('periodName')
                result['period'] = result['period'] + '/' + result['year']
                result.pop('year')
                values.append(result)
        
        print(values)
        return values
    
    except:
        print('ERROR : error while parsing data')
        sys.exit(1)
    
# Fetching the data on the website with a GET request according to @dictionary  
def fetch_data(dictionary):
    try:
        url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/' + dictionary.get('product') + '.json'
        request = requests.get(url)
        data = request.json()
        results = data['Results']['series'][0]['data']
        print(data['status'])
        return(results)

    except:
        print("Error while requesting API")

def main():
    arguments = check_arguments()

    check_productID(arguments[0])
    check_years(arguments[1], arguments[2])
    dictionary = {
        'product' : arguments[0],
        'start_year' : int(arguments[1]),
        'end_year' : int(arguments[2])
    }
    data = fetch_data(dictionary)
    parse_data(data, dictionary)
main()