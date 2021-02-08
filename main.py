import uuid
import time
import random
import sqlite3
from colorama import Fore

# conn = sqlite3.connect('calculon.db')

# todo: read from db
user_details = {
    'user_level': '2',
    'last_completed_kata_id': None
}

kata_levels = {
    '1': {
        'factor_range': [10, 100]
    },
    '2': {
        'factor_range': [10, 200]
    }
}

def generate_multiplication_problem():
    factor_range = kata_levels[user_details['user_level']]['factor_range']

    multiplicand = random.randrange(factor_range[0], factor_range[1]) # todo: read range from difficulty setting
    multiplier = random.randrange(factor_range[0], factor_range[1])

    if (multiplicand % 2 != 0) and (multiplier % 2 != 0):
        print(f'Unsimplifiable problem ({multiplicand} x {multiplier}). Generating a better one.')
        return generate_multiplication_problem()

    product = multiplicand * multiplier
    # difficulty = calculate_difficulty(product,mult)
    difficulty = 2

    return {
        'factors': {
            'multiplicand': multiplicand,
            'multiplier': multiplier
        },
        'product': product,
        'difficulty': difficulty,
        'time_based_awards': {
            'unit': 'seconds',
            'gold': 30, # eventually calculate time based on difficulty
            'silver': 60,
            'bronze': 90
        },
        'kata_id': str(uuid.uuid4())
    }


def find_award(kata, time_taken):
    kata_medals = kata['time_based_awards']

    if time_taken <= kata_medals['gold']:
        return 'Gold'
    elif time_taken <= kata_medals['silver']:
        return 'Silver'
    elif time_taken <= kata_medals['bronze']:
        return 'Bronze'
    else:
        return None


def multiplication_handler(prev_attempted_kata = None):
    kata = generate_multiplication_problem() if not prev_attempted_kata else prev_attempted_kata
    factors = kata['factors']
    product = kata['product']

    start_time = int(time.time())

    print(f"Find the product of {factors['multiplicand']} x {factors['multiplier']}")
    user_answer = input('Answer: ')
    
    time_taken_on_kata = time.time() - start_time

    if int(user_answer) == product:
        print('That is correct. Well done.')
        # handle_passed_kata(kata)—
        print(f'Time taken: {int(time_taken_on_kata)} seconds')
        print(f'Medals: {find_award(kata, time_taken_on_kata)}')
        multiplication_handler()

    else:
        print('Incorrect. Try again.')
        multiplication_handler(kata)


handlers = {
    'multiplication': multiplication_handler
}

def generate_multiplication_problem():
    factor_range = kata_levels[user_details['user_level']]['factor_range']

    multiplicand = random.randrange(factor_range[0], factor_range[1]) # todo: read range from difficulty setting
    multiplier = random.randrange(factor_range[0], factor_range[1])

    if (multiplicand % 2 != 0) and (multiplier % 2 != 0):
        print(f'Unsimplifiable problem ({multiplicand} x {multiplier}). Generating a better one.')
        return generate_multiplication_problem()

    product = multiplicand * multiplier
    # difficulty = calculate_difficulty(product,mult)
    difficulty = 2

    return {
        'factors': {
            'multiplicand': multiplicand,
            'multiplier': multiplier
        },
        'product': product,
        'difficulty': difficulty,
        'time_based_awards': {
            'unit': 'seconds',
            'gold': 30, # eventually calculate time based on difficulty
            'silver': 60,
            'bronze': 90
        },
        'kata_id': str(uuid.uuid4())
    }

def header():
    print('Math Dojo version 0.0.1')
    print('Creator: FRTNX')
    print('Contact: frtnx@protonmail.com')
    print('\n\n')
    print('                ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMM' + Fore.RESET + ' ################')
    print('              ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMM' + Fore.RESET + ' ####################')
    print('            ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMM' + Fore.RESET + ' #######################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMM' + Fore.RESET + ' ###########################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMM' + Fore.RESET + ' ############################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMM' + Fore.RESET + ' ##########     ##############')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMM' + Fore.RESET + ' ##########     ##############')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMM' + Fore.RESET + ' #############################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMM' + Fore.RESET + ' ############################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMM' + Fore.RESET + ' ###########################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMM' + Fore.RESET + ' #########################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' ######################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' ###################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' #################')
    print('           ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' ###############')
    print('            ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' ############')
    print('              ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.RESET + ' ##########')
    print('                ' + Fore.LIGHTBLACK_EX + ' MMMMMMMMMM     MMMMMMMMM' + Fore.RESET + ' ########')
    print('\n\n')
    print("""Welcome to the Dojo where true skills are forged and tested.\n""")
    return


def exit_banner():
    print('\n\n')
    print('                 MMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ################' + Fore.RESET)
    print('               MMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ####################' + Fore.RESET)
    print('             MMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' #######################' + Fore.RESET)
    print('            MMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ###########################' + Fore.RESET)
    print('            MMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ############################' + Fore.RESET)
    print('            MMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ##########     ##############' + Fore.RESET)
    print('            MMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ##########     ##############' + Fore.RESET)
    print('            MMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' #############################' + Fore.RESET)
    print('            MMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ############################' + Fore.RESET)
    print('            MMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ###########################    MATH DOJO' + Fore.RESET)
    print('            MMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' #########################' + Fore.RESET)
    print('            MMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ######################' + Fore.RESET)
    print('            MMMMMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ###################' + Fore.RESET)
    print('            MMMMMMMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' #################' + Fore.RESET)
    print('            MMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ################' + Fore.RESET)
    print('             MMMMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ############' + Fore.RESET)
    print('               MMMMMMMMMMMMMMMMMMMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ##########' + Fore.RESET)
    print('                 MMMMMMMMMM     MMMMMMMMM' + Fore.LIGHTBLACK_EX + ' ########' + Fore.RESET)
    print('\n\n')
    return

if __name__ == '__main__':
    try:
        header()
        # category = category_selection()
        category = 'multiplication'
        handlers[category]()
    except KeyboardInterrupt:
        exit_banner()
        

