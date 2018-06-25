# freestyle-project
reference: https://github.com/s2t2/stocks-app-py-2018

A monthly bookkeeping app for international students, which helps user to record and manage their spending each month. Start recording expenses at the beginning of each month, and clear the records at the end of each. Then start over.
The app will also request updated currency exchange rate from the [ExchangeRate-API](https://www.exchangerate-api.com/) to help user convert their spending from USD to another currency.

## Installation

First, "fork" this upstream repository under your own control.

Then, download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

```sh
git clone https://github.com/iriskhu/freestyle-project.git
```

After downloading your forked repository, navigate into its root directory:

```sh
cd freestyle-project/
```

> NOTE: all commands in this document assume you are running them from this root directory.


Install package dependencies using one of the following commands, depending on how you have installed Python and how you are managing packages:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.


> NOTE: all commands below assume you are running them from this repository's root directory.

## Setup

### Environment Variables

Obtain an [ExchangeRate-API](https://www.exchangerate-api.com/).

Create a new file in this directory called ".env" and place inside the following contents:

    CURRENCY_API_KEY="YOUR API KEY"

## Usage

Run the bookkeeping script:

```sh
# Homebrew-installed Python 3.x on Mac OS:
python3 app.py

# All others:
python app.py
```

## Testing

Run tests:

```sh
pytest
```

## [License](LICENSE.md)
