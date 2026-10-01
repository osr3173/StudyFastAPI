from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile):
    content = file.file.read()

    text = content.decode('utf-8')   # 한글이라 깨져서 읽을 수 있는 글자로 변환
    lines = text.splitlines()        # 줄단위로 잘라 리스트로
    rows = len(lines) - 1            # 헤더 1개 제외한 줄 개수
    return{
        'filename': file.filename,
        'size': len(content),
        'rows': rows
    }