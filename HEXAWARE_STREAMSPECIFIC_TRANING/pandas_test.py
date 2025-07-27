import pandas as pd
print(pd.__version__)

# Data Creation
# Data Clean up
# Data Transformation

df1 = pd.DataFrame({'Team 1': [24, 12, 9], 'Team 2': [5, 12, 14]})
print(df1)

df2 = pd.DataFrame({
    'customer 1': ['Product was Good', 'worth for cost'],
    'customer 2': ['Moderate Quality', 'Not as expected']
}, index=['comment 1', 'comment 2'])
print(df2)

oddSeries = pd.Series(
    [10, 30, 50, 70],
    index=['row 1', 'Row 2', 'Row 3', 'Row 4'],
    name='Odd Numbers'
)
print(oddSeries)

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())  # top 5 records

# Select Columns
print(wine_reviews.country)
print(wine_reviews['country'])
print(wine_reviews['country'].iloc[5])
print(wine_reviews.iloc[0])
print(wine_reviews.iloc[:, 0])
print(wine_reviews.iloc[:3, 1])
print(wine_reviews.iloc[[1, 3, 4, 6], 1])
print(wine_reviews.iloc[-5])

# Select based on Label
print(wine_reviews.loc[10, 'country'])
print(wine_reviews)  # Native Accessor

# Select specific Columns
new_reviews = wine_reviews.loc[:, ['country', 'points', 'price', 'winery']]
print(new_reviews)

# Set index
print(wine_reviews.set_index("winery"))

# Conditional Selections
print(wine_reviews.country == "France")
print(wine_reviews.loc[wine_reviews.country == "France"])
print(wine_reviews.loc[(wine_reviews.country == "Italy") & (wine_reviews.price > 60)])  # returns matched rows
print(wine_reviews.loc[(wine_reviews.country == "Italy") & (wine_reviews.price > 60), ["country", "price"]])
print(wine_reviews.loc[wine_reviews.country.isin(["Italy", "France"]), ["country", "price"]])
print(wine_reviews.loc[wine_reviews.price.notnull()])
wine_reviews['test column'] = "test 1"
print(wine_reviews.head())

# Summary Functions
print(wine_reviews.describe())
print(wine_reviews.country.describe())
print(wine_reviews.points.mean())

# These lines were originally problematic or unnecessary
print(wine_reviews.title.mean())  # title is likely a string column
print(wine_reviews.title.unique())
print(wine_reviews.country.value_counts().get("Argentina"))
print((wine_reviews.country == "Spain").sum())
print(wine_reviews.loc[wine_reviews.country == "Spain"].shape[0])


first_price = df1['price'].iloc[0]
print(first_price)


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


