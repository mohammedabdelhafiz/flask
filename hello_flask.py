from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)   # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/say/flask')
def flask():
  return "Hi Flask!!"

@app.route('/say/<name>')
def funcname(name):
    return f'Hello {name}'


@app.route('/repeat/<num>/<word>')
def repeat(num,word):
  return f'{word} ' * int(num)



            
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.