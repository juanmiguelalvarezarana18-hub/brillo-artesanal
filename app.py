from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_pedidos = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        cantidad = request.form.get('cantidad')
        aroma = request.form.get('aroma')
        direccion = request.form.get('direccion')

        if cliente and cantidad and aroma and direccion:
            pedido = {
                "cliente": cliente,
                "cantidad": cantidad,
                "aroma": aroma,
                "direccion": direccion
            }
            lista_pedidos.append(pedido)
            return redirect(url_for('home'))

    return render_template('apple.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
