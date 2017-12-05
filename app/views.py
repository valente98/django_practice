from django.shortcuts import render


def add(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    if num1 is not None and num2 is not None:
        num1 = float(num1)
        num2 = float(num2)
        answer = num1 + num2
        return render(request, 'app/add.html', {'answer': answer})
    else:
        return render(request, 'app/add.html')


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
