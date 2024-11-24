<template>
  <div class="sidebar">
    <div class="profile">
      <img class="profile-image" src="../assets/avatar.png" alt="Profile" />
      <h2 class="profile-name">{{ nickname }}</h2>
    </div>
    <h3 class="interest-title">요즘 당신의 관심사</h3>
    <!-- <h4>산업: {{ industry }}</h4>
    <h4>기업: {{ company }}</h4>
    <h4>직무: {{ domain }}</h4> -->
    <div class="social-buttons">
      <button 
        v-for="(company, index) in interest.companies.values" 
        :key="index" 
        class="companies-button"
        @click="sendMessage(company.name)">
        {{ company.name }}
      </button>
      <button 
        v-for="(job_role, index) in interest.job_roles" 
        :key="index" 
        class="job_roles-button"
        @click="sendMessage(job_role.name)">
        {{ job_role.name }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { defineEmits } from 'vue';
import { useUserStore } from '@/stores/user';

const emit = defineEmits(['send-message']);
const userStore = useUserStore();
const nickname = computed(() => userStore.userPayload.nickname);
const industry = computed(() => userStore.userPayload.industry);
const company = computed(() => userStore.userPayload.company);
const domain = computed(() => userStore.userPayload.domain);
const interest = computed(() => userStore.userPayload.interest);

console.log('interest (side bar):', interest.values)

const sendMessage = (platform) => {
  emit('send-message', platform);
};
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

.companies-button {
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

.companies-button:hover {
  background-color: #0056b3; /* 호버 시 색상 변화 */
}

.job_roles-button {
  margin: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #00ffdd; /* 기본 배경 색상 */
  color: white;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.job_roles-button:hover {
  background-color: #00b374; /* 호버 시 색상 변화 */
}
</style>
