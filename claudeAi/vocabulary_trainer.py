import random
from typing import List, Dict, Tuple


class VocabularyTrainer:
    def __init__(self, world_list: List[Dict[str, str]]):
        self.word_list = world_list
        self.score = 0
        self.total_words = len(world_list)

    def get_random_word(self) -> Dict[str, str]:
        return random.choice(self.word_list)

    def check_answer(self, world: Dict[str, str], user_answer: str) -> bool:
        return user_answer.lower() == world["translation"].lower()

    def run_quiz(self, num_questions) -> None:
        counter = 0
        for _ in range(num_questions):
            counter += 1
            word = self.get_random_word()
            print(f"\nTranslate this word : {word['english']}")
            user_answer = input("Your answer")

            if self.check_answer(word, user_answer):
                print("Correct, you are duro! ")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is : {word['translation']}")

            if counter == num_questions:

                print(f"\nQuiz finished! Your score : {self.score}/{num_questions}")
            else:
                print(f"\nYour score : {self.score}/{num_questions}")


def main():
    print("Welcome to the learing console app")
    print("------------WIZ------------")
    print("@GM GROUP.")
    selected_rounds = input("How may round you want try, example: 1, 2, 3? ")
    word_list = [
        {"english": "Hello", "translation": "Hola"},
        {"english": "Goodbye", "translation": "Adiós"},
        {"english": "Thank you", "translation": "Gracias"},
        {"english": "Please", "translation": "Por favor"},
        {"english": "How are you?", "translation": "¿Cómo estás?"},
    ]

    # trainer
    trainer = VocabularyTrainer(word_list)
    trainer.run_quiz(int(selected_rounds))


if __name__ == "__main__":
    main()
