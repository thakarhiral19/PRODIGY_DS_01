import pandas as pd
import matplotlib.pyplot as plt

# Load downloaded CSV
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2.csv", skiprows=4)

# Check columns
print(df.head())

# Example: Top 10 countries by latest available population
latest_year = '2023'   # or latest year column available
top10 = df[['Country Name', latest_year]].dropna().sort_values(by=latest_year, ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(top10['Country Name'], top10[latest_year])
plt.title(f"Top 10 Most Populous Countries ({latest_year})")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.show()
