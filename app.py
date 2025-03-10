from flask import Flask, render_template, request, send_from_directory
import os 

from model.predecir import calcularImg

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

# Determinar si estamos en Vercel
EN_VERCEL = os.getenv("VERCEL_ENV") is not None

# Definir ruta de almacenamiento
UPLOAD_FOLDER = "tmp" if EN_VERCEL else "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/convertir", methods=['POST'])


def getImg():
    archivo = request.files['archivo']
    ruta_guardado = os.path.join(UPLOAD_FOLDER, "temp.png")
    archivo.save(ruta_guardado)
    numCal = calcularImg(ruta_guardado)
    return render_template('base.html', num = numCal)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)