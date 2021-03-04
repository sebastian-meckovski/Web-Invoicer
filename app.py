from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        print("this is what we get:  ", entry_content)


    return render_template("home.html")

if __name__ == '__main__':
    app.run()