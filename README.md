

````markdown
# 🦠 COVID-19 Data Analysis and Visualization

**Author:** Hosama Adem  
**Libraries Used:** `requests`, `pandas`, `matplotlib`, `seaborn`

---

## 📘 Overview
This Python project fetches real-time COVID-19 data for a selected country using the **COVID-19 API** and performs data analysis and visualization.  
It shows daily trends for confirmed cases, deaths, and recoveries, and visualizes correlations between these metrics.

---

## ⚙️ Features
- Fetches COVID-19 historical data for any country from the public API  
- Cleans and processes data using **pandas**  
- Calculates **daily new cases**, **deaths**, and **recoveries**  
- Visualizes data using **matplotlib** and **seaborn**  
- Displays a **correlation heatmap** between total cases, deaths, and recoveries  

---

## 🧩 Requirements
Install the necessary Python libraries:

```bash
pip install requests pandas matplotlib seaborn
````

---

## 🚀 How to Run

1. Clone or download this project folder
2. Open the folder in **VS Code** or any Python IDE
3. Run the script:

   ```bash
   python covid_analysis.py
   ```
4. The script will fetch data (default: **Ethiopia**) and display:

   * Summary statistics in the terminal
   * Line plots for daily trends
   * A correlation heatmap

---

## 🌍 Change Country

To analyze a different country, edit the line in the script:

```python
country = "ethiopia"
```

For example:

```python
country = "kenya"
```

---

## 📊 Example Output

* **Line Chart:** Daily confirmed, deaths, and recovered cases
* **Heatmap:** Correlation between total confirmed, deaths, and recovered

---

## ⚠️ Notes

* Requires an active internet connection
* If you are behind a proxy or VPN, add this to the request:

  ```python
  response = requests.get(url, proxies={"http": None, "https": None})
  ```
* API used: [COVID19 API](https://covid19api.com)

---

## 🧠 Future Improvements

* Add automatic retries for failed API requests
* Include data caching for offline analysis
* Support multi-country comparison

---

```

