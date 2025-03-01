from random import randint
from flask import Flask, session, redirect, url_for
from quiz_db import get_question

def index():
    max_quiz = 3
    session ['quiz'] = randint(1, max_quiz)
    session ['last_question'] = 0
    return "<a href='/test'>Тест</a>"


def test():
    global last_question
    result = get_question(session['last_question']),(session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for("result"))

    else:
        session['last_question'] = result[0]
        return "<h1>" + str(session['quiz']) + "<br>" + str(result) + "</h1>"


def result():
    return "that's all folks!"


# Створюємо об'єкт веб-застосунку:
app = Flask(__name__)
app.add_url_rule("/", "index", index)  # створює правило для URL "/"
app.add_url_rule("/test", "test", test)  # створює правило для URL "/test"
app.add_url_rule("/result", "result", result)  # створює правило для URL "/result"

if __name__ == "__main__":
    # Запускаємо веб-сервер:
    app.run()
