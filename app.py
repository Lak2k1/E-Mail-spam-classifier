from flask import *
app = Flask(__name__) 

import pickle
with open('spmprd_pkl', 'rb') as f:
    sp=pickle.load(f)

@app.route('/') 
def home():  
    return render_template("layout.html",pr='')

@app.route('/pred',methods=['GET','POST'])   
def pred():
    msg=[request.form['msg']]
    if((sp[0].predict(sp[1].transform(msg))[0])==1):
        return render_template("layout.html",pr="It's a spam!!!")
    else:
        return render_template("layout.html",pr="It's a genuine text.")

if __name__ =='__main__':  
    app.run(debug = True)