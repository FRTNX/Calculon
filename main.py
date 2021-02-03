import uuid
import time
import random
import sqlite3

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
        print(f'Unsimplifiable problem ({multiplicand} x {multiplier}). Generating a better one')
        return generate_multiplication_problem()

    product = multiplicand * multiplier
    # difficulty = calculate_difficulty(product)
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
        'challenge_id': str(uuid.uuid4())
    }


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
        # handle_passed_kata(kata)
        print(f'Time taken: {int(time_taken_on_kata)} seconds')
        multiplication_handler()

    else:
        print('Incorrect. Try again.')
        multiplication_handler(kata)


handlers = {
    'multiplication': multiplication_handler
}

def header():
    print("""Welcome to the Dojo where true skills are forged and tested.""")
    return

if __name__ == '__main__':
    try:
        header()
        # category = category_selection()
        category = 'multiplication'
        handlers[category]()
    except Exception as e:
        print(e)

