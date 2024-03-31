from flask import Flask
from src.logger import logging 

app = Flask(__name__) 
@app.route('/',methods=['GET','POST'])
def index():
    logging.info("Testing Logging Information")
    return "Welcome to Machine Learning End to End Project"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)