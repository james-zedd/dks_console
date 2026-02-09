#!/usr/bin/env python3

import os
import json

def count_questions():
    """
    Counts the number of dictionaries in the dks.json file

    Returns:
        int: The number of dictionaries in the dks.json file
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'dks.json')

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    num_dictionaries = len(data)
    return num_dictionaries

def count_my_answers():
    """
    Counts the number of user answers stored in my_answers.json file

    Returns:
        int: The number of user answers in the my_answers.json file
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'my_answers.json')

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    num_answers = len(data)
    return num_answers

def calculate_percentage():
    """
    Calculates the percentage of questions answered by the user

    Returns:
        float: The percentage of questions answered by the user
    """
    total_questions = count_questions()
    total_answers = count_my_answers()

    if total_questions == 0:
        print("No questions available to calculate percentage.")
        return 0.0

    percentage = (total_answers / total_questions) * 100
    return percentage

def count_questions_remaining():
    """
    Counts the number of questions remaining for the user to answer

    Returns:
        int: The number of questions remaining for the user to answer
    """
    total_questions = count_questions()
    total_answers = count_my_answers()

    questions_remaining = total_questions - total_answers
    return questions_remaining  

def display_stats():
    """
    Displays the statistics of the user's progress in answering questions
    """
    total_questions = count_questions()
    total_answers = count_my_answers()
    percentage = calculate_percentage()
    questions_remaining = count_questions_remaining()

    print(f"Total Questions: {total_questions}")
    print(f"Total Answers: {total_answers}")
    print(f"Percentage Answered: {percentage:.2f}%")
    print(f"Questions Remaining: {questions_remaining}")
    
if __name__ == "__main__":
    display_stats()
    