import pandas as pd
 
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'East'],
    'Q1': [100, 150, 200, 250, 120, 220],
    'Q2': [120, 180, 240, 300, 130, 230],
    'Q3': [130, 190, 250, 310, 140, 240],
    'Q4': [140, 200, 260, 320, 150, 250]
}

"""
Output: 
Region  Total_Sales
0   East        1020.0
1  North         590.0
"""

"""
Question:
1.  Add a new column “Total_Sales” which is the sum of “Q1”, “Q2”, “Q3”, and “Q4”.
2.  Filter out all rows where “Total_Sales” is less than 500.
3.  Group the DataFrame by “Region” and calculate the average “Total_Sales” for each region.
4.  Sort the grouped DataFrame by “Total_Sales” in descending order.
5.  Return the modified DataFrame.
"""

