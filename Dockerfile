# Python 베이스 이미지 사용
FROM python:3.10-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /code

# 의존성 복사 및 설치
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 프로젝트 코드 복사
COPY . /code/
