# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    s1 = "aabbddreeecccaabddd"
    s="abbbaca"
    char_list = []  # newer versions of Python support ordered sets

    for i in range(len(s1)):
        if char_list and char_list[-1]==s1[i]:
            char_list.pop()
            continue
        elif char_list and s1[i-1]==s1[i]:
            continue
        char_list.append(s1[i])
    print(''.join(char_list))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
