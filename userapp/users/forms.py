
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class TeacherSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        return user        