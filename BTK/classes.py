from operator import index
from random import choices


class Question:
    def __init__(self, question = "", choices = [], answer = ""):
        self.question = question
        self.choices = choices
        self.answer = answer
    def check_answer(self,user_answer):
        return user_answer == self.answer

        print()
class Quiz(Question):
    def __init__(self, questions):
        super().__init__(question = "", choices = [], answer = "")
        self.questions = questions
        self.questionIndex = 0
        self.score = 0
    def getQuestions(self):
        return self.questions[self.questionIndex]
    #def print_questions(self):
        #print(questions[self.questionIndex].question)
        #for choice in questions[self.questionIndex].choices:
        #    print(f"*{choice}", end="")
        #print()
        #self.questionIndex += 1
    def displayQuestion(self):
        problem = self.getQuestions()
        self.displayProgress()
        print(f"Soru {self.questionIndex + 1}: {problem.question}")

        for c in problem.choices:
            print(c)
        answer = input("answer: ")
        self.guess(answer)
    def guess(self, answer):
        problem = self.getQuestions()
        if problem.check_answer(answer):
            self.score += 1
        
        self.questionIndex += 1
        self.loadQuestion()
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
    def showScore(self):
        print(f"Your final score is {self.score}")
    def displayProgress(self):
        print(f"Question number {self.questionIndex+1}/{len(self.questions)}".center(195, '-'))

q1 = Question("Hangisi tek sayidir?", ['3', '4', '6', '10'], '3')
q2 = Question("Hangisi çift sayidir?", ['3', '4', '31', '69'], '4')
questions = [q1,q2]
quiz = Quiz(questions)
quiz.loadQuestion()
#inputChoice = str(input())
#print(quiz.check_answer(inputChoice))
            
    