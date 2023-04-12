from django.shortcuts import render
from .forms import CadastroForm, ProdutoModelForm
from django.contrib import messages # para adcionar mensagens no contexto da nossa pagina


# Create your views here.

def index(request):
    return render (request, 'index.html')



def cadastro_cliente(request):
    form = CadastroForm(request.POST or None )

    if str(request.method) == 'POST':
        if form.is_valid(): # se os  formularios forem validos ..
            form.send_mail()
            # nome = form.cleaned_data['nome']
            # sobrenome = form.cleaned_data['sobrenome']
            # data_nascimento = form.cleaned_data['data_nascimento']
            # telefone = form.cleaned_data['telefone']
            # email = form.cleaned_data['email']
            # cpf = form.cleaned_data['cpf'] # cada chave dessa é a variavel de forms.py a variavel

            # print('Cadastro Realizado com Sucesso!!')
            # print(f'Nome: {nome}')
            # print(f'Sobrenome: {sobrenome}')
            # print(f'Data de Nascimento: {data_nascimento}')
            # print(f'Telefone: {telefone}')
            # print(f'E-mail: {email}')
            # print(f'CPF: {cpf}')

            messages.success(request, 'Cadastro realziado com Sucesso!!')
            form = CadastroForm() # limpando o processo e deixando extamente como iniciou
        else:
            messages.error(request, 'Erro, Cadastro não Realizado, entre em contaot com o suporte')

    context = {
        'form': form
    }
    return render (request, 'cadastro_cliente.html', context)



def promocao(request):
    return render(request, 'endereco_cliente.html')



def produtos(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }

    return render(request, 'produtos.html', context)

