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
    earningForm = forms.Earningsform(request.GET)
    if earningForm.is_valid():
        answer = earningForm.answer()
        return render(request, 'app/earning.html',
                      {'form': earningForm,
                       'answer': answer})
    else:
        return render(request, 'app/earning.html', {'form': earningForm})


def bothTrue(request):
    bool1 = request.GET.get('bool1')
    bool2 = request.GET.get('bool2')

    if bool1 is not None and bool2 is not None:
        answer = bool1.lower() == 'true' and bool2.lower() == 'true'
        return render(request, 'app/bothTrue.html', {'answer': answer})
    else:
        return render(request, 'app/bothTrue.html')
