# IMDb-API

A REST-API for IMDb based on Flask and BeautifulSoup using Python3. This API is deployed on Heroku's server on non-production dynos. Thus, the first call to the API may take longer time than expected. The following calls will be fast comparatively.

# Features

1. [Home](#home)
2. [Search](#search)
3. [TV Shows](#tv-shows)

# Home

**Endpoint:** https://imdbapi.herokuapp.com/

**Description:** This API will give a simple JSON response regarding the services currently available along with
date when API has been called, status and GitHub repository URL.

**Sample Response:**

```json
{
    "api-services-available": {
        "Search by name": "http://imdbapi.herokuapp.com/search?stype=name&q=Jim",
        "Search by title": "http://imdbapi.herokuapp.com/search?stype=title&q=Titanic",
        "Top25 TV Shows": "https://imdbapi.herokuapp.com/tv-shows/top250"
    },
    "date": "Oct-31-2020",
    "docs": "https://github.com/chauhannaman98/IMDb-API#imdb-api",
    "status": true
}
```

# Search

**Endpoint:** https://imdbapi.herokuapp.com/search

1. [Search by title](#search-by-title)
2. [Search by name](#search-by-name)

## Search by title

**Params:**

1. `stype` = search type(`title` to search by title)
2. `q` = query or the title to be searched

**Description:** This API will give a JSON response with a list of search results on the basis of the
title you sent as the param(`q`). List contains dictionaries where each dictionary consists of 2 
key-value pairs, `title`, `url` to the page on IMDb, `year-of-release` and `details` having list of
strings having additional information regarding the title searched.

In case, no additional details are available on IMDb, `details` list will have no elements.

**Sample Response:**

```json
{
    "date": "Nov-03-2020",
    "docs": "https://github.com/chauhannaman98/IMDb-API#search-by-title",
    "search-results": [
        {
            "details": [
                "TV Episode"
            ],
            "title": "Intersteller",
            "url": "https://www.imdb.com/title/tt5169292/",
            "year-of-release": 2014
        },
    ],
    "status": true
}
```

## Search by name

**Params:**
1. `stype` = search type(`name` to search by name of celebrity)
2. `q` = query or the name of celebrity to be searched

**Description:** This API will give a JSON response with a list of search results on the basis of the
name of celebrity you sent as the param(`q`). List contains dictionaries where each dictionary consists of 2 
key-value pairs, `name` and `url`.

**Sample Response:**

```json
{
    "date": "Nov-02-2020",
    "docs": "https://github.com/chauhannaman98/IMDb-API#search-by-name",
    "search-results": [
        {
            "name": "Jim Carrey",
            "url": "https://www.imdb.com/name/nm0000120/"
        },
    ],
    "status": true
}
```


# TV Shows

1. [Top 250](#top-250)

## Top 250

**Endpoint:** https://imdbapi.herokuapp.com/tv-shows/top250

**Description:** This API will give a JSON response having top 250 TV shows in the ranked according to 
their ratings on [IMDb](https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250). In short, it gives the
top rates 250 shows from IMDb in a JSON format. Key `top250` here has a list of 250 dictonaries. Each
dictionary of key-value pairs that have details of TV Shows including `rank`, `rating`, `starcast`, `title`,
`url` and `year-of-release`.

**Sample Response:**

```json
{
    "date": "Oct-31-2020",
    "status": true,
    "top250": [
        {
            "rank": 1,
            "rating": 9.5,
            "starcast": "David Attenborough",
            "title": "Planet Earth II",
            "url": "https://www.imdb.com/title/tt5491994/",
            "year-of-release": 2016
        },
    ]
}
```