# adk-artifact

이 프로젝트는 Google의 Agent Development Kit(ADK)를 활용하여 이미지 아티팩트를 생성하는 예제입니다.

## 소개

adk-artifact는 Google의 Agent Development Kit을 사용하여 이미지 생성 기능을 구현한 프로젝트입니다. 이 예제는 ADK의 도구(tool) 기능을 활용하여 에이전트가 이미지 아티팩트를 생성하는 방법을 보여줍니다.

## 설치 및 설정

### 1. 환경 설정

`artifact` 폴더에 있는 `.env.example` 파일을 복사하여 같은 폴더에 `.env` 파일을 생성하고 필요한 환경 변수를 설정해야 합니다:

```bash
cp artifact/.env.example artifact/.env
```

생성된 `.env` 파일을 열고 필요한 API 키와 설정 값을 채워넣으세요.

### 2. 의존성 설치

필요한 패키지를 설치합니다:

```bash
uv sync
```

## 실행 방법

ADK 웹 인터페이스를 실행하려면 다음 명령어를 사용합니다:

```bash
uv run adk web
```

이 명령어는 로컬 개발 서버를 시작하며, 브라우저에서 ADK 웹 인터페이스에 접근할 수 있습니다.

## 프로젝트 구조

```
adk-artifact/
├── .venv/                  # 가상 환경 (gitignore)
├── artifact/               # 아티팩트 관련 디렉토리
│   ├── .env                # 환경 변수 (gitignore)
│   ├── .env.example        # 환경 변수 예제 파일
│   ├── __init__.py         # Python 패키지 초기화
│   ├── agent.py            # 에이전트 정의 파일
│   └── tools/              # ADK 도구 정의
│       └── tools.py        # 이미지 생성 도구 구현
├── .gitignore              # Git 무시 파일 목록
├── pyproject.toml          # 프로젝트 메타데이터
├── python-version          # Python 버전 요구사항
├── README.md               # 프로젝트 설명서
├── LICENSE                 # 라이센스 파일
└── uv.lock                 # UV 잠금 파일
```

## 사용 예시

이 예제는 ADK의 도구를 사용하여 이미지 아티팩트를 생성하는 방법을 보여줍니다. `tools.py` 파일에서 정의된 도구는 이미지 생성 API를 호출하고 결과를 아티팩트로 제공합니다.

에이전트는 다음과 같은 방식으로 이미지를 생성할 수 있습니다:

1. 사용자가 이미지 생성을 요청합니다
2. 에이전트는 요청을 처리하여 적절한 프롬프트를 생성합니다
3. `tools.py`에 정의된 도구를 사용하여 이미지를 생성합니다
4. 생성된 이미지는 ADK 웹 프론트엔드에서 아티팩트로 제공됩니다

## 라이센스

이 프로젝트는 [LICENSE](LICENSE) 파일에 명시된 조건 하에 배포됩니다.
