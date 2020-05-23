from flask import Flask, render_template, request
from com.nico.webapp.data.postgresdb import save,  select


app = Flask(__name__)

#variables
id = [1, 2]
person_hobby = ['rugby', 'cooking', 'cooking', 'cooking', 'cooking']


@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/about')
def home():
    return render_template("about_page.html")

@app.route('/contact')
def contact():
    return render_template("contact_page.html")

@app.route('/register_post', methods = ['POST'])
def register_post():
    return render_template("register.html")

@app.route('/register_post', methods = ['POST'])
def register_post_data():
    try:
        if request.method == 'POST':
            person_name = request.form['name_person_register']
            person_familly_name = request.form['family_name_person_register']
            person_hobby = request.form['hobbies_person_register']
            person_adding_new_hobby = request.form['new_hobby_person_register']
            save(person_name, person_familly_name, person_hobby, person_adding_new_hobby)
    except Exception as e:
        print(e)


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/registered')
def vieuw_registered():
    return render_template("registered.html", id_person = id)

register_post_data()


if __name__ == '__main__':
     app.run(debug=True)