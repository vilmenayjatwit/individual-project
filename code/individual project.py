#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# In[2]:


data3 = pd.read_csv('2022-2023 NBA Player Stats - Regular.csv', sep=';')


# In[3]:


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

top_scorers = data3.sort_values(by='PTS', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_scorers['Player'], top_scorers['PTS'], color='skyblue')

plt.title('Top 10 NBA Players by Average Points per Game (2022-2023)', fontsize=14)
plt.xlabel('Player', fontsize=12)
plt.ylabel('Average Points per Game (PTS)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)


plt.yticks(np.arange(0, top_scorers['PTS'].max() + 1, 2))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot with improved x-axis label readability
plt.tight_layout()
plt.show()


# In[4]:


print(data3.columns.tolist())


# In[5]:


# Grouping the data by position and calculating the average points per game using the initially loaded dataset
position_scoring_avg = data3.groupby('Pos')['PTS'].mean().sort_values()

# Create the bar chart
plt.figure(figsize=(12, 6))
position_scoring_avg.plot(kind='bar', color='teal')

# Adding titles and labels
plt.title('Average Points per Game by Position (2022-2023)', fontsize=14)
plt.xlabel('Position', fontsize=12)
plt.ylabel('Average Points per Game', fontsize=12)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[6]:


# Create the scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data3, x='Age', y='PTS')

# Adding a trend line
sns.regplot(data=data3, x='Age', y='PTS', scatter=False, color='red')

# Adding titles and labels
plt.title('Correlation Between Age and Scoring Ability (PTS) in NBA Players (2022-2023)', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Points per Game (PTS)', fontsize=12)

# Show the plot
plt.show()


# In[7]:


# Grouping the data by team and calculating the average points per game
team_performance_avg = data3.groupby('Tm')['PTS'].mean().sort_values()

# Create the bar chart
plt.figure(figsize=(14, 8))
team_performance_avg.plot(kind='bar', color='purple')

# Adding titles and labels
plt.title('Average Points per Game by Team (2022-2023 NBA Season)', fontsize=16)
plt.xlabel('Team', fontsize=14)
plt.ylabel('Average Points per Game', fontsize=14)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:




