from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el envío del formulario
@app.route('/submit', methods=['POST'])
def submit_user():
    name = request.form.get('name')
    email = request.form.get('email')
        
    return f'Usuario agregado: {name}, {email}'

if __name__ == '__main__':
    app.run(debug=True)
