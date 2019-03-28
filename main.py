import re
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

def crawl_sitemap(url):
    sitemap = download(url)
    #links = re.findall('<div class="book-info">(.*)</div>', sitemap)
    links = re.findall('<h3 class="bigsize">(.*?)</h3>', sitemap)
    for link in links:
        if not link:
            link = 'None'
        return type(link)


if __name__ == "__main__":
    url = 'https://book.douban.com'
    print(download(url))
    print('download end')
    print(crawl_sitemap(url))
