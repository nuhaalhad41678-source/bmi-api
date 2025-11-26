from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "BMI API is running with Flask!"})

@app.route("/bmi", methods=["POST"])
def calculate_bmi():
    data = request.get_json()
    weight = data.get("weight")
    height = data.get("height")

    if not weight or not height:
        return jsonify({"error": "يرجى إدخال الوزن والطول"}), 400

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "نقص في الوزن"
    elif 18.5 <= bmi < 24.9:
        category = "وزن طبيعي"
    elif 25 <= bmi < 29.9:
        category = "زيادة في الوزن"
    else:
        category = "سمنة"

    return jsonify({
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "category": category
    })

if __name__ == "__main__":
    app.run()

