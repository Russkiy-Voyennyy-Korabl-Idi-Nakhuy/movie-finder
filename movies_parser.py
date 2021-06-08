import json
import ssl
import urllib.request
from movie_finder.settings import OMDB_KEY
import csv

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

new_movies = open('new_movies.txt', 'r').readlines()
all_movies = open('movies.csv', 'a', encoding='utf-8')

for imdb_id in new_movies:
    data_URL = 'http://www.omdbapi.com/?i=' + imdb_id.strip() + '&apikey=' + OMDB_KEY
    print('-' * 70 + '\nRetrieving:', data_URL)

    json_data = urllib.request.urlopen(data_URL).read().decode()
    print('Retrieved', len(json_data), 'characters')

    data = json.loads(json_data)
    # imdb_id, title, rating, link, votes, genre, cast, runtime, type, netflix, plot, keywords, year, poster
    all_movies.write('\n' +
                     data["imdbID"] + ',' + data["Title"] + ',' + data["imdbRating"] + ',https://www.imdb.com/title/' +
                     data["imdbID"] + ',' + data["imdbVotes"].replace(',', '') + ',"' + data["Genre"] + '","' +
                     str(data["Actors"].split(',')) + '",' + data["Runtime"].split()[0] + ',' + data["Type"].title() +
                     ',,"' + data["Plot"] + '",,' + data["Year"] + ',' + data["Poster"])

all_movies.close()
