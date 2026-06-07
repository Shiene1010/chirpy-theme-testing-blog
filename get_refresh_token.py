import os
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv  # 👈 .env 파일을 읽기 위한 라이브러리 임포트

# 구글 블로거 API 전체 주소
SCOPES = ['https://googleapis.com']

# 👈 프로그램 시작 전 .env 파일의 변수들을 환경 변수로 로드합니다.
load_dotenv()

def main():
    # .env 파일에서 값을 안전하게 읽어옵니다.
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    
    # 보안 키가 정상적으로 로드되었는지 검증합니다.
    if not client_id or not client_secret:
        print("❌ 에러: .env 파일에서 GOOGLE_CLIENT_ID 또는 GOOGLE_CLIENT_SECRET을 찾을 수 없습니다.")
        print("프로젝트 최상위 폴더에 .env 파일이 있고 올바른 값이 적혀있는지 확인하세요.")
        return

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://google.com",
            "token_uri": "https://googleapis.com"
        }
    }
    
    # 외부 파일의 오염·원천·차단
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    
    # 핵심 해결책: open_browser=False를 설정하여 일반 브라우저 탭이 멋대로 열리는 현상 제어
    creds = flow.run_local_server(
        port=0,
        prompt='consent',
        open_browser=False,
        login_hint='logintobuysome@gmail.com'
    )
    
    print("\n" + "="*10 + " 🎉 드디어 대성공! GitHub Secrets에 넣을 값입니다 " + "="*10)
    print(f"GOOGLE_CLIENT_ID : {creds.client_id}")
    print(f"GOOGLE_CLIENT_SECRET : {creds.client_secret}")
    print(f"GOOGLE_REFRESH_TOKEN : {creds.refresh_token}")

if __name__ == '__main__':
    main()
