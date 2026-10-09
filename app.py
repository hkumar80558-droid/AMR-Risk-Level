from flask import Flask, render_template
import json

app = Flask(__name__)

districts = [
    "Bilaspur",
    "Chamba",
    "Hamirpur",
    "Kangra",
    "Kinnaur",
    "Kullu",
    "Lahaul and Spiti",
    "Mandi",
    "Shimla",
    "Sirmaur",
    "Solan",
    "Una"
]


@app.route("/")
def home():
    return render_template("index.html", districts=districts)


@app.route("/district/<district_name>")
def district(district_name):

    with open("data/amr_data.json", "r", encoding="utf-8") as file:
        amr_data = json.load(file)

    district_data = amr_data.get(district_name, [])

    return render_template(
        "district.html",
        district=district_name,
        data=district_data
    )


if __name__ == "__main__":
    app.run(debug=True)