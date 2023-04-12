from django import forms 
from django.core.mail.message import EmailMessage
from .models import Produto

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome')
    sobrenome = forms.CharField(label='Sobrenome')
    data_nascimento = forms.DateField(label='Data de Nascimento')
    telefone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='E-mail')
    cpf = forms.CharField(label='CPF')
    

    def send_mail(self):
        nome = self.cleaned_data['nome']
        sobrenome = self.cleaned_data['sobrenome']
        data_nascimento = self.cleaned_data['data_nascimento']
        telefone = self.cleaned_data['telefone']
        email = self.cleaned_data['email']
        cpf = self.cleaned_data['cpf'] 

        conteudo = f'Nome: {nome}\nSobrenome: {sobrenome}\n Data de Nascimento: {data_nascimento}\n Telefone: {telefone}\n E-mail {email}\n CPF: {cpf} '

        mail = EmailMessage(
            subject='E-mail enviado pelo Supermercado O Vitão',
            body=conteudo,
            from_email='coontato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={'Reaply=-To' : email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']