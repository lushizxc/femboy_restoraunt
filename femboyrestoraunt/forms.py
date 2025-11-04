from django.contrib.auth.forms import UserCreationForm
from femboyrestoraunt.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.                                        Meta):
        model = CustomUser
        fields = ('username','email','phone_number')