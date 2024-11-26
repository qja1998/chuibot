<template>
  <div class="reference-container">
    <div v-for="item in items" :key="item.id" class="reference-card" @click="goToUrl(item.url)">
      <img v-if="item.image" :src="item.image" alt="사이트 아이콘" class="reference-icon" />
      <h3 class="reference-title">{{ item.title }}</h3>
      <p class="reference-content">{{ item.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, defineProps } from 'vue';

// 부모 컴포넌트에서 전달받은 props
const props = defineProps(['news_sources', 'recruit_sources']);
const items = ref([]);
const API_KEY = "0b59f0fe6019e4eea8b24cb48ed92754"
// 메타데이터를 가져오는 함수
const fetchMeta = async (url) => {
  try {
    const response = await fetch(`https://api.linkpreview.net?key=${API_KEY}&q=${url}`);
    const data = await response.json();

    return {
      id: items.value.length + 1,
      url: url,
      title: data.title,
      content: data.description.substr(0, 100) + '...',
      image: data.image,
    };
  } catch (error) {
    console.error('Error fetching article data:', error);
  }
};

// URL로 이동하는 함수
const goToUrl = (url) => {
  if (url) {
    window.open(url, '_blank'); // 새 탭에서 열기
  }
};

console.log("props:", props)

// 데이터를 가져오는 함수
const fetchData = async () => {
  items.value = []; // 기존 항목 초기화
  const sources = [...props.news_sources, ...props.recruit_sources]; // 두 소스를 합칩니다
  for (const url of sources) {
    const metaData = await fetchMeta(url);
    items.value.push(metaData);
  }
};

// 컴포넌트가 마운트될 때 메타데이터를 자동으로 가져오기
onMounted(() => {
  fetchData();
});

// props가 변경될 때마다 fetchData 호출
watch(() => [props.news_sources, props.recruit_sources], () => {
  fetchData();
}, { deep: true }); // deep: true를 통해 배열의 변경을 감지
</script>

<style scoped>
.reference-container {
  margin: 20px;
}
.reference-card {
  background-color: white;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  box-shadow: -3px -2px 1px rgba(0, 0, 0, 0.2), 0px -2px 0px rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
}
.reference-card:hover {
  background-color: #e0f7fa; /* 마우스 오버 시 배경색 변경 */
  transform: scale(1.02); /* 약간 확대 */
}
.reference-icon {
  width: 100%; /* 이미지가 카드 폭에 맞춰서 보이도록 수정 */
  height: auto; /* 비율 유지 */
  border-radius: 5px; /* 이미지 모서리 둥글게 */
  margin-bottom: 10px; /* 이미지와 제목 사이의 간격 */
}
.reference-info {
  display: flex;
  flex-direction: column; /* 세로 정렬 */
}
.reference-title {
  font-size: medium;
  margin: 0;
  color: white; /* 제목 색상 */
}
.reference-content {
  margin: 5px 0 0;
  color: lightgray; /* 내용 색상 */
  font-size: 0.9em; /* 내용 글자 크기 조정 */
}
</style>
