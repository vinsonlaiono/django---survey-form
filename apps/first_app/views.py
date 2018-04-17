from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'name' not in request.session:
        request.session['name'] = ''
    if 'location' not in request.session:
        request.session['location'] = ''
    if 'language' not in request.session:
        request.session['language'] = ''
    if 'comment' not in request.session:
        request.session['comment'] = ''

    return render(request, "first_app/index.html")

def process(request):
    print('im in process')
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    return redirect('/results')

def results(request):
    request.session['count'] += 1
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }

    return render(request, 'first_app/results.html', context)
