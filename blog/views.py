from django.shortcuts import render
from .models import Post

posts = [
  {
    "author": "John Doe",
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    "date_posted": "2020-01-01"
  },
  {
    "author": "Jane Doe2",
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
    "date_posted": "2023-11-02"
  },
  {
    "author": "Jane Doe3",
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
    "date_posted": "2023-11-03"
  },
]

def home(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
