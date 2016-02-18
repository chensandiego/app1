from flask import Flask
app=Flask(__name__)


import application.models
import application.views


if __name__=='__main__':
    app.run()
