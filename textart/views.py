from django.shortcuts import render
import pyfiglet

def text_to_ascii(request):

    fonts = pyfiglet.FigletFont.getFonts()

    # getting form data or setting default values
    text = request.GET.get('text', '')
    font = request.GET.get('font', 'slant')

    # sorting fonts list alphabetically so that it is easier to find a font

    result = pyfiglet.figlet_format(text, font=font)

    context = {
        'fonts': sorted(fonts),
        'result': result
    }

    return render(request, 'index.html', context)