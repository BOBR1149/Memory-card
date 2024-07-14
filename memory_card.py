from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox,QApplication,QMessageBox,QRadioButton,QPushButton,QWidget,QLabel,QVBoxLayout,QHBoxLayout
from random import shuffle,randint
from questions import QUESTIONS

app = QApplication([])
main_win = QWidget()
radioGroupBox = QGroupBox("Варианты ответа")

qestion = QLabel('Самая маленькая страна Европе')
rbtn_1 = QRadioButton('Люксембург')
rbtn_2 = QRadioButton('Албания')
rbtn_3 = QRadioButton('Бельгия')
rbtn_4 = QRadioButton('Ватикан')
resultGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_correct = QLabel('Ватикан')
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result)
layout_result.addWidget(lb_correct)
resultGroupBox.setLayout(layout_result)
button = QPushButton('Ответить')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radioGroupBox.setLayout(layout_ans1)
main_layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout1.addWidget(qestion)
layout2 = QHBoxLayout()
layout2.addWidget(radioGroupBox)
layout2.addWidget(resultGroupBox)
layout3 = QHBoxLayout()
layout3.addWidget(button)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)
main_win.setLayout(main_layout)
resultGroupBox.hide()
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def handle_group_box():
    if button.text() == 'Ответить':
        if answers[0].isChecked():
            lb_result.setText('Правильно')
        else:
            lb_result.setText('Неправильно')
        radioGroupBox.hide()
        resultGroupBox.show()
        button.setText('Следующий вопрос')
    else:
        radioGroupBox.show()
        resultGroupBox.hide()
        button.setText('Ответить')
def ask(question_list):
    question_text,right_answer,wrong1,wrong2,wrong3 = question_list
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    qestion.setText(question_text)
    lb_correct.setText(right_answer)

ask(QUESTIONS[randint(0, 2)])
button.clicked.connect(handle_group_box)

main_win.show()
app.exec_()
