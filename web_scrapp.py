from goose3 import Goose
import bs4
import requests

g = Goose()
def get_article(url): 
        article = g.extract(url=url)
        return article.cleaned_text
    

def get_urls(content,start = 1):
    text = "lates news article on {0}".format(content)
    urls = []
    search = "https://www.google.com/search?q={0} -youtube.com&start={1}".format(text,start)
    response = requests.get(search)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if link['href'].startswith('/url?q='):
                url = link['href'].split('/url?q=')[1].split('&sa=U&')[0]
                urls.append(url)
        urls = urls[2:]
    if urls:
        return urls
    return None