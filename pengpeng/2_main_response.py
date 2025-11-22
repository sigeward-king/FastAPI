from fastapi import FastAPI
from typing import Annotated, Path, Query

from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse

from fastapi.responses import FileResponse

from fastapi.responses import RedirectResponse

app = FastAPI()

"""
### 各种回应格式：

1. reponse 返回的是一个 json 的格式。
2. response 返回的是一个 html 的格式。
3. response 纯文字的格式。
4. responese 整个文件，使用 FileResponse 来返回。
"""

@app.get("/")
def index():
    return HTMLResponse("""
          <h3>网页标题</h3>
          <div>网页内容</div>
          <a href='https://www.google.com'>Google</a>
    """)

# 这样返回的就是一个 JSON 的格式：
@app.get("/")
def index():
      return JSONResponse({"data": "Home Page", "title": "My Data"})


# 这样会返回一个 HTML 的格式：
@app.get("/")
def index():
      return FileResponse("www/home.html")


# 返回一个图片的格式：
@app.get("/img/logo")
def logo():
      return FileResponse("www/logo.png")

