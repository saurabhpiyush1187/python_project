# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    int_number = '786890'
    print(int_number)
    int_k =2
    lent = len(int_number)

    #for moving last 2 digits to front shifting right
    int_k%=lent
    for i in range(0,lent):
         p = int_number[(i+(lent-int_k))%lent]
         print(str(p),end="")
    print("\n")

    #shifting left
    k=2
    msg=" "
    k= lent-k
    for i in range(0,lent):
        p1 = int_number[(i+(lent-k))%lent]
        msg = msg+str(p1)+ ""
    print(msg[1:])







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






