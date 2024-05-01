"""Q4. Ask 5 integers from user. 
Then ask a single character from user. Print those integers 
separated by that character entered by user"""


def func() -> str:
    user_input_list = []
    result_string = ""

    for i in range(0, 5):
        temp1 = input("Enter an interger :")
        user_input_list.append(temp1)

    temp2 = input("Enter a Character: ")

    return temp2.join(user_input_list)


print(func())
