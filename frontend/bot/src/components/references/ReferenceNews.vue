<template>
  <div class="reference-container">
    <h2>참고 자료</h2>
    <div v-for="item in items" :key="item.id" class="reference-card">
      <h3 class="reference-title">{{ item.title }}</h3>
      <p class="reference-content">{{ item.content }}</p>
    </div>
    <button class="more-button">더 보기</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          id: 1,
          title: "아정당뉴스",
          content: "아이폰 스크롤캡쳐 스크린 전체화면 길게 캡쳐 2분 요약본\n캡쳐가 필요할 때 Assistive Touch 아이콘을 클릭해 빠르게 캡쳐할 수 있습니다."
        },
        {
          id: 2,
          title: "네이버 블로그",
          content: "아이폰 길게 캡쳐 : 스크롤 스크린샷 따라 하세요 - 네이버 블로그\n여러분들이 찍으려고 하는 페이지를 열어 둔 상태에서 버튼을 올리기 버튼 + 스크롤 ..."
        },
        {
          id: 3,
          title: "티스토리",
          content: "[C#] 셀레니움,Selenium 사용법 (6) - 스크린샷 - ForestBird\n... 스크린샷이 작동하였습니다. 그런데 만약 특수요소부분을 클릭해 사진을 캡쳐하..."
        },
        {
          id: 4,
          title: "아이폰 전체 화면 캡쳐 길게 스크롤 스크린샷 방법 기초까지",
          content: "스크린샷을 찍으려면 아이폰 모델에 따라 버튼 등으로 설명이 있으니, 관련 내용을 확인해 주세요."
        }
      ]
    };
  }
};
</script>

<style scoped>
.reference-container {
  padding: 16px;
  background-color: #f9f9f9;
  border-radius: 8px;
  max-width: 600px;
  margin: auto;
}

.reference-card {
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.reference-title {
  font-size: 18px;
  font-weight: bold;
  margin: 0 0 8px;
}

.reference-content {
  font-size: 14px;
  color: #555;
}

.more-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}

.more-button:hover {
  background-color: #0056b3;
}
</style>
