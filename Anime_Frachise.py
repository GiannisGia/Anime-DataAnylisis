'''
[
    {
        '$match': {
            'Related_anime': {
                '$exists': True
            }
        }
    }, {
        '$group': {
            '_id': '$Related_anime', 
            'Total_Anime': {
                '$sum': 1
            }, 
            'Average_Episodes': {
                '$avg': '$Episodes'
            }, 
            'Production_Period': {
                '$min': '$Release_year'
            }, 
            'Rating_MO': {
                '$avg': '$Rating'
            }
        }
    }, {
        '$sort': {
            'Total_Anime': -1
        }
    }
]
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read data from JSON file
df = pd.read_json('Franchise.json')
print(df.info())

# Filter rows where Total_Anime is not null
df_filtered = df[df['Total_Anime'].notna()]

# Extract franchise name from _id column
df['Franchise'] = df['_id'].apply(lambda x: x[0].split(':')[0] if isinstance(x, list) and len(x) > 0 else None)

# Select the first 20 rows
top_20_franchise = df.head(20)

# Create a subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Set ticks and rotate x-axis labels
franchise_names = top_20_franchise['Franchise']
x_values = range(len(franchise_names))

ax1.set_xticks(x_values)
ax1.set_xticklabels(franchise_names, rotation=45, ha='right')
ax2.set_xticks(x_values)
ax2.set_xticklabels(franchise_names, rotation=45, ha='right')

# Plot the bar chart for the count of studios
ax1.bar(x_values, top_20_franchise['Average_Episodes'])
ax1.set_title('Bar Chart of Average Episodes per Franchise')
ax1.set_xlabel('Franchise')
ax1.set_ylabel('Average Episodes')

# Plot the bar chart for the count of studios
ax2.bar(x_values, top_20_franchise['Rating_MO'])
ax2.set_title('Bar Chart of Mean Rating per Franchise')
ax2.set_xlabel('Franchise')
ax2.set_ylabel('Rating_MO')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
