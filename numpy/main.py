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

3. Creating Arrays  '''

a = np.array([1, 2, 3])

'''     
    Analogy:
        Think of np.array() as packing apples into a box.

        [1,2,3] is a loose bunch of apples.

        np.array() packs them into a box with structure.

        Memory Hook:

        array() = Arrange into an array (sounds like "array" → "arrange").     

4. Shapes & Dimensions
    1D array: Like a single row of lockers.
    2D array: Like rows and columns in a table.
    3D array: Like a Rubik’s cube (shelves with rows and columns). '''

np.array([[1,2,3], [4,5,6]])

'''
    Think: Rows = horizontal shelves, Columns = vertical stacks.
    Memory trick: "Shape tells you the layout."

5. NumPy Operations (Vectorized) 
    Normal Python: '''
lst = [1,2,3]
lst2 = [x+10 for x in lst]
print("lst: ", lst)
print("lst2: ", lst2)

'''
    NumPy: '''

a = np.array([1,2,3])
print("a: ", a)
b = a + 10  # हर element में 10 add होगा
print("b: ", b)

'''
    Analogy:
    Instead of adding 10 to each apple manually, NumPy uses a machine gun of math—adds to all at once.
    
    Memory Hook:    
    Broadcasting = Broadcast signal to all receivers at once.
    
    
6. Indexing & Slicing in NumPy (Detailed)
    What is Indexing?
    Indexing means picking a specific element from an array using its position.    
    Just like you have a row of lockers and each locker has a number tag (index).    
    In NumPy, indexing always starts at 0 (like Python lists).

    1D Array Indexing: '''

arr = np.array([10, 20, 30, 40, 50])
print("first element:  arr[0] = ", arr[0])  # 10 (first element)
print("fourth element: arr[3] = ", arr[3])   # 40 (fourth element)

'''
    Think: arr[3] means "locker number 3", starting from 0.
    If you use negative index, you count from the back '''
print("last element:   arr[-1] = ", arr[-1])  # 50 (last element)
print("second last:    arr[-2] = ", arr[-2])  # 40 (second last)

'''  
    NumPy slicing works like cutting pizza slices:
    
    a[0] → first slice    
    a[0:2] → first two slices    
    a[:, 0] in 2D → first slice from each row (vertical cut)
    
    Memory Hook:    
        Think: "colon = all" → : selects all items along that axis.
    
'''