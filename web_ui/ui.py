from flask import Flask, render_template,session, redirect
from scratch import test
test_image_data = ""
app = Flask(__name__)
class TestPark():
        def __init__(self):
            self.lat = 44.59824417
            self.lon = -110.5471695
            self.park_code = "yell"
            self.forecast: OrderedDict = None
            self.full_name = 'Yellowstone'
yellowstone=TestPark()
extracted_data,err = test.get_api_response(yellowstone)
# print(extracted_data)
test.extract_data(yellowstone, extracted_data)
park_list=[yellowstone]
@app.route("/")
def home():
    return render_template("index.html", image_list=test_image_data)

@app.route("/save", methods=['POST'])
def save():
    park = request.form.get('park_code')
    include_weather = request.form.get('include_weather')
    print(park, include_weather)


@app.route("/display_saved_parks")
def display_saved_parks():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)