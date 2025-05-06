# 🐼 14-Day Pandas Mastery Plan – From Beginner to Job-Ready

**Goal:** Learn and master Pandas for real-world data analysis through structured, industry-standard daily practice.

---

## 🧠 How to Use This Plan

Each day is structured into:

- ✅ Concepts with real-world context  
- 🛠️ Practice Tasks  
- 📊 Mini Projects  
- 🔄 Enhancement Tips  

**Tools:**  
Use **Jupyter Notebook** or **VS Code**.  
Track progress with **Notion**, **Google Sheets**, or a **Markdown journal**.

---

## 📅 Day-by-Day Breakdown

### 🗓️ Day 1 – Intro to Pandas & Series

**🔍 Real-World Scenario:**  
Track daily expenses or student marks using Series (better than Excel formulas).

**✅ Concepts**
- What is Pandas? Why it’s vital in Data Science
- Installing & importing Pandas
- Creating Series from list, dict, NumPy array
- Indexing, slicing, broadcasting
- Series operations: arithmetic, comparison

**🛠️ Practice**
- Create a Series of daily expenses
- Create Series for temperatures
- Series of student marks

**📊 Mini Project**
- Budget Tracker (food, transport, rent)

**🔄 Enhancements**
- Use `.index`, `.values`, `.name`
- Try slicing with steps: `series[::2]`

---

### 🗓️ Day 2 – DataFrames

**🔍 Real-World Scenario:**  
Manage structured data like students' info: name, subject, and marks.

**✅ Concepts**
- Create DataFrames from dicts, lists, arrays
- Understand `.shape`, `.dtypes`, `.columns`, `.index`
- Inspect with `.head()`, `.tail()`, `.info()`, `.describe()`

**🛠️ Practice**
- Build student DataFrame (name, subject, marks)

**📊 Mini Project**
- Movie catalog: name, genre, rating, year

**🔄 Enhancements**
- Rename columns
- Convert Series dict to DataFrame

---

### 🗓️ Day 3 – Indexing & Filtering

**🔍 Real-World Scenario:**  
Filter top students or products under ₹1000 with high ratings.

**✅ Concepts**
- Column selection
- `.loc[]` (label), `.iloc[]` (position)
- Boolean filters & conditional chaining

**🛠️ Practice**
- Filter marks > 80
- Filter products under ₹1000 and rating > 4.5

**📊 Mini Project**
- Filter job listings by location & salary

**🔄 Enhancements**
- Use `&`, `|`, and `~` for advanced conditions

---

### 🗓️ Day 4 – Data Cleaning

**🔍 Real-World Scenario:**  
Clean messy CSV files with missing values and bad formatting.

**✅ Concepts**
- Handle nulls: `.isnull()`, `.fillna()`, `.dropna()`
- Remove duplicates: `.duplicated()`, `.drop_duplicates()`
- Change data types: `.astype()`
- Clean strings: `.str.strip()`, `.str.lower()`, `.str.replace()`

**🛠️ Practice**
- Clean fake data CSV with nulls and string issues

**📊 Mini Project**
- Clean e-commerce reviews dataset

**🔄 Enhancements**
- Use regex in `.str.replace()`
- Clean phone numbers, emails

---

### 🗓️ Day 5 – Data Transformation

**🔍 Real-World Scenario:**  
Grade students, normalize prices, group sales.

**✅ Concepts**
- `.apply()`, `.map()`, `.applymap()`
- `.sort_values()`, `.sort_index()`
- `.groupby()` with `.agg()`, `.transform()`

**🛠️ Practice**
- Grade assignment using `.apply()`
- Group movies by genre and calculate averages

**📊 Mini Project**
- Supermarket sales grouped by product & region

**🔄 Enhancements**
- Try lambda functions with `.apply()`

---

### 🗓️ Day 6 – Merge & Combine

**🔍 Real-World Scenario:**  
Combine employee info, salaries, and departments.

**✅ Concepts**
- Combine: `pd.concat()`
- Merge: `pd.merge()` with different joins
- Join: `.join()`

**🛠️ Practice**
- Merge student info with grades
- Concatenate monthly sales DataFrames

**📊 Mini Project**
- Merge orders, payments, and shipping status

**🔄 Enhancements**
- Handle mismatched/missing keys

---

### 🗓️ Day 7 – File Input/Output

**🔍 Real-World Scenario:**  
Load and save data from CSV, Excel, or JSON.

**✅ Concepts**
- Load: `pd.read_csv()`, `.read_excel()`, `.read_json()`
- Save: `.to_csv()`, `.to_excel()`
- Handle encodings, separators

**🛠️ Practice**
- Load Titanic dataset, save cleaned version

**📊 Mini Project**
- Import Excel → Clean → Export to JSON

**🔄 Enhancements**
- Work with `sep='|'` or `encoding='utf-8'`

---

### 🗓️ Day 8 – Categorical & Text Data

**🔍 Real-World Scenario:**  
Analyze job titles or product names with text functions.

**✅ Concepts**
- `.astype(\"category\")`
- `.value_counts()`
- String methods: `.str.lower()`, `.str.extract()`, `.str.contains()`

**🛠️ Practice**
- Clean and count top job titles
- Extract domain names from emails

**📊 Mini Project**
- Analyze product review text

**🔄 Enhancements**
- Use `.cat.codes` for ML encoding

---

### 🗓️ Day 9 – Time Series Analysis

**🔍 Real-World Scenario:**  
Analyze COVID trends or temperature logs over time.

**✅ Concepts**
- `pd.to_datetime()`
- Set datetime index
- Resample with `.resample('M')`
- Rolling average: `.rolling().mean()`

**🛠️ Practice**
- Parse dates from CSV
- Monthly average sales plot

**📊 Mini Project**
- COVID/Weather trend analysis

**🔄 Enhancements**
- Try hourly/daily rolling average

---

### 🗓️ Day 10 – Mini Projects

**✅ Tasks**
- Choose datasets (NYC Schools, LA Crime, E-commerce)
- Clean → Filter → Group → Analyze → Report

**Deliverables**
- Insights summary
- Cleaned datasets
- Exported reports (CSV or Excel)

---

### 🗓️ Day 11 – EDA & Visualization

**🔍 Real-World Scenario:**  
Extract patterns visually for reports.

**✅ Concepts**
- `.mean()`, `.std()`, `.corr()`
- `.plot()`, `.hist()`, `.boxplot()`
- Seaborn: `sns.pairplot()`, `sns.heatmap()`

**🛠️ Practice**
- Titanic dataset EDA
- Visualize student or sales data

**📊 Mini Project**
- Iris dataset visual exploration

---

### 🗓️ Day 12 – Performance Optimization

**🔍 Real-World Scenario:**  
Work with 100k+ rows? Optimize everything.

**✅ Concepts**
- `.memory_usage()`
- Downcast floats/ints
- `read_csv()` with `chunksize`

**🛠️ Practice**
- Load large CSV in chunks
- Reduce memory usage

**📊 Mini Project**
- Optimize a public dataset (e.g., Airbnb listings)

---

### 🗓️ Day 13 – Pivoting & MultiIndex

**🔍 Real-World Scenario:**  
You need sales summary reports by category and region.

**✅ Concepts**
- `.pivot_table()`
- `pd.crosstab()`
- MultiIndex: `.set_index()`, `.stack()`, `.unstack()`

**🛠️ Practice**
- Pivot marks by subject/class
- Crosstab of job vs gender

**📊 Mini Project**
- Sales summary dashboard

---

### 🗓️ Day 14 – Capstone Project

**🎯 Final Task:**  
Build a full data pipeline using a real-world dataset.

**Steps**
- Load → Clean → Transform → EDA → Save Output

**Suggested Projects**
- Netflix dataset (genre, rating, year)
- Superstore dataset (sales, profit, region)

**Deliverables**
- Jupyter Notebook
- Exported CSV reports
- Graphs & visual summaries

---

## 🧰 Bonus Tools & Resources

- **Environments:** JupyterLab, Colab, VS Code  
- **Datasets:** Kaggle, UCI ML Repo, Data.gov  
- **Docs:** [Pandas Official Documentation](https://pandas.pydata.org)  
- **Track Progress:** GitHub + Markdown or Notion

---

**🔥 Now you're ready to become a confident, job-ready Pandas pro!**  
Stick to the plan. Break things. Ask questions. Google shamelessly. PRACTICE RELENTLESSLY. 🚀
