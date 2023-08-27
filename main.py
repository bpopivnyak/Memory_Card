from PyQt5.QtWidgets import *
import random
import base

app = QApplication([])
window = QWidget()
window.resize(500, 500)
mainLine = QVBoxLayout()
menuBth = QPushButton("Меню")
restBth = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
answerBth = QPushButton("Відповісти")
nextQuestBth = QPushButton("Наступне питання")
nextQuestBth.hide()
firstLine = QHBoxLayout()
firstLine.addWidget(menuBth)
firstLine.addWidget(restBth)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)

answersGroup = QGroupBox("Варіанти відповідей")
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answers = [answer1, answer2, answer3, answer4]
answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)

result = QLabel("Результат")
answersLine.addWidget(result)
result.hide()

answersGroup.setLayout(answersLine)

mainLine.addWidget(answersGroup)
mainLine.addWidget(answerBth)
mainLine.addWidget(nextQuestBth)

def setQuest():
    random.shuffle(answers)
    questLbl.setText(base.quest[base.currentQuest]["питання"])
    answers[0].setText(base.quest[base.currentQuest]["Правильна відповідь"])
    answers[1].setText(base.quest[base.currentQuest]["не правильна1"])
    answers[2].setText(base.quest[base.currentQuest]["не правильна2"])
    answers[3].setText(base.quest[base.currentQuest]["не правильна3"])

def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    result.show()
    nextQuestBth.show()
    answerBth.hide()
    if answers[0].isChecked():
        result.setText("Правильно")
    else:
        result.setText("не правильно")


answerBth.clicked.connect(showResult)

window.setLayout(mainLine)
window.show()
app.exec()