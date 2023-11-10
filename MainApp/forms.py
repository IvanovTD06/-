from django.forms import ModelForm
from MainApp.models import TRF, DRF, BRF, ERF, CTRF, CRF, Connection_data


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

class E_R_F(ModelForm):
    class Meta:
        model = ERF
        fields = ["Equipment_name"]

class C_T_R_F(ModelForm):
    class Meta:
        model = CTRF
        fields = ["Cabinet_type_name"]

class C_R_F(ModelForm):
    class Meta:
        model = CRF
        fields = ["Building", "Cabinet_number", "Cabinet_type", "Equipment"]

class C_D(ModelForm):
    class Meta:
        model = Connection_data
        fields = ["db_name", "db_user", "db_password", "db_host", "db_port"]
        