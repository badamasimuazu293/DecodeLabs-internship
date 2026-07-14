from flask import Flask, render_template, request
import os
import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    image = cv2.imread(filepath)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    text = pytesseract.image_to_string(gray)

    return render_template(
        "results.html",
        text=text,
        image=file.filename
    )

if __name__ == "__main__":
    app.run(debug=True)