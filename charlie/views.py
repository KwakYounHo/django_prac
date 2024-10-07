from django.shortcuts import render, HttpResponse

topics = [
  {"id": 1, "title": "create", "body": "Hello Create"},
  {"id": 2, "title": "read", "body": "Hello Read"},
  {"id": 3, "title": "update", "body": "Hello Update"},
  {"id": 4, "title": "delete", "body": "Hello Delete"}, 
]

def HTMLLayout(children):
  global topics
  lists = ""
  for topic in topics:
    lists += f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
  return f"""
  <html>
    <body>
      <header>
        <h1>Charlie World</h1>
        <nav>
          <ol>
            {lists}
          </ol>
        </nav>
      </header>
      {children}
    </body>
  </html>
  """

def index(request):
  main = """
  <p>Hello Django!</p>
  <p>This page's route is Index!</p>
  """
  return HttpResponse(HTMLLayout(main))

def read(request, id):
  global topics
  title = ""
  article = ""
  for topic in topics:
    if topic["id"] == int(id):
      title += f"<h2>{topic['title']}</h2>"
      article += f"<p>{topic['body']}</p>"
      break

  main = f"""
  {title}
  {article}
  """
  return HttpResponse(HTMLLayout(main))

def create(request):
  return HttpResponse("Create Section")