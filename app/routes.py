from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Configurar la conexión a la base de datos SQLite
DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

# Función para obtener todos los usuarios
def get_users():
    con = connect_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    con.close()
    return users

# Ruta para obtener todos los usuarios en formato JSON
@app.route('/users', methods=['GET'])
def users():
    users = get_users()
    # Convertir los resultados a un formato JSON
    users_json = [{'id': user[0], 'username': user[1], 'email': user[2]} for user in users]
    return jsonify(users_json)

if __name__ == '__main__':
    app.run(debug=True)
