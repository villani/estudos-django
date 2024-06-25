from django.shortcuts import render

def calc(request):
    resultado = ''
    try:
        if request.method == 'GET':
            num1 = eval(request.GET.get('num1'))
            num2 = eval(request.GET.get('num2'))
            resultado = num1 + num2
    except:
        resultado = 'Erro na operação...'

    return render(request, 'calculadora.html', {'resultado': resultado})