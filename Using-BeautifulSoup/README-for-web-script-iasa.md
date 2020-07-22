## README FOR PYTHON SCRIPT: web-script-iasa.py

#### STEP 1: Step up the environment
* import requests = HTTP Requests: The Internet verbs like GET, POST, DELETE
* from bs4 import BeautifulSoup = Python library for web scraping
* import pandas as pd = PANDAS aka python excel

#### STEP 2: put my long af URL into a variable that I called url
* `url = "https://iasa2019annualconference.sched.com/"`

#### STEP 3: Using requests to get url
* Using my HTTP Requests to get the url and then putting it into another variable called response (which is (should be) my Response [200])
  * `response = requests.get(url)`


#### STEP 4: Collect DOC!HTML from the Internet
* Converting that response into text and naming that to the variable, html
  * `html = response.text`
