from flask import Flask, render_template


app = Flask(__name__) # корінь проекту

@app.route("/")
def home():
    return render_template("index.html", title="Main")


sign_routes = {
    "cancer": "cancer_page.html",
    "capricorn": "capricorn_page.html",
    "aries": "aries_page.html",
    "taurus": "taurus_page.html",
    "twin": "twin_page.html",
    "diva": "diva_page.html",
    "teresa": "teresa_page.html",
    "scorpio": "scorpio_page.html",
    "sagittarius": "sagittarius_page.html",
    "aquarius": "aquarius_page.html",
    "fish": "fish_page.html"
}




@app.route("/page/<int:id>")
def page(id):
    name = Sign.query.get(id)
    sign_name = name.name.lower()
    page_function = sign_routes.get(sign_name)
    if page_function is not None:
        return page_function
    else:
        return "404 - Page Not Found", 404

if __name__ == "__main__":
    app.run(debug=True)