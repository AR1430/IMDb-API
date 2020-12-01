# IMDb-API

<p align="center">
   <img alt="View Demo" src="https://img.shields.io/badge/View-Demo-brightgreen" href="https://imdbapi.herokuapp.com">
   <img alt="Make pull request" src="https://img.shields.io/badge/Make-Pull%20Request-yellowgreen" href="https://github.com/chauhannaman98/IMDb-API/issues/new?assignees=&labels=&template=bug_report.md&title=">
   <img alt="Request Feature" src="https://img.shields.io/badge/Request-Feature-blueviolet" href="https://github.com/chauhannaman98/IMDb-API/issues/new?assignees=&labels=&template=feature_request.md&title=">
</p>

IMDb API is a web based REST API which can be used in various projects by web developers and even developers working on application development which needs to utilize any feature of IMDb website. This API will enable developers to get data according to their needs in an easy to read javascript object-notation (JSON) format.

This API is still in developement phase and running on non-production server. You may experience unexcepted outputs or internal server errors. Also, the first call to the API may take longer time than expected. The following calls will be fast comparatively.

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
    "docs": "https://chauhannaman98.github.io/IMDb-API/",
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
title you sent as the param(`q`). List contains dictionaries where each dictionary consists of 4 
key-value pairs, `title`, `url` to the page on IMDb, `year-of-release` and `details` having list of
strings having additional information regarding the title searched.

In case, no additional details are available on IMDb, `details` list will have no elements.

**Sample Response:**

```json
{
    "date": "Nov-03-2020",
    "docs": "https://chauhannaman98.github.io/IMDb-API/#search-by-title",
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
name of celebrity you sent as the param(`q`). List contains dictionaries where each dictionary consists of 4 
key-value pairs, `major_work`, `name`, `occuation` and `url`.

**Sample Response:**

```json
{
    "date": "Nov-02-2020",
    "docs": "https://chauhannaman98.github.io/IMDb-API/#search-by-name",
    "search-results": [
        {
            "major_work": "Ace Ventura: Pet Detective (1994)",
            "name": "Jim Carrey",
            "occupation": "Actor",
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