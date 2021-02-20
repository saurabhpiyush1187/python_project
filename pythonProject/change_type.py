# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    number =12345
    #changing to [1,2,3,4,5]
    lst_num = [int(x) for x in str(number)]
    print(lst_num)

    lst_num1 = [1,2,3,4,5]
    #now chaning back to 12345
    str_n = [str(x) for x in lst_num1]
    nu = "".join(str_n)
    print(nu)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
