from jinja2 import Environment, FileSystemLoader
from flask import Flask


app = Flask(__name__)


@app.route('/')
def persons_online():

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("persons.html")

    persons = [
        {'name': 'Andrej', 'age': 34},
        {'name': 'Mark', 'age': 17},
        {'name': 'Thomas', 'age': 44},
        {'name': 'Lucy', 'age': 14},
        {'name': 'Robert', 'age': 23},
        {'name': 'Dragomir', 'age': 54}
    ]

    return template.render(persons=persons)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
