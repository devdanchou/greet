from flask import Flask, request
app = Flask(__name__)

DIRECTIONS = {

}

@app.get('/welcome')
def print_welome():
    """returns welcome"""

    return """
        <html>
        <body>
        <h1> welcome </h1>
        <body>
        <html>
    """

@app.get('/welcome/<direction>')
def print_welome():
    """returns welcome"""

    return """
        <html>
        <body>
        <h1> welcome </h1>
        <body>
        <html>
    """