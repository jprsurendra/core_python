import numpy as np

'''
Real life example of Numpy
Scenario 1: You are analyzing sales data for a retail chain.
    The company has 5 stores.
    Each store reports monthly sales for 12 months.
    You want to:
        1.1. Find total and average sales per store.
        1.2. Identify the best and worst performing month for each store.
        1.3. Flag months where sales were below 50% of the store’s average (to trigger marketing efforts).
        1.4. Normalize sales (scale values between 0 and 1) for comparison across stores.

'''

# Step 1: Create the Data
'''
# Simulated sales data: 5 stores (rows), 12 months (columns)
np.random.seed(42)  # for reproducibility
sales = np.random.randint(20000, 100000, (5, 12))
print("Sales Data (Rows=Stores, Cols=Months):")
print(sales)
                       ------ ------  Month wise sales of each Store  ------ ------
                                    Jan   Feb   March April May   June  July  Aug   Sep   Oct   Nov   Dec     -------   -------  -------   Calculate Each store’s performance summary --------  -------  -------
                                                                                                              Calculate Total (Jan-Dec)  Calculate Average Sales Per Month
                                                                                                                Total Sales per Store          Average Sales per Store       Best sales in Month    Worst sales in Month
        Store-A's Sales (in Rs):    35795 20860 96820 74886 26265 57194 64131 80263 36023 61090 87221 84820        = 725368                     = 60447.33333333                 Mar                    Feb  
        Store-B's Sales (in Rs):    20769 79735 82955 84925 87969 25311 73707 48693 91932 45658 38431 22747        = 702832                     = 58569.33333333                 Sep                    Jan  
        Store-C's Sales (in Rs):    79150 85725 55773 87435 76886 86803 51551 31394 89092 23890 61606 30627        = 759932                     = 63327.66666667                 Sep                    Oct  
        Store-D's Sales (in Rs):    28792 93969 63001 96552 43897 88148 43483 68555 37159 55920 87121 89479        = 796076                     = 66339.66666667                 Apr                    Jan  
        Store-E's Sales (in Rs):    39457 86557 97189 98953 72995 60757 29692 65758 92409 91211 85697 57065        = 877740                     = 73145.0                        Apr                    Jul 
 
'''
sales = np.array([ [35795, 20860, 96820, 74886, 26265, 57194, 64131, 80263, 36023, 61090, 87221, 84820],
                   [20769, 79735, 82955, 84925, 87969, 25311, 73707, 48693, 91932, 45658, 38431, 22747],
                   [79150, 85725, 55773, 87435, 76886, 86803, 51551, 31394, 89092, 23890, 61606, 30627],
                   [28792, 93969, 63001, 96552, 43897, 88148, 43483, 68555, 37159, 55920, 87121, 89479],
                   [39457, 86557, 97189, 98953, 72995, 60757, 29692, 65758, 92409, 91211, 85697, 57065] ])
#    35795+ 20860+ 96820+ 74886+ 26265+ 57194+ 64131+ 80263+ 36023+ 61090+ 87221+ 84820 = 725368
#    35795 + 20769 + 79150 + 28792 + 39457 35795 + 20769 + 79150 + 28792 + 39457  = 203963
# Step 2: Total & Average Sales per Store
total_sales_per_store = sales.sum(axis=1)  # axis=1 means sum across columns (for each row).
avg_sales_per_store = sales.mean(axis=1)   # Each store’s performance is now summarized.

print("Total Sales per Store:", total_sales_per_store)
print("Average Sales per Store:", avg_sales_per_store)
'''
Total Sales per Store: [725368 702832 759932 796076 877740]
Average Sales per Store: [60447.33333333, 58569.33333333, 63327.66666667, 66339.66666667, 73145. ]

Result:
                Calculate Total (Jan-Dec)  Calculate Average Sales Per Month
                Total Sales per Store          Average Sales per Store   
Store-A                725368                      60447.33333333          
Store-B                702832                      58569.33333333          
Store-C                759932                      63327.66666667          
Store-D                796076                      66339.66666667          
Store-E                877740                      73145.0                 


'''

# Step 3: Best and Worst Month for Each Store
best_month_indices = sales.argmax(axis=1)  # argmax(axis=1) → finds column index with highest(MAX) sales.
worst_month_indices = sales.argmin(axis=1) # argmax(axis=1) → finds column index with lowest(MIN) sales.

print("Best Month Index per Store:", best_month_indices)
print("Worst Month Index per Store:", worst_month_indices)
'''
Best Month Index per Store: [2 8 8 3 3]
Worst Month Index per Store: [1 0 9 0 6]
'''
# You could map indices to month names:
months = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
best_months = months[best_month_indices]
worst_months = months[worst_month_indices]
print("Best Month Names:", best_months)
print("Worst Month Names:", worst_months)
'''
Best Month Names: ['Mar' 'Sep' 'Sep' 'Apr' 'Apr']
Worst Month Names: ['Feb' 'Jan' 'Oct' 'Jan' 'Jul']
Result:
            Best sales in Month    Worst sales in Month
Store-A          Mar                    Feb
Store-B          Sep                    Jan
Store-C          Sep                    Oct
Store-D          Apr                    Jan
Store-E          Apr                    Jul

'''

# Step 4: Flag Low-Performance Months
# A month is flagged if sales < 50% of store’s average:
low_performance_mask = sales < (0.5 * avg_sales_per_store[:, np.newaxis])
# avg_sales_per_store[:, np.newaxis] reshapes to (5,1) for broadcasting

print("Low Performance Mask (True=Low Sales):")
print(low_performance_mask)

# Get actual values:
low_sales_values = np.where(low_performance_mask, sales, 0)
print("Low Sales Values (zeros where OK):")
print(low_sales_values)
'''
[    [     0    20860     0     0   26265        0        0        0     0       0     0      0 ] 
     [ 20769        0     0     0       0    25311        0        0     0       0     0  22747 ] 
     [     0        0     0     0       0        0        0    31394     0   23890     0  30627 ] 
     [ 28792        0     0     0       0        0        0        0     0       0     0      0 ] 
     [     0        0     0     0       0        0    29692        0     0       0     0      0 ] ]

'''
# This creates a Boolean mask and extracts actual low-performing month sales.

# Step 5: Normalize Sales Data
# For comparison across stores, normalize each store’s sales between 0 and 1:
min_sales = sales.min(axis=1)[:, np.newaxis]
max_sales = sales.max(axis=1)[:, np.newaxis]

normalized_sales = (sales - min_sales) / (max_sales - min_sales)
print("Normalized Sales (0 to 1):")
print(normalized_sales)
'''
[[ 0.19661664    0.            1.            0.71124276    0.07115587 0.4783307    0.56965508    0.78203002    0.19961822    0.52962085    0.87363086    0.84202212 ] 
 [ 0.            0.82860475    0.87385299    0.90153591    0.94431095 0.0638253    0.74389781    0.39239492    1.            0.34974636    0.24819077    0.02779534 ] 
 [ 0.84752001    0.94836048    0.48898807    0.97458667    0.81279715 0.96489371   0.42423545    0.11508849    1.            0.            0.57844851    0.10332505 ] 
 [ 0.            0.96188017    0.50485537    1.            0.22291913 0.87597403   0.21680933    0.58682113    0.12347993    0.40035419    0.86081759    0.89561688 ] 
 [ 0.14098844    0.82102482    0.97453112    1.            0.62521477 0.44852081   0.            0.52072595    0.90551681    0.88821992    0.80860802    0.3952152  ] ]
'''
# Now, each store’s lowest sale = 0 and highest sale = 1.

'''
Why is this Powerful?
    No loops needed; everything works with NumPy vectorization.
    Can scale to thousands of stores & years of data efficiently.
    Works great for business analytics, ML preprocessing, and reporting.
'''

'''
Practice Challenge for You:
    Using the same data:
    Find the total sales per month (across all stores).
    Identify the month with the highest company-wide sales.
    Calculate year-over-year growth if sales represent 2 years (24 months).
    Replace low-performing months with the average sales of that store (using Boolean indexing assignment).
'''

print("========================================================================================")

# 1. Total sales per month (across all stores)
total_sales_per_month = np.sum(sales, axis=0)
print("1. Total sales per month:")
print(total_sales_per_month)
'''
Total sales per month:
    [203963 366846 395738 442751 308012 318213 262564 294663 346615 277769 360076 284738]
'''
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
# 2. Month with highest company-wide sales
highest_sales_month = np.argmax(total_sales_per_month) + 1  # +1 because months start at 1
highest_sales_value = np.max(total_sales_per_month)
print(f"2. Month with highest sales: Month {highest_sales_month}")
print(f"   Total sales: {highest_sales_value}")
'''
Month with highest sales: Month 4
    Total sales: 442751
'''
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
# 3. Year-over-year growth (assuming first 12 months = year 1, next 12 = year 2)
# Since we only have 12 months, I'll calculate month-over-month growth instead
# If you meant comparing the same month across years, please clarify
monthly_growth = np.diff(total_sales_per_month) / total_sales_per_month[:-1] * 100
print("3. Monthly growth rates (%):")
print(monthly_growth)
print(f"   Average monthly growth: {np.mean(monthly_growth):.2f}%")
'''
Monthly growth rates (%):
[ 79.85909209   7.87578439  11.87982958 -30.4322294    3.31188395  -17.48797189  12.22520985  17.63098862 -19.86238334  29.63145635 -20.92280519]
Average monthly growth: 6.70%
'''
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
# 4. Replace low-performing months with store average
# Define "low-performing" as months below 75% of store's average
store_averages = np.mean(sales, axis=1, keepdims=True)
low_performing_threshold = 0.75 * store_averages

# Create boolean mask for low-performing months
low_performing_mask = sales < low_performing_threshold

# Replace low-performing months with store average
sales_cleaned = sales.copy()
sales_cleaned[low_performing_mask] = store_averages[low_performing_mask]

print("4. Sales data after replacing low-performing months:")
print(sales_cleaned)
print()

# Additional analysis: Show which months were replaced
print("Low-performing months replaced (store, month):")
low_performing_indices = np.where(low_performing_mask)
for store, month in zip(low_performing_indices[0], low_performing_indices[1]):
    print(f"  Store {store+1}, Month {month+1}: {sales[store, month]} → {sales_cleaned[store, month]:.0f}")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
'''
Output Explanation:

Total sales per month: Sum of all stores' sales for each month

Highest sales month: The month with the maximum total sales across all stores

Growth calculation: Shows month-over-month percentage change (you mentioned 24 months but data shows 12 months)

Low-performing replacement: Months where sales are below 75% of that store's average are replaced with the store's average

Note about year-over-year growth: The data appears to be for 12 months (1 year) across 5 stores. If you meant this represents 2 years (24 months), please clarify the structure. The current code calculates month-over-month growth instead.

If you want to calculate year-over-year growth for the same months across different years, you would need to organize the data differently (e.g., first 6 months = year 1, next 6 months = year 2). Let me know if you'd like me to adjust this calculation!
'''
'''
Me: Yes
I'll adjust the year-over-year growth calculation assuming the sales data represents 2 years (24 months). Since we have 5 stores × 12 months, I'll reorganize the data to represent 2 years.

'''
print("Original Sales Data:")
print(sales)
print()

# 1. Total sales per month (across all stores)
total_sales_per_month = np.sum(sales, axis=0)
print("1. Total sales per month:")
for i, sales_amount in enumerate(total_sales_per_month):
    print(f"   Month {i+1:2d}: {sales_amount:8,d}")
print()

# 2. Month with highest company-wide sales
highest_sales_month = np.argmax(total_sales_per_month) + 1
highest_sales_value = np.max(total_sales_per_month)
print(f"2. Month with highest sales: Month {highest_sales_month}")
print(f"   Total sales: {highest_sales_value:,}")
print()

# 3. Year-over-year growth (assuming first 6 months = Year 1, next 6 months = Year 2)
# Reshape to separate years (assuming 6 months per year)
year1_sales = sales[:, :6]  # First 6 months = Year 1
year2_sales = sales[:, 6:]  # Next 6 months = Year 2

# Calculate total sales for each year
total_year1 = np.sum(year1_sales)
total_year2 = np.sum(year2_sales)

# Calculate year-over-year growth
yoy_growth = ((total_year2 - total_year1) / total_year1) * 100

print("3. Year-over-Year Growth Analysis:")
print(f"   Year 1 total sales (months 1-6): {total_year1:,}")
print(f"   Year 2 total sales (months 7-12): {total_year2:,}")
print(f"   Year-over-year growth: {yoy_growth:.2f}%")
print()

# Monthly year-over-year comparison (comparing same month across years)
# Since we only have 6 months per year, we can compare month 1 vs month 7, etc.
print("   Monthly Year-over-Year Comparison:")
for i in range(6):
    month_year1 = np.sum(year1_sales[:, i])
    month_year2 = np.sum(year2_sales[:, i])
    monthly_growth = ((month_year2 - month_year1) / month_year1) * 100 if month_year1 != 0 else 0
    print(f"   Month {i+1} vs Month {i+7}: {monthly_growth:6.1f}% "
          f"({month_year1:,} → {month_year2:,})")

print()

# 4. Replace low-performing months with store average
# Define "low-performing" as months below 75% of store's average
store_averages = np.mean(sales, axis=1, keepdims=True)
low_performing_threshold = 0.75 * store_averages

# Create boolean mask for low-performing months
low_performing_mask = sales < low_performing_threshold

# Replace low-performing months with store average
sales_cleaned = sales.copy()
sales_cleaned[low_performing_mask] = store_averages[low_performing_mask]

print("4. Sales data after replacing low-performing months:")
print(sales_cleaned)
print()

# Show which months were replaced
print("Low-performing months replaced (store, month):")
low_performing_indices = np.where(low_performing_mask)
replaced_count = 0
for store, month in zip(low_performing_indices[0], low_performing_indices[1]):
    print(f"   Store {store+1}, Month {month+1:2d}: {sales[store, month]:6,d} → {sales_cleaned[store, month]:6.0f}")
    replaced_count += 1

print(f"\n   Total low-performing months replaced: {replaced_count}")
print(f"   Percentage of data points replaced: {(replaced_count / sales.size * 100):.1f}%")
'''
Key Changes for Year-over-Year Analysis:

Assumed 2-year structure: First 6 months = Year 1, Next 6 months = Year 2

Overall YoY growth: Compares total sales of Year 2 vs Year 1

Monthly YoY comparison: Shows growth for each month position (Month 1 vs Month 7, Month 2 vs Month 8, etc.)

Output includes:

Total monthly sales across all stores

Highest performing month

Overall year-over-year growth percentage

Monthly comparison showing growth for each month position

Cleaned data with low-performing months replaced by store averages

Details on which specific months were replaced

This gives you a comprehensive analysis of your retail chain's performance!
'''