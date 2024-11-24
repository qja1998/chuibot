<template>
  <div class="side-board">
    <div class="toggle-buttons">
      <button 
        class="toggle-button" 
        :class="{ active: isContentA, first: true }" 
        @click="isContentA = true">
        추천 기사
      </button>
      <button 
        class="toggle-button" 
        :class="{ active: !isContentA, last: true }" 
        @click="isContentA = false">
        추천 게시글
      </button>
    </div>
    <div class="content">
      <div v-if="isContentA">
        <ReferenceNews :news_sources="props.news_sources" :recruit_sources="props.recruit_sources"/>
      </div>
      <div v-else>
        <ReferenceBoard/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import ReferenceNews from './references/ReferenceNews.vue';
import ReferenceBoard from './references/ReferenceBoard.vue';

const isContentA = ref(true);
const props = defineProps(['news_sources', 'recruit_sources']);
console.log('sideboard:', props)
</script>

<style scoped>
.side-board {
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 8px; /* 바깥쪽 둥글게 */
  background-color: #f9f9f9;
  display: flex;
  flex-direction: column; /* 세로 방향으로 정렬 */
}

.toggle-buttons {
  display: flex;
  margin-bottom: 10px; /* 내용과 버튼 사이의 간격 */
}

.toggle-button {
  flex: 1;
  padding: 10px;
  border: 1px solid #007bff; /* 기본 테두리 색상 */
  background-color: white; /* 기본 배경 색상 */
  color: #007bff; /* 기본 글자 색상 */
  cursor: pointer;
  font-weight: bold; /* 글자 두껍게 */
  text-align: center; /* 중앙 정렬 */
  transition: background-color 0.3s, color 0.3s; /* 부드러운 전환 효과 */
}

.toggle-button.first {
  border-top-left-radius: 8px; /* 왼쪽 둥글게 */
  border-bottom-left-radius: 8px; /* 왼쪽 둥글게 */
}

.toggle-button.last {
  border-top-right-radius: 8px; /* 오른쪽 둥글게 */
  border-bottom-right-radius: 8px; /* 오른쪽 둥글게 */
}

.toggle-button.active {
  background-color: #007bff; /* 선택된 버튼 배경 색상 */
  color: white; /* 선택된 버튼 글자 색상 */
}

.content {
  font-size: 14px;
  color: #333;
}
</style>
