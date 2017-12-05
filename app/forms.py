from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()

    def answer(self):
        return self.cleaned_data['num1'] + self.cleaned_data['num2']