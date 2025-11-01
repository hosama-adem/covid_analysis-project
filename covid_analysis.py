# COVID-19 Data Analysis and Visualization
# Author: Hosama Adem
# Libraries: requests, pandas, matplotlib, seaborn

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Fetch data from COVID-19 API
country = "ethiopia"   # You can change to any country name, we peck ethiopia
url = f"https://api.covid19api.com/dayone/country/{country}"

print(f"Fetching data for {country.title()}...")
response = requests.get(url)
data = response.json() #we convert to json 

# 2️⃣ Load into pandas DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Confirmed', 'Deaths', 'Recovered']].drop_duplicates()

# 3️⃣ Create new columns for daily trends
df['DailyConfirmed'] = df['Confirmed'].diff().fillna(0)
df['DailyDeaths'] = df['Deaths'].diff().fillna(0)
df['DailyRecovered'] = df['Recovered'].diff().fillna(0)

# 4️⃣ Summary stats
print("\nSummary of the data:")
print(df.describe())

# 5️⃣ Plot trends
plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='DailyConfirmed', data=df, label='Daily Confirmed', color='blue')
sns.lineplot(x='Date', y='DailyDeaths', data=df, label='Daily Deaths', color='red')
sns.lineplot(x='Date', y='DailyRecovered', data=df, label='Daily Recovered', color='green')
plt.title(f'COVID-19 Daily Trends in {country.title()}')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.show()

# 6️⃣ Correlation heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df[['Confirmed','Deaths','Recovered']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between COVID-19 Metrics')
plt.show()
