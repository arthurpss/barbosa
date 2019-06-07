from django import forms
from app.models import TB_Autor, TB_Livro


class AutorForm(forms.ModelForm):
    class Meta:
        model = TB_Autor
        fields = "__all__"
        # widgets = {
        #     'email': forms.EmailField(attrs={'placeholder': 'exemplo@exemplo.com'}),
        #     'senha': forms.PasswordInput(),
        #     'avaliacao': forms.ChoiceField(choices=AVALIACOES)
        # }

class LivroForm(forms.ModelForm):
    class Meta:
        model = TB_Livro
        fields = "__all__"
