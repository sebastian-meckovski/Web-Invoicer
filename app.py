from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
       first_name = request.form.get("firstname")
       last_name = request.form.get("lasttname")
       adress_line1 = request.form.get("adress_line1")
       adress_line2 = request.form.get("adress_line2")
       zip_postal = request.form.get("zip_postal")

       first_name_client = request.form.get("firstnameclient")
       last_name_client = request.form.get("lasttnameclient")
       adress_line1_client = request.form.get("adress_line1_client")
       adress_line2_client = request.form.get("adress_line2_client")
       zip_postal_client = request.form.get("zip_postal_client")

       item_name = request.form.get("item_name")
       quantity = request.form.get("qty")
       rate = request.form.get("rate")

       print("Name:", first_name, "\n",
             "lasttname:", last_name, "\n",
             "AdressLine1:", adress_line1, "\n",
             "AdressLine2:", adress_line2, "\n",
             "postal code:", zip_postal, "\n")
 
       
       print("client first Name:", first_name_client, "\n",
             "client lasttname:", last_name_client, "\n",
             "client AdressLine1:", adress_line1_client, "\n",
             "client AdressLine2:", adress_line2_client, "\n",
             "client postal code:", zip_postal_client, "\n")

       print("item name:", item_name, "\n",
             "Qantity:", quantity, "\n",
              "Rate:", rate, "\n")


    return render_template("home.html")

if __name__ == '__main__':
    app.run()