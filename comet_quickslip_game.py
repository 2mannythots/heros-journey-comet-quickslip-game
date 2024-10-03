import random

def start_journey():
    print("Hey, Nova! Ready to chase a comet? Meet Comet Quickslip – he’s fast, flashy, and full of potential, but he always seems just out of reach. Sound familiar? We’re going on a journey together to discover how we can catch the fleeting starlight and seize the moment.")
    user_input = input("Type 'I'm Ready' to get started: ").lower()
    if user_input == "i'm ready":
        user_sun_sign = input("Before we continue, type in your Sun Sign (e.g., Aries, Taurus, etc.): ").capitalize()
        handle_sun_sign(user_sun_sign)
    else:
        print("Come back when you're ready!")


def handle_sun_sign(sun_sign):
    responses = {
        "Aries": "Quickslip's speed is something you can relate to – always on the go. But even a fire sign needs to slow down and be present.",
        "Taurus": "I know you prefer a steady pace, but Quickslip’s zippy nature will push you out of your comfort zone.",
        "Gemini": "Quickslip’s quick flashes are just like your thoughts – constantly moving. Let’s see if we can capture a moment together.",
        # Add more signs here...
    }
    if sun_sign in responses:
        print(f"Hey, {sun_sign}! {responses[sun_sign]} Type 'Next' to continue.")
        user_input = input().lower()
        if user_input == "next":
            present_challenge(sun_sign)
        else:
            print("Looks like you're not ready yet. Take your time!")
    else:
        print("Sorry, I didn't recognize that Sun Sign. Please try again.")
        sun_sign = input("Type in your Sun Sign (e.g., Aries, Taurus, etc.): ").capitalize()
        handle_sun_sign(sun_sign)


def present_challenge(sun_sign):
    games = {
        "Aries": "Quickslip zooms through space, just like the way you charge ahead, Aries. But sometimes, rushing can make us miss out. Think about a time when moving too fast caused you to miss something important.",
        "Taurus": "Quickslip zooms through space, Taurus, and while your steady pace is comforting, sometimes opportunities require quick action. When did taking too long to decide cause you to miss out?",
        # Add more signs here...
    }
    if sun_sign in games:
        print(games[sun_sign])
        user_input = input("Type 'Next' to proceed: ").lower()
        if user_input == "next":
            present_puzzle(sun_sign)
        else:
            print("Take your time to reflect and type 'Next' when you're ready.")
    else:
        print("Unexpected error. Please restart the game.")


def present_puzzle(sun_sign):
    word_scramble = {
        "trust": "TSRUT",
        "hope": "PEHO",
    }
    word, scramble = random.choice(list(word_scramble.items()))
    print(f"Quickslip’s whizzing by with a message—unscramble this word: {scramble}")
    user_answer = input("Your answer: ").lower()
    if user_answer == word:
        print(f"Boom! Nailed it. Trust is key, {sun_sign}! Reflect on how trusting yourself might change your approach to opportunities. Hit 'Next' to continue.")
    else:
        print(f"Not quite! The correct answer was '{word}'. Don't worry; it's all part of the journey.")


if __name__ == "__main__":
    start_journey()
