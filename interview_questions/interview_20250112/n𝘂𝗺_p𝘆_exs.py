'''
    Q6. Create a NumPy array from a list of integers
    Q7. Explain the difference between arange(), linspace(), and logspace()
        -> arange(): Generates values with a specific step size (e.g., np.arange(0, 10, 2) -> [0, 2, 4, 6, 8]).
        -> linspace(): Generates evenly spaced values between a start and end point, including both (e.g., np.linspace(0, 10, 5) -> [0, 2.5, 5, 7.5, 10]).
        -> logspace(): Generates values evenly spaced on a logarithmic scale (e.g., np.logspace(1, 3, 3) -> [10^1, 10^2, 10^3]).
    Q8. Reshape a 1D array into a 2D matrix
    Q9. Find the mean, median, and standard deviation of a NumPy array
    Q10. Perform element-wise addition and multiplication of two arrays

'''

import numpy as np




if __name__ == "__main__":
    # Q6. Create a NumPy array from a list of integers
    # Create a NumPy array
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("arr:", arr)

    # Q8. Reshape a 1D array into a 2D matrix
    # Reshape into 2x3 matrix
    reshaped_arr = arr.reshape(2, 3)

    print("reshaped_arr: ", reshaped_arr)

    # Q9. Find the mean, median, and standard deviation of a NumPy array
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)

    print(f"Mean: {mean}, Median: {median}, Std Dev: {std_dev}")

    # Q10. Perform element-wise addition and multiplication of two arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    # Element-wise addition
    add_result = arr1 + arr2

    # Element-wise multiplication
    mult_result = arr1 * arr2

    print(f"Addition: {add_result}, Multiplication: {mult_result}")
