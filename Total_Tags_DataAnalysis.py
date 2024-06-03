'''
db.getCollection('Anime').aggregate(
  [
    { $unwind: '$Tags' },
    {
      $group: { _id: '$Tags', count: { $sum: 1 } }
    },
    { $sort: { count: -1 } },
    {
      $project: {
        _id: 0,
        tag: '$_id',
        anime_count: '$count'
      }
    }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);

'''

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_json('Total_Tags_Used.Anime.json')

print(df.info())

# Select the top 15 and least 15 tags
top_15_tags = df.head(15)
least_15_tags = df.tail(15)

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# Plot for top 15 tags
top_bars = axes[0].bar(top_15_tags['tag'], top_15_tags['anime_count'], color='blue')
axes[0].set_title('Top 15 Tags')
axes[0].set_xlabel('Tag')
axes[0].set_ylabel('Anime Count')
axes[0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# Annotate bars with actual anime_count
for bar in top_bars:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval)}', ha='center', va='bottom')

# Plot for least 15 tags
least_bars = axes[1].bar(least_15_tags['tag'], least_15_tags['anime_count'], color='red')
axes[1].set_title('Least 15 Tags')
axes[1].set_xlabel('Tag')
axes[1].set_ylabel('Anime Count')
axes[1].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# Annotate bars with actual anime_count
for bar in least_bars:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval)}', ha='center', va='bottom')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()