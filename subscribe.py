from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')        
    

@app.route('/thankyou',methods = ['POST', 'GET'])
def thankyou():
    if request.method == 'GET':
        return render_template('thankyou.html')        
    elif request.method == 'POST':        
        emailid = request.form.get('eid')
        conn = sqlite3.connect("emailist")        
        cur=conn.cursor()
        cur.execute("SELECT * from emails_table") 
        print(cur.fetchall())       
#cur.execute('INSERT INTO emails_table (email) VALUES (?), ("t@iron.com")')
#cur.execute("INSERT INTO movie VALUES(%s,%s)",(movID,Name))
        cur.execute("INSERT INTO emails_table (email) VALUES (?)", (emailid,))
        conn.commit()
        conn.close() 
        return render_template('thankyou.html') 
    


if __name__ == '__main__':
   app.run(debug=True)
