import random

def generate_random_list(l_bound, u_bound):
    new_list = []
    for _ in range(u_bound - l_bound):
        new_list.append(random.randint(l_bound, u_bound))

    new_list = set(new_list)
    new_list = list(new_list)
    return new_list

lower_bound = 5
upper_bound = 100
search_list = sorted(generate_random_list(lower_bound, upper_bound))
computer_choice = random.choice(search_list)
print(computer_choice)

print(f"Guess between {lower_bound} to {upper_bound} included both ranges.")

def binary_search(s_list, c_choice):
    user_input = int('Enter your guess: ')

    if user_input == c_choice:
        print(f"Congratulation! {user_input} is the correct number.")
    elif user_input > c_choice:
        s_list = s_list[]
