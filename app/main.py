# 웹 서비스(API) 개발 예제

# 1. 패키지 모듈 로드
from fastapi import FastAPI

# 2. 앱 생성 (flask랑 똑같다고 함)
app = FastAPI()

# 3. 라우팅 구성 (특정 URL 요청을 특정 함수가 담당하도록 정의)
@app.get("/")
def home():
    return {"message" : "HOME !"} # response -> dictionary -> 자동 직렬화(JSON)