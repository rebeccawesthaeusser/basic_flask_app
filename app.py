from flask import Flask, render_template, request
import database_logic_pymongo
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/database_action_search', methods=['GET'])
def database_action_search():
    if request.method == 'GET':
        try:
            username = request.args['search_user']
            message = database_logic_pymongo.find_user(username)
            return render_template('database.html', username_search=username, message_search=message)

        except KeyError:
            return render_template('database.html', username="")


@app.route('/database_action_add', methods=['POST'])
def database_action_add():
    if request.method == 'POST':
        try:
            username = request.form['add_user']
            message = database_logic_pymongo.add_user(username)
            return render_template('database.html', username_add=username, message_add=message)

        except KeyError:
            return render_template('database.html', username_add="", message_add="")


@app.route('/database_action_delete', methods=['POST'])
def database_action_delete():
    if request.method == 'POST':
        try:
            username = request.form['delete_user']
            message = database_logic_pymongo.delete_user(username)
            return render_template('database.html', username_delete=username, message_delete=message)

        except KeyError:
            return render_template('database.html', username_delete="", message_delete="")


@app.route('/database_action_update', methods=['POST'])
def database_action_update():
    if request.method == 'POST':
        try:
            username = request.form['update_user']
            age = request.form['update_age']
            if age == "":
                age = None
            message = database_logic_pymongo.update_user(username, age)
            return render_template('database.html', username_update=username, message_update=message)

        except KeyError:
            return render_template('database.html', username_update="", message_update="")


if __name__ == '__main__':
    app.run(debug=False, host=config.host, port=config.port)
