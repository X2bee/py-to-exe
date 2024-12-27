# 어떻게 실행?

### 1. Poetry 설치
Poetry가 없는 경우 아래 명령어로 설치
안되면 GPT 한테 물어보셈. OS마다 다른거 같기도
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
또는
```bash
pip install poetry
```

---

### 2. 의존성 설치
Poetry를 사용해 프로젝트 의존성을 설치
```bash
poetry install
```

---

### 3. 가상환경 활성화
가상환경을 활성화하여 프로젝트를 실행
```bash
poetry shell
```

---

### 4. exe 빌드
python 파일을 실행파일(exe)로 빌드
```bash
poetry run python setup.py build 
```
