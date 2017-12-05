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
    num1 = request.GET.get('num1')

    if num1 is not None:
        num1 = int(num1)
        answer = num1 * 2
        return render(request, 'app/double.html', {'answer': answer})
    else:
        return render(request, 'app/double.html')


def multThree(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')

    if num1 is not None and num2 is not None and num3 is not None:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        answer = num1 * num2 * num3
        return render(request, 'app/multThree.html', {'answer': answer})
    else:
        return render(request, 'app/multThree.html')


def earning(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')

    if num1 is not None and num2 is not None and num3 is not None:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        answer = num1 * 15 + num2 * 12 + num3 * 9
        return render(request, 'app/earning.html', {'answer': answer})
    else:
        return render(request, 'app/earning.html')


def bothTrue(request):
    bool1 = request.GET.get('bool1')
    bool2 = request.GET.get('bool2')

    if bool1 is not None and bool2 is not None:
        answer = bool1.lower() == 'true' and bool2.lower() == 'true'
        return render(request, 'app/bothTrue.html', {'answer': answer})
    else:
        return render(request, 'app/bothTrue.html')
