from django.shortcuts import render


def success(request):
  if request.method == 'POST':
    search_word = request.POST.get('search_word', '')
    print(search_word)  # 디버깅용
    context = {'search_word': search_word, "remote": "1"}
  else:
    context = {"remote": "0"}
  return render(request, 'success.html', context)

def test4(request):
  return render(request, 'test4.html')

def weather(request):
  return render(request, 'weather.html')