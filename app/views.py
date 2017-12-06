from django.shortcuts import render
from app import forms


def add(request):
    addForm = forms.AddForm(request.GET)
    if addForm.is_valid():
        answer = addForm.answer()
        return render(request, 'app/add.html',
                      {'form': addForm,
                       'answer': answer})
    else:
        return render(request, 'app/add.html', {'form': addForm})


def double(request):
    doubleForm = forms.DoubleForm(request.GET)

    if doubleForm.is_valid():
        answer = doubleForm.answer()
        return render(request, 'app/double.html',
                      {'form': doubleForm,
                       'answer': answer})
    else:
        return render(request, 'app/double.html', {'form': doubleForm})


def multThree(request):
    multThreeForm = forms.MultThreeForm(request.GET)

    if multThreeForm.is_valid():
        answer = multThreeForm.answer()
        return render(request, 'app/multThree.html',
                      {'form': multThreeForm,
                       'answer': answer})
    else:
        return render(request, 'app/multThree.html', {'form': multThreeForm})


def earning(request):
    earningForm = forms.EarningsForm(request.GET)
    if earningForm.is_valid():
        answer = earningForm.answer()
        return render(request, 'app/earning.html',
                      {'form': earningForm,
                       'answer': answer})
    else:
        return render(request, 'app/earning.html', {'form': earningForm})


def bothTrue(request):
    bothTrueForm = forms.BothTrueForm(request.GET)

    if bothTrueForm.is_valid():
        answer = bothTrueForm.answer()
        return render(request, 'app/bothTrue.html',
                      {'form': bothTrueForm,
                       'answer': answer})
    else:
        return render(request, 'app/bothTrue.html', {'form': bothTrueForm})


def WalkorDrive(request):
    walkorDriveForm = forms.WalkorDriveForm(request.GET)

    if walkorDriveForm.is_valid():
        answer = walkorDriveForm.answer()
        return render(request, 'app/WalkorDrive.html',
                      {'form': walkorDriveForm,
                       'answer': answer})
    else:
        return render(request, 'app/WalkorDrive.html',
                      {'form': walkorDriveForm})


def howPopulated(request):
    howPopulatedForm = forms.HowPopulatedForm(request.GET)

    if howPopulatedForm.is_valid():
        answer = howPopulatedForm.answer()
        return render(request, 'app/problem.html',
                      {'form': howPopulatedForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html', {'form': howPopulatedForm})


def goldStar(request):
    goldStarForm = forms.GoldStarsForm(request.GET)

    if goldStarForm.is_valid():
        answer = goldStarForm.answer()
        return render(request, 'app/problem.html',
                      {'form': goldStarForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html', {'form': goldStarForm})


def howManyPoints(request):
    howManyPointsForm = forms.HowManyPointsForm(request.GET)

    if howManyPointsForm.is_valid():
        Points = howManyPointsForm.answer()
        return render(request, 'app/problem.html',
                      {'form': howManyPointsForm,
                       'answer': Points})
    else:
        return render(request, 'app/problem.html', {'form': howManyPointsForm})


def lastThree(request):
    lastThreeForm = forms.LastThreeForm(request.GET)

    if lastThreeForm.is_valid():
        answer = lastThreeForm.answer()
        return render(request, 'app/problem.html',
                      {'form': lastThreeForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html', {'form': lastThreeForm})


def SumofList(request):
    sumofListForm = forms.SumofListForm(request.GET)

    if sumofListForm.is_valid():
        answer = sumofListForm.answer()
        return render(request, 'app/problem.html',
                      {'form': sumofListForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html', {'form': sumofListForm})


def SumofLonger(request):
    sumofLongerForm = forms.SumofLongerForm(request.GET)

    if sumofLongerForm.is_valid():
        answer = sumofLongerForm.answer()
        return render(request, 'app/problem.html',
                      {'form': sumofLongerForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html', {'form': sumofLongerForm})


def differenceFromMinimum(request):
    differenceFromMinForm = forms.DifferenceFromMinimumForm(request.GET)

    if differenceFromMinForm.is_valid():
        answer = differenceFromMinForm.answer()
        return render(request, 'app/problem.html',
                      {'form': differenceFromMinForm,
                       'answer': answer})
    else:
        return render(request, 'app/problem.html',
                      {'form': differenceFromMinForm})
