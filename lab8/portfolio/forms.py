from django import forms
from django.forms import ModelForm
from .models import Tarefa
from .models import Blog_Post


"""class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }


        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }


        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }"""

class BlogPostForm(ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Blog_Post
        fields = '__all__'

        #autor data titulo descricao

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao...'}),

            'data': forms.DateInput(format='%m/%d/%Y'),

        }


        # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Author',
            'data': 'Data',
            'titulo': 'Title',
            'descricao': 'Description',
            'image': 'Image',
        }


        # texto auxiliar a um determinado campo do formulário
        help_texts = {}