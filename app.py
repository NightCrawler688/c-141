from flask import Flask,jsonify,request
import csv
from storage import all_movies,liked_movies,disliked_movies,did_not_watch_movies
from demographic_filtering import output
from content_filtering import get_recommendations

all_movies = []
liked_movies = []
dislike_movies = []
did_not_watch_movies = []


app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
        movie_data = {
                'title':all_movies[0][19],
                'poster_link':all_movies[0][27],
                'release_data':all_movies[0][13] or 'N/A',
                'duration':all_movies[0][15],
                'rating':all_movies[0][20],
                'overview':all_movies[0][9]
        }
        return jsonify({
              'data':movie_data,
              'status':'success'
        })

@app.route("/liked-movie",methods = ['POST'])
def liked_movie():
                movie = all_movies[0]
                all_movies = all_movies[1:]
                liked_movies.append(movie)
                return jsonify({
                        'status':'success'
                }),201

@app.route("/disliked-movie",methods = ['POST'])
def disliked_movie():
                movie = all_movies(0)
                all_movies = all_movies[1:]
                dislike_movies.append(movie)
                return jsonify({
                        'status':'success'
                }),201

@app.route("/did-not-watch",methods = ['POST'])
def did_not_watch_movie():
                movie = all_movies(0)
                all_movies = all_movies[1:]
                did_not_watch_movies.append(movie)
                return jsonify({
                        'status':'success'
                }),201

if __name__ == '__main__':
        app.run()
