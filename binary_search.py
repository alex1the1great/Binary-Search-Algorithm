user_number = int(input('Enter a number for computer to guess: '))
user_lower_bound = int(input('Enter lower bound: '))
user_upper_bound = int(input('Enter upper bound: '))


def generate_list(lower_bound, upper_bound):
    return (list(range(lower_bound, upper_bound + 1)))

