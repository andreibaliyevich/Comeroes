from django import forms
from contacts.models import Store
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """ Order Create Form """

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'store',
        ]

    def __init__(self, request, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        city_code = request.session.get('city_code')
        stores = Store.objects.filter(city=city_code)

        STORE_CHOICES = []
        STORE_CHOICES.append(('', '---------'))
        for store in stores:
            if request.LANGUAGE_CODE == 'en':
                STORE_CHOICES.append((str(store.id), store.address))
            else:
                for store_translation in store.storetranslation_set.all():
                    if store_translation.language == request.LANGUAGE_CODE:
                        STORE_CHOICES.append(
                            (str(store.id), store_translation.address))
                        break

        self.fields['store'].choices = STORE_CHOICES
