import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def title_from_index(index):
    return movie[movie.index == index]["title"].values[0]

def index_from_title(title):
    title_list = movie['title'].tolist()
    common = difflib.get_close_matches(title, title_list, 1)
    titlesim = common[0]
    return movie[movie.title == titlesim]["index"].values[0]

movie = pd.read_csv("moviedata.csv")
features = ['keywords','cast','genres','director','tagline']
for feature in features:
    movie[feature] = movie[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'] +" "+row['cast']+" "+row['genres']+" "+row['director']+" "+row['tagline']
    except:
        print ("Error:", row)

movie["combined_features"] = movie.apply(combine_features,axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(movie["combined_features"])
cosine_sim = cosine_similarity(count_matrix) 

user_movie = input("Enter movie of your choice:\t")
movie_index = index_from_title(user_movie)

similar_movies =  list(enumerate(cosine_sim[movie_index]))
similar_movies_sorted = sorted(similar_movies,key=lambda x:x[1],reverse=True)
i=0
print("\nOther movies you might be interested in:-\n")
for rec_movie in similar_movies_sorted:
        if(i!=0):
            print (i,") ",title_from_index(rec_movie[0]),sep="")
        i=i+1
        if i>50:
            break