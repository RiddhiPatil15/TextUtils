# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

# To add a link on your page usimg html.
#def example(request):
#   return HttpResponse('''Hello <a href="https://www.youtube.com/"> YouTube''')

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")
    #parameters = {'name': 'python', 'framework':'django'} parameter to be included in render parameters


def analyze(request):
    dj_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        paras = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', paras)

    if(fullcaps == 'on'):
        analyzed = ""
        for char in dj_text:
            analyzed = analyzed + char.upper()
        paras = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', paras)

    if(newlineremove == 'on'):
        analyzed = ""
        for char in dj_text:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
                else:
                     print("No")
        print("pre", analyzed)
        paras = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', paras)

    if(spaceremove == 'on'):
        analyzed = ""
        for index, char in enumerate(dj_text):
                if not (dj_text[index] == " " and dj_text[index+1]==" "):
                    analyzed = analyzed + char
        paras = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', paras)

    if(charcount == 'on'):
        analyzed = ""
        count =0
        for char in dj_text:
             count +=1
        print(count)
        paras = {'purpose': 'counts the characters', 'analyzed_text': count}
        return render(request, 'analyze.html', paras)
    else:
         return HttpResponse("Error! \n Please select any one of the operations.")

