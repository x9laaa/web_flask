from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_total = tarros * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        if descuento > 0:
            descuento= precio_total * descuento

        total_descuento = precio_total - descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': precio_total,
            'descuento': descuento,
            'total_con_descuento': total_descuento 
        }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == 'juan' and password == 'admin':
            mensaje = f'Bienvenido administrador {usuario}'
        elif usuario == 'pepe' and password == 'user':
            mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrecta'
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)