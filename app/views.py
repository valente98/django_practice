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
