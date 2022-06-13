import pymongo
import json
from flask import Flask,session,render_template,request,redirect,url_for,jsonify
import os

# conexion a la base de datos
class Conexion:
    def Mostrar_Datos(self):
        client    = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
        db        = client["Ordinario"]
        coleccion = db['registro']
        print("Nombre de la DB: ",db.name)
        return coleccion


app = Flask(__name__)
app.secret_key = os.urandom(24)

# inicio de sesión
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':# recibe una petición post
        # verificamos que las credenciales sean correctas
        if request.form['usuario'] == "admin":
            if request.form['contrasena'] == "admin123":
                session['usuario'] = request.form['usuario']
                # retornamos una redireción a una url "/personas"
                return redirect(url_for('personas'))
            
    # retornamos una redireción html 
    return render_template('index.html')

# muesta toda la colección
@app.route('/personas')
def personas():
    tabla     = Conexion()
    coleccion = tabla.Mostrar_Datos()
    lista     = []
    # nos agrega a la lista de todo los registros 
    for col in coleccion.find():
        col['_id'] = str(col['_id'])
        lista.append(col)
    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    return render_template('personas.html',diccionario=lista,usuario=session['usuario'])

# función main
def main():
    app.run(debug=True,host="0.0.0.0")


if __name__=="__main__":
    main()
    









