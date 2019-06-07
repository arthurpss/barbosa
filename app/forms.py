from django import forms
from app.models import TB_Usuario
from app.models import TB_Treino


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = TB_Usuario
        fields = "__all__"
        # widgets = {
        #     'email': forms.EmailField(attrs={'placeholder': 'exemplo@exemplo.com'}),
        #     'senha': forms.PasswordInput(),
        #     'avaliacao': forms.ChoiceField(choices=AVALIACOES)
        # }

class TreinoForm(forms.ModelForm):
    class Meta:
        model = TB_Treino
        fields = "__all__"