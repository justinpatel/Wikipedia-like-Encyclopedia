from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import numpy as np

class CreateNewEntryForm(forms.Form):
    title = forms.CharField()

    textarea = forms.CharField(widget=forms.Textarea(attrs={'cols': 80,'rows':10}))
    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, title):
    return render(request, "encyclopedia/content.html",{
        "title": title,
        "content": util.get_entry(title.upper())
    })

def newpage(request):
    if request.method == 'POST':
        form = CreateNewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['textarea']
            util.save_entry(title, content)
            #return HttpResponseRedirect(reverse("ency:index"))

    return render(request, "encyclopedia/newpage.html",{
        "form": CreateNewEntryForm()
    })

def random(request):
    n = np.random.randint(1,len(util.list_entries()))
    title = util.list_entries()[n]
    return render(request,  "encyclopedia/content.html",{
        "title": title,
        "content": util.get_entry(title)
    })

'''def search(request):
    if request.method == "GET":
        return index(request)

    search = []
    form = request.POST
    search = form["search"]
    entries = util.list_entries()
    found = []

    # searched title is in wiki
    regex = r"\b"+f"{search}"+r"\b"
    r = re.compile(regex, re.IGNORECASE)
    found = list(filter(r.match, entries))
    if found:
        return redirect('title', title=found[0])

    # searched title partially matched entries
    r = re.compile(rf".*{search}.*", re.IGNORECASE)
    found = list(filter(r.match, entries))
    if found:
        return index(request, entries=found)

    return render(request, "encyclopedia/error.html", {"msg": "Title not found"})'''