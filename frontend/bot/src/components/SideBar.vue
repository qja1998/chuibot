<template>
  <div class="sidebar">
    <div class="profile">
      <img class="profile-image" src="../assets/avatar.png" alt="Profile" />
      <h2 class="profile-name">{{ nickname }}</h2>
    </div>
    <h3 class="interest-title">요즘 당신의 관심사</h3>
    <div class="social-buttons">
      <button 
        v-for="(platform, index) in socialPlatforms" 
        :key="index" 
        class="social-button">
        {{ platform }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

const socialPlatforms = ref([
  '삼성전자', 'LG전자'
]);

const payload = useUserStore.payload
const nickname = payload.nickname

</script>

<style scoped>
.sidebar {
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: #ffffff;
}

.profile {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.profile-image {
  width: 50px;
  height: 50px;
  border-radius: 50%; /* 프로필 이미지를 둥글게 */
  margin-right: 10px;
}

.profile-name {
  font-size: 18px;
  font-weight: bold;
}

.interest-title {
  font-size: 16px;
  margin-bottom: 10px;
}

.social-buttons {
  display: flex;
  flex-wrap: wrap; /* 버튼들이 여러 줄로 배치되도록 */
}

.social-button {
  margin: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #007bff; /* 기본 배경 색상 */
  color: white;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.social-button:hover {
  background-color: #0056b3; /* 호버 시 색상 변화 */
}
</style>
