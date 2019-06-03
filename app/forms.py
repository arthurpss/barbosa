from django import forms
from app.models import TB_Usuario

AVALIACOES = [
    ('Excelente', 10),
    ('Bom', 8),
    ('Médio', 5),
    ('Ruim', 3),
    ('Péssimo', 1)
]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = TB_Usuario
        fields = "__all__"


        # widgets = {
        #     'email': forms.EmailField(attrs={'placeholder': 'exemplo@exemplo.com'}),
        #     'senha': forms.PasswordInput(),
        #     'avaliacao': forms.ChoiceField(choices=AVALIACOES)
        # }