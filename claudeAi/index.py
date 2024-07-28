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

    # def run_quiz(self)


def main():
    word_list = [
        {"english": "Hello", "translation": "Hola"},
        {"english": "Goodbye", "translation": "Adiós"},
        {"english": "Thank you", "translation": "Gracias"},
        {"english": "Please", "translation": "Por favor"},
        {"english": "How are you?", "translation": "¿Cómo estás?"},
    ]

    # trainer


if __name__ == "__main__":
    main()
