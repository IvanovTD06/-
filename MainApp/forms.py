from django.forms import ModelForm
from MainApp.models import TRF, DRF, BRF, SRF, CTRF


class T_R_F(ModelForm):
   class Meta:
       model = TRF
       # Описываем поля, которые будем заполнять в форме
       fields = ['Name', 'Surname', 'Surname1']

class D_R_F(ModelForm):
    class Meta:
        model = DRF
        fields = ["Discipline_name"]

class B_R_F(ModelForm):
    class Meta:
        model = BRF
        fields = ["Building_name"]

class S_R_F(ModelForm):
    class Meta:
        model = SRF
        fields = ["Subject_name"]

class C_T_R_F(ModelForm):
    class Meta:
        model = CTRF
        fields = ["Cabinet_type_name"]