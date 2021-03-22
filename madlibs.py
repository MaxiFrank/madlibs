"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def index():
    """Display homepage."""

    return render_template("index.html")

# @app.route('/hello')
# def say_hello():
#     """Say hello to user."""

#     return render_template("hello.html")


# @app.route('/greet')
# def greet_person():
#     """Greet user with compliment."""

#     player = request.args.get("person")

#     compliment = choice(AWESOMENESS)

#     return render_template("compliment.html",
#                            person=player,
#                            compliment=compliment)

@app.route('/game')
def show_madlib_form():
    render_template("index.html")
    # print(request.args)
    if request.args.get('response') == 'yes':
        color_list = ['red', 'green','blue']
        return render_template("game.html", color_list=color_list)
    if request.args.get('response') == 'no':
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    print(request.args.getlist('dream'))
    # I would only get food dream here....
    print(request.args.get('dream'))

    color = request.args.get("color")
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    dream = request.args.getlist('dream')
    num_dreams = len(dream)
    return render_template("madlib.html", color=color, person=person, noun=noun, adjective=adjective, dream=dream, num_dreams=num_dreams)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
