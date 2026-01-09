# 서버 본체 클래스
from fastapi import FastAPI

# JSON 형태의 문자열 검증을 위한 라이브러리
# content라는 문자열 형태의 키를 가지고 있어야 함
from pydantic import BaseModel


# 서버 본체 생성
# title은 docs에 보이는 이름
app = FastAPI(title="FastApi Test")

# Get /ping : 서버 헬스 체크
@app.get("/ping")
def ping():
    return {"status": "ok"}


# Get /echo?msg=hello : 쿼리 파라미터 받는 법
# msg : str -> fastapi가 자동 타입 검사해줌
@app.get("/echo")
def echo(msg: str):
    return {"echo": msg}

# POST body(JSON) 구조 정의(pydantic)
class Message(BaseModel):
    content: str

# POST /messages : JSON Body를 Message로 받아 처리
# message: Message -> FastApi가 JSON을 검증/변환해 message 객체로 반환
@app.post("/messages")
def create_message(message: Message):
    return {
        "received": message.content,
        "length": len(message.content)
    } 