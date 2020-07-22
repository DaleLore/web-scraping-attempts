# STEP 1
import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 2
url = "https://iasa2019annualconference.sched.com/"

# STEP 3
response = requests.get(url)
# print response ##Testing

# STEP 4
html = response.text
# print html ##Testing

# STEP 5: Parsing the data with BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print soup ##Testing

# STEP 6: This is the part where we looked at the website to see how the divs and stuff were divided


# STEP 7: CREATE A LIST OF EVERY DIV THAT HAS A CLASS OF "EVENT"
event_divs = soup.find_all('span', {'class', 'event'})
# print len(event_divs) ## Testing

# STEP 8: EVENTS_DIVS is a list(or an array) of events so I'mma put it into an array
schedule_of_events = []

for event in event_divs:
    schedule_of_events.append(event.text)
    print schedule_of_events


df = pd.DataFrame(schedule_of_events)
df.to_csv('test.csv', encoding='utf-8')
