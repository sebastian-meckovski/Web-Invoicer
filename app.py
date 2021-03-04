from flask import Flask, render_template, request
from invoicingCopy2 import run_stuff
from SampleData import sample_list

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
       full_name = request.form.get("firstname")
       adress_line = request.form.get("lasttname")
       city = request.form.get("city")
       country = request.form.get("country")
       zip_postal = request.form.get("zip_postal")

       full_name_client = request.form.get("firstnameclient")
       adress_line_client = request.form.get("lasttnameclient")
       city_client = request.form.get("city_client")
       country_client = request.form.get("country_client")
       zip_postal_client = request.form.get("zip_postal_client")

       item_name = request.form.get("item_name")
       quantity = request.form.get("qty")
       rate = request.form.get("rate")

       print("Name:", full_name, "\n",
             "lasttname:", adress_line, "\n",
             "AdressLine1:", city, "\n",
             "AdressLine2:", country, "\n",
             "postal code:", zip_postal, "\n")
 
       
       print("client first Name:", full_name_client, "\n",
             "client lasttname:", adress_line_client, "\n",
             "client AdressLine1:", city_client, "\n",
             "client AdressLine2:", country_client, "\n",
             "client postal code:", zip_postal_client, "\n")

       print("item name:", item_name, "\n",
             "Qantity:", quantity, "\n",
             "Rate:", rate, "\n")
      
       run_stuff(sample_list, full_name=full_name, adress_line=adress_line)



    return render_template("home.html")



if __name__ == '__main__':
    app.run()