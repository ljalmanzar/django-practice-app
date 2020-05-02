from django.shortcuts import render

# fake data for now
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Mike',
        'title': 'Blog Post 3',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })