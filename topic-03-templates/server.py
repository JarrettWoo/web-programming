from bottle import route, run, template

# http://localhost:8068/.... <route> 

@route("/")
def get_index():
    return ("home page!")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="world"):
    return template('hello', name=name, extra=None)

@route("/greet")
@route("/greet/<name>")
def get_greet(name="Bob"):
    return template("hello", name=name, extra="Happy Birthday!")

@route("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings", names=names)

run(host="localhost", port=8068)