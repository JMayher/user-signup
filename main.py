from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True


    


@app.route("/", methods=['POST'])
def validate():
    user=request.form['user']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']
    usererror=""
    passworderror=""
    emailerror=""
    lenerror=""
    c = 0
    p = 0
    error = "Your password cannot contain spaces"
    emailerror = "The email you entered is invalid"

    if email.strip() != "":
        for y in email:
            if y in string.whitespace:
                return render_template('edit.html', emailerror=emailerror)
            elif y == "@":
                c = c + 1
                if c != 1:
                    return render_template('edit.html', emailerror=emailerror)
            elif y == ".":
                p = p + 1
                if p != 1:
                    return render_template('edit.html', emailerror=emailerror, user=user, email=email)
            
            elif len(email) < 3 or len(email) > 20:
                return render_template('edit.html', emailerror=emailerror, user=user, email=email)
        if "@" not in email:
            return render_template('edit.html', emailerror=emailerror, user=user, email=email)
        if "." not in email:
            return render_template('edit.html', emailerror=emailerror, user=user, email=email)

    

    for x in password:
        if x in string.whitespace:
            return render_template('edit.html', error=error, user=user, email=email)
    
    if user.strip() == "" or password.strip() == "" or verify.strip() == "":
        
        usererror = "Please complete all the mandatory fields"  
        return render_template('edit.html', usererror=usererror, user=user, email=email)
    elif password != verify:
        passworderror = "Your Password and Verify Password do not match"
        return render_template('edit.html', passworderror=passworderror, user=user, email=email)
    elif len(user) < 3 or len(user) > 20:
        lenerror = "Your username does not contain the proper number of characters"
        return render_template('edit.html', lenerror=lenerror, user=user, email=email)
    elif len(password) < 3:
        lenerror1 = "Your password does not contain the proper number of characters"
        return render_template('edit.html', lenerror1=lenerror1, user=user, email=email)
    else:
        return render_template('welcome.html', user=user)

@app.route("/")
def index():
    return render_template('edit.html')


app.run()