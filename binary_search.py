user_number = int(input('Enter a number for computer to guess: '))
user_lower_bound = int(input('Enter lower bound: '))
user_upper_bound = int(input('Enter upper bound: '))


def generate_list(lower_bound, upper_bound):
    return (list(range(lower_bound, upper_bound + 1)))


search_list = generate_list(user_lower_bound, user_upper_bound)


def computer_guessing_user_number(s_list):
    mid_index = len(s_list) // 2

    if s_list == []:
        return 'Value not found'

    if s_list[mid_index] == user_number:
        print(search_list)
        return f"Computer found {s_list[mid_index]} in index: {search_list.index(s_list[mid_index])}"
    elif s_list[mid_index] > user_number:
        s_list = s_list[:mid_index]
        return computer_guessing_user_number(s_list)
    elif s_list[mid_index] < user_number:
        s_list = s_list[mid_index + 1: ]
        return computer_guessing_user_number(s_list)


print(computer_guessing_user_number(search_list))