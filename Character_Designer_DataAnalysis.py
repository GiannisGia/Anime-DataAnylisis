'''
db.getCollection('Anime').aggregate(
  [
    { $unwind: '$staff' },
    {
      $match: {
        'staff.Character Design': {
          $exists: true
        }
      }
    },
    {
      $group: {
        _id: '$staff.Character Design',
        animeCount: { $sum: 1 },
        studios: { $addToSet: '$Studio' },
        averageRating: { $avg: '$Rating' }
      }
    },
    {
      $project: {
        _id: 0,
        designerName: '$_id',
        animeCount: 1,
        studios: 1,
        averageRating: 1
      }
    },
    { $sort: { animeCount: 1 } }
  ],
  { maxTimeMS: 60000, allowDiskUse: true }
);
'''
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# Load data
df = pd.read_json('Character_Designer.json')

# Display basic information about the DataFrame
print(df.head())

# Sample data if it's too large
df_sample = df.sample(frac=0.1, random_state=42)

# Get the top 5 character designers based on anime count
top_5_anime_count = df.nlargest(20, 'animeCount')

# Bar plot for anime count (Top 5)
plt.figure(figsize=(12, 6))
sns.barplot(x='animeCount', y='characterDesigner', data=top_5_anime_count, palette='viridis')
plt.title('Top 20 Character Designers by Anime Count')
plt.xlabel('Anime Count')
plt.ylabel('Character Designer')
plt.show()

# Get the top 5 character designers based on production studios count
top_5_production_studios = df.nlargest(20, 'productionStudios')

# Bar plot for production studios count (Top 5)
plt.figure(figsize=(12, 6))
sns.barplot(x='productionStudios', y='characterDesigner', data=top_5_production_studios, palette='viridis')
plt.title('Top 20 Character Designers by Production Studios Count')
plt.xlabel('Production Studios Count')
plt.ylabel('Character Designer')
plt.show()

# Get the top 5 character designers based on average rating
top_5_average_rating = df.nlargest(20, 'averageRating')

# Bar plot for average rating (Top 5)
plt.figure(figsize=(12, 6))
sns.barplot(x='averageRating', y='characterDesigner', data=top_5_average_rating, palette='viridis')
plt.title('Top 20 Character Designers by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Character Designer')
plt.show()
