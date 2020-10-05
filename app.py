from flask import Flask,flash,render_template,request
from main import get_board
import os
app=Flask(__name__)
@app.route('/')
def new():
    leader_board=get_board()
    print(leader_board)
    return render_template('main.html',value=leader_board)


if __name__=='__main__' :
    app.run()
