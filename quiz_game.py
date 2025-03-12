'''
QUIZ GAME:
    Write a program to create a quiz where the player answers multiple-choice
    questions. The program should evaluate the player's answers and provide a score
    at the end.
    
    Optional Enhancements
        • Allow the player to choose from different categories of questions, such as
          history, science, or geography.
    < Similar to above >
        • Implement different difficulty levels by varying the complexity of the questions.
    < TO-DO >
        • Modify the game to import questions from a CSV or JSON file, allowing for
          easy updates and additions to the quiz content.
'''
from random import shuffle
from termcolor import cprint

CATEGORY = 'category'
QUESTIONS = 'questions'
QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

categories_dict = {1: 'Geography', 2: 'Science', 3: 'History'}

def ask_category(categories):
    categories_list = ['{}. {}'.format(key, value) for key, value in categories.items()]
    print('Hello welcome to the Quiz game!!')
    print()
    print('Please select a category: ')

    for category in categories_list:
        print(category)

    selection = int(input('Your Selection: ').strip())
    cprint(f'You selected {categories[selection]}', 'green')

    return selection

def ask_question(question_number, question, options):
    print(f'Question {question_number}: {question}')
    for option in options:
        print(option)
    return input('Your answer: ').upper().strip()

def get_questions_by_category(category_name, quiz_data):
    for category in quiz_data:
        if category[CATEGORY].lower() == category_name.lower():
            return category[QUESTIONS]
    return None

def run_quiz(quiz, categories):
    
    quiz_category = ask_category(categories)
    quiz_by_category = get_questions_by_category(categories_dict[quiz_category], quiz)
    
    shuffle(quiz_by_category)

    score = 0

    for index, item in enumerate(quiz_by_category, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint(f'Wrong! The correct answer is {item[ANSWER]}.', 'red')
        print()

    print(f'Quiz over! Your final score is {score} out of {len(quiz_by_category)}.')

    return

def main():

    quiz = [
        {
            CATEGORY: 'Geography',
            QUESTIONS: [
                {
                    QUESTION: 'What is the capital of India?',
                    OPTIONS: ['A. Delhi', 'B. Mumbai', 'C. Hyderabad', 'D. Chennai'],
                    ANSWER: 'A'
                },
                {
                    QUESTION: 'Which ocean is located between Europe and USA?',
                    OPTIONS: ['A. Pacific ocean', 'B. Atlantic ocean', 'C. Indian ocean', 'D. Arctic ocean'],
                    ANSWER: 'B'
                },
                {
                    QUESTION: 'Which continent is Mangolia located in?',
                    OPTIONS: ['A. Europe', 'B. Australia', 'C. Asia', 'D. Africa'],
                    ANSWER: 'C'
                },
                {
                    QUESTION: 'What is the capital of Australia?',
                    OPTIONS: ['A. Melborne', 'B. Adelide', 'C. Sydney', 'D. Canberra'],
                    ANSWER: 'D'
                }
            ]
        },
        {
            CATEGORY: 'History',
            QUESTIONS: [
                {
                    QUESTION: 'Who was the first Emperor of the Maurya Dynasty?',
                    OPTIONS: ['A. Ashoka', 'B. Chandragupta Maurya', 'C. Bindusara', 'D. Samudragupta'],
                    ANSWER: 'B'
                },
                {
                    QUESTION: 'In which year did India gain independence from British rule?',
                    OPTIONS: ['A. 1947', 'B. 1950', 'C. 1935', 'D. 1942'],
                    ANSWER: 'A'
                },
                {
                    QUESTION: 'Who was the leader of the Indian National Congress during the Salt March in 1930?',
                    OPTIONS: ['A. Jawaharlal Nehru', 'B. Subhas Chandra Bose', 'C. Mahatma Gandhi', 'D. Sardar Patel'],
                    ANSWER: 'C'
                },
                {
                    QUESTION: 'The Battle of Plassey (1757) was fought between the forces of the British East India Company and which Indian ruler?',
                    OPTIONS: ['A. Tipu Sultan', 'B. Shershah Suri', 'C. Rani Durgavati', 'D. Mir Jafar'],
                    ANSWER: 'D'
                }
            ]
        },
        {
            CATEGORY: 'Science',
            QUESTIONS: [
                {
                    QUESTION: 'What is the chemical symbol for water?',
                    OPTIONS: ['A. O2', 'B. H2O', 'C. CO2', 'D. O3'],
                    ANSWER: 'B'
                },
                {
                    QUESTION: 'What planet is known as the Red Planet?',
                    OPTIONS: ['A. Venus', 'B. Earth', 'C. Jupiter', 'D. Mars'],
                    ANSWER: 'D'
                },
                {
                    QUESTION: 'Which gas do plants absorb during photosynthesis?',
                    OPTIONS: ['A. Oxygen', 'B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen'],
                    ANSWER: 'C'
                },
                {
                    QUESTION: 'What is the powerhouse of the cell?',
                    OPTIONS: ['A. Mitochondria', 'B. Ribosome', 'C. Nucleus', 'D. Chloroplast'],
                    ANSWER: 'A'
                }
            ]
        }
    ]


    run_quiz(quiz, categories_dict)

if __name__ == '__main__':
    main()
