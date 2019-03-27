import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        response = urllib.request.urlopen(request)
        cs = response.headers.get_content_charset()
        if not cs:
            cs = charset
        html = response.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Downloading error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <600:
                return download(url, num_retries - 1)
    return html
        

if __name__ == "__main__":
    url = 'https://book.douban.com'
    #url = 'http://httpstat.us/500' 
    print(download(url))

