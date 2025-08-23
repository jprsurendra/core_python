import numpy as np

'''
Me: Act as a study Coach. Teach me numpy in python using real-life analogies and memory trick. So I never forget it again.
ChatGPT: Absolutely! Let's make NumPy so intuitive and memorable that you’ll never forget it. We’ll use real-life analogies, memory hooks, and storytelling.

0. Install NumPy:
    pip install --upgrade pip
    pip install numpy
    
1. What is NumPy?
    Imagine you’re running a warehouse. You store lots of similar items (like boxes of apples).

    If you store them randomly on shelves, you’ll waste time searching and counting (like normal Python lists).

    But if you store them in a neat grid (like in a well-arranged warehouse), you can quickly count, move, and process them.

    This well-arranged warehouse = NumPy array (ndarray).

2. Why NumPy? (Compared to Lists)
    Normal lists are like a messy shopping cart—you check each item one by one.

    NumPy arrays are like a conveyor belt in an Amazon warehouse—organized, super-fast, and can handle bulk operations at once.

3. Creating Arrays  

    a = np.array([1, 2, 3])
   
    Analogy:
        Think of np.array() as packing apples into a box.

        [1,2,3] is a loose bunch of apples.

        np.array() packs them into a box with structure.

        Memory Hook:

        array() = Arrange into an array (sounds like "array" → "arrange").     

4. Shapes & Dimensions
    1D array: Like a single row of lockers.
    2D array: Like rows and columns in a table.
    3D array: Like a Rubik’s cube (shelves with rows and columns).  

    np.array([[1,2,3], [4,5,6]]) 
 
    Think: Rows = horizontal shelves, Columns = vertical stacks.
    Memory trick: "Shape tells you the layout."

5. NumPy Operations (Vectorized) 
    Normal Python:  
    lst = [1,2,3]
    lst2 = [x+10 for x in lst]
    print("lst: ", lst)
    print("lst2: ", lst2)
    # print("---------------------------------------------------")
 
    NumPy: 
    a = np.array([1,2,3])
    print("a: ", a)
    b = a + 10  # हर element में 10 add होगा
    print("b: ", b)
    # print("---------------------------------------------------")
 
    Analogy:
    Instead of adding 10 to each apple manually, NumPy uses a machine gun of math—adds to all at once.
    
    Memory Hook:    
    Broadcasting = Broadcast signal to all receivers at once.
    
    
6. Indexing & Slicing in NumPy (Detailed)
    What is Indexing?
        Indexing means picking a specific element from an array using its position.    
        Just like you have a row of lockers and each locker has a number tag (index).    
        In NumPy, indexing always starts at 0 (like Python lists).
    
        6.A.1 1D Array Indexing:  
            arr = np.array([10, 20, 30, 40, 50])
            print("first element:  arr[0] = ", arr[0])  # 10 (first element)
            print("fourth element: arr[3] = ", arr[3])   # 40 (fourth element)
            # print("---------------------------------------------------")
 
            Think: arr[3] means "locker number 3", starting from 0.
        6.A.1.1 If you use negative index, you count from the back  
            print("last element:   arr[-1] = ", arr[-1])  # 50 (last element)
            print("second last:    arr[-2] = ", arr[-2])  # 40 (second last)
            print("---------------------------------------------------")

            Memory Hook:
            Negative index = back door entry.
    
        6.A.2 2D Array Indexing (Rows & Columns)
            Think of rows = horizontal shelves, columns = vertical stacks. 

            arr = np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]])
            print("row 0, column 1:                   arr[0, 1] => ", arr[0, 1])  # 2 (row 0, column 1)
            print("row 2, column 2:                   arr[2, 2] => ", arr[2, 2])  # 9 (row 2, column 2)
            print("Full row: (row 1, all columns):    arr[1, :] ==>", arr[1, :])  # [4 5 6] (row 1, all columns)
            print("Full column: (all rows, column 0): arr[:, 0] ==>", arr[:, 0])  # [1 4 7] (all rows, column 0)
            print("---------------------------------------------------")
        
            Memory Hook:
                First index = row (horizontal), Second index = column (vertical).
        6.A.3  Boolean Indexing (Condition-based)
                Pick elements based on condition: 
                arr = np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])
                print("Boolean Indexing: ", arr[arr > 4])
                output: Boolean Indexing:  [5 6 7 8 9]

                NumPy checks each element of the array and compares it with 4.
                The result is a Boolean array (True/False values):
                    [ [False False False]
                      [False  True  True]
                      [ True  True  True] ]
                 * False where the element is NOT > 4
                 * True where the element IS > 4

            print("Boolean Indexing: all even numbers => ", arr[arr % 2 == 0] )          # [2 4 6 8]
            print("Boolean Indexing: all numbers <= 7 =>", arr[arr <= 7])                # [1 2 3 4 5 6 7]
            print("Boolean Indexing: elements >4 and <8 =>", arr[(arr > 4) & (arr < 8)]) # [5 6 7]

        6.B What is Slicing?
            Slicing means picking a range (सीमा) of elements.
        6.B.1 1D Slicing
            Syntax:
                arr[start:end:step]
                start → where to begin (included)
                end → where to stop (excluded)            
                step → gap between elements (optional)            
                Example: 

                    arr = np.array([10,20,30,40,50])
                    print( "arr = np.array([10,20,30,40,50])")
                    print("from index 1 to 3:       arr[1:4] => ", arr[1:4])    # [20 30 40]  (from index 1 to 3)
                    print("start omitted (from 0):  arr[:3]  => ", arr[:3])     # [10 20 30]  (start omitted → from 0)
                    print("end omitted (till last): arr[2:]  => ", arr[2:])     # [30 40 50]  (end omitted → till last)
                    print("step=2 (pick alternate): arr[::2] => ", arr[::2])    # [10 30 50]  (step=2 → pick alternate)
                    print("---------------------------------------------------")
                Memory Hook:
                ": colon" means "all values along that direction."

        6.B.2 2D Slicing
            You can slice both rows and columns: 
            In a 2D array (matrix), you have rows (horizontal shelves) and columns (vertical stacks).
            With slicing, you can select a specific region (sub-matrix) of that table. 
            Syntax: array[row_start:row_end, column_start:column_end]
                row_start:row_end → Which rows to pick (row_end excluded)
                column_start:column_end → Which columns to pick (column_end excluded)
                Colon : means “all along that axis” 
                
            arr = np.array([[ 1,  2,  3,  4],
                            [ 5,  6,  7,  8],
                            [ 9, 10, 11, 12],
                            [13, 14, 15, 16]])
            
            print(arr[0:2, 1:3])

                # Rows 0 to 1 (0 included, 2 excluded),  
                    [ 1,  2,  3,  4],
                    [ 5,  6,  7,  8],
                # Columns 1 to 2 (1 included, 3 excluded)
                 1st Col 2nd Col
                     2,    3,
                     6,    7,
                    10,   11,  (3rd row excluded)
                    14,   15,  (4th row excluded)
                # Out put:
                [  [2 3]
                   [6 7]  ]
                   
            print("take all rows, columns 1 & 2: arr[:, 1:3]=> ", arr[:, 1:3])

                Output: [    [ 2  3]
                             [ 6  7]
                             [10 11]
                             [14 15]   ]

            print("take rows 1 & 2, all columns: arr[1:3, :]=> ", arr[1:3, :])
            
                Output: [[ 5  6  7  8]
                         [ 9 10 11 12] ]                            
 
            print("take Picks rows 0(1st) & 2(3rd) fully (all columns): arr[[0,2], :]=> ", arr[[0,2], :])
             
            Output: [[ 1  2  3  4]
                     [ 9 10 11 12]]
                     
        Skipping with Step Size
            Syntax with step: arr[row_start:row_end:row_step, col_start:col_end:col_step]
 
            print("Take every 2nd row and every 2nd column: arr[::2, ::2]=> ", arr[::2, ::2])
                  
            Output: [[ 1  3]
                     [ 9 11]]  
        Negative Index Slicing
            You can count from the end using negative indices:

            print("Take Last 2 rows and Last 2 columns: arr[-2:, -2:]=> ", arr[-2:, -2:])
      
            Output: [[11 12]
                     [15 16]]   
               
        Selecting Non-Contiguous Columns or Rows (Fancy Slicing)    
            arr[[0,2], [1,3]]  # picks (0,1) and (2,3)
            print("Fancy Slicing: arr[[0,2], [1,3]]=> ", arr[[0,2], [1,3]])
                The first list [0,2] specifies row indices. => Take row 0(1st) and column(-1) 1(2nd) → arr[0,1]
                The second list [1,3] specifies column indices. => Take row(+1) 2(3rd) and column 3(4th) → arr[2,3] 
                Output: [ 2 12]  
                
            print("Fancy Slicing: arr[[1,2], [1,2]]=> ", arr[[1,2], [1,2]])
                The first list 1,2 specifies row indices. => Take row 1(2nd) and column(-1) 1(2nd) → arr[1,1]
                The second list [1,2] specifies column indices. => Take row(+1) 2(3rd) and column 2(3rd) → arr[2,2]  
            Output: [ 6 11]   


Real life example of Numpy
Scenario 1: You are analyzing sales data for a retail chain.
    The company has 5 stores.
    Each store reports monthly sales for 12 months.
    You want to:
        1. Find total and average sales per store.
        2. Identify the best and worst performing month for each store.
        3. Flag months where sales were below 50% of the store’s average (to trigger marketing efforts).
        4. Normalize sales (scale values between 0 and 1) for comparison across stores.


'''

# Step 1: Create the Data
# Simulated sales data: 5 stores (rows), 12 months (columns)
np.random.seed(42)  # for reproducibility
sales = np.random.randint(20000, 100000, (5, 12))

print("Sales Data (Rows=Stores, Cols=Months):")
print(sales)
'''
                    Jan   Feb   March April May   June  July  Aug   Sep   Oct   Nov   Dec
Store-A's Sales:   [35795 20860 96820 74886 26265 57194 64131 80263 36023 61090 87221 84820]
Store-B's Sales:   [20769 79735 82955 84925 87969 25311 73707 48693 91932 45658 38431 22747]
Store-C's Sales:   [79150 85725 55773 87435 76886 86803 51551 31394 89092 23890 61606 30627]
Store-D's Sales:   [28792 93969 63001 96552 43897 88148 43483 68555 37159 55920 87121 89479]
Store-E's Sales:   [39457 86557 97189 98953 72995 60757 29692 65758 92409 91211 85697 57065]
 
'''
