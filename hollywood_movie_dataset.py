import pandas as pd
import matplotlib.pyplot as plt

hollywood_movies = pd.read_csv("movies.csv")

print("Hollywood movie dataset")



plt.hist(hollywood_movies["Rotten Tomatoes %"])