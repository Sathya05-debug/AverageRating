import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('Dataset.csv')
print(data.head())
print(data.info())
relevant_data=data[['Aggregate rating','Votes']]
print(relevant_data.isnull().sum())
plt.figure(figsize=(10,6))
sns.histplot(data['Aggregate rating'],bins=20,kde=True,color='skyblue')
plt.title('Distribution of Aggregate Ratings',fontsize=16)
plt.xlabel('Aggregate Ratings',fontsize=12)
plt.ylabel('Frequency of Aggregate Ratings',fontsize=12)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()
rating_bins=pd.cut(data['Aggregate rating'],bins=[0,1,2,3,4,5],right=False)
most_common_range=rating_bins.value_counts.idxmax()
print(f"The Most Common Votes Rating is:{most_common_range}")
avg_votes=data['Votes'].mean()
print(f"The Average Votes Rating is:{avg_votes}")
plt.figure(figsize=(10,6))
sns.barplot(x=['Average Votes'],y=[avg_votes],palette='viridis')
plt.title('Average number of votes',fontsize=16)
plt.xlabel('Votes',fontsize=12)
plt.show()


