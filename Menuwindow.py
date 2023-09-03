from PyQt5.QtWidgets import *

def menuWind():
    window = QDialog()

    questLbl = QLabel("Питання")
    questEdit = QLineEdit()

    rightAnswerLbl = QLabel("Правильна відповідь")
    rightAnswerEdit = QLineEdit()

    addBtn = QPushButton("Добавити")

    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(questLbl)
    h1.addWidget(questEdit)
    mainLine.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(questLbl)
    h2.addWidget(rightAnswerEdit)
    mainLine.addLayout(h2)

    def addFunc():
        base.quest.append(
        {
            "питання": questEdit.text(),
            "Правильна відповідь": rightAnswerLbl(),
            "не правильна1": "",
            "не правильна2": "",
            "не правильна3": "",
        }
    )

    mainLine.addWidget(addBtn)
    addBtn.clicked.connect(addFunc)


    window.setLayout(mainLine)
    window.show()
    window.exec()