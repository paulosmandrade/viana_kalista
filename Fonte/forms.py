from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class FormPessoaJuridica(FlaskForm):
    razao_social = StringField('Razao Social', id="razao_social")
    cnpj = StringField('CNPJ', validators=[Length(min= 14, max = 14)], id="cnpj")
    regime_tributario = SelectField(
        'Escolha uma opção', 
        choices=[
            ('Simples Nacional', 'Simples Nacional'),
            ('Lucro Presumido', 'Lucro Presumido'),
            ('Lucro Real', 'Lucro Real')
        ],
        default= 'Simples Nacional', id="regime_tributario"
    )
    
    inscricao_estadual = StringField('Inscrição estadual', id="inscricao_estadual")
    submit = SubmitField(label = 'Enviar')
    
    def limpar_formulario(self):
        self.razao_social.data = ''
        self.cnpj.data = ''
        self.regime_tributario.data = ''
        self.inscricao_estadual.data = ''

