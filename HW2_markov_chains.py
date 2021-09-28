# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:38:42 2021

@author: Hriday Singh, Iain Muir, and Connor Smith
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import expon
import scipy

# data = pd.read_csv(r"C:/Users/hrida/Documents/Stat_sports_analytics/SB_box_scores_2019_without_rank.csv")
data = pd.read_csv(r"/Users/iainmuir/Desktop/4Y 1S/STAT 4800/Homework/HW 2/SB_box_scores_2019_without_rank.csv")


teams = np.unique(pd.concat([data["Winner"],data["Loser"]]))

teams = pd.Series(teams).reset_index()

teams["team_id"]= teams["index"]

#teams.index = teams.iloc[:,1]

data2 = data.merge(teams, left_on="Winner",right_on= 0)

data2 = data2.merge(teams, left_on="Loser",right_on= 0)

data2["winner_id"] = data2["team_id_x"].astype(int)
data2["loser_id"] = data2["team_id_y"].astype(int)

data2["diff"] = data2.Pts_winner-data2.Pts_loser

#%%

### Matrix of point differentials with winning team as columns and losing team
### as rows
points_matrix = np.zeros((len(teams),len(teams)))
points_list = []

for row in data2[["team_id_x","team_id_y","diff"]].values:
    x, y, diff = row
    # points_matrix[x,y] += min(75 + diff,100)
    # points_matrix[y,x] -= max(25-diff,1)
    points_matrix[x, y] += min(diff+75, 100)
    points_matrix[y, x] -= max(25-diff, 1)
    points_list.append(diff)

#%%

#%%

### Matrix of point differentials as a percentage of total point differential
points_matrix_props = points_matrix/points_matrix.sum(axis=0)
        
points_matrix_props[points_matrix_props == -0.] = 0

print(points_matrix_props)
exit(0)
        
#%%



initial_steady = np.ones(len(teams))*(1/217)
initial_steady = initial_steady.reshape(1, 217)




current = np.zeros(217).reshape(1,217)



epsilon = 0.05
for i in range(100):
    if sum(sum(initial_steady-current))<epsilon:
        break
    else:
        current= initial_steady
    initial_steady = initial_steady.dot(points_matrix_props)
    
# while sum(sum(initial_steady-current))<epsilon:
#     current= initial_steady
#     initial_steady = initial_steady.dot(points_matrix_props)


#%%

ranking = pd.DataFrame(np.flip(np.argsort(initial_steady[0])))

ranking.columns = ["team_id"]

team_rankings = ranking.merge(teams, left_on = "team_id", right_on = "index").loc[:,0]
print(team_rankings)

#%%


# plt.hist(points_list)
_, bins, _ = plt.hist(points_list, 20, density=1, alpha=0.5)
loc, scale = expon.fit(points_list)
best_fit_line = scipy.stats.expon.pdf(bins, loc, scale)
plt.plot(bins, best_fit_line)
plt.show()





