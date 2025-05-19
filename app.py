from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return (
        "¡Hola desde Azure!\n"
        "Gabriel Josué Márquez Torrres\n"
        "21550316\n"
        "Edgar Alejandro Martínez Chávez\n"
        "21550364\n"
        "Sebastian Emilio Murillo Andrade\n"
        "21550384\n"
        "Bryan Alexis Quintana Juárez\n"
        "21550295\n"
        "Ingeniería en Sistemas Computacionales\n"
        "8° semestre\n"
    )

if __name__ == "__main__":
    app.run()


    