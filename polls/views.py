from django.shortcuts import render
import nltk
import urllib.parse as urlparse
from urllib.parse import parse_qs
# Create your views here.
from django.http import HttpResponse
from django.http import QueryDict
from django.http import HttpRequest
from django.urls import path
from . import views


def index(request):
    a = "I'll love you <3. Because you're stupid."
    # print("request:", c)

    qd = request.GET
    print("qd = ", qd)
    language = qd['L']
    classify = qd['C']
    text = qd['T']

    print("language = ", language)
    print("classify = ", classify)
    print("text = ", text)
    b = []

    c = "but I'm worse than him :("
    if classify == "P":
        sent_text = nltk.sent_tokenize(text)  # this gives us a list of sentences
        # now loop over each sentence and tokenize it separately
        for sentence in sent_text:
            tokenized_text = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokenized_text)
            print(tagged)
            b.append(tagged)
    return HttpResponse(b)
