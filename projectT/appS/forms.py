from django.forms import ModelForm
from .models import User_req

class User_reqForm(ModelForm):
    class Meta:
        model = User_req
        fields = ('fname', 'sname', 'umail')