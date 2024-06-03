'''
db.getCollection('Anime').aggregate(
  [
    {
      $group: {
        _id: '$Studio',
        avgEpisodes: { $avg: '$Episodes' },
        avgRating: { $avg: '$Rating' }
      }
    },
    {
      $project: {
        Studio: '$_id',
        avgEpisodes: 1,
        avgRating: 1
      }
    },
    { $sort: { avgEpisodes: -1 } }
  ]
);
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json('Average_Episodes.Anime.json')

print(df.info())


#detect outliers in our dataset
q1 = df['avgEpisodes'].quantile(0.25)
q3 = df['avgEpisodes'].quantile(0.75)
iqr = q3 - q1
print(f'Q1 percentile: {q1}')
print(f'Q3 percentile: {q3}')
print(f'IQR percentile: {iqr}')

lower_bound_tags = q1 - 1.5 * iqr
upper_bound_tags = q3 + 1.5 * iqr

outliers_tags = ((df['avgEpisodes'] < lower_bound_tags) | (df['avgEpisodes'] > upper_bound_tags))
outlier_indices_tags = df.index[outliers_tags].tolist()
#print("Outlier indices:", outlier_indices)

print(lower_bound_tags)
print(upper_bound_tags)

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Create a boxplot for the 'avgEpisodes' column
sns.boxplot(x=df['avgEpisodes'])

# Set plot title and labels
plt.title('Boxplot of avgEpisodes')
plt.xlabel('avgEpisodes')

# Show the plot
plt.show()


# Group by 'Studio' and calculate the mean for 'avgEpisodes' and 'avgRating'
studio_stats = df.groupby('Studio').agg({'avgEpisodes': 'mean', 'avgRating': 'mean'}).reset_index()


# Select the top 10 studios based on mean episodes and ratings
top_studios_episodes = studio_stats.nlargest(10, 'avgEpisodes')
top_studios_ratings = studio_stats.nlargest(10, 'avgRating')

# Plotting the first diagram (Top 10 studios with mean episodes)
fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

# Subplot 1: Mean Episodes
ax1.bar(top_studios_episodes['Studio'], top_studios_episodes['avgEpisodes'], color='b', alpha=0.7, label='Mean Episodes')
ax1.set_ylabel('Mean Episodes', color='b')
ax1.tick_params('y', colors='b')
ax1.set_title('Top 10 Studios by Mean Episodes')

# Subplot 2: Mean Ratings
ax2.bar(top_studios_episodes['Studio'], top_studios_episodes['avgRating'], color='r', alpha=0.7, label='Mean Ratings')
ax2.set_ylabel('Mean Ratings', color='r')
ax2.tick_params('y', colors='r')

# Adjust layout and display the first plot
plt.tight_layout()
plt.show()

# Plotting the second diagram (Top 10 studios with mean ratings)
fig2, (ax3, ax4) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

# Subplot 1: Mean Ratings
ax3.bar(top_studios_ratings['Studio'], top_studios_ratings['avgRating'], color='r', alpha=0.7, label='Mean Ratings')
ax3.set_ylabel('Mean Ratings', color='r')
ax3.tick_params('y', colors='r')
ax3.set_title('Top 10 Studios by Mean Ratings')

# Subplot 2: Mean Episodes
ax4.bar(top_studios_ratings['Studio'], top_studios_ratings['avgEpisodes'], color='b', alpha=0.7, label='Mean Episodes')
ax4.set_ylabel('Mean Episodes', color='b')
ax4.tick_params('y', colors='b')

# Adjust layout and display the second plot
plt.tight_layout()
plt.show()
