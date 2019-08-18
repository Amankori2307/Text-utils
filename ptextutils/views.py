from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    pr = request.POST.get('pr','off')
    nlr = request.POST.get('nlr','off')
    esr = request.POST.get('esr','off')
    uc = request.POST.get('uc','off')
    cc = request.POST.get('cc','off')
    analyzed = djtext

    #removing punctuation
    if pr == 'on':
        djtext = analyzed
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
    
    #removing newlines
    if nlr == 'on':
        djtext = analyzed
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
    
    #removing extra spces
    if esr == 'on':
        djtext = analyzed
        analyzed = ''
        for i in range(0,len(djtext)):
            if not(djtext[i] == ' ' and djtext[i+1] == ' '):
                analyzed += djtext[i]
    
    #changing to uppercase
    if uc == 'on':
        djtext = analyzed
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
    
    #counting characters
    if cc == 'on':
        djtext = analyzed
        analyzed += "\n\n---------------------------------------------------------\n Total no of Characters in your output string are "+str(len(djtext))

    #printing all the data
    # print(f"Text : {analyzed}\npr : {pr}\nnlr : {nlr}\nesr : {esr}\nuc : {uc}\ncc : {cc}")
    
    #dictionary to pass data
    params = {'analyzed_text' : analyzed,}
    return render(request, 'analyze.html',params)