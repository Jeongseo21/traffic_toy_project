from django import forms
from .models import List
# 사용자가 입력한 데이터를 데이터 형태로 db에 저장하기 위한 form
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]