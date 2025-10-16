

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
hollywood_movies = pd.read_csv("movies.csv")

print("Hollywood movie dataset")

#Part 3 filtering out movies with a rotten tomatoes score less than 45%.

filtered_list = []

for i in range(len(hollywood_movies["Rotten Tomatoes %"])):
    if hollywood_movies["Rotten Tomatoes %"][i] >= 45:
        filtered_list.append(hollywood_movies["Rotten Tomatoes %"][i])


print(filtered_list)


# F (Scatter plot of Profitability vs Audience Score)
clean_data=hollywood_movies.dropna(subset=["Profitability","Audience score %"])
profitability=clean_data["Profitability"].to_numpy()                       
audience_score=clean_data["Audience score %"].to_numpy()
plt.scatter(profitability,audience_score,color="blue",marker="o",label="Movies")
plt.title("Profitability vs Audience Score")
plt.xlabel("Profitability (x times the budget)")
plt.ylabel("Audience Score (%)")
plt.grid(True)
plt.legend()
plt.show()

#Part 4 H 

plt.hist(hollywood_movies["Rotten Tomatoes %"])

x=np.array([0.,20.,40.6,80.1])
y=np.array([0,2,8,10])

plt.plot(x,y)
plt.xlabel("Rotten Tomatoes %")
plt.ylabel("Number of movies")
plt.title("Correlation of Rottan Tomatoes and Number of Movies")
plt.show()


#Part 4,i(Lead Studio)
rt_count = hollywood_movies.groupby("Lead Studio").size()
print(rt_count)
y=np.array([2,1,8,6,18,2,1,4,4,5,3,7,14])
mylabels=["20th Century Fox","CBS","Disney","Fox","Independent","Lionsgate","New Line","Paramount","Sony","Summit","The Weinstein Company","Universal","Warner Bros."]
plt.pie(y,labels=mylabels)
plt.show()
   