import os
import ast
import shutil
from pathlib import Path

def validate_python_files(codebase_dir):
    """
    생성된 Python 파일들이 유효한지 검증하고 기본 통계 수집
    오류가 있는 파일은 errored_files 폴더로 이동시킵니다
    """
    valid_files = 0
    invalid_files = 0
    total_lines = 0
    functions_count = 0
    classes_count = 0

    # errored_files 디렉토리 생성
    errored_dir = Path("errored_files")
    errored_dir.mkdir(exist_ok=True)

    # 모든 Python 파일의 목록 미리 수집 (이동 중에 glob 패턴이 변경될 수 있으므로)
    python_files = list(Path(codebase_dir).glob('**/*.py'))

    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                code = f.read()

            # 구문 분석으로 유효성 검사
            tree = ast.parse(code)

            # 기본 통계 수집
            lines = len(code.split('\n'))
            total_lines += lines

            # 함수 및 클래스 카운트
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions_count += 1
                elif isinstance(node, ast.ClassDef):
                    classes_count += 1

            valid_files += 1

        except SyntaxError as e:
            print(f"Syntax error in {py_file}: {e}")
            invalid_files += 1

            # 오류 파일 이동
            try:
                relative_path = py_file.relative_to(codebase_dir)
                target_dir = errored_dir / relative_path.parent
                target_dir.mkdir(parents=True, exist_ok=True)

                target_file = target_dir / py_file.name

                # 파일 이동 (기존 파일 삭제 후 이동)
                if target_file.exists():
                    os.remove(target_file)

                # 이동 (shutil.move 사용)
                shutil.move(str(py_file), str(target_file))
                print(f"  - 파일 이동됨: {py_file} -> {target_file}")

            except Exception as move_error:
                print(f"  - 파일 이동 실패: {move_error}")

        except Exception as e:
            print(f"Error processing {py_file}: {e}")
            invalid_files += 1

            # 오류 파일 이동
            try:
                relative_path = py_file.relative_to(codebase_dir)
                target_dir = errored_dir / relative_path.parent
                target_dir.mkdir(parents=True, exist_ok=True)

                target_file = target_dir / py_file.name

                # 파일 이동 (기존 파일 삭제 후 이동)
                if target_file.exists():
                    os.remove(target_file)

                # 이동 (shutil.move 사용)
                shutil.move(str(py_file), str(target_file))
                print(f"  - 파일 이동됨: {py_file} -> {target_file}")

            except Exception as move_error:
                print(f"  - 파일 이동 실패: {move_error}")

    print(f"검증 완료:")
    print(f"- 유효한 파일: {valid_files}")
    print(f"- 유효하지 않은 파일: {invalid_files}")
    print(f"- 총 코드 라인: {total_lines}")
    print(f"- 함수 수: {functions_count}")
    print(f"- 클래스 수: {classes_count}")
    print(f"- 오류 파일은 'errored_files' 디렉토리로 이동되었습니다.")

    return valid_files, invalid_files

# 사용 예:
validate_python_files("company_codebase")
