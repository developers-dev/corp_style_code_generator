# 사내용 코드 코파일럿 PoC를 위한 가상 코드데이터 생성기

이 프로젝트는 사내용 코드 코파일럿 PoC를 위한 가상 코드데이터를 생성하기 위한 코드입니다.

`generator.py` - 실제 실수도 있을 수 있는 가상 코드 생성기 (사내 코드코파일럿 테스트용)

`generator_improved.py` - 코드 품질이 좋은 가상 코드 생성기

## 사용방법

### 1. 코드 생성하기

`generator.py` 에서 페르소나를 설정합니다. (설정이유: 다양한 코드 스타일을 생성하기 위함)

```python
personas = [
    {
        "name": "jin.park",
        "role": "시니어 백엔드 개발자",
        "style": "체계적이고 방어적인 코딩 스타일, 상세한 에러 처리와 로깅",
        "modules": ["payment", "security", "validation"]
    },
    # 다른 페르소나 설정...
]
```

각 페르소나는 다음 속성을 가집니다:
- `name`: 개발자 이름 (생성된 파일이 저장될 폴더명)
- `role`: 개발자 역할
- `style`: 코딩 스타일 특성
- `modules`: 생성할 코드 모듈 목록

생성된 데이터는 `company_codebase` 디렉토리에 저장됩니다.

고급 코드 생성기는 `company_codebase_improved` 디렉토리에 저장됩니다.


### 2. 코드 유효성 검증하기

`validate_python_files.py`는 생성된 코드의 유효성을 검증하고, 검증에 실패한 데이터를 `company_codebase`에서 `validate/errored_files` 디렉토리로 이동시킵니다.

```bash
python validate_python_files.py
```

## 검증 결과 예시

```
검증 완료:
- 유효한 파일: 135
- 유효하지 않은 파일: 15
- 총 코드 라인: 18750
- 함수 수: 540
- 클래스 수: 270
- 오류 파일은 'validate/errored_files' 디렉토리로 이동되었습니다.
```

## 프로젝트 구조

- `generator.py`: 가상 코드 생성기
- `company_codebase/`: 생성된 코드 저장 디렉토리
- `errored_files/`: 유효성 검증에 실패한 파일 이동 디렉토리


