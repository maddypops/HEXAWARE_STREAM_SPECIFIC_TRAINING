import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)


print("🔹 Initial Data Sample:")
print(df[['country', 'price', 'points']].head(5))

country_map = {
    "US": "USA",
    "England": "UK",
    "South Korea": "Korea"
}
df['country_standardized'] = df['country'].map(country_map).fillna(df['country'])

def price_category(price):
    if pd.isna(price):
        return "Unknown"
    elif price < 20:
        return "Budget"
    elif price < 50:
        return "Standard"
    elif price < 100:
        return "Premium"
    else:
        return "Luxury"

df['price_category'] = df['price'].apply(price_category)

df['points_grade'] = df['points'].map(lambda x: 'High' if x >= 90 else 'Low')

def summarize(row):
    return f"{row['country']} - {row['variety']} - {row['points']} pts"

df['summary'] = df.apply(summarize, axis=1)

print("\n Transformed Sample:")
print(df[['country', 'country_standardized', 'price', 'price_category', 'points', 'points_grade', 'summary']].head(10))

df.to_csv("transformed_winemag_data.csv", index=False)
print("\nTransformed data saved to 'transformed_winemag_data.csv'")


# isin()
print(df[df['country'].isin(['US', 'Portugal', 'Spain'])])

# str.contains()
print(df[df['description'].str.contains("Blackberry", case=False, na=False)]['description'])

# between
print(df[df['price'].between(10, 30)]['price'])

# isnull
print(df[df['price'].isnull()])
print(df[df['price'].isnull()][['title', 'price']])

# notnull
print(df[df['price'].notnull()][['title', 'price']])

# Filter Duplicates
duplicate_df = df[df.duplicated('title', keep=False)]
print(duplicate_df[['title', 'points', 'price']])

# Keep Only First Occurrence and drop the rest
df_no_duplicates = df.drop_duplicates(subset='title', keep='first')
print(df_no_duplicates[['title', 'points', 'price']].head(20))

# Display unique rows of title column
unique_titles = df[df.duplicated('title', keep=False)]['title'].unique()
print(unique_titles)

# How many times each title occurs
title_counts = df['title'].value_counts()
print(title_counts[title_counts > 1])

# Find the duplicates in multiple columns
multi_column_duplicates = df[df.duplicated(subset=['title', 'points'], keep=False)]
print(multi_column_duplicates[['title', 'points', 'country']])


