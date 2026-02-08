#!/usr/bin/env python3

import json
import os
import random
import uuid
from datetime import datetime

def load_questions(filename):
	"""Load and return questions from a JSON file.

	Args:
		filename: Path to the JSON file containing questions.

	Returns:
		A list of question dictionaries.
	"""
	with open(filename, 'r') as f:
		return json.load(f)

def ask_random_question(questions):
	"""Select a random question, prompt the user for an answer, and return the question id and answer.

	Args:
		questions: A list of question dictionaries, each containing "id" and "question" keys.

	Returns:
		A tuple of (question_id, answer).
	"""
	question = random.choice(questions)
	print("Question:", question["question"])
	answer = input("Your answer: ")
	print(f"You answered: {answer}")
	return question["id"], answer

def save_answer(question_id, answer):
	"""Save an answer entry with a UUID, question id, timestamp, and answer to my_answers.json.

	Args:
		question_id: The id of the question that was answered.
		answer: The user's answer string.
	"""
	dir_path = os.path.dirname(os.path.abspath(__file__))
	filepath = os.path.join(dir_path, "my_answers.json")

	if os.path.exists(filepath):
		with open(filepath, 'r') as f:
			answers = json.load(f)
	else:
		answers = []

	entry = {
		"id": str(uuid.uuid4()),
		"questionId": question_id,
		"timestamp": datetime.now().isoformat(),
		"answer": answer
	}
	answers.append(entry)

	with open(filepath, 'w') as f:
		json.dump(answers, f, indent=4)

if __name__ == "__main__":
	questions = load_questions("dks.json")
	last_question_id, last_answer = ask_random_question(questions)
	
while True:
    cont = input("Please select one of the following options:\n 1. Ask another question\n 2. Save your answer with today's date\n 3. Exit\n Your choice: ").strip().lower()
    if cont == '1':
        last_question_id, last_answer = ask_random_question(questions)
    elif cont == '2':
        save_answer(last_question_id, last_answer)
        print("Your answer has been saved.")
    elif cont == '3':
        print("Program terminated. OSU!")
        break
    else:
        print("Invalid option. Please try again.")

