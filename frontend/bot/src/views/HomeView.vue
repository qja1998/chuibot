<script setup>
import { ref } from 'vue';
import ChatBox from '@/components/ChatBox.vue'
import SideBar from '@/components/SideBar.vue';
import SideBoard from '@/components/SideBoard.vue';

const news_sources = ref([]);
const recruit_sources = ref([]);

// 부모 컴포넌트가 update-sources 이벤트를 처리
const updateSources = (sources) => {
  news_sources.value = sources.news_sources;
  recruit_sources.value = sources.recruit_sources;
  console.log('home:', news_sources.value)
};

const name = ref('');

const handleSendMessage = (message) => {
  console.log(message)
  name.value = message;
  // 추가적인 로직이 필요하다면 여기에 추가
};
</script>

<template>
  <div class="chat-layout">
    <nav class="side">
      <SideBar @send-message="handleSendMessage"/>
    </nav>
    <div class="chat-component">
      <ChatBox @update-sources="updateSources" :messages="name"/>
    </div>
    <nav class="side">
      <SideBoard :news_sources="news_sources" :recruit_sources="recruit_sources"/>
    </nav>
  </div>
</template>

<style scoped>
.chat-layout {
  display: flex; /* Flexbox 레이아웃 사용 */
  justify-content: space-between; /* 두 컴포넌트 사이에 공간을 균등하게 배치 */
  height: 80%; /* 전체 높이 설정 */
  margin-top: 5%;
}


.chat-component {
  width: 45%;
  height: 80%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc; /* 테두리 추가 */
  border-radius: 10px; /* 경계 부드럽게 */
}

.side {
  width: 25%; /* SideBoard의 너비 설정 */
  margin-left: 1%; /* 사이드바와 ChatBox 사이의 간격 */
  margin-right: 1%;
}
</style>