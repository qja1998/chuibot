<script setup>
import ChatBox from '@/components/ChatBox.vue'
import SideBar from '@/components/SideBar.vue';
import SideBoard from '@/components/SideBoard.vue';
</script>

<template>
  <div class="chat-layout">
    <nav class="side">
      <SideBar/>
    </nav>
    <div class="chat-component">
      <ChatBox/>
    </div>
    <nav class="side">
      <SideBoard/>
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