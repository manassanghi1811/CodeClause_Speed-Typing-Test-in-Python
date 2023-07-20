import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an amazing programming language.",
        "Practice makes perfect.",
        "I love coding challenges!",
        "Keep calm and code on.",
        "Learning new things is always exciting.",
        "Coding is fun and rewarding.",
        "The best way to learn is by doing.",
        "Never give up on your dreams.",
        "Strive for progress, not perfection."
    ]
    return random.choice(sentences)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    sentence = generate_random_sentence()
    print("\nType the following sentence:\n")
    print(sentence)

    start_time = time.time()
    user_input = input("\nStart typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_chars = sum(a == b for a, b in zip(user_input, sentence))
    accuracy = (correct_chars / len(sentence)) * 100
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {words_per_minute:.2f}")

if __name__ == "__main__":
    typing_test()
