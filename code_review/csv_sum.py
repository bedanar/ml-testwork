import pandas as pd

EPS = 1e-10

def check_if_ten(path):
    df = pd.read_csv(path, sep=',', header=None)

    # We should check, if the file exists, so that our program doesn't crash
    if df.empty:
        print("Error reading the file: file doesn't exist or it is empty.")
        return
    
    # We must take into account the data structures laying in the CSV-file. If there are strings, 
    # we cannot make a sum. Also, if we have floating point numbers, we should also consider overflow and underflow. 
    try:
        total_sum = df.values.astype(float).sum()
    except ValueError:
        print("Error summing the numbers: the data in csv is not numeric.")
        return

    return abs(total_sum - 10) < EPS

# Writing a code this way allows us to make accessible the 'check_if_ten' function in commandline without side effects.
if __name__ == '__main__':
    print(check_if_ten('data.csv'))