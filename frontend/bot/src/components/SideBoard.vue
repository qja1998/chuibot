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
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0), 1px 2px 7px rgba(255, 255, 255, 0.3);
  width: 100%;
  height: 59vh;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
  overflow-y: auto;
}

.toggle-buttons {
  display: flex;
  margin-bottom: 10px; /* 내용과 버튼 사이의 간격 */
}

.toggle-button {
  flex: 1;
  padding: 10px;
  color: white; /* 기본 글자 색상 */
  cursor: pointer;
  text-align: center; /* 중앙 정렬 */
  transition: background-color 0.3s, color 0.3s; /* 부드러운 전환 효과 */

  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  box-shadow: -3px -2px 1px rgba(0, 0, 0, 0.2), 0px -2px 0px rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
}

.toggle-button.first {
  font-family: 'main';
  border-top-left-radius: 8px; /* 왼쪽 둥글게 */
  /* border-bottom-left-radius: 8px; 왼쪽 둥글게 */
}

.toggle-button.last {
  font-family: 'main';
  border-top-right-radius: 8px; /* 오른쪽 둥글게 */
  /* border-bottom-right-radius: 8px; 오른쪽 둥글게 */
}

.toggle-button.active {
  background-color: rgba(1, 247, 160, 0); /* 선택된 버튼 배경 색상 */
  color: white; /* 선택된 버튼 글자 색상 */
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.4), -1px -1px 2px rgba(255, 255, 255, 0.5);
}

.content {
  flex-grow: 1; /* 가능한 공간을 모두 차지하도록 설정 */
  overflow-y: auto; /* 세로 스크롤 가능 */
  font-size: 14px;
  color: #fffefe;
  padding: 10px; /* 패딩 추가 */
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  box-shadow: -3px -2px 1px rgba(0, 0, 0, 0.2), 0px -2px 0px rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
}
</style>
