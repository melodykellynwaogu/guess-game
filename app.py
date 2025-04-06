from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'melody123kellyvictoria'

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    if 'number' not in session:
        session['number'] = random.randint(1, 10)
        session['attempts'] = 3
        message = "Welcome to the Guessing Game! You have 3 attempts to guess the number between 1 and 10."
    else:
        message = ""

    if request.method == 'POST':
        try:
            user_guess = int(request.form['guess'])
        except ValueError:
            message = "Please enter a valid number."
            return render_template('index.html', message=message)

        session['attempts'] -= 1
        if user_guess == session['number']:
            message = f"Hurray! You guessed the number right! The number was {session['number']}."
            session.pop('number')
            session.pop('attempts')
        elif session['attempts'] <= 0:
            message = f"Sorry, you've used all attempts. The number was {session['number']}."
            session.pop('number')
            session.pop('attempts')
        else:
            message = f"Wrong guess. Try again! You have {session['attempts']} attempts left."

    return render_template("index.html", message=message)

if __name__ == '__main__':
    print("Running Flask app.py")
    app.run(debug=True)