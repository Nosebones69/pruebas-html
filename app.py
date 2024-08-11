from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Lógica a implementar
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/vaso-de-leche')
def vaso_de_leche():
    return render_template('vaso-de-leche.html')

@app.route('/complemento-preparado')
def complemento_preparado():
    return render_template('complemento-preparado.html')

@app.route('/enviar_inconformidad', methods=['POST'])
def enviar_inconformidad():
    nombre = request.form.get('nombre', '')
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    descripcion = request.form.get('descripcion')
    calificacion = request.form.get('calificacion')
    foto = request.files.get('foto')

    # Lógica a implementar
    return redirect(url_for('home'))

@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')

    # Lógica a implementar
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
