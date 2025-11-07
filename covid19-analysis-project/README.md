# 🌍 COVID-19 & World Happiness Data Analysis

This project explores how global happiness indicators correlate with the impact of the COVID-19 pandemic across different countries.
It merges **COVID-19 data** (cases, deaths) with **World Happiness Report data** (happiness score, GDP, life expectancy, etc.) to uncover meaningful insights.

---

## 📊 Objectives

* Analyze and visualize COVID-19 trends globally.
* Explore happiness indicators such as GDP per capita, social support, and life expectancy.
* Merge both datasets to study relationships between happiness and COVID-19 outcomes.
* Visualize correlations and global patterns using Python.

---

## 🧰 Tools & Libraries

* **Python 3.x**
* **Jupyter Notebook**
* **Libraries:**

  * `pandas`
  * `numpy`
  * `matplotlib`
  * `seaborn`
  * `plotly` *(optional for interactive visualizations)*

---

## 🧮 Dataset Sources

* **COVID-19 Dataset:** Daily confirmed cases, deaths, and recoveries by country.
* **World Happiness Dataset:** Happiness scores and key indicators such as GDP per capita, social support, life expectancy, and freedom.

Example happiness dataset columns:

```
Overall rank, Country or region, Score, GDP per capita, 
Social support, Healthy life expectancy, 
Freedom to make life choices, Generosity, Perceptions of corruption
```

---

## 🧹 Steps Performed

1. **Load Data:** Import and inspect COVID-19 and Happiness datasets.
2. **Clean & Preprocess:** Handle missing values and rename inconsistent columns.
3. **EDA:** Explore patterns and trends in both datasets.
4. **Merge:** Combine datasets on the `Country` column.
5. **Visualization:**

   * Correlation heatmap between happiness and COVID-19 impact.
   * Scatter plots showing how GDP and life expectancy relate to COVID-19 death rates.
6. **Insights:** Evaluate whether happier, wealthier countries had lower COVID-19 fatality rates.

---

## 🧩 Environment Setup

Create and activate a virtual environment (recommended):

```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/PulkitDubey046/covid19-analysis-project.git
   cd covid19-analysis-project
   ```

2. Open the Jupyter Notebook:

   ```bash
   jupyter notebook covid19_analysis_notebook.ipynb
   ```

3. Run all cells to reproduce the analysis and visualizations.

---

## 📈 Sample Visualizations

* **Correlation Heatmap** — relationship between happiness indicators and COVID-19 impact
* **Scatter Plot** — *Death Rate vs Happiness Score (Bubble size = Life Expectancy)*

---

## 📚 Key Insights

* Countries with **higher GDP and life expectancy** generally had **lower COVID-19 death rates**.
* Strong **social support and freedom** correlated positively with happiness and resilience during the pandemic.
* Economic and healthcare strength were critical in managing pandemic outcomes.

---

## 🧑‍💻 Author

**Pulkit Dubey**
Data Analysis | Python | Visualization


---

⭐ *If you found this useful, consider starring the repository on GitHub!*
