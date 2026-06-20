import pandas as pd
import matplotlib.pyplot as plt

# load the netflix dataset
df = pd.read_csv("netflix_titles.csv")
print(df.shape)

# quick check - any missing data?
print(df.isnull().sum())

# movies vs tv shows
print(df['type'].value_counts())

plt.figure(figsize=(6, 4))
df['type'].value_counts().plot(kind='bar', color=['#E50914', 'gray'])
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')

# which countries produce the most content?
print(df['country'].value_counts().head(10))

plt.figure(figsize=(10, 6))
df['country'].value_counts().head(10).plot(kind='barh', color='#E50914')
plt.title('Top 10 Countries on Netflix')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_countries.png')

# how many titles have no director listed?
missing = df['director'].isnull().sum()
print(f"{missing} titles missing a director ({round(missing/len(df)*100)}%)")

# average movie length
movies = df[df['type'] == 'Movie'].copy()
movies = movies.dropna(subset=['duration'])
movies['minutes'] = movies['duration'].str.replace(' min', '').astype(int)
print(f"average movie length: {round(movies['minutes'].mean())} mins")

print("done!")