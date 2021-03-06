from flask import Flask, render_template, request, send_file, redirect
from exportPDF_function import export_PDF
from concurrent.futures import ThreadPoolExecutor
import urllib.request as urllib2
import time

app = Flask(__name__)


def openurl():
    url = 'https://seb-invoicer.herokuapp.com/'
    print('opening URL')
    urllib2.urlopen(url)
    print('URL loaded')


def reload(period=1200):
    """Load URL every 'period' seconds"""
    while True:
        openurl()
        time.sleep(period)


@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == "POST":

        full_name = request.form.get("firstname")
        adress_line = request.form.get("adress_line")
        city = request.form.get("city")
        country = request.form.get("country")
        zip_postal = request.form.get("zip_postal")
 
        full_name_client = request.form.get("firstnameclient")
        adress_line_client = request.form.get("adress_line_client")
        city_client = request.form.get("city_client")
        country_client = request.form.get("country_client")
        zip_postal_client = request.form.get("zip_postal_client")
 
        item_name = request.form.get("item_name")
        quantity = request.form.get("qty")
        rate = request.form.get("rate")
 
        sample_list = [[item_name, float(quantity), float(rate)]]
       
        print("sample LIST:", sample_list)
 
        export_PDF(sample_list,
                   full_name=full_name, 
                   adress_line=adress_line,
                   city=city,
                   country=country,
                   zip_postal=zip_postal,
                   full_name_client=full_name_client,
                   adress_line_client=adress_line_client,
                   city_client=city_client,
                   country_client=country_client,
                   zip_postal_client=zip_postal_client
                   )
 
        return redirect("/download")

    return render_template("home.html")


@app.route('/download')
def download_file():
    p = "Invoice.pdf"
    return send_file(p, as_attachment=True)


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(reload)

if __name__ == '__main__':
    app.run()
