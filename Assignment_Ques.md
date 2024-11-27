# Assignment: Python & SQL Integration with Exploratory Data Analysis
### Objective:
In this assignment, you will:
Generate a dataset using Python with predefined columns.
Insert the generated data into a SQL database and perform various queries on it.
Retrieve the data using Python and perform Exploratory Data Analysis (EDA), followed by visualizations.
<br></br>
<hr></hr>
<br></br>

### Step 1: Dataset Generation
#### Task 1: Dataset Creation
Using Python, create a dataset containing random values for 200 rows with the following columns:
customer_id (int): A unique ID for each customer (values ranging from 1001 to 1200)
customer_name (string): Random customer names (can use a list of names or generate randomly)
product_id (int): A unique ID for each product (values ranging from 1 to 20)
purchase_date (date): Random dates within the last year
quantity (int): Random quantity purchased (between 1 to 10)
price_per_unit (float): Random price between 10.00 and 1000.00
region (string): Random regions like "North", "South", "East", "West"
<br></br>
<hr></hr>
<br></br>

#### Task 2: Dataset Insertion into SQL
Insert this dataset into an SQL database (SQLite or MySQL).
You may need to create an SQL table with appropriate data types corresponding to the columns mentioned above.
<br></br>
<hr></hr>
<br></br>

### Step 2: SQL Queries
#### Task 3: Write and Execute SQL Queries
Once the dataset is stored in the SQL database, perform the following queries:
Total Sales: Calculate the total sales amount (quantity * price_per_unit) per region.
Top Products: Retrieve the top 5 products by total sales (quantity * price_per_unit).
Monthly Sales: Calculate the total sales for each month.
Customer Purchase Analysis: Retrieve the total amount spent by each customer.
Product Sales by Region: List the total sales of each product per region.
<br></br>
<hr></hr>
<br></br>

### Step 3: Exploratory Data Analysis (EDA) and Visualization
#### Task 4: Retrieve Data into Python
Using Python (with libraries like pandas and sqlite3/mysql-connector), retrieve the data back from the SQL database.
<br></br>
<hr></hr>
<br></br>

#### Task 5: EDA Tasks
Perform the following analyses:
Summary Statistics: Use Python to calculate the mean, median, max, min, and standard deviation for the quantity and price_per_unit columns.
Sales per Region: Show a breakdown of total sales (quantity * price_per_unit) per region.
Top 5 Customers: Identify the top 5 customers based on the total amount spent.
<br></br>
<hr></hr>
<br></br>

#### Task 6: Data Visualization
Using Python libraries such as matplotlib or seaborn, create the following visualizations:
Bar Plot: Visualize total sales per region.
Pie Chart: Show the proportion of sales for each product.
Line Plot: Plot monthly sales trends over the last year.
Scatter Plot: Visualize the relationship between quantity and price_per_unit.
<br></br>
<hr></hr>
<br></br>

### Deliverables:
Python script for dataset creation and insertion into SQL.
SQL script with the required queries.
Python notebook or script for data retrieval, EDA, and visualizations.
<br></br>
<hr></hr>
<br></br>

### Submission Guidelines:
Submit your Python scripts and SQL queries.
The Python script should be clean, commented, and well-organized.
Include a brief report (in markdown or as part of the notebook) summarizing the insights from your EDA.
nu
