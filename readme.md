# 개요
    - Web + WAS + DB 형태의 도커 컴포즈 구성

# 구성
```
    / #root
        ㄴ docker-compose.yaml      # 메인 구성 파일

        ㄴ app                      # WAS 포지션의 루트 디렉토리
            ㄴ main.py              # 백엔드 소스코드 부분
            ㄴ requirements.txt     # 백엔드 코드 구동을 위한 라이브러리 및 패키지 버전 등
            ㄴ Dockerfile           # WAS 담당 이미지/컨테이너 구성을 위한 빌드 파일

        ㄴ proxy                    # WEB 포지션 담당
            ㄴ web.conf             # nginx의 프록시 구성에 대한 공유 폴더(바운드 마운트 타입)
        
        ㄴ .env
```