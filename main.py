'''
@ author: Jinhan Kim
Generating Virtual Codebase for Danal
'''

from openai import OpenAI  # 새 임포트 방식
import os
import time

client = OpenAI(api_key="")
# 각 페르소나별 여러 파일 생성
personas = [
    # 백엔드 개발자
    {
        "name": "jin.park",
        "role": "시니어 백엔드 개발자",
        "style": "체계적이고 방어적인 코딩 스타일, 상세한 에러 처리와 로깅",
        "modules": ["payment", "security", "validation"]
    },

    # 프론트엔드 개발자
    {
        "name": "mina.kim",
        "role": "프론트엔드 개발자",
        "style": "간결하고 현대적인 JS/TS 패턴, 함수형 접근법 선호",
        "modules": ["ui_component", "form", "dashboard"]
    },

    # 데이터 사이언티스트
    {
        "name": "alex.wong",
        "role": "데이터 사이언티스트",
        "style": "분석적이고 문서화가 충실한 스타일, 파라미터 최적화 중심",
        "modules": ["analytics", "reporting", "prediction"]
    },

    # 주니어 백엔드 개발자
    {
        "name": "jaewon.lee",
        "role": "주니어 백엔드 개발자",
        "style": "기본적인 구현에 집중, 간헐적 주석, 선임자 스타일 모방",
        "modules": ["notification", "user", "utility"]
    },

    # DevOps 엔지니어
    {
        "name": "sofia.mendez",
        "role": "DevOps 엔지니어",
        "style": "인프라 중심, 강력한 에러 처리, 설정 및 배포 전문",
        "modules": ["config", "deployment", "monitoring"]
    },

    # 시스템 아키텍트
    {
        "name": "hyunwoo.park",
        "role": "시스템 아키텍트",
        "style": "높은 추상화 수준, 디자인 패턴 활용, 시스템 통합 중심",
        "modules": ["core", "integration", "service"]
    },

    # QA 엔지니어
    {
        "name": "emma.chen",
        "role": "QA 엔지니어",
        "style": "테스트 중심, 엣지 케이스 처리, 철저한 검증 로직",
        "modules": ["testing", "mocking", "validation"]
    },

    # 모바일 개발자
    {
        "name": "jun.kim",
        "role": "모바일 개발자",
        "style": "효율적인 UI 렌더링, 상태 관리 패턴, 디바이스 최적화",
        "modules": ["mobile_ui", "device", "storage"]
    },

    # 보안 엔지니어
    {
        "name": "neha.sharma",
        "role": "보안 엔지니어",
        "style": "철저한 입력 검증, 암호화 중심, 보안 모범 사례 적용",
        "modules": ["auth", "encryption", "audit"]
    },

    # 레거시 시스템 전문가
    {
        "name": "david.wilson",
        "role": "레거시 시스템 전문가",
        "style": "옛 스타일 코드, 최소 변경 접근법, 호환성 중심",
        "modules": ["legacy_adapter", "compatibility", "refactoring"]
    }
]

# 각 페르소나별로 코드 생성
for persona in personas:
    for module in persona["modules"]:
        for i in range(5):  # 각 모듈당 파일 3개씩
            prompt = f"""
            당신은 '{persona["name"]}'라는 이름의 {persona["role"]}입니다. 
            'Danal'라는 회사의 코드베이스에서 '{module}' 기능과 관련된 Python 파일을 작성해주세요.
            
            다음 특징을 가진 코드를 작성해주세요:
            1. 모든 함수, 클래스, 변수 이름에 'dn_' 접두사 사용 (클래스는 'DN'으로 시작)
            2. 파일 상단에 @dn- 형식의 주석 포함 (주석은 한국어 또는 영문일 수 있음)
            3. 당신의 고유한 코딩 스타일을 반영
            4. 약 100-200줄 분량의 실제 작동 가능한 코드
            5. 충분한 함수와 클래스 포함 (최소 3-5개)
            
            파일명: dn_{module}_{i+1}.py
            """

            try:
                # 새로운 API 호출 방식
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # 대부분의 사용자가 접근 가능한 모델
                    messages=[{"role": "user", "content": prompt}]
                )
                code = response.choices[0].message.content

                # 코드 부분만 추출 (필요시)
                if "```python" in code:
                    code = code.split("```python")[1].split("```")[0]

                # 파일 저장
                output_dir = f"company_codebase/{persona['name']}"
                os.makedirs(output_dir, exist_ok=True)
                with open(f"{output_dir}/dn_{module}_{i+1}.py", "w") as f:
                    f.write(code)

                print(f"Created {output_dir}/dn_{module}_{i+1}.py")
                time.sleep(1)  # API 속도 제한 방지

            except Exception as e:
                print(f"Error generating {module} for {persona['name']}: {e}")
