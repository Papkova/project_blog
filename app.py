from flask import Flask, render_template


app = Flask(__name__) # корінь проекту

@app.route("/")
def home():
    return render_template("index.html", title="Main")


@app.route("/cancer_page")
def cancer_page():
    return render_template("cancer_page.html")


@app.route("/capricorn_page")
def capricorn_page():
    return render_template("capricorn_page.html")


@app.route("/aries_page")
def aries_page():
    return render_template("aries_page.html")


@app.route("/taurus_page")
def taurus_page():
    return render_template("taurus_page.html")


@app.route("/twin_page")
def twin_page():
    return render_template("twin_page.html")


@app.route("/diva_page")
def diva_page():
    return render_template("diva_page.html")


@app.route("/teresa_page")
def teresa_page():
    return render_template("teresa_page.html")


@app.route("/scorpio_page")
def scorpio_page():
    return render_template("scorpio_page.html")


@app.route("/sagittarius_page")
def sagittarius_page():
    return render_template("sagittarius_page.html")


@app.route("/aquarius_page")
def aquarius_page():
    return render_template("aquarius_page.html")


@app.route("/fish_page")
def fish_page():
    return render_template("fish_page.html")


if __name__ == "__main__":
    app.run(debug=True)