from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coleta os dados do formulário
        var1 = request.form.get('var1', '')
        var2 = request.form.get('var2', '')
        var3 = request.form.get('var3', '')

        # Redireciona para a rota resultado com os dados processados
        return render_template('resultado.html', var1=var1, var2=var2, var3=var3)

    return render_template('index.html')


@app.route('/resultado')
def resultado():
    return render_template('resultado.html')


@app.route('/autor')
def autor():
    # Informações sobre o autor
    autor_info = {
        "nome": "Antonio Alves",
        "formacoes": [
            {"curso": "Engenharia civil", "instituicao": "Universidade estadual vale do acarau", "ano": "2019"},
            {"curso": "Informatica para internet", "ifce": "instituto federal do ceará campos Sobral", "ano": "2024"},
        ],
    }
    return render_template('autor.html', autor=autor_info)


if __name__ == '__main__':
    app.run(debug=True)
