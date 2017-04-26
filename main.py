import pandas as pd
import numpy as np
import graphlab as gl
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep ='\t', names=r_cols, encoding='latin-1')

i_cols = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'Unknown',
          'Action','Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='\t', names=i_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')

# gl.get_dependencies()

train_data = gl.SFrame(ratings_base)
test_data = gl.SFrame(ratings_test)

# A simple Popularity model
popularity_model = gl.popularity_recommender.create(train_data, user_id='user_id', item_id='movie_id',
                                                    target='rating')
#demo slice
popularity_recomm = popularity_model.recommend(users=range(1,6),k=5)
# popularity_recomm.print_rows(num_rows=25)

# print ratings_base.groupby(by='movie_id')['rating'].mean().sort_values(ascending=False).head(20)

#Collaborative Filtering
# Jaccard Similarity, Cosine Similairty, Pearson Similarity

item_sim_model = gl.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id',
                                                       target='rating',similarity_type='pearson')
#demo slice
item_sim_recomm = item_sim_model.recommend(users=range(1,6), k=5)
# item_sim_recomm.print_rows(num_rows=25)

model_performance = gl.compare(test_data,[popularity_model, item_sim_model])
gl.show_comparison(model_performance, [popularity_model, item_sim_model])