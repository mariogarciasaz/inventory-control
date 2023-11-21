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
        self.fields['total_deuda'].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        cantidad_enviada = cleaned_data.get('cantidad_enviada')

        if product and cantidad_enviada is not None:
            try:
                product = Product.objects.get(pk=product.pk)
                if product.quantity < cantidad_enviada:
                    self.add_error('cantidad_enviada', 'No hay suficiente stock para este producto.')
            except Product.DoesNotExist:
                pass

        return cleaned_data