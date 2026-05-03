import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import zipfile

# Updated URL to directly download the CSV data from the World Bank API
url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"

# Download the ZIP file content
response = requests.get(url)
response.raise_for_status() # Raise an exception for HTTP errors

# Read the content as a BytesIO object
zip_file_content = io.BytesIO(response.content)

# Open the ZIP file
with zipfile.ZipFile(zip_file_content, 'r') as zf:
    # Find the CSV file within the ZIP archive (usually only one data CSV)
    # The actual data CSV usually starts with 'API_' and ends with '.csv'
    csv_file_name = [f for f in zf.namelist() if f.startswith('API_') and f.endswith('.csv')][0]
    
    # Read the CSV file into a DataFrame
    # World Bank CSVs often have metadata at the beginning; typically the actual header starts later.
    df = pd.read_csv(zf.open(csv_file_name), encoding='latin1', skiprows=3)

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
plt.savefig("population_chart.png")
plt.show()

