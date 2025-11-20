from typing import Annotated
from fastapi import FastAPI, Path, Query


app = FastAPI() # 创建后端 Fastapi 对象


# 处理路径 /
@app.get("/")
def index():
    return{"data": "Home Page"}


# 处理路径 /square/数字
@app.get("/square/{number}")
def square(number: Annotated[int, Path(ge=1)]):
    number=int(number)
    result=number*number
    return{"data": result}


# 处理要求字串：（什么是要求字串？）
@app.get("/multiply")
def multiply(
    n1: Annotated[int, Query(ge=1)], 
    n2: Annotated[int, Query(ge=1)],
    ):
    n1=int(n1)
    n2=int(n2)
    result=n1*n2
    return{"data": result}


# 处理路径参数：(什么是路径参数？)
@app.get("/multiply/{n1}/{n2}")
def multiply(
    n1: Annotated[int, Path(ge=1)],
    n2: Annotated[int, Path(ge=1)],
    ):
    n1=int(n1)
    n2=int(n2)
    result=n1*n2
    return{"data": result}


# 处理路径参数：字符串的方式
@app.get("/echo/{name}")
def echo(name: Annotated[str, Path(min_length=3, max_length=10)]):
    return{"message": "Hello, " + name}

 
# 处理路径 /hello?name=名字 处理要求字串
@app.get("/hello")
def hello(name: Annotated[str, Query(min_length=3, max_length=10)]):
    return{"message": "Hello, " + name}
