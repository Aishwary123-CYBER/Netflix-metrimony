from flask import Flask,render_template
import requests
import csv
import random
import config



app = Flask(__name__)

@app.route('/')
def home():
    
    with open('catalog.csv',encoding="utf8") as f:
        reader = csv.reader(f)
        row = random.choice(list(reader))

    movie = {
        'id': row[0],
        'category': row[1],
        'title': row[2],
        'director': row[3],
        'cast': row[4],
        'country': row[5],
        'date_added': row[6],
        'release_year': row[7],
        'maturity': row[8],
        'duration': row[9],
        'genre': row[10],
        'description': row[11],
        # default poster just so we see something
        'image': 'https://live.staticflickr.com/4422/36193190861_93b15edb32_z.jpg',
        'imdb': 'not avaiable'}

   
    url = f"http://www.omdbapi.com/?t={movie['title']}&apikey=df4a7b15"
    response = requests.request('GET',url)

    movie_data = response.json()
    
    if 'Poster' in movie_data:
        movie['image'] = movie_data['Poster']

    if 'imdb_rating' in movie_data:
        movie['imdb'] = movie_data['imdb_rating']
    

    return render_template('home.html',movie=movie)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/feature')
def feature():
    return render_template("features.html")










if __name__=='__main__':
    app.run(debug=True)