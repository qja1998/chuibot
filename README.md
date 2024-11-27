# chuibot

1. 도커 엔진을 실행하고 `docker-compose up --build`를 환경을 도커 상으로 띄웁니다.

2. backend, frontend 컨테이너에 각각 접근

3. backend
  - 다음 명령어들을 순서대로 실행해 서버를 실행합니다.
  - root는 home 디렉토리입니다.
  ```sh
  service postgresql start
  poetry shell
  cd app/backend
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
  ```

4. frontend
  - 다음 명령어들을 순서대로 실행해 npm을 실행합니다.
  - root는 app 디렉토리입니다.
  ```sh
  cd frontend/bot
  npm run dev
  ```