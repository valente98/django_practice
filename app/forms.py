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


class LastThreeForm(forms.Form):
    l1 = forms.CharField()

    def answer(self):
        return list(map(int, self.cleaned_data['l1'].split()))[-3:]


class SumofListForm(forms.Form):
    l = forms.CharField()

    def answer(self):
        return sum(list(map(int, self.cleaned_data['l'].split())))


class SumofLongerForm(forms.Form):
    L1 = forms.CharField()
    L2 = forms.CharField()

    def answer(self):
        l1 = list(map(int, self.cleaned_data['L1'].split()))
        l2 = list(map(int, self.cleaned_data['L2'].split()))
        if len(l1) > len(l2):
            return sum(l1)
        elif len(l1) < len(l2):
            return sum(l2)
        else:
            return sum(l1) + sum(l2)


class DifferenceFromMinimumForm(forms.Form):
    l = forms.CharField()

    def answer(self):
        L = list(map(int, self.cleaned_data['l'].split()))
        lowest = min(L)
        return list(map(lambda x: x - lowest, L))


class HashtagsForm(forms.Form):
    Tweet = forms.CharField()

    def answer(self):
        words = self.cleaned_data['Tweet'].split()
        return list(filter(lambda l: l.startswith('#'), words))


class MentionsForm(forms.Form):
    Mentions = forms.CharField()

    def answer(self):
        words = self.cleaned_data['Mentions'].split()
        return list(filter(lambda l: l.startswith('@'), words))


class ParseInventoryStringForm(forms.Form):
    Inventory = forms.CharField()

    def answer(self):
        Inv = self.cleaned_data['Inventory'].split()
        return [Inv[0], float(Inv[1]), float(Inv[2])]


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_dollar_item(self):
        return self.price <= 1


class IsDollarStoreForm(forms.Form):
    L1 = forms.CharField()

    def parse_item(self, string):
        name, price, quantity = string.split(',')
        return Item(name, float(price), int(quantity))

    def answer(self):
        item_strings = self.cleaned_data['L1'].split(' ')
        return all(self.parse_item(s).is_dollar_item() for s in item_strings)
