# Prodigy InfoTech Task 1
# Visualizing World Bank Population Distribution

import pandas as pd
import matplotlib.pyplot as plt

# STEP 1:
# After downloading and extracting the ZIP file,
# keep the CSV file in the same folder as this script.
# Example file name:
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2.csv"

# STEP 2: Load dataset
# World Bank files usually have metadata in first 4 rows
df = pd.read_csv(file_path, skiprows=4)

# STEP 3: Preview data
print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

# STEP 4: Choose latest year column
# Change if your file has a different latest year
latest_year = "2023"

# STEP 5: Remove missing values and sort
population_data = df[["Country Name", latest_year]].dropna()

# STEP 6: Top 10 most populous countries
top10 = population_data.sort_values(by=latest_year, ascending=False).head(10)

print("\nTop 10 Countries by Population:")
print(top10)

# STEP 7: BAR CHART
plt.figure(figsize=(12,6))
plt.bar(top10["Country Name"], top10[latest_year])

plt.title(f"Top 10 Most Populous Countries ({latest_year})")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
