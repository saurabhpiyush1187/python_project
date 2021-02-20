# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    regex = "^-?[0-9]\d*(\.\d+)?$"
    p=re.compile(regex)
    a=str(np.inf)
    b=str(-np.inf)
    c= str(-10.0)

    print(bool(re.match(p,a)))
    print(bool(re.match(p,c)))

    print(5//3)
    print(5/3)
    print(3//5)
    print(0/5)
    print(3/5)
    print(10/5)
    print(0/0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
