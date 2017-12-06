from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()

    def answer(self):
        return self.cleaned_data['num1'] + self.cleaned_data['num2']


class DoubleForm(forms.Form):
    num = forms.FloatField()

    def answer(self):
        return self.cleaned_data['num'] * 2


class MultThreeForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()
    num3 = forms.FloatField()

    def answer(self):
        return self.cleaned_data['num1'] * self.cleaned_data[
            'num2'] * self.cleaned_data['num3']


class EarningsForm(forms.Form):
    seat1 = forms.FloatField()
    seat2 = forms.FloatField()
    seat3 = forms.FloatField()

    def answer(self):
        return self.cleaned_data['seat1'] * 15 + self.cleaned_data['seat2'] * 12 + self.cleaned_data['seat3'] * 9


class BothTrueForm(forms.Form):
    bool1 = forms.BooleanField(required=False)
    bool2 = forms.BooleanField(required=False)

    def answer(self):
        return self.cleaned_data['bool1'] and self.cleaned_data['bool2']


class WalkorDriveForm(forms.Form):
    miles = forms.FloatField()
    Weather = forms.BooleanField(required=False)

    def answer(self):
        if self.cleaned_data['miles'] <= 0.25 and self.cleaned_data['Weather']:
            return "You should walk"
        else:
            return 'You should drive'