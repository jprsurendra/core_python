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
    
    Q. What is NumPy?
        NumPy (Numerical Python) = A library for fast mathematical computation on arrays/matrices.
        Think of it as "Excel on steroids" – works with huge data faster than Python lists.
        
    Q Why is it fast?
        Internally uses C language, optimized memory layout.
        Supports vectorized operations (no slow loops).

2. Why NumPy? (Compared to Lists)
    Normal lists are like a messy shopping cart—you check each item one by one.

    NumPy arrays are like a conveyor belt in an Amazon warehouse—organized, super-fast, and can handle bulk operations at once.

3. Creating Arrays  
    Core Object: ndarray (NumPy Array)
    
    arr_1d = np.array([1, 2, 3])                          # 1D Array: Like a list.
    arr_2d = np.array([ [1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]  ])  #2D Array: Like an Excel sheet.
    # Create a 3D array with 2 "slices" (2D arrays), each with 2 rows and 3 columns
    arr_3d = np.array([ 
                        [ [1, 2, 3],    
                          [4, 5, 6] ],     # First "slices" (2D arrays)

                        [ [7, 8, 9],    
                          [10, 11, 12] ]   # Second "slices" (2D arrays)
                      ])               # 3D Array: Like a stack of Excel sheets.
   
    Analogy:
        Think of np.array() as packing apples into a box.
        [1,2,3] is a loose bunch of apples.
        np.array() packs them into a box with structure.
        
        Memory Hook:
            array() = Arrange into an array (sounds like "array" → "arrange").    

    Q Check attributes:
        arr.ndim      # number of dimensions
        arr.shape     # (rows, cols)
        arr.size      # total elements
        arr.dtype     # data type 
        
        print("number of dimensions:")
        print("arr_1d.ndim: ", arr_1d.ndim) # 1
        print("arr_2d.ndim: ", arr_2d.ndim) # 2
        print("arr_3d.ndim: ", arr_3d.ndim) # 3
        print("(rows, cols):")
        print("arr_1d.shape: ", arr_1d.shape) # (3,)
        print("arr_2d.shape: ", arr_2d.shape) # (3, 3)
        print("arr_3d.shape: ", arr_3d.shape) # (2, 2, 3)
        print("total elements:")
        print("arr_1d.size: ", arr_1d.size) # 3
        print("arr_2d.size: ", arr_2d.size) # 9
        print("arr_3d.size: ", arr_3d.size) # 12
        print("data type:")
        print("arr_1d.dtype: ", arr_1d.dtype) # int64
        print("arr_2d.dtype: ", arr_2d.dtype) # int64
        print("arr_3d.dtype: ", arr_3d.dtype) # int64

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
7. Useful NumPy Functions with Analogies

    array = np.zeros((2,3)) # Creates a table with all empty plates (0).
    print(array)
    putput:
    [[0. 0. 0.]
     [0. 0. 0.]]
     
    array = np.ones((2,3)) # Creates a table with plates full of one apple each.
    print(array)
    putput:
        [[1. 1. 1.]
         [1. 1. 1.]]
  
    array = np.arange(0,10,2) # Like numbering lockers from 0 to 10, skipping by 2.
    print(array)
    putput:
        [0 2 4 6 8]
    
    array = np.linspace(0,1,5) # Like splitting a rope evenly into 5 parts between 0 and 1.
    print(array)
    putput:
        [0.   0.25   0.5    0.75   1.  ]
        np.linspace(0,2,5) ==>  [0.  0.5   1.   1.5    2. ]
        np.linspace(0,100,10) ==> [  0.          11.11111111  22.22222222  33.33333333  44.44444444
                                    55.55555556  66.66666667  77.77777778  88.88888889  100.        ]
   
    Memory Hook:    
        arange → "arranged with step"
        linspace → "linear space evenly divided"
        
    Q. Array Creation Methods
        Memory trick: “ar, ze, fu, ra, li”
        (think of it as a mantra for array creation)
    
        np.array() – manual list/tuple.
        np.zeros((r,c)) – matrix full of 0s.
        np.ones((r,c)) – matrix full of 1s.
        np.full((r,c), value) – filled with custom value.
        np.arange(start, stop, step) – like Python range.
        np.linspace(start, stop, n) – equally spaced numbers.
        np.eye(n) – identity matrix. It creates an identity matrix: 
                    A square matrix with 1s on the main diagonal (top-left to bottom-right) and 0s everywhere else.
            I = np.eye(4)
                [[1. 0. 0. 0.]
                 [0. 1. 0. 0.]
                 [0. 0. 1. 0.]
                 [0. 0. 0. 1.]]
            Diagonal mask (filtering):
            matrix = np.array([[5,2,3],
                       [4,9,1],
                       [7,6,8]])
            diag_only = matrix * np.eye(3)
            print(diag_only)
                [[5. 0. 0.]
                 [0. 9. 0.]
                 [0. 0. 8.]]
            Extra Trick: np.eye(n, k=shift)
                You can shift the diagonal:
                np.eye(4, k=1) # (Diagonal shifted 1 step right)
                [[0. 1. 0. 0.]
                 [0. 0. 1. 0.]
                 [0. 0. 0. 1.]
                 [0. 0. 0. 0.]]
     
            
        np.random – random numbers:
            a = np.random.randint(1,100,(3,4)) # 3x4 random int 1-100
            output:
                [[48 24 47 41]
                 [14 44 65 79]
                 [82 11 93 60]]
             
            b = np.random.rand(3,4)            # 0-1 uniform random
            Output:
            [[0.10553606 0.21940231 0.45609387 0.77875042]
             [0.69480337 0.06376717 0.68530417 0.67520827]
             [0.96443717 0.96372821 0.27185541 0.71918808]]
            
8. Key Array Operations
    Arithmetic: arr + 2, arr1 + arr2, arr1 * arr2
    Universal Functions (ufuncs):
    np.sqrt(arr), np.log(arr), np.exp(arr), np.sin(arr)
    Aggregate: arr.sum(), arr.mean(), arr.min(), arr.max(), arr.std() 

    arr = np.array([1,2,3,4])
    arr1 = arr + 2
    print(arr1) # [3 4 5 6]
    arr2 = arr + arr1
    print(arr2) # [ 4  6  8 10]
    arr3 = arr * arr1
    print(arr3) # [ 3  8 15 24]
     
    arr = np.array([1,4,9,16])
    arr1 = np.sqrt(arr)
    # print(arr1) # [1. 2. 3. 4.]
    # arr1 = np.log(arr)
    # np.exp(arr)
    # np.sin(arr)     
    
    Q. Broadcasting (Magic Trick)
        Broadcasting = automatic expansion of arrays for arithmetic.
        a = np.array([[1,2,3],
                  [4,5,6]])
        b = np.array([10,20,30])
    
        c = a + b
        print(c)
        putput: 
            [[11 22 33]
             [14 25 36]]
             
        Here b is broadcasted to match a.
        Think of short array as paint spreading over the bigger one.
    Q Reshape – Changing the Shape of Data     
         

9. Statistics & Aggregations
    np.sum(a) → Count total apples.  
        a = np.array([1, 2, 3])
        b = np.sum(a) #output: 6
        
        a1 = np.array([[1, 2, 3],
                       [4, 5, 6]])
        b1 = np.sum(a1) #output: 21
 
    np.mean(a) → Average apples per box.  
        a = np.array([1, 2, 3])
        b = np.mean(a) #output: 6/3 => 2.0
        
        a1 = np.array([[1, 2, 3],
                       [4, 5, 6]])
        b1 = np.mean(a1) #output: 21/6 => 3.5
 
    np.max(a) → Biggest apple pile.

        a = np.array([1, 2, 3])
        b = np.max(a) #output: 3 
        a1 = np.array([[1, 2, 3],
                       [4, 5, 6]]) 

10. Reshape & Transpose
    arr.reshape(3,4) – change shape.
    arr.T – transpose rows ↔ columns. 
    arr.flatten() – 2D → 1D
    
    1. Reshape – Changing the Shape of Data
        arr.reshape() lets you change the rows & columns of an array without changing the data.
        
        arr = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])  # OR => np.arange(12)
        
        reshaped = arr.reshape(3, 4)  # 3 rows, 4 columns
        print(reshaped)
         
        [[ 0  1  2  3]
         [ 4  5  6  7]
         [ 8  9 10 11]]
    
        Memory Trick:
            arr.reshape(R, C) ==> Total elements must match! (RxC = 3×4 = 12)

        arr1 = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
        reshaped1 = arr1.reshape(3, 4)  # 3 rows, 4 columns   => ValueError: cannot reshape array of size 13 into shape (3,4)
        print(reshaped1)
        
        Practical Use Case (Real Life):
            You receive a flat list of daily sales for 15 days, and you want to organize it week-wise (3 weeks × 5 days):
            # np.arange(15).reshape(3,5)
            arr_daily_sales_for_15_days = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
            week_wise_5days_in_a_week_sales = arr_daily_sales_for_12_days.reshape(3, 5)  # 3 rows(weeks), 5 columns(days in a day)
            # Each row now represents a week’s sales
            week_wise_5days_in_a_week_sales =>
                            [[  0       1       2           3         4]
                             [  5       6        7          8         9]
                             [ 10      11       12         13        14]]
            More visual view:
                               Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
                      week-1   0       1        2          3         4       OFF       OFF
                      week-2   5       6        7          8         9       OFF       OFF
                      week-3   10      11       12         13        14      OFF       OFF
         
    2. Transpose – Flipping Rows & Columns (पंक्ति और स्तम्भ बदलना) => Transpose swaps rows and columns.     
        Real-Life Analogy: 
            Imagine a classroom attendance sheet:
                Students   Mon	Tue	Wed Thu Fri
                student-1  P	A	P   P   A
                student-2  A	P	P   A   P
            
            If you transpose it, days become rows and students become columns:
                Days 	student-1	student-2
                Mon	    P	        A
                Tue	    A	        P
                Wed	    P	        P
                Thu	    P           A
                Fri	    A	        P
        Memory Trick:
        Think of transpose as rotating the matrix over its diagonal.
    3. flatten() converts any N-dimensional array into a 1D array.
        It makes a copy of the data in row-major (C-style) order by default.
        Think of it as unfolding a folded bedsheet into one straight line.
        arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

        flat = arr.flatten()
        print(flat)  
        Output: [1 2 3 4 5 6 7 8 9]
        
        arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
                
11. Stacking & Splitting     
    Stack:
        np.hstack([a,b])  # horizontal
        np.vstack([a,b])  # vertical           
        h_arr = np.hstack(arr)  # horizontal
        print(h_arr) #Output: [1 2 3 4 5 6 7 8 9]
        v_arr = np.vstack(arr)  # vertical
        Output: No change
            [[1 2 3]
             [4 5 6]
             [7 8 9]]
        arr = np.array([1, 2, 3, 4 ])
        v_arr = np.vstack(arr)  # vertical
        print(v_arr)
        Output: 
            [[1]
             [2]
             [3]
             [4]]
                               
11. NumPy Axis Concept (NumPy Axes Trick)
    When confused about axis, use the table analogy:    
    Axis 0 → down the rows (like summing each column). → Vertical (down) → 0 like a vertical stick. 
           → Operation works vertically down the rows (columns wise).   
    Axis 1 → across the columns (like summing each row). → Horizontal (across) → 1 like a horizontal dash.
           → Operation works horizontally across columns (rows wise). 
    _____________________________________________________________________________________________________________________________
                                Each Store's Sales data (In Rs) Month wise
    ------------------------------------------------------------------------------------------------------------------------------
                   || Jan    | Feb    | March  | April  | May    | June   | July   | Aug   | Sept    | Oct    | Nov    | Dec    ||  Total of all months sales        Avg Sales
    ------------------------------------------------------------------------------------------------------------------------------
    Store-A ->     ||  35795 |  20860 |  96820 |  74886 |  26265 |  57194 |  64131 |  80263 |  36023 |  61090 |  87221 |  84820 ||           725368             | 60447.33333333   |   |
    Store-B ->     ||  20769 |  79735 |  82955 |  84925 |  87969 |  25311 |  73707 |  48693 |  91932 |  45658 |  38431 |  22747 ||           702832             | 58569.33333333   |   |
    Store-C ->     ||  79150 |  85725 |  55773 |  87435 |  76886 |  86803 |  51551 |  31394 |  89092 |  23890 |  61606 |  30627 ||           759932             | 63327.66666667   |   |
    Store-D ->     ||  28792 |  93969 |  63001 |  96552 |  43897 |  88148 |  43483 |  68555 |  37159 |  55920 |  87121 |  89479 ||           796076             | 66339.66666667   |   |
    Store-E ->     ||  39457 |  86557 |  97189 |  98953 |  72995 |  60757 |  29692 |  65758 |  92409 |  91211 |  85697 |  57065 ||           877740             | 73145.0          |   |
    ------------------------------------------------------------------------------------------------------------------------------
    Company Total  || 203963 | 366846 | 395738 | 442751 | 308012 | 318213 | 262564 | 294663 | 346615 | 277769 | 360076 | 284738 ||
    ______________________________________________________________________________________________________________________________
    Here: Rows → Stores   and  Columns → Months

    sales = np.array([ [35795, 20860, 96820, 74886, 26265, 57194, 64131, 80263, 36023, 61090, 87221, 84820],
                       [20769, 79735, 82955, 84925, 87969, 25311, 73707, 48693, 91932, 45658, 38431, 22747],
                       [79150, 85725, 55773, 87435, 76886, 86803, 51551, 31394, 89092, 23890, 61606, 30627],
                       [28792, 93969, 63001, 96552, 43897, 88148, 43483, 68555, 37159, 55920, 87121, 89479],
                       [39457, 86557, 97189, 98953, 72995, 60757, 29692, 65758, 92409, 91211, 85697, 57065] ])
    # Calculate store-wise total sales (sum of all months for each store)
    store_totals = sales.sum(axis=1)  # # Sum row-wise => [725368 702832 759932 796076 877740]
    store_avg = sales.mean(axis=1)  # [60447.33333333 58569.33333333 63327.66666667 66339.66666667  73145. ]
     
    Here:
        axis=1 → works across columns (months).
        Each row (store) is summed individually.
     
    month_totals = sales.sum(axis=0)  # Sum column-wise =>[203963 366846 395738 442751 308012 318213 262564 294663 346615 277769  360076 284738]
     
    This will:
        Take all store sales for Jan and sum them.
        Then take all store sales for Feb and sum them.
        …and so on till Dec.
    
    Result shape: (203963, 366846, 395738, 442751, 308012, 318213, 262564, 294663, 346615, 277769,  360076, 284738) → one value per month.






11. Real-Life Use Cases 
    Finance: Stock price arrays, bulk calculations.
    Images: Photos are just 3D NumPy arrays (height, width, color).
    AI/ML: Every neural network uses NumPy-like arrays internally.
    Logistics: Inventory management (rows = products, columns = warehouses).

12. Super Memory Trick: The Warehouse Story
    Whenever you think of NumPy, visualize a warehouse:
    Arrays = neatly arranged shelves.
    Operations = forklift machines doing work at lightning speed.
    Broadcasting = speaker system sending one message to all workers at once.
    Axis 0 & 1 = walking vertically vs horizontally across shelves.
    
    
    
    
  
        

        

 

'''
