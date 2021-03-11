# Imports

from flask import Flask, jsonify
from flask import render_template
import pandas as pd

# Flask setup 
app = Flask(__name__) 


##############
# Flask routes
##############

# Main route 
@app.route("/")
def welcome(): 
    return render_template("index.html")

@app.route("/data")
def data():
    return pd.read_csv("data.csv").to_csv()


      

if __name__ == "__main__":
  app.run(debug=True) 