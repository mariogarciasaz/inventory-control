from django import forms
from clientsdata.models import ClientData
from clients.models import Client
from products.models import Product


class ClientDataForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientDataForm, self).__init__(*args, **kwargs)

        # Añade el atributo 'disabled' al widget del campo 'total_deuda'
        self.fields['total_deuda'].widget.attrs['disabled'] = True