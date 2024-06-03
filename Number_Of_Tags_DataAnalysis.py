'''
    db.getCollection('Anime')
    .find(
        {},
        {
        Rank: 1,
        Rating: 1,
        Tags: { $size: '$Tags' }
        }
    )
    .sort({ Rating: -1 });

'''

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_json('NumberOfTagsPerAnime.json')
print(df.info())


print(df['Tags'].mean())

# Assuming df is your DataFrame
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(df['Tags'], df['Rating'], alpha=0.5)
plt.title('Relationship between Tags and Rating of Animes')
plt.xlabel('Number of Tags')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

correlation_coefficient = df['Tags'].corr(df['Rating']) #   pearson : Standard correlation coefficient
print(f'Correlation Coefficient: {correlation_coefficient}')

#detect outliers in our dataset
Q1 = df['Rating'].quantile(0.25)
Q3 = df['Rating'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = ((df['Rating'] < lower_bound) | (df['Rating'] > upper_bound))
outlier_indices = df.index[outliers].tolist()

print(lower_bound)
print(upper_bound)

#detect outliers in our dataset
q1 = df['Tags'].quantile(0.25)
q3 = df['Tags'].quantile(0.75)
iqr = q3 - q1

lower_bound_tags = q1 - 1.5 * iqr
upper_bound_tags = q3 + 1.5 * iqr

outliers_tags = ((df['Tags'] < lower_bound_tags) | (df['Tags'] > upper_bound_tags))
outlier_indices_tags = df.index[outliers_tags].tolist()
#print("Outlier indices:", outlier_indices)

print(lower_bound_tags)
print(upper_bound_tags)
