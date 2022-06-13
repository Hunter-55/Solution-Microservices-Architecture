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

#Se hace un llamado a la funcion del render_template
def __ren_temp(dato):
    #retorna una redireccion html.
    return render_template('personas.html',diccionario=dato,usuario=session['usuario'])

# muesta toda la colección
@app.route('/personas')
def personas():
    return __ren_temp(__personas())

#Funcion que ejecuta el trabajo mostrar personas
def __personas():
    tabla     = Conexion()
    coleccion = tabla.Mostrar_Datos()
    lista     = []
    # nos agrega a la lista de todo los registros 
    for col in coleccion.find():
        col['_id'] = str(col['_id'])
        lista.append(col)
    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    return lista

#muestra un json de los datos
@app.route("/transactions")
def test():
    tabla     = Conexion()
    coleccion = tabla.Mostrar_Datos()
    lista     = []
    #Agrega los registros a la lista
    for col in coleccion.find():
        lista.append(col)
    #regresa un json de la coleccion en la base de datos
    return jsonify({'Data': lista})

#Muestra las transacciones de inflow y outflow por usuario
@app.route('/transacciones/<tipo>', methods=['GET','POST'])
def transacciones(tipo):
    return __ren_temp(__transacciones(tipo))

#Funcion que ejecuta el trabajo de las transacciones
def __transacciones(tipo):
    #se hace un llamado a la url /transactions para conseguir un json de la bd
    response = app.test_client().get('/transactions')
    res      = json.loads(response.data.decode('utf-8')).get("Data")
    
    list1 = []
    list2 = []
    #ciclo para llenar la lista con todos los emails si no existen
    for each in res:
        if each["user_email"] not in list1:
            list1.append(each["user_email"])
    #ciclo para introducir diccionario con inflow-outflow-total_inflow-total_outflow a la lista2
    for each in list1:
        lv_dict = {}
        tot_inflow  = 0.0
        tot_outflow = 0.0
        #ciclo para sumar la cantidad de inflow/outflow a las variables
        for each2 in res:
    
            try:
                if each2["user_email"] == each:
                    
                    if each2[tipo] == "inflow":
                        lv = float(each2['amount'])
                        tot_inflow = tot_inflow + lv
                    elif each2[tipo] == "outflow":
                        lv = float(each2['amount'])
                        tot_outflow = tot_outflow + lv
            except:
                print("Hubo un error") #Code error handler

        lv_dict["user_email"]  = each
        lv_dict["total_inflow"]  = round(tot_inflow,2)
        lv_dict["total_outflow"] = round(tot_outflow,2)
        list2.append(lv_dict) 
    #Regresa una lista con los diccionarios del user_email, total_inflow/outflow
    return list2

# función main
def main():
    app.run(debug=True,host="0.0.0.0")


if __name__=="__main__":
    main()
    









