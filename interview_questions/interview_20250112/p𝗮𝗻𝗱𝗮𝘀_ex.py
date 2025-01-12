'''
    Q1. Find the most frequent element in a list
    Q2. Merge two DataFrames using a common column
    Q3. Write a DataFrame to a CSV file without the index
    Q4. Handle missing data by replacing NaN values with the column mean
    Q5. Convert a DataFrame column from string to datetime format
'''

import pandas as pd
import numpy as np

def ans_01():
    # Read the CSV file
    df = pd.read_csv("student_scores2.csv")

    # Q6. Create a NumPy array from a list of integers
    # Filter rows where the column 'Scores' is greater than 50
    filtered_df = df[df['Scores'] > 50]

    print(filtered_df)

def ans_02():
    # Q2. Merge two DataFrames using a common column
    # Create DataFrames
    df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    # df2 = pd.DataFrame({'id': [1, 2, 4], 'salary': [50000, 60000, 70000]})
    df2 = pd.DataFrame({'id': [1, 2, 3], 'salary': [50000, 60000, 70000]})

    # Merge using the 'id' column
    merged_df = pd.merge(df1, df2, on='id', how='inner')

    print(merged_df)

def ans_03():
    # Q3. Write a DataFrame to a CSV file without the index
    # Sample DataFrame
    df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})

    # Write to CSV without index
    df.to_csv("output.csv", index=False)


def ans_04():
    # Q4. Handle missing data by replacing NaN values with the column mean
    # Create a DataFrame with NaN values
    df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})

    # Replace NaN with column mean
    df.fillna(df.mean(), inplace=True)

    print(df)
def ans_05():
    # Q5. Convert a DataFrame column from string to datetime format
    # Sample DataFrame
    df = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03']})

    # Convert to datetime
    df['date'] = pd.to_datetime(df['date'])

    print(df)

if __name__ == "__main__":
    ans_04()







