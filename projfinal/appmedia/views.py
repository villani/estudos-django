from django.shortcuts import render

def media_final(request):
    media = ''
    try:
        if request.method == 'GET':
            nota1 = eval(request.GET.get('nota1'))
            nota2 = eval(request.GET.get('nota2'))
            nota3 = eval(request.GET.get('nota3'))
            nota4 = eval(request.GET.get('nota4'))
            media = (nota1 + nota2 + nota3 + nota4) / 4
    except:
        media = 'Preencha as notas para calcular a média...'

    return render(request, 'media.html', {'media': media})
