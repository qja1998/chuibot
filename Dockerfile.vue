# 베이스 이미지 선택
FROM kwon0528/vue_frontend:0.3

# 작업 디렉토리 설정
WORKDIR /app

# # front.sh 파일 복사
# COPY front.sh /app/chuibot/front.sh

# # 실행 권한 부여
# RUN chmod +x /app/chuibot/front.sh

# # 실행
# CMD ["sh", "/app/front.sh"]
# CMD cd ~/chuibot && git pull