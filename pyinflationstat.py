import sys
import requests
import matplotlib.pyplot as plt
from selenium import webdriver

def create_graph(data, dictionary):
    '''
    Create the graph
    '''
    values = []
    periods = []

    try:
        for value in data:
            values.append(float(value.get('value')))
            periods.append(value.get('period'))
        periods.reverse()
        values.reverse()
        plt.plot(periods, values)
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.title(dictionary['product'])
        plt.show()
    except:
        print("ERROR : error while creating the graph")
        sys.exit(1)

def open_url(driver, url):
    '''
    Open a Specific @url with Selenium @driver
    '''
    try:
        driver.get(url)
    except:
        driver.quit()
    finally:
        driver.quit()

def init_driver():
    '''
    Initiate the Selenium Web Driver
    '''
    try:
        driver = webdriver.Chrome(executable_path=".//chromedriver")
        return driver
    except:
        print("chromedriver not found, please place it on the root of the project's folder")
        sys.exit(1)

def print_help():
    '''
    Print Usage
    '''
    print('[USAGE]: pyinflationstat.py [PRODUCT_ID] [START_YEAR] [END_YEAR]\n')
    print('Example:\n$> pipenv run python3.6 pyinflationstat.py APU0000701111 2018 2019\n')
    print('Flags:\n')
    print('\t--help : Print Usage\n')

def check_product_id(product_id):
    '''
    Checking the formart of the @product_id
    '''
    try:
        if len(product_id) != 13:
            print("Incorrect product format, Try : APU0000701111 ")
            sys.exit(1)
    except:
        sys.exit(1)

def check_years(starting_year, ending_year):
    '''
    Checking the format of the @starting_year and the @ending_year
    '''
    try:
        if int(starting_year) >= int(ending_year):
            print('ERROR : Incorrect Starting or Ending year')
            sys.exit(1)
        elif (len(starting_year) != 4 or len(ending_year) != 4):
            print('ERROR : Incorrect year format\nExample: 2017')
            sys.exit(1)
    except:
        sys.exit(0)

def check_arguments():
    '''
    Check the argument given to the program
    '''
    argument_number = len(sys.argv) - 1
    arguments = []
    if argument_number != 3:
        print("ERROR: Incorrect Number of argument\n")
        print_help()
        sys.exit(1)
    for argument in sys.argv:
        if argument == '--help':
            print_help()
            sys.exit(0)
        else:
            arguments.append(argument)
    arguments.pop(0)
    return arguments

def parse_data(data, dictionary):
    '''
    Parsing the @data receive from the GET request according to the @dictionary
    '''
    values = []
    try:
        for result in data:
            if int(result.get('year')) >= dictionary.get('start_year')\
                and int(result.get('year')) <= dictionary.get('end_year'):
                result.pop('footnotes')
                result.pop('periodName')
                result['period'] = result['period'] + '/' + result['year']
                result.pop('year')
                values.append(result)
        return values
    except:
        print('ERROR : error while parsing data')
        sys.exit(1)

def fetch_data(dictionary):
    '''
    Fetching the data on the website with a GET request according to @dictionary
    '''
    try:
        url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'\
            + dictionary.get('product') + '.json'
        request = requests.get(url)
        data = request.json()
        results = data['Results']['series'][0]['data']
        print(data['status'])
        return results
    except:
        print("Error while requesting API")

def main():
    '''
    Main Function
    '''
    arguments = check_arguments()
    check_product_id(arguments[0])
    check_years(arguments[1], arguments[2])
    dictionary = {
        'product' : arguments[0],
        'start_year' : int(arguments[1]),
        'end_year' : int(arguments[2])
    }
    data = fetch_data(dictionary)
    graph_data = parse_data(data, dictionary)
    create_graph(graph_data, dictionary)

main()
