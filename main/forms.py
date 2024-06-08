from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    copiar = forms.BooleanField(required=False)