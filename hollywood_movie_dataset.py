import pandas as pd
import matplotlib.pyplot as plt

hollywood_movies = pd.read_csv("movies.csv")

print("Hollywood movie dataset")

#Part 3 filtering out movies with a rotten tomatoes score less than 45%.

filtered_list = []

for i in range(len(hollywood_movies["Rotten Tomatoes %"])):
    if hollywood_movies["Rotten Tomatoes %"][i] >= 45:
        filtered_list.append(hollywood_movies["Rotten Tomatoes %"][i])


print(filtered_list)

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