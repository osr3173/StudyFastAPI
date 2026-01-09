# FastAPI Study - Day 1

## Purpose
FastAPI 기본 구조와 요청/응답 흐름을 이해하기 위한 학습 프로젝트입니다.

## What I Learned
- FastAPI 애플리케이션 기본 구조
- GET / POST 엔드포인트 작성
- Query Parameter 처리
- Pydantic을 활용한 요청 바디 검증
- Swagger UI 자동 문서화

## Endpoints
- GET /ping  
  서버 상태 확인용 엔드포인트

- GET /echo?msg=hello  
  Query Parameter 처리 예제

- POST /messages  
  Pydantic 모델 기반 JSON 요청 처리

## How to Run
python -m uvicorn app.main:app --reload
