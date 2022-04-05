import random
from django.http import HttpResponse 
from django.template.loader import render_to_string, get_template
from articles.models import Article   


def home_view(request, *args, **kwargs):
  print(id)
  name = 'Peter'
  number = random.randint(10,123432432)
  article_obj = Article.objects.get(id=2)
  article_queryset = Article.objects.all()
  my_list = [102, 23, 344]
  
  
  context = {
    "object_list": article_queryset,
    "object": article_obj,
    "my_list": my_list,
    "title": article_obj.title,
    "id": article_obj.id,
    "content": article_obj.content
  }
  

  
  HTML_STRING = render_to_string("home-view.html", context=context)
  
  
  return HttpResponse(HTML_STRING)