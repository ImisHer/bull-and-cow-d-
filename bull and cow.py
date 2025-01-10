"""
project_2.py: druhý projekt do Engeto Online Python Akademie
autor: Dao Quang Dung
email: daoquangdung2806@gmail.com
discord: zunz
"""
import random

def generate_secret_number():
    digits = list(range(10))
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)
    remaining_digits = random.sample(digits, 3)
    secret_number = [first_digit] + remaining_digits
    return ''.join(map(str, secret_number))

def validate_guess(guess):

    if not guess.isdigit():
        return "Zadejte pouze číslice."
    if len(guess) != 4:
        return "Číslo musí mít přesně 4 číslice."
    if len(set(guess)) != 4:
        return "Číslo musí obsahovat unikátní číslice."
    if guess[0] == '0':
        return "Číslo nesmí začínat nulou."
    return None

def evaluate_guess(secret, guess):

    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def play_game():
    print("Vítejte ve hře Bulls and Cows!")
    print("Vaším úkolem je uhodnout 4 místné tajné číslo.")
    print("Číslice jsou unikátní a číslo nezačíná nulou.")
    print("----------------------------------------------")

    secret_number = generate_secret_number()


    while True:
        guess = input("Zadejte svůj tip: ")
        validation_error = validate_guess(guess)
        if validation_error:
            print(validation_error)
            continue

        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls == 4:
            print("Gratulujeme! Uhodli jste správně tajné číslo!")
            break


        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_text}, {cows} {cow_text}")

if __name__ == "__main__":
    play_game()
