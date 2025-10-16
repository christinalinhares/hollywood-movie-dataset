import pandas as pd
import matplotlib.pyplot as plt

hollywood_movies = pd.read_csv("movies.csv")

print("Hollywood movie dataset")

#Part 4. H 

plt.hist(hollywood_movies["Rotten Tomatoes %"])

import numpy as np 


x=np.array([0.,20.,40.6,80.1])
y=np.array([0,2,8,10])

plt.plot(x,y)
plt.xlabel("Rotten Tomatoes %")
plt.ylabel("Number of movies")
plt.title("corellation of rottan tomatoes and number of movies")
plt.show()