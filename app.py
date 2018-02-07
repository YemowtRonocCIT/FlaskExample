from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "Conor",
        'description': "Example of REST API"
    }, 
    {
        'id': 2,
        'name': "Mary",
        'description': "Example 2 of REST API"
    }, 
    {
        'id': 3,
        'name': "Harry",
        'description': "Example 3 of REST API"
    }
]

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

@app.route("/hello/<name>")
def hello_name_v2(name):
    return "Hello %s!" % name

@app.route("/template/<name>")
def template_example(name=None):
    return render_template('hello.html', name=name)

@app.route("/rest/example")
def rest_example():
    return jsonify(tasks)

@app.route("/input/form")
def flask_input():
    return render_template('form_input.html')

@app.route("/input/form/response", methods=['POST'])
def form_input_response():
    request_form = request.form
    print(request_form)
    response = request_form.get('response')

    return_string = "I don't understand"
    if response == 'ok':
        return_string = "That's good"
    elif response == 'not ok':
        return_string = "That's not good"
        
    template = render_template('form_response.html', response=return_string)
    return template

@app.route("/input/js")
def js_input():
    return render_template('js_input.html')

if __name__ == "__main__":
    app.run()