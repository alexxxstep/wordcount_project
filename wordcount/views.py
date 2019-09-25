from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hi': 'This is me'})

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    w_dic = {}

    for w in words:
        w_low = w.lower()

        if not w_low.isalpha():
            continue

        if w_low in w_dic:
            # Increase
            w_dic[w_low] += 1
        else:
            w_dic[w_low] = 1

    n_words = len(words)

    sorted_words = sorted(w_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'n_words': n_words,
                                          'sorted_words': sorted_words
                                          })
