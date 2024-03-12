import os
import base64

# 32바이트(256비트) 길이의 무작위 바이트 시퀀스 생성
secret_key = os.urandom(64)

# 바이트를 base64 인코딩하여 문자열로 변환
base64_secret_key = base64.urlsafe_b64encode(secret_key).decode('utf-8')

print("JWT Secret Key:", base64_secret_key)