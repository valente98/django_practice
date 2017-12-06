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


class HowPopulatedForm(forms.Form):
    Population = forms.FloatField()
    LandArea = forms.FloatField()

    def answer(self):
        if self.cleaned_data['Population'] / self.cleaned_data['LandArea'] > 100:
            return 'Densely Populated'
        else:
            return 'Sparsely Populated'


class GoldStarsForm(forms.Form):
    Points = forms.FloatField()

    def answer(self):
        if self.cleaned_data['Points'] < 1000:
            return '*'
        elif self.cleaned_data['Points'] < 5000:
            return '**'
        elif self.cleaned_data['Points'] < 8000:
            return '***'
        elif self.cleaned_data['Points'] < 10000:
            return '****'
        else:
            return '*****'


class HowManyPointsForm(forms.Form):
    score_type = {
        'td': 'Touch Down',
        'ek': 'Extra Kick',
        'ec': 'Extra Convertion',
        'fg': 'Field Goal',
        'sa': 'Safety'
    }
    scoringAction = forms.ChoiceField(choices=(score_type.items()))

    def answer(self):
        point = self.cleaned_data['scoringAction']
        points = {'td': '6', 'ek': '1', 'ec': '2', 'fg': '3', 'sa': '2'}
        return points[point]