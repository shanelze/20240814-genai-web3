from flask import Flask,render_template,request

app = Flask(__name__) #confirm that this application belongs to the user

@app.route("/", methods=["GET", "POST"]) #get means you get from frontend, post means you send to frontend
def index():
    return(render_template("index.html"))

if __name__ == "__main__": #this is a verficiation to ensure that you want to run it on cloud 
    app.run()
