from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm,LoginForm
# url_for is used for importing css/j files
# rennder_template is used for importing html files
# this is an instance of Flask class
app = Flask(__name__) #name of the module __name__
app.config['SECRET_KEY'] = '1865120e927423386b2a69296f7c5ebd'

# dummy data

posts = [
    {
        'author' : 'Corey Schafer',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'jane Schafer',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2018'
    },
]

@app.route("/") #home page
@app.route('/home')
def home():
                            #html file  # posts(left) is the arg and posts(ryt) is the dummy data from above
    return render_template('home.html', posts = posts)

@app.route("/about") #about page
def about():
    return render_template('about.html', title='About page')


                        #providing methods for form 
@app.route("/register", methods = ['GET','POST']) #register page
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash is under flask just to flash a msg and second arg is bootstrap class
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET','POST']) #login page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. PLease check username ans password", 'danger')
    return render_template('login.html', title='Login', form=form)


# Not cleared
if __name__ == '__main__':
    app.run(debug=True)


 