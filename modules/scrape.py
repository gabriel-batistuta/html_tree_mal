from requests import get
from bs4 import BeautifulSoup

def create_example_html():
    with open('test/page_user.html', 'w') as file:
        file.write(get('https://myanimelist.net/profile/gabsbatistuta').text)

def get_example_html() -> BeautifulSoup:
    with open('test/page_user.html', 'r') as file:
        page = BeautifulSoup(file.read(), 'html.parser')
    return page

def get_avatar():
    page = get_example_html()
    image_div = page.find('div',attrs={'class':'user-image mb8'})
    print(image_div)
    image_url = image_div.find('img', attrs={'class':'lazyload'})['data-src']
    print(image_url)
    with open('test/avatar.jpg','wb') as file:
        file.write(get(image_url).content)