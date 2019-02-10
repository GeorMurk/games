#!/usr/bin/python

#!Multiple Choices

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color is the sky?\n(A) Orange\n(B) Teal\n(C) Blue\n(D) Pink\n\n",
    "What name do we give to cats?\n(A) Canines\n(B) Feline\n(C) Pony\n(D) Trot\n\n",
    "What is 4*4?\n(A) 8\n(B) 1\n(C) 44\n(D) 16\n\n",
    "What color are strawberries?\n(A) Red\n(B) Yellow\n(C) Blue\n(D) Brown\n\n"
]

questions = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "D"),
    Question(question_prompts[3], "A"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

#!Go ahead and test it out!!!

