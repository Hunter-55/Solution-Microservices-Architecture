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
def ren_temp(dato,url,usuario):
    #retorna una redireccion html.
    return render_template(url,diccionario=dato,usuario=usuario)

# muesta toda la colección
@app.route('/personas')
def personas():
    return ren_temp(personas(),'personas.html',session['usuario'])

#Funcion que ejecuta el trabajo mostrar personas
def personas():
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
        col['_id'] = str(col['_id'])
        lista.append(col)
    #regresa un json de la coleccion en la base de datos
    return jsonify({'Data': lista})

#Muestra las transacciones de inflow y outflow por usuario
@app.route('/transacciones/<tipo>', methods=['GET','POST'])
def transacciones(tipo):
    return ren_temp(transacciones(tipo),'transacciones.html',session['usuario'])

#Funcion que ejecuta el trabajo de las transacciones
def transacciones(tipo):
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

#Funcion para generar un diccionario con categorias y sus valores dado un json apuntador
def categories(res,dict1,user_email):
    #ciclo para llenar un diccionario con las categorias y los valores
    for each in dict1:
        dict2 = {}
        #ciclo para sumar si la categoria existe en el diccionario, o agregarla nueva si no.
        for each2 in res:
            if each2["user_email"] == user_email:
                if each == each2["type"]:
                    if each2["category"] in dict2:
                        amou_sum = float(dict2[each2["category"]])
                        lv = float(each2["amount"])
                        amou_sum = round(lv + amou_sum,2)
                        dict2[each2["category"]] = amou_sum
                    else:
                        dict2[each2["category"]] = each2["amount"]
        dict1[each] = dict2
    #retorno de un diccionario lleno (el mismo recibido)
    return dict1

#Muestra un summary de las categorias y sus valores de acuerdo al inflow/outflow del user_email recibido
@app.route("/monto/<user_email>/summary")
def monto(user_email):
    return ren_temp(monto(user_email),'monto.html',user_email)

#Funcion principal para el summary del user_email. Esta funcion solamente recibe el email y manda a llamar a las demas
def monto(user_email):
    response = app.test_client().get('/transactions')
    res      = json.loads(response.data.decode('utf-8')).get("Data")
    dict1    = {"inflow": "", "outflow": ""}
    dict1    = categories(res,dict1,user_email)   
                
    return dict1

# función main
def main():
    app.run(debug=True,host="0.0.0.0")


if __name__=="__main__":
    main()
    









