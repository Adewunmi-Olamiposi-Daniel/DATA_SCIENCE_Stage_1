🧠 **DSWK4D3 — PANDAS SERIES & DATAFRAMES: CREATION, INDEXING & FILTERING**

📅 **DAY 3 — WEDNESDAY, NOV 19**

Today’s lesson focused on Pandas, specifically understanding **Series** and **DataFrames**, how to create them, inspect datasets, select and filter data, and perform basic statistical operations. This marks the transition from raw Python and NumPy into real-world data analysis workflows.

📚 **WHAT I LEARNED:**

* A **Pandas Series** is a one-dimensional labeled array, similar to a column in a table.
* Series can have default numeric indexes or custom labels like subject names.
* A **DataFrame** is a two-dimensional table made up of rows and columns, similar to Excel sheets or SQL tables.
* How to create DataFrames from Python dictionaries.
* How to inspect data using:

  * `head()` and `tail()` to preview data
  * `shape` to see rows and columns
  * `columns` to list column names
  * `info()` to understand data types and missing values
* Selecting data using:

  * Column names (`df["Score"]`)
  * Position-based indexing with `iloc`
* Filtering rows using conditions and boolean logic.
* Performing basic statistical operations like `mean()`, `sum()`, and `max()` on columns.

🧩 **PRACTICE CHALLENGES:**

1️⃣ **Student Scores Analysis**
Created a DataFrame containing student names, ages, and scores.
Performed:

* Column selection
* Row filtering (scores above a threshold)
* Combined conditions (score and age)

2️⃣ **CGPA Dataset Practice**
Built a DataFrame of students, departments, and CGPAs.
Tasks included:

* Selecting the CGPA column
* Filtering students with CGPA above 3.5
* Checking the shape of the dataset

💭 **REFLECTION:**

This lesson made it very clear why Pandas is the backbone of data science. Unlike NumPy, Pandas adds meaning to data through labels and structure. I now understand how analysts explore datasets, ask questions, and extract insights without writing complex loops. Working with Series and DataFrames feels like working directly with data, not just numbers. This was a major confidence boost and a clear step toward professional data analysis.

✅ **Status:** Completed
📅 **Next Lesson:** Importing & Exporting CSV Files with Pandas
🧠 **Next Code:** DSWK4D4 — Thursday, Nov 20
