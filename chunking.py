import ast
import json
from pathlib import Path
import os
import re
from typing import Dict, List, Set, Any, Optional

def extract_functions_and_classes_with_context(codebase_dir, output_dir):
    """하이브리드 방식으로 함수와 클래스 청킹 (컨텍스트 포함)"""
    Path(output_dir).mkdir(exist_ok=True, parents=True)

    chunks = []
    error_files = []
    processed_files = 0

    for py_file in Path(codebase_dir).glob('**/*.py'):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                code = f.read()

            # 구문 분석으로 유효성 검사
            try:
                tree = ast.parse(code)
            except SyntaxError:
                error_files.append(str(py_file))
                continue

            relative_path = str(py_file.relative_to(codebase_dir))
            file_lines = code.split('\n')

            # 파일 수준 정보 분석
            file_info = analyze_file_structure(tree, file_lines)
            imports = file_info["imports"]
            global_vars = file_info["global_vars"]
            file_docstring = file_info["docstring"]

            # 파일 메타데이터 추출
            metadata = extract_metadata(file_lines)

            # 함수 및 클래스 추출
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    if not hasattr(node, 'lineno') or not hasattr(node, 'end_lineno'):
                        continue

                    start_line = node.lineno - 1
                    end_line = node.end_lineno if hasattr(node, 'end_lineno') else len(file_lines)

                    # 코드 청크가 너무 큰 경우 건너뜀
                    if end_line - start_line > 300:
                        continue

                    # 함수/클래스 위의 주석 포함
                    comment_start = start_line
                    for i in range(start_line-1, max(0, start_line-10), -1):
                        if i < 0:
                            break
                        line = file_lines[i].strip()
                        if line.startswith('#') or line == '':
                            comment_start = i
                        else:
                            break

                    # 노드에 필요한 임포트 및 전역 변수 찾기
                    node_code = '\n'.join(file_lines[comment_start:end_line])
                    required_imports = find_required_imports(node, imports, node_code)
                    required_globals = find_required_globals(node, global_vars, node_code)

                    # 청크 내용 구성 (임포트, 전역 변수, 함수/클래스)
                    chunk_parts = []

                    # 파일 문서 문자열 추가 (있는 경우)
                    if file_docstring:
                        chunk_parts.append(file_docstring)

                    # 필요한 임포트 추가
                    if required_imports:
                        chunk_parts.append("\n".join(required_imports))

                    # 필요한 전역 변수 추가
                    if required_globals:
                        chunk_parts.append("\n".join(required_globals))

                    # 함수/클래스 코드 추가
                    chunk_parts.append(node_code)

                    # 최종 청크 내용
                    chunk_content = "\n\n".join(chunk_parts)

                    # 청크 메타데이터 확장
                    enhanced_metadata = {
                        **metadata,
                        "node_type": node.__class__.__name__,
                        "imports_count": len(required_imports),
                        "globals_count": len(required_globals)
                    }

                    # 청크 추가
                    chunks.append({
                        'type': node.__class__.__name__,
                        'name': node.name,
                        'content': chunk_content,
                        'file_path': relative_path,
                        'start_line': comment_start + 1,
                        'end_line': end_line,
                        'metadata': enhanced_metadata,
                        'persona': relative_path.split(os.sep)[0]  # 첫번째 디렉토리는 페르소나 이름
                    })

            processed_files += 1
            if processed_files % 10 == 0:
                print(f"{processed_files} 파일 처리 완료")

        except Exception as e:
            print(f"Error processing {py_file}: {e}")
            error_files.append(str(py_file))

    # 청크를 JSON으로 저장
    with open(f"{output_dir}/code_chunks.json", 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    # 오류 파일 목록 저장
    with open(f"{output_dir}/error_files.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(error_files))

    print(f"총 {len(chunks)}개의 코드 청크 추출 완료")
    print(f"오류 파일: {len(error_files)}개")

    return chunks


def analyze_file_structure(tree, file_lines):
    """파일 구조 분석: 임포트, 전역 변수, 문서 문자열 등 추출"""
    result = {
        "imports": [],
        "global_vars": [],
        "docstring": None
    }

    # 파일 수준 문서 문자열 확인
    if (isinstance(tree.body[0], ast.Expr) and
            isinstance(tree.body[0].value, ast.Constant) and
            isinstance(tree.body[0].value.value, str)):
        result["docstring"] = file_lines[0:tree.body[0].end_lineno]
        result["docstring"] = '\n'.join(result["docstring"])

    # 모든 최상위 노드 분석
    for node in tree.body:
        # 임포트 문 수집
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            start_line = node.lineno - 1
            end_line = getattr(node, 'end_lineno', start_line + 1)
            import_stmt = '\n'.join(file_lines[start_line:end_line])
            result["imports"].append(import_stmt)

        # 전역 변수 및 상수 수집
        elif isinstance(node, ast.Assign):
            # 간단한 변수 할당만 고려 (복잡한 표현식은 건너뜀)
            targets_ok = all(isinstance(target, (ast.Name, ast.Attribute)) for target in node.targets)
            if targets_ok:
                start_line = node.lineno - 1
                end_line = getattr(node, 'end_lineno', start_line + 1)
                global_var = '\n'.join(file_lines[start_line:end_line])
                result["global_vars"].append(global_var)

    return result

def extract_metadata(file_lines, max_lines=30):
    """파일 상단에서 메타데이터 추출 (@tn- 또는 @dn- 형식)"""
    metadata = {}

    # 파일 상단 일부분만 검사
    for i, line in enumerate(file_lines[:max_lines]):
        if line.strip().startswith(('@tn-', '@dn-')):
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                key = parts[0].replace('@tn-', '').replace('@dn-', '').strip()
                value = parts[1].strip()
                metadata[key] = value

    return metadata

def find_required_imports(node, all_imports, node_code):
    """노드(함수/클래스)에 필요한 임포트 찾기"""
    if not all_imports:
        return []

    required_imports = []

    # 임포트한 모듈, 클래스, 함수 이름 추출
    imported_names = set()
    for import_stmt in all_imports:
        # 'import x' 형식 처리
        match = re.search(r'import\s+([\w\.]+)(?:\s+as\s+(\w+))?', import_stmt)
        if match:
            module = match.group(1)
            alias = match.group(2)
            if alias:
                imported_names.add(alias)
            else:
                imported_names.add(module.split('.')[0])

        # 'from x import y' 형식 처리
        match = re.search(r'from\s+([\w\.]+)\s+import\s+(.+)', import_stmt)
        if match:
            items = match.group(2).split(',')
            for item in items:
                item = item.strip()
                if ' as ' in item:
                    name, alias = item.split(' as ')
                    imported_names.add(alias.strip())
                else:
                    imported_names.add(item.strip())

    # 노드 코드에서 임포트한 이름이 사용되는지 확인
    for import_stmt in all_imports:
        for name in imported_names:
            # 이름이 단어 경계에 있는지 확인 (부분 일치 방지)
            if re.search(r'\b' + re.escape(name) + r'\b', node_code):
                required_imports.append(import_stmt)
                break

    return list(set(required_imports))  # 중복 제거

def find_required_globals(node, all_globals, node_code):
    """노드(함수/클래스)에 필요한 전역 변수 찾기"""
    if not all_globals:
        return []

    required_globals = []

    # 전역 변수 이름 추출
    global_var_names = set()
    for global_var in all_globals:
        # 'x = y' 형식 처리
        match = re.search(r'(\w+)\s*=', global_var)
        if match:
            global_var_names.add(match.group(1))

    # 노드 코드에서 전역 변수가 사용되는지 확인
    for global_var in all_globals:
        for name in global_var_names:
            # 이름이 단어 경계에 있는지 확인 (부분 일치 방지)
            if re.search(r'\b' + re.escape(name) + r'\b', node_code):
                required_globals.append(global_var)
                break

    return list(set(required_globals))  # 중복 제거


def main():
    """청킹 프로세스 실행"""
    codebase_dir = "company_codebase"
    output_dir = "processed_data"

    print("하이브리드 코드 청킹 시작...")
    chunks = extract_functions_and_classes_with_context(codebase_dir, output_dir)
    print(f"청킹 완료: {len(chunks)}개 청크 생성됨")

if __name__ == "__main__":
    main()
