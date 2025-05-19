from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # Datos de los estudiantes
    students = [
        ("Gabriel Josué Márquez Torrres", "21550316"),
        ("Edgar Alejandro Martínez Chávez", "21550364"),
        ("Sebastián Emilio Murillo Andrade", "21550384"),
        ("Bryan Alexis Quintana Juárez", "21550295"),
    ]
    program = "Ingeniería en Sistemas Computacionales"
    semester = "8° semestre"

    # Generamos la lista en HTML
    items = "".join(
        f"<li><strong>{name}</strong> &mdash; <code>{stu_id}</code></li>"
        for name, stu_id in students
    )

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>¡Hola desde Azure!</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 2rem;
            background: #fafafa;
        }}
        h1 {{
            color: #0078d4;
        }}
        ul {{
            list-style: none;
            padding: 0;
            max-width: 400px;
        }}
        li {{
            background: #ffffff;
            margin: 0.5rem 0;
            padding: 0.75rem 1rem;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        code {{
            background: #f0f0f0;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }}
        p {{
            margin-top: 1.5rem;
            font-style: italic;
            color: #555;
        }}
    </style>
</head>
<body>
    <h1>¡Hola desde Azure!</h1>
    <ul>
        {items}
    </ul>
    <p>{program} &mdash; {semester}</p>
</body>
</html>"""

if __name__ == "__main__":
    app.run()
