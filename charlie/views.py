from django.shortcuts import render, HttpResponse

topics = [
  {"id": 1, "title": "create", "body": "Hello Create"},
  {"id": 2, "title": "read", "body": "Hello Read"},
  {"id": 3, "title": "update", "body": "Hello Update"},
  {"id": 4, "title": "delete", "body": "Hello Delete"}, 
]

def index(request):
  global topics
  lists = ""
  for topic in topics:
    lists += f"<li style='text-transform:capitalize;'><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
  return HttpResponse(f"""
  <html>
  <body>
    <h1>Welcome to Charlie</h1>
    <ol>
      {lists}
    </ol>
  </body>
  </html>
""")

def create(request):
  return HttpResponse("Create Section")

def read(request, id):
  return HttpResponse(f"Read seq: {id}")