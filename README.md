# Movie-Recommendation-System
Built a Movie Recommendation System which will take as input a movie title from the user and return the top 50 recommended movies to the user based on the input movie.

We will use a movie dataset for our purpose. We will filter out which features to include to train our model and which features to exclude as there are many features which have no significance for recommendation purposes.

We will use difflib library here to find most common movie title to the one provided by user to account for spelling mistakes and typos. This helps us to avoid errors and make our model more usable. 

Here we will be using count vectorizer and will calculate cosine values to find out similarities so as to return to user the top 50 movies they should watch after the one they provided. It is a content based recommendation system and works pretty well!
