import requests
import re
import urllib

URL = 'http://www.subzin.com/search.php?q='
quote = input('Enter quote: ')
encodedQuote = urllib.parse.quote(quote)
'''payload = {
    'q':quote,
    'submit':'Search'
    }'''

session_requests = requests.session()
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers['Referer'] = URL
page = session_requests.get(URL+encodedQuote, headers = headers)

movies = re.findall(r'<div class="title"><h3>(.*?)</h3>', str(page.text))
final_movies = movies[0:5]
print(final_movies)
