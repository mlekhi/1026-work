# defining the class
class QuizQuestion:
    # initializing the instance variables in the constructor
    def __init__(self, qNum, qText, possibleAnswers, correctAnswer):
        self._qNum = int(qNum)
        self._qText = str(qText)
        self._possibleAnswers = list(possibleAnswers)
        self._correctAnswer = int(correctAnswer)

    # method displaying the question and possible answers
    def show(self):
        # printing the question number and text
        print(f"Question {self._qNum}: {self._qText}")
        # setting option number to 1
        option = 1
        # looping through the possible answers to display them individually
        for answer in self._possibleAnswers:
            print(f"{option}. {answer}")
            # increasing option by increments of 1 to denote which number corresponds to a possible answer
            option += 1

    # method correcting the question
    def mark(self, answerAttempt):
        # checking if the correct answer matches the inputted one; returning True if so
        if (self._correctAnswer) == int(answerAttempt):
            return True
        # returning False if they don't match
        else:
            return False
