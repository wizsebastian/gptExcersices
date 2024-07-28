import random
from typing import List, Dict, Tuple

from transformers import GPT2LMHeadModel, GPT2Tokenizer, MarianMTModel, MarianTokenizer


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

    def generate_random_words(self, model, tokenizer, num_words=10):
        input_ids = tokenizer.encode("List of random words:", return_tensors="pt")
        outputs = model.generate(
            input_ids,
            max_length=100,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        words = generated_text.split()[
            4 : 4 + num_words
        ]  # Obtener las palabras generadas
        return words

    def translate_text(self, text, model, tokenizer):
        inputs = tokenizer.encode(
            text,
            return_tensors="pt",
            max_length=512,
            truncation=True,
            pad_token_id=tokenizer.eos_token_id,
        )
        translated = model.generate(
            inputs,
            max_length=512,
            num_beams=4,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id,
        )
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text


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

    gpt2_model_name = "gpt2"
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained(gpt2_model_name)
    gpt2_model = GPT2LMHeadModel.from_pretrained(gpt2_model_name)

    translation_model_name = "Helsinki-NLP/opus-mt-en-es"
    translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
    translation_model = MarianMTModel.from_pretrained(translation_model_name)

    random_words = trainer.generate_random_words(
        gpt2_model, gpt2_tokenizer, num_words=5
    )
    translations = [
        {
            "english": word,
            "translation": trainer.translate_text(
                word, translation_model, translation_tokenizer
            ),
        }
        for word in random_words
    ]

    for item in translations:
        print(f"{item['english']} -> {item['translation']}")


if __name__ == "__main__":
    main()
