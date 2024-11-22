// vue.config.js
module.exports = {
    devServer: {
      host: '0.0.0.0',   // 모든 외부 요청을 허용
      port: 5174,        // 포트 설정 (default 8080)
      hot: true,         // 핫 모듈 리로딩 활성화
      https: false,      // https를 사용하지 않음
    },
  };
  