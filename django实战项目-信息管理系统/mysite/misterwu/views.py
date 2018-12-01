from django.shortcuts import render

def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api": api})
    #  字典中的key是啥，html中就写啥

def user(request):
    if(request.method == 'POST'):
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)
        return render(request, 'user.html', {'user': user, 'username': username})
        #  字典中的key是啥，html中就写啥
    else:
        notfound = '请在搜索框中输入您需要查询的用户...'
        return render(request, 'user.html', {'notfound': notfound})