'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    x = []
    for i in arr:           # looping through the array
        if i in x:          # checking if the number is already there
            x.remove(i)     # if so remove it 
        else:
            x.append(i)     # if it does not exist append it
    return x[0]              



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")