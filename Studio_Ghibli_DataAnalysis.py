'''
    Python script that contains the data analysis of question
    2.1 Τι ξέρουμε για τις παραγωγές του πολύ δημοφιλούς Studio Ghibli

    Query : 
            db.getCollection('Anime')
            .find(
                { Studio: 'Studio Ghibli' },
                {
                Rank: 1,
                Name: 1,
                Release_year: 1,
                Type: 1,
                Tags: 1,
                Rating: 1,
                Content_Warning: 1
                }
            )
            .sort({ Release_year: 1 });

'''

import pandas as pd 
import json
import matplotlib.pyplot as plt

df = pd.read_json('Studio_Ghibli.json')
print(df.info())

# Filter rows where Release_year is not 0
df_filtered = df[df['Release_year'] != 0]

# Group by Release_year and calculate the sum of anime productions
sum_per_year = df_filtered.groupby('Release_year').size()

# Group by Release_year and calculate the mean of ratings
mean_ratings_per_year = df_filtered.groupby('Release_year')['Rating'].mean()

# Create two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot the bar chart for the sum of anime productions per year
sum_per_year = df_filtered.groupby('Release_year').size()
sum_per_year.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_xlabel('Release Year')
ax1.set_ylabel('Number of Anime Productions')
ax1.set_title('Sum of Anime Productions per Year')

# Plot the bar chart for the mean ratings per year
mean_ratings_per_year.plot(kind='bar', color='lightcoral', ax=ax2)
ax2.set_xlabel('Release Year')
ax2.set_ylabel('Mean Rating')
ax2.set_title('Mean Ratings of Anime Productions per Year')

# Adjust layout for better spacing
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Create a new DataFrame by exploding the 'Tags' column
tags_df = df.explode('Tags')

# Count the occurrences of each tag
tag_counts = tags_df['Tags'].value_counts()

# Display the top N tags (adjust N as needed)
top_tags = tag_counts.head(10)
least_used_tags = tag_counts.tail(10)

# Create subplots for top and least used tags
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the top tags
top_tags.plot(kind='bar', color='lightgreen', ax=ax1)
ax1.set_xlabel('Tag')
ax1.set_ylabel('Frequency')
ax1.set_title('Top Tags in Anime Productions')

# Plot the least used tags
least_used_tags.plot(kind='bar', color='lightcoral', ax=ax2)
ax2.set_xlabel('Tag')
ax2.set_ylabel('Frequency')
ax2.set_title('Least Used Tags in Anime Productions')

plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Count the occurrences of each anime type
type_counts = df['Type'].value_counts()

# Create a bar chart for anime types
plt.figure(figsize=(10, 6))
type_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Anime Type')
plt.ylabel('Number of Productions')
plt.title('Distribution of Anime Types')
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Count the occurrences of each content warning
content_warning_counts = df['Content_Warning'].value_counts()

# Create a bar chart for content warnings
plt.figure(figsize=(10, 6))
content_warning_counts.plot(kind='bar', color='lightcoral')
plt.xlabel('Content Warning')
plt.ylabel('Number of Productions')
plt.title('Distribution of Content Warnings in Anime Productions')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Filter rows where Release_year is not 0
df_filtered = df[df['Release_year'] != 0]

# Group by Release_year and calculate the mean of the 'Rating' column
average_rank_per_year = df_filtered.groupby('Release_year')['Rank'].mean()

# Create a line chart for the average rank per year
plt.figure(figsize=(10, 6))
average_rank_per_year.plot(marker='o', color='orange', linestyle='-', linewidth=2)
plt.xlabel('Release Year')
plt.ylabel('Average Rank')
plt.title('Average Anime Rank per Year')
plt.grid(True)
plt.show()
