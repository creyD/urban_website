from django.shortcuts import render


def steam_with_friends(request):
    context = {}
    return render(request, 'steam_tools/swf.html', context)
