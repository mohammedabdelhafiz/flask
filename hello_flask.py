from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)   # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/say/flask')
def flask():
  return "Hi Flask!!"

@app.route('/say/micheal')
def micheal():
  return "Hi micheal !!"

@app.route('/say/john')
def john():
  return "Hi john !!"



@app.route('/hello')
def hello():
  return render_template('index.html', phrase="hello", times=35)


@app.route('/repeat/80/bye')
def bye():
  for b in range (80):
    return "Bye"

@app.route('/repeat/99/dog')
def dog():
  for i in range (99):
    print("Dog")
  return dog()



            
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.