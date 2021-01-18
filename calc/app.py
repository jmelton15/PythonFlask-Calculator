from flask import Flask
from flask import request
from operations import add,sub,mult,div
import operator



# Put your app in here.

app = Flask(__name__)

@app.route("/")
def landing_page():
    """landing page
    """
    html = """
    <html>
        <body>
            <h1> Welcome To The Calculations Landing Page</h1>
            <ul>
                <li>Type /add at end of URL for addition feature</li>
                    <ul>
                        <li>Also add in these parameters to your URL for the operation (a, b) as follows below:</li>
                        <li>"?a=(some number)&b=(some number)"
                    </ul>
                    <br>
                    <br>
                <li>Type /sub at end of URL for subtraction feature</li>
                    <ul>
                        <li>Also add in these parameters to your URL for the operation (a, b) as follows below:</li>
                        <li>"?a=(some number)&b=(some number)"
                    </ul>
                    <br>
                    <br>
                <li>Type /mult at end of URL for multiplication feature</li>
                    <ul>
                        <li>Also add in these parameters to your URL for the operation (a, b) as follows below:</li>
                        <li>"?a=(some number)&b=(some number)"
                    </ul>
                    <br>
                    <br>
                <li>Type /div at end of URL for division feature</li>
                    <ul>
                        <li>Also add in these parameters to your URL for the operation (a, b) as follows below:</li>
                        <li>"?a=(some number)&b=(some number)"
                    </ul>
                    <br>
                    <br>
                <li>Type /math/<insert add,sub,mult,or div here> at end of URL for any off the math features</li>
                    <ul>
                        <li>Also add in these parameters to your URL for the operation (a, b) as follows below:</li>
                        <li>"?a=(some number)&b=(some number)"
                        <li><b>Using /math/<some operation> is a faster way to access the calculations pages!!<b></li>
                    </ul>      
            </ul>
            <br>
            <br>
            <h1> You can also put your values here and choose the operation you'd like to do</h1>
            <form method="POST">
                <input name="a" placeholder="value for a">
                <input name="b" placeholder="value for b">
                <select name="select_ops" id="ops">
                    <option value="add">Addition</option>
                    <option value="sub">Subtraction</option>
                    <option value="mult">Multiplication</option>
                    <option value="div">Division</option>
                </select>
                <button>Submit</button>
            </form>
            <script type="text/javascript" src="brython.js"></script>
            <script type="text/javascript" src="brython_stdlib.js"></script>
        </body>
    </html>
    """
    return html

def create_url(operation):
    url = f"/math/{operation}"
    return url

@app.route("/add")
def add_queries():
    a = request.args["a"]
    b = request.args["b"]
    response = add(a,b)
    return f"""<h1>Welcome To The Addition Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} + {b} = {response}</h3>
            """
    
@app.route("/sub")
def sub_queries():
    a = request.args["a"]
    b = request.args["b"]
    response = sub(a,b)
    return f"""<h1>Welcome To The Subtraction Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} - {b} = {response}</h3>
            """
                
@app.route("/mult")
def mult_queries():
    a = request.args["a"]
    b = request.args["b"]
    response = mult(a,b)
    return f"""<h1>Welcome To The Multiplication Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} x {b} = {response}</h3>
            """
                
@app.route("/div")
def div_queries():
    a = request.args["a"]
    b = request.args["b"]
    response = div(a,b)
    return f"""<h1>Welcome To The Division Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} / {b} = {response}</h3>
            """


@app.route("/math/<operation>")
def all_in_one(operation):
    switcher = {
        "add":{
            "func":add,
            "name":"Addition",
            "symbol":"+"
            },
        "sub":{
            "func":sub,
            "name":"Subtraction",
            "symbol":"-"
            },
        "mult":{
            "func":mult,
            "name":"Multiplication",
            "symbol":"x"
            },
        "div":{
            "func":div,
            "name":"Division",
            "symbol":"/"
            }
    }
    a = request.args["a"]
    b = request.args["b"]
    
    op = switcher.get(operation, "Page For Operation Not Found")
    response = op["func"](a,b)
    
    return f"""<h1>Welcome To The {op["name"]} Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} {op["symbol"]} {b} = {response}</h3>
            """
            

@app.route("/", methods=["POST"])
def all_in_one_form():
    switcher = {
        "add":{
            "func":add,
            "name":"Addition",
            "symbol":"+"
            },
        "sub":{
            "func":sub,
            "name":"Subtraction",
            "symbol":"-"
            },
        "mult":{
            "func":mult,
            "name":"Multiplication",
            "symbol":"x"
            },
        "div":{
            "func":div,
            "name":"Division",
            "symbol":"/"
            }
    }
    operation = request.form['select_ops']
    a = request.form["a"]
    b = request.form["b"]
    op = switcher.get(operation, "Page For Operation Not Found")
    response = op["func"](a,b)
    
    return f"""<h1>Welcome To The {op["name"]} Page</h1> <br> <h2>Here Is Your Answer</h2> 
                <h3>{a} {op["symbol"]} {b} = {response}</h3> <br>
                <a href="/">Go Back To Home</a>
            """
    
        
    
    