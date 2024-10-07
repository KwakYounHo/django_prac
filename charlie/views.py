from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

topics = [
  {"id": 1, "title": "create", "body": "Hello Create"},
  {"id": 2, "title": "read", "body": "Hello Read"},
  {"id": 3, "title": "update", "body": "Hello Update"},
  {"id": 4, "title": "delete", "body": "Hello Delete"}, 
]
nextId = 5

def HTMLLayout(children):
  global topics
  lists = ""
  for topic in topics:
    lists += f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
  return f"""
  <html>
    <body>
      <header>
        <h1><a href="/">Charlie World</a></h1>
        <nav>
          <ol>
            {lists}
          </ol>
        </nav>
      </header>
      {children}
      <footer>
        <h3>Features</h3>
        <ul>
          <li><a href="/create">Create</a></li>
        </ul>
      </footer>
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
  <ul>
    <li>
      <a href="/update/{id}">
        <button>update article</button>
      </a>
    </li>
    <li>
      <a href="/delete/{id}">
        <button>delete article</button>
      </a>
    </li>
  </ul>
  """
  return HttpResponse(HTMLLayout(main))

@csrf_exempt
def create(request):
  if request.method == "GET":
    main = f"""
    <form action="/create/" method="post">
      <div>
        <label>Title</label>
        <p><input type="text" name="title"></p>
      </div>
      <div>
        <label>Body</label>
        <p><textarea name="body"></textarea></p>
      </div>
      <input type="submit">
    </form>
    """
    return HttpResponse(HTMLLayout(main))
  elif request.method == "POST":
    global nextId
    global topics
    newTopic = {"id": nextId, "title": request.POST["title"], "body": request.POST["body"]}
    redirectUrl = f"/read/{newTopic['id']}"
    topics.append(newTopic)
    nextId = nextId + 1
    return redirect(redirectUrl)
  
def delete(_, id):
  global topics
  for topic in topics:
    if topic["id"] == id:
      topics.remove(topic)
      break
  return redirect("/")

@csrf_exempt
def update(request, id):
  global topics
  if request.method == "GET":
    main = ""
    for topic in topics:
      if topic["id"] == int(id):
        main = f"""
        <form action="/update/{id}" method="post">
          <div>
            <label>Title</label>
            <p><input type="text" name="title" value={topic["title"]}></p>
          </div>
          <div>
            <label>Body</label>
            <p><textarea name="body">{topic["body"]}</textarea></p>
          </div>
          <input type="submit">
        </form>
        """
        return HttpResponse(HTMLLayout(main))
  elif request.method == "POST":
    for topic in topics:
      if topic["id"] == int(id):
        topic["title"] = request.POST["title"]
        topic["body"] = request.POST["body"]
        break
    redirectUrl = f"/read/{id}"
    return redirect(redirectUrl)