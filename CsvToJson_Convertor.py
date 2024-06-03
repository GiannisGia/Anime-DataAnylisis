'''
Authors:    GIANNOPOULOS GEORGIOS
            GIANNOPOULOS IOANNIS

Description:    1.Quick view of our data
                2.Fill NaN values of the columns with placeholder values
                3.Format the csv file to json with the right 
                
         
'''
import pandas as pd 
import json

df = pd.read_csv('Anime.csv')

print(df.info())
#Output of the df info 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18495 entries, 0 to 18494
Data columns (total 17 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   Rank             18495 non-null  int64  
 1   Name             18495 non-null  object 
 2   Japanese_name    7938 non-null   object 
 3   Type             18495 non-null  object 
 4   Episodes         9501 non-null   float64
 5   Studio           12018 non-null  object 
 6   Release_season   4116 non-null   object 
 7   Tags             18095 non-null  object 
 8   Rating           15364 non-null  float64
 9   Release_year     18112 non-null  float64
 10  End_year         2854 non-null   float64
 11  Description      18491 non-null  object 
 12  Content_Warning  1840 non-null   object 
 13  Related_Mange    7627 non-null   object 
 14  Related_anime    10063 non-null  object 
 15  Voice_actors     15309 non-null  object 
 16  staff            13005 non-null  object 
dtypes: float64(4), int64(1), object(12)
memory usage: 2.4+ MB
None
'''
# Fill missing values with a specific value, fill NaN values in 'Episodes' with 0
df['Episodes'].fillna(0, inplace=True)

#Fill missing values with a specific value
df['Japanese_name'].fillna('Unknown', inplace=True)

# Fill missing values in 'Studio' with a placeholder value, 'Unknown'
df['Studio'].fillna('Unknown', inplace=True)

# Fill missing values in 'Release_season' with a placeholder value, 'Unknown'
df['Release_season'].fillna('Unknown', inplace=True)

# Fill missing values in 'Tags' with a placeholder value, 'Unknown'
df['Tags'].fillna('Unknown', inplace=True)

# Fill missing values in 'Rating' with the mean of the existing values
mean_rating = df['Rating'].mean()
rounded_mean_rating = round(mean_rating, 2)
df['Rating'].fillna(rounded_mean_rating, inplace=True)

# Fill missing values in 'Release_year' with a placeholder value, 0
df['Release_year'].fillna(0, inplace=True)

# Fill missing values in 'End_year' with a placeholder value, 0
df['End_year'].fillna(0, inplace=True)

# Fill missing values in 'Content_Warning' with a placeholder value, 'None'
df['Description'].fillna('Unknown', inplace=True)

# Fill missing values in 'Content_Warning' with a placeholder value, 'None'
df['Content_Warning'].fillna('None', inplace=True)

# Fill missing values in 'Related_Mange' with a placeholder value, 'None'
df['Related_Mange'].fillna('None', inplace=True)

# Fill missing values in 'Related_anime' with a placeholder value, 'None'
df['Related_anime'].fillna('None', inplace=True)

# Fill missing values in 'Voice_actors' with a placeholder value, 'Unknown'
df['Voice_actors'].fillna('Unknown', inplace=True)

# Fill missing values in 'staff' with a placeholder value, 'Unknown'
df['staff'].fillna('Unknown', inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_anime.csv', index=False)


print(f'Updated csv info\n {df.info()}')

# Function to convert comma-separated values to a list

def convert_to_array(val_str):
    '''
    Function in order to seperate the values in columns with\n
    with the pattern val1, val2, val3,..., valn\n
    and return an array \n
    that we need to access later in mongoDB

    '''
    if pd.notna(val_str):
        return [val.strip() for val in val_str.split(',')]
    return None

# Apply the function to the 'Tags' column


df['Tags'] = df['Tags'].apply(convert_to_array)

df['Content_Warning'] = df['Content_Warning'].apply(convert_to_array)

df['Related_Mange'] = df['Related_Mange'].apply(convert_to_array)

df['Related_anime'] = df['Related_anime'].apply(convert_to_array)

# Function to parse the 'staff' field and extract details
def parse_staff_details(staff_str):
    details = []
    if pd.notna(staff_str):
        entries = staff_str.split(', ')
        for entry in entries:
            if ' : ' in entry:
                name, role = entry.split(' : ', 1)
                details.append({role : name})
            else:
                details.append({None : entry})
    return details

# Apply the parsing function to the 'staff' column
df['staff'] = df['staff'].apply(parse_staff_details)

# Convert DataFrame to JSON 
json_data = df.to_json(orient='records', lines=False, force_ascii=False)

# Save the JSON data to a file
with open('anime.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)