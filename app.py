from logging import NullHandler
from flask import Flask, send_from_directory 
from pywebio.input import *
from pywebio.output import * 
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio import start_server



import pickle 
import numpy as np
import pandas as pd
import argparse

model = pickle.load(open('sat.pkl', 'rb'))
app = Flask(__name__)

def predict():
    SAT  = input("Enter the SAT Number :", type = NUMBER)

    prediction = model.predict([[SAT]])
    #output("The predicted chance of getting admitted is {}%".format(prediction[0]*100))
    put_text("Your score is: ", str(prediction))


app.add_url_rule('/tool', 'webio_view', webio_view(predict), methods=['GET', 'POST', 'OPTIONS'])
#app.run(host = 'localhost', port = 5000, debug = True)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)

