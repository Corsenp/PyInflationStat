# PyInflationStat

PyInflationStat is a school project (Assignment 6) gathering data about the price a commodity over the years
and creating a graph to display this data.

## Installation

Python 3 is required in order to run this program
Pipenv is required in order to run this program

### OSX

```bash
brew install python3
```

```bash
brew install pipenv
```

## Usage

In order to install the dependencies run :

```bash
pipenv install
```

Then to run the project use the following command:

```bash
pipenv run python3.6 pyinflationstat.py PRODUCT_ID STARTING_YEAR ENDING_YEAR
```

Example:

```bash
pipenv run python3.6 pyinflationstat.py APU0000701111 2016 2019
```



If you have any trouble with pipenv use the help flag:

```bash
pipenv --help
```

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)