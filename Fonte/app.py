from flask import Flask, render_template, flash, redirect, url_for, request
from forms import FormPessoaJuridica
from model import PessoaJuridica
from database import session
from query import consulta_clientes, consultar_cliente_cnpj, consultar_cliente_razao_social
from sqlalchemy import exc

app = Flask(__name__)
app.secret_key = '12h3u4hyu5'


@app.route("/home")
def home(): 
    return render_template("home.html")


@app.route("/clientes", methods=['GET', 'POST'])
def clientes():
    form = FormPessoaJuridica()

    tabela = consulta_clientes()

    # Apenas processa se o método for POST
    if request.method == 'POST':
        action = request.form.get("action")  # Verifica o que foi pressionado
        
        if action == "cadastrar":
            if form.razao_social.data == '' or form.cnpj.data == '' or form.regime_tributario.data == '':
                flash('Preencher os campos obrigatórios','warning')
            else:
                try:
                    cliente = consultar_cliente_cnpj(form.cnpj.data)
                    if cliente:
                        cliente.razao_social = form.razao_social.data
                        cliente.cnpj = form.cnpj.data
                        cliente.regime_tributario = form.regime_tributario.data
                        cliente.inscricao_estadual = form.inscricao_estadual.data
                        session.commit()
                        flash("Cliente atualizado com sucesso!", "success")
                    else:
                        nova_cliente = PessoaJuridica(
                            razao_social=form.razao_social.data,
                            cnpj=form.cnpj.data,
                            regime_tributario=form.regime_tributario.data,
                            inscricao_estadual=form.inscricao_estadual.data,
                            status=True
                        )
                        session.add(nova_cliente)
                        session.commit()
                        flash("Cliente cadastrado com sucesso!", "success")
                    tabela = consulta_clientes()
                    form.limpar_formulario()  # Limpa os dados do formulário
                    return redirect(url_for("clientes"))
                except exc.IntegrityError:
                    session.rollback()
                    flash("Erro: O CNPJ já está cadastrado no sistema.", "danger")
                except Exception as e:
                    session.rollback()
                    flash("Ocorreu um erro inesperado. Por favor, tente novamente.", "danger")

        elif action == "buscar":
            # Não aplica validação, realiza apenas a busca
            if form.razao_social.data:
                tabela = consultar_cliente_razao_social(form.razao_social.data) or []
            elif form.cnpj.data:
                cliente = consultar_cliente_cnpj(form.cnpj.data)
                tabela = [cliente] if cliente else []

            return render_template("clientes.html", form=form, tabela=tabela)

    return render_template("clientes.html", form=form, tabela=tabela)




@app.route("/transportadoras" , methods=['GET', 'POST'])
def transportadoras():
    return render_template('transportadoras.html')


@app.route("/produtos", methods = ['GET', 'POST'])
def produtos():
    return render_template('produtos.html')


@app.route("/pedidos", methods = ['GET', 'POST'])
def pedidos():
    return render_template('pedidos.html')