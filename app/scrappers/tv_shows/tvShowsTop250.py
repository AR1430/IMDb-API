try:
    from bs4 import BeautifulSoup
    import requests
except Exception as e:
    print('Caught exception while importing: {}'.format(e))


URL = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')    


def get_data():
    show_ranks = []
    show_title = []
    year_of_release = []
    show_url = []
    show_ratings = []
    show_starcast = []
    top250 = []

    main_div = soup.find('div', class_='lister')
    tbody = main_div.find('tbody', class_='lister-list')
    trs = tbody.find_all('tr')
    i = 1

    for tr in trs:
        title = tr.find('td', class_='titleColumn').find('a')
        title = tr.find('td', class_='titleColumn').find('a')
        year = tr.find(
            'td', class_='titleColumn').find('span').get_text()
        rating = tr.find('td', class_='ratingColumn imdbRating').find(
            'strong').get_text()
        url = 'https://www.imdb.com'+title['href']

        # Store data to lists
        show_ranks.append(i)
        show_title.append(title.get_text())
        year_of_release.append(int(year.strip('(').strip(')')))
        show_url.append(url)
        show_ratings.append(float(rating))
        show_starcast.append(title['title'])

        i += 1

    for i in range(250):
        item_dict = {}
        item_dict['rank'] = show_ranks[i]
        item_dict['title'] = show_title[i]
        item_dict['year-of-release'] = year_of_release[i]
        item_dict['starcast'] = show_starcast[i]
        item_dict['url'] = show_url[i]
        item_dict['rating'] = show_ratings[i]

        top250.append(item_dict)
    
    return top250


def getTop250Shows():
    top250 = get_data()
    return top250


def main():
    result = getTop250Shows()
    print(result)


if __name__ == '__main__':
    main()
