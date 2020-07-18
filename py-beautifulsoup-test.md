# RESOURCES:
First, confirm versions:
  python3 --version
  pip --version

* BeautifulSoup - https://www.crummy.com/software/BeautifulSoup/#Download

* BeautifulSoup Tutorial - https://www.youtube.com/watch?v=87Gx3U0BDlo
  * pip install requests
  * pip install beautifulsoup4
  * pip install pandas

Joél Collins (Flatiron)
https://github.com/joelsewhere/Scraping/blob/master/wikipedia.py

DataQuest: https://www.dataquest.io/blog/web-scraping-tutorial-python/

# ERRORS:
------------------------
 - ImportError: No module named requests(or bs4 or etc)
  python py-test.py
  Traceback (most recent call last):
    File "py-test.py", line 1, in <module>
      import bs3 as bs
  ImportError: No module named bs3

  - ANSWER: Gotta install them first
  pip install requests
  pip install beautifulsoup4

------------------------
- UnicodeEncodeError: 'ascii' codec can't encode character u'\u201c' in position 0: ordinal not in range(128)
If you getUnicodeEncodeError , simply add encoding='utf-8' ;

- ANSWER:
df.to_csv('file_name.csv', encoding='utf-8')
Barney H. "How to Export Pandas DataFrame to CSV." Mar 21. Accessed July 18, 2020. https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03

------------------------
