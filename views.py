# I have created this file - Dishank
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

# get the text
    djtext = request.POST.get('text', 'default')

# Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

#check which checkbox is on
    if (removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"Removing Punctuations", 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Change to Uppercase", 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': "Removed Extraspace", 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)


    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)