from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'practicas',
    'password': 'practicas',
    'database': 'test_db',
}

# Función para conectar y obtener una conexión a MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el envío del formulario
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    # Conectar a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insertar el nuevo usuario en la tabla users
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
