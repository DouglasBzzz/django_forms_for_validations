from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .classe_viagem import tipos_de_classes
from .validation import *
from .models import ClasseViagem, Passagem, Pessoa

class PassagemForms(forms.ModelForm):
    #como tem muita alteracao no campo de pesquisa, ele tem que entrar antes do carregamento do modulo base.
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True,
                                    initial=datetime.today())  # assim a pessoa nem consegue alterar.
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida' : 'Data de Ida',
            'data_volta' : 'Data de Volta',
            'informacoes' : 'Informações',
            'classe_viagem' : 'Classe da Viagem'
        }
        widgets = {
            'data_ida' : DatePicker(),
            'data_volta' : DatePicker()
        }
        classe_viagem = forms.ChoiceField(label='Classe do Vôo', choices=tipos_de_classes) #comboBox

    """def clean_origem(self):
        origem = self.cleaned_data.get('origem') #se eu usar colchetes, ele retorna NONE - sem o get
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Preenchimento Inválido: Não inclua números.')
        else:
            return origem

    def clean_destino(self):
        destino = self.cleaned_data.get('destino') #se eu usar colchetes, ele retorna NONE - sem o get
        if any(char.isdigit() for char in destino):
            raise forms.ValidationError('Preenchimento Inválido: Não inclua números.')
        else:
            return destino
    """

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        campo_tem_numeros(origem, 'origem', lista_de_erros)
        campo_tem_numeros(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)

        data_ida_maior_que_volta(data_ida, data_volta, lista_de_erros)

        data_compra_menor_que_compra(data_ida, data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] #o exclude é literalmente exclusivo a partir do parametro.

