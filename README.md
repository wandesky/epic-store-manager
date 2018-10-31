# Store-manager
[![Maintainability](https://api.codeclimate.com/v1/badges/88b4e281398dabeee3a0/maintainability)](https://codeclimate.com/github/wandesky/epic-store-manager/maintainability)
[![Build Status](https://travis-ci.com/wandesky/epic-store-manager.svg?branch=ch-add-travis-pure-161532711)](https://travis-ci.com/wandesky/epic-store-manager)
[![Coverage Status](https://coveralls.io/repos/github/wandesky/epic-store-manager/badge.svg?branch=ch-add-travis-pure-161532711)](https://coveralls.io/github/wandesky/epic-store-manager?branch=ch-add-travis-pure-161532711)

[![Run in Postman - Heroku](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/10603920350da8c05494)
[![Run in Postman - Localhost](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/39428fe334c131564a1e)
## Introduction
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Running the app locally (UI-Challenge 1)
- Clone the repo using ` git clone https://github.com/wandesky/store-manager.git `.
- Move to the application's directory using ` cd store-manager `.
- Open ` index.html` with your browser to access the homepage.

## Running the app online (UI - Challenge 1)
You can access a live version of the user interface by clicking the link below:
- [Store Manager](https://wandesky.github.io/store-manager/)

## Running the app locally (API - Challenge 2&3)
### Challenge 2
**Follow the instructions below to run a copy of the app from challenge 2 _(does not support data persistence)_**
1. Git clone the repo using `git clone https://github.com/wandesky/epic-store-manager.git`
2. Switch to the project folder using `cd epic-store-manager`
3. Checkout the bootcamp-week one branch using `git checkout pure-develop`
4. Create a virtual environment using `virtualenv venv`
5. Activate the virtual environment using `source venv/bin/activate` in linux or `venv/script/activate` for windows
5. Install the required dependencies using `pip install -r requirements.txt`
6. Start the server and launch the app using `python run.py`

### Challenge 3
**Follow the instructions below to run a copy of the app from challenge 3 _(supports data persistence using PostgreSQL database)_**
1. Git clone the repo using `git clone https://github.com/wandesky/store-manage-with-database.git`
2. Checkout the bootcamp-week one branch using `git checkout bootcamp-week-one`
3. Switch to the project folder using `cd store-manager`
4. Create a virtual environment using `virtualenv venv`
5. Activate the virtual environment using `source venv/bin/activate` in linux or `venv/script/activate` for windows
5. Install the required dependencies using `pip install -r requirements.txt`
6. Start the server and launch the app using `python run.py`

## Running the app online (API - Challenge 2&3)
- The API following specifications from Challenge 2 can be accessed on Heroku by [clicking here](https://wandesky-store-manager.herokuapp.com/).
- The API following specifications from Challenge 3 can be accessed on Heroku by [clicking here](https://wandesky-stg-store-manager-ch3.herokuapp.com/).

### View Sales Records page (Admin)
![Admin's view of Sales Records](https://user-images.githubusercontent.com/19204205/46824614-1a9db180-cd9a-11e8-94b1-7c38318e6744.png)

## How to Contribute
If you wish to contribute to this projects:
* Fork the repo
* Create a feature branch e.g. ``` git checkout -b your-custom-branch-name ```
* Push the changes to your branch e.g. ``` git push origin your-custom-branch-name```
* Create a pull request
