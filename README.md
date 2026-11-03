# Retrieving Remote Data from an API

## Overview

This project demonstrates how to retrieve remote data using Python and the Requests library.

The GetRequester class sends HTTP GET requests and converts JSON responses into Python data structures.

## Features

- Accepts a URL during initialization.
- Sends HTTP GET requests.
- Returns raw response bytes.
- Converts JSON responses into Python lists and dictionaries.

## API Endpoint

https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json

## Project Structure

- lib/GetRequester.py: Contains the GetRequester class.
- lib/testing/get_requester_test.py: Contains automated tests.

## Installation

Install dependencies using pipenv install.

## Usage

Create a GetRequester object with the API URL.

Call get_response_body() to retrieve the raw response.

Call load_json() to convert the response into Python data.

## Run Tests

Run pipenv run pytest -v.

## Technologies

- Python 3.8
- Requests
- JSON
- Pytest

## Author

Abdulsalam
