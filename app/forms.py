from django import forms
from app.models import TB_Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = TB_Usuario
<<<<<<< Updated upstream
        fields = '__all__' #['email', 'senha', 'avaliacao', 'notificacao', 'comentarios']
        widgets = {
            'email': forms.EmailField(attrs={'placeholder': 'exemplo@exemplo.com'}),
            'senha': forms.PasswordInput(),
            'avaliacao': forms.ChoiceField(choices=AVALIACOES)
        }
=======
        fields = "__all__"
        # widgets = {
        #      'email': forms.EmailField(attrs={'placeholder': 'exemplo@exemplo.com'}),
        #      'senha': forms.PasswordInput(),
        #  }
>>>>>>> Stashed changes
