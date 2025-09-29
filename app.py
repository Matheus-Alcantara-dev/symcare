import os
from flask import Flask, render_template, request, jsonify
from models.symcare import SymCare

app = Flask(__name__)
symcare = SymCare()

@app.route('/')
def index():
    return render_template('index.html', sintomas=symcare.sintomas_lista)

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/api/buscar')
def api_buscar():
    termo = request.args.get('termo', '')
    resultados = symcare.buscar_medicamento(termo)
    return jsonify(resultados)

@app.route('/recomendacao')
def recomendacao():
    sintoma = request.args.get('sintoma')
    if sintoma:
        medicamentos = symcare.get_recomendacoes(sintoma)
        return render_template('recomendacao.html', 
                             sintoma=sintoma, 
                             medicamentos=medicamentos)
    return render_template('recomendacao.html', 
                         sintomas=symcare.sintomas_lista)

@app.route('/pagamento')
def pagamento():
    medicamento = request.args.get('medicamento')
    if medicamento:
        preco = symcare.get_preco_medicamento(medicamento)
        return render_template('pagamento.html', 
                             medicamento=medicamento, 
                             preco=preco)
    return render_template('pagamento.html')

# Configuração para o Vercel
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run()