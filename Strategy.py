'''
[
    {
        '$group': {
            '_id': '$Studio', 
            'average_episodes': {
                '$avg': '$Episodes'
            }, 
            'average_rating': {
                '$avg': '$Rating'
            }
        }
    }, {
        '$project': {
            'Studio': '$_id', 
            'average_episodes': 1, 
            'average_rating': 1, 
            '_id': 0
        }
    }
]
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read data from JSON file
df = pd.read_json('Studio_Strategy.json')
print(df.info())

# Filter rows where Studio is not null
df_filtered = df[df['Studio'].notna()]

# Select the first 20 rows
top_20_studios = df.head(20)


# Create two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,6))

# Rotate x-axis labels for better readability
ax1.set_xticklabels(top_20_studios['Studio'], rotation=45, ha='right')

#custom_y_ticks = [1.0, 3.0]
#ax1.set_yticks(custom_y_ticks)

# Plot the bar chart for the count of studios
ax1.bar(top_20_studios['Studio'], top_20_studios['average_rating'])
ax1.set_title('Bar Chart of Studio Ratings')
ax1.set_xlabel('Studio')
ax1.set_ylabel('Average Rating')

ax2.set_xticklabels(top_20_studios['Studio'], rotation=45, ha='right')
# Plot the box plot for the studios
ax2.bar(top_20_studios['Studio'], top_20_studios['average_episodes'])
ax2.set_title('Bar Chart of Studio Episodes')
ax2.set_xlabel('Studio')
ax2.set_ylabel('Average Episodes')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
