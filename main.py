"""
개선된 가상 코드베이스 생성기
- 구문 유효성 검증
- 다양한 복잡도 제어
- 파인튜닝 데이터 품질 최적화
"""

import ast
import os
import time
import json
from openai import OpenAI
from typing import Dict, List, Any
import random

class ImprovedCodeGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.generated_files = []

    def validate_python_syntax(self, code: str) -> bool:
        """Python 구문 유효성 검증"""
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    def calculate_complexity_score(self, code: str) -> float:
        """코드 복잡도 점수 계산"""
        try:
            tree = ast.parse(code)
            complexity = 1  # 기본 복잡도

            for node in ast.walk(tree):
                if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
                    complexity += 1
                elif isinstance(node, ast.FunctionDef):
                    complexity += 0.5
                elif isinstance(node, ast.ClassDef):
                    complexity += 1

            # 코드 길이로 정규화
            lines = len([line for line in code.split('\n') if line.strip()])
            normalized = min(complexity / max(lines, 1), 1.0)
            return round(normalized, 3)
        except:
            return 0.0

    def generate_code_with_complexity(self, persona: Dict, module: str, file_index: int,
                                      target_complexity: str = "medium") -> Dict[str, Any]:
        """특정 복잡도를 목표로 코드 생성"""

        complexity_prompts = {
            "low": "간단하고 기본적인 함수들 위주로, 복잡한 로직 없이",
            "medium": "적당한 복잡도의 비즈니스 로직과 에러 처리를 포함하여",
            "high": "복잡한 알고리즘, 다중 클래스 상속, 디자인 패턴을 활용하여"
        }

        task_types = [
            ("code_completion", "부분적으로 구현된 함수를 완성하는"),
            ("code_explanation", "코드의 동작을 설명하는"),
            ("code_refactoring", "기존 코드를 개선하고 리팩토링하는"),
            ("bug_fix", "버그가 있는 코드를 수정하는"),
            ("test_generation", "테스트 코드를 작성하는"),
            ("documentation", "코드에 문서화를 추가하는")
        ]

        # 랜덤하게 task 타입 선택
        task_type, task_description = random.choice(task_types)
        complexity_prompt = complexity_prompts.get(target_complexity, complexity_prompts["medium"])

        prompt = f"""
        당신은 '{persona["name"]}'라는 이름의 {persona["role"]}입니다.
        'Danal'라는 회사의 코드베이스에서 '{module}' 기능과 관련된 Python 파일을 작성해주세요.
        
        코딩 스타일: {persona["style"]}
        
        요구사항:
        1. {complexity_prompt} 작성
        2. 모든 함수, 클래스, 변수 이름에 'dn_' 접두사 사용 (클래스는 'DN'으로 시작)
        3. 파일 상단에 '# @dn- {module.title()} Module' 주석 포함
        4. {task_description} 스타일의 실제 작동 가능한 코드
        5. 100-250줄 분량
        6. 함수 최소 4-7개, 클래스 최소 1-3개 포함
        7. 적절한 docstring과 타입 힌트 포함
        8. 실제 비즈니스 로직이 포함된 완전한 구현
        
        중요: 반드시 구문적으로 올바른 Python 코드만 생성하세요.
        """

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4",  # 더 나은 품질을 위해 GPT-4 사용
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                code = response.choices[0].message.content

                # 코드 부분만 추출
                if "```python" in code:
                    code = code.split("```python")[1].split("```")[0]
                elif "```" in code:
                    code = code.split("```")[1].split("```")[0]

                code = code.strip()

                # 구문 유효성 검증
                if not self.validate_python_syntax(code):
                    print(f"  ⚠️ Syntax error in attempt {attempt + 1}, retrying...")
                    continue

                # 복잡도 계산
                actual_complexity = self.calculate_complexity_score(code)

                return {
                    "code": code,
                    "complexity": actual_complexity,
                    "task_type": task_type,
                    "author": persona["name"],
                    "module": module,
                    "file_index": file_index,
                    "target_complexity": target_complexity,
                    "syntax_valid": True
                }

            except Exception as e:
                print(f"  ❌ Error in attempt {attempt + 1}: {e}")
                if attempt == max_retries - 1:
                    return None
                time.sleep(2)

        return None

    def generate_finetuning_data(self, code_info: Dict[str, Any]) -> Dict[str, Any]:
        """파인튜닝 데이터 생성 (Input-Output 중복 방지)"""
        code = code_info["code"]
        task_type = code_info["task_type"]

        # 코드를 함수별로 분할
        try:
            tree = ast.parse(code)
            functions = []

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # 함수의 시작과 끝 라인 추출
                    func_lines = code.split('\n')[node.lineno-1:node.end_lineno]
                    functions.append({
                        "name": node.name,
                        "code": '\n'.join(func_lines),
                        "lineno": node.lineno
                    })

            if not functions:
                return None

            # 랜덤하게 함수 선택
            selected_func = random.choice(functions)

            # Task 타입별로 다른 Input-Output 생성
            if task_type == "code_completion":
                # 함수의 일부만 input으로, 전체를 output으로
                func_lines = selected_func["code"].split('\n')
                if len(func_lines) > 3:
                    # 함수 시그니처 + 첫 줄만 input으로
                    input_lines = func_lines[:2] + ["    # TODO: 구현 완료"]
                    input_code = '\n'.join(input_lines)
                    output_code = selected_func["code"]
                else:
                    # 짧은 함수는 시그니처만
                    input_code = func_lines[0] + ":\n    # TODO: 구현"
                    output_code = selected_func["code"]

                instruction = "다음 함수를 완성해주세요."

            elif task_type == "code_explanation":
                input_code = selected_func["code"]
                output_code = f"이 함수는 {selected_func['name']}로, 다음과 같은 기능을 수행합니다:\n\n[함수의 동작과 목적에 대한 상세한 설명]"
                instruction = "다음 코드의 동작을 설명해주세요."

            elif task_type == "code_refactoring":
                # 간단한 버전을 input으로, 개선된 버전을 output으로
                input_code = selected_func["code"].replace('"""', '').replace("'''", "")  # 문서 제거
                output_code = selected_func["code"]  # 원본 유지
                instruction = "다음 코드를 더 나은 구조로 리팩토링해주세요."

            else:
                # 기본적으로 completion 스타일
                input_code = f"# {task_type} 작업\n{selected_func['code'][:50]}..."
                output_code = selected_func["code"]
                instruction = f"다음 {task_type} 작업을 수행해주세요."

            # 메타데이터 포함한 input 생성
            full_input = f"""파일: company_codebase/{code_info['author']}/dn_{code_info['module']}_{code_info['file_index']}.py
작성자: {code_info['author']}
모듈: {code_info['module']}
복잡도: {code_info['complexity']}

# 코드 시작점:
{input_code}"""

            return {
                "instruction": instruction,
                "input": full_input,
                "output": output_code,
                "task_type": task_type,
                "complexity": code_info['complexity'],
                "author": code_info['author'],
                "module": code_info['module']
            }

        except Exception as e:
            print(f"  ❌ Error generating finetuning data: {e}")
            return None

    def generate_codebase(self, personas: List[Dict], output_dir: str = "company_codebase"):
        """개선된 코드베이스 생성"""
        print("🚀 Starting Improved Virtual Codebase Generation")
        print("=" * 60)

        all_finetuning_data = []
        complexity_targets = ["low", "medium", "high"]

        total_files = sum(len(persona["modules"]) * 5 for persona in personas)
        current_file = 0

        for persona in personas:
            print(f"\n👨‍💻 Generating for {persona['name']} ({persona['role']})")

            for module in persona["modules"]:
                print(f"  📁 Module: {module}")

                for i in range(5):  # 각 모듈당 5개 파일
                    current_file += 1

                    # 복잡도 균형 맞추기
                    if i < 2:
                        target_complexity = "low"
                    elif i < 4:
                        target_complexity = "medium"
                    else:
                        target_complexity = "high"

                    print(f"    📄 File {i+1}/5 (Target: {target_complexity})", end=" ")

                    # 코드 생성
                    code_info = self.generate_code_with_complexity(
                        persona, module, i+1, target_complexity
                    )

                    if code_info is None:
                        print("❌ Failed")
                        continue

                    # 파일 저장
                    persona_dir = f"{output_dir}/{persona['name']}"
                    os.makedirs(persona_dir, exist_ok=True)

                    filename = f"dn_{module}_{i+1}.py"
                    filepath = f"{persona_dir}/{filename}"

                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(code_info["code"])

                    # 파인튜닝 데이터 생성
                    finetuning_sample = self.generate_finetuning_data(code_info)
                    if finetuning_sample:
                        all_finetuning_data.append(finetuning_sample)

                    print(f"✅ (Complexity: {code_info['complexity']:.3f})")

                    # Progress
                    progress = (current_file / total_files) * 100
                    print(f"    Progress: {progress:.1f}% ({current_file}/{total_files})")

                    time.sleep(1)  # API 제한 방지

        # 파인튜닝 데이터 저장
        print(f"\n💾 Saving Fine-tuning Data...")

        # Train/Val 분할 (80/20)
        random.shuffle(all_finetuning_data)
        split_idx = int(len(all_finetuning_data) * 0.8)

        train_data = all_finetuning_data[:split_idx]
        val_data = all_finetuning_data[split_idx:]

        finetuning_dir = f"{output_dir}/finetuning_data"
        os.makedirs(finetuning_dir, exist_ok=True)

        with open(f"{finetuning_dir}/improved_train_dataset.json", "w", encoding="utf-8") as f:
            json.dump(train_data, f, ensure_ascii=False, indent=2)

        with open(f"{finetuning_dir}/improved_val_dataset.json", "w", encoding="utf-8") as f:
            json.dump(val_data, f, ensure_ascii=False, indent=2)

        # 통계 출력
        print(f"\n📊 Generation Complete!")
        print(f"=" * 60)
        print(f"📁 Total Files Generated: {len(self.generated_files)}")
        print(f"🎯 Fine-tuning Samples: {len(all_finetuning_data)}")
        print(f"🚂 Training Samples: {len(train_data)}")
        print(f"🧪 Validation Samples: {len(val_data)}")

        # 복잡도 분포 분석
        complexities = [sample["complexity"] for sample in all_finetuning_data]
        low_count = len([c for c in complexities if c <= 0.3])
        medium_count = len([c for c in complexities if 0.3 < c <= 0.6])
        high_count = len([c for c in complexities if c > 0.6])

        print(f"\n📈 Complexity Distribution:")
        print(f"  🟢 Low (0.0-0.3): {low_count} ({low_count/len(complexities)*100:.1f}%)")
        print(f"  🟡 Medium (0.3-0.6): {medium_count} ({medium_count/len(complexities)*100:.1f}%)")
        print(f"  🔴 High (0.6-1.0): {high_count} ({high_count/len(complexities)*100:.1f}%)")

        # Task 타입 분포
        task_types = {}
        for sample in all_finetuning_data:
            task_type = sample["task_type"]
            task_types[task_type] = task_types.get(task_type, 0) + 1

        print(f"\n🎨 Task Type Distribution:")
        for task_type, count in task_types.items():
            print(f"  • {task_type}: {count} samples ({count/len(all_finetuning_data)*100:.1f}%)")


def main():
    """메인 실행 함수"""
    # 기존 페르소나 정의 (동일)
    personas = [
        {
            "name": "jin.park",
            "role": "시니어 백엔드 개발자",
            "style": "체계적이고 방어적인 코딩 스타일, 상세한 에러 처리와 로깅",
            "modules": ["payment", "security", "validation"]
        },
        {
            "name": "mina.kim",
            "role": "프론트엔드 개발자",
            "style": "간결하고 현대적인 JS/TS 패턴, 함수형 접근법 선호",
            "modules": ["ui_component", "form", "dashboard"]
        },
        {
            "name": "alex.wong",
            "role": "데이터 사이언티스트",
            "style": "분석적이고 문서화가 충실한 스타일, 파라미터 최적화 중심",
            "modules": ["analytics", "reporting", "prediction"]
        },
        {
            "name": "jaewon.lee",
            "role": "주니어 백엔드 개발자",
            "style": "기본적인 구현에 집중, 간헐적 주석, 선임자 스타일 모방",
            "modules": ["notification", "user", "utility"]
        },
        {
            "name": "sofia.mendez",
            "role": "DevOps 엔지니어",
            "style": "인프라 중심, 강력한 에러 처리, 설정 및 배포 전문",
            "modules": ["config", "deployment", "monitoring"]
        },
        {
            "name": "hyunwoo.park",
            "role": "시스템 아키텍트",
            "style": "높은 추상화 수준, 디자인 패턴 활용, 시스템 통합 중심",
            "modules": ["core", "integration", "service"]
        },
        {
            "name": "emma.chen",
            "role": "QA 엔지니어",
            "style": "테스트 중심, 엣지 케이스 처리, 철저한 검증 로직",
            "modules": ["testing", "mocking", "validation"]
        },
        {
            "name": "jun.kim",
            "role": "모바일 개발자",
            "style": "효율적인 UI 렌더링, 상태 관리 패턴, 디바이스 최적화",
            "modules": ["mobile_ui", "device", "storage"]
        },
        {
            "name": "neha.sharma",
            "role": "보안 엔지니어",
            "style": "철저한 입력 검증, 암호화 중심, 보안 모범 사례 적용",
            "modules": ["auth", "encryption", "audit"]
        },
        {
            "name": "david.wilson",
            "role": "레거시 시스템 전문가",
            "style": "옛 스타일 코드, 최소 변경 접근법, 호환성 중심",
            "modules": ["legacy_adapter", "compatibility", "refactoring"]
        }
    ]

    # API 키 입력
    # api_key = input("OpenAI API Key를 입력하세요: ").strip()
    api_key = ''
    if not api_key:
        print("❌ API 키가 필요합니다.")
        return

    # 개선된 코드 생성기 실행
    generator = ImprovedCodeGenerator(api_key)
    generator.generate_codebase(personas)

    print(f"\n🎉 완료! 개선된 코드베이스가 'company_codebase' 폴더에 생성되었습니다.")
    print(f"📋 다음 단계: enhanced_inspect_chunks.py로 품질 검증을 수행하세요.")


if __name__ == "__main__":
    main()
