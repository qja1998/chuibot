<template>
  <div class="sidebar">
    <div class="profile">
      <img class="profile-image" src="../assets/avatar.png" alt="Profile" />
      <h2 class="profile-name">{{ nickname }}</h2>
    </div>
    <h3 class="interest-title">요즘 당신의 관심사</h3>
    <div class="social-buttons">
      <button 
        v-for="(item, index) in combinedInterests" 
        :key="index" 
        v-if="combinedInterests.length > 0"
        class="interest-button"
        :style="{ 
          backgroundColor: getButtonColor(item.frequency),
          color: getTextColor(item.frequency) // 텍스트 색상 설정
        }"
        @click="sendMessage(item.name)">
        {{ item.name }}
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
const interest = computed(() => userStore.userPayload.interest);

// 관심사를 통합하여 단일 배열로 변환하고 병합
const combinedInterests = computed(() => {
  // const companies = userStore.userPayload.interest.companies.map(company => ({
  //   name: company.name,
  //   frequency: company.frequency || 1 // 기본 빈도 1로 설정
  // }));
  
  const jobRoles = userStore.userPayload.interest.job_roles.map(jobRole => ({
    name: jobRole.name,
    frequency: jobRole.frequency || 1 // 기본 빈도 1로 설정
  }));

  // 두 배열을 합치고 병합
  const allInterests = [...jobRoles];
  
  return allInterests.reduce((acc, current) => {
    const existing = acc.find(item => item.name === current.name);
    if (existing) {
      // 이미 존재하는 항목이면 빈도수 합치기
      existing.frequency += current.frequency;
    } else {
      // 새로운 항목 추가
      acc.push(current);
    }
    return acc;
  }, []);
});

// 버튼 색상 결정 로직
const getButtonColor = (frequency) => {
  if (frequency >= 7) return '#003C43';
  if (frequency >= 5) return '#003C43';
  if (frequency >= 3) return '#135D66';
  if (frequency >= 2) return '#77B0AA';
  return '#E3FEF7';
};

// 텍스트 색상 결정 로직
const getTextColor = (frequency) => {
  if (frequency >= 7) return '#FFFFFF'; // 흰색
  if (frequency >= 5) return '#FFFFFF'; // 흰색
  if (frequency >= 3) return '#FFFFFF'; // 흰색
  if (frequency >= 2) return '#000000'; // 검은색
  return '#000000'; // 검은색
};

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
  font-family: 'maingothic';
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

.interest-button {
  margin: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
  font-family: 'main';
}

.interest-button:hover {
  filter: brightness(0.9); /* 호버 시 밝기 감소 */
}
</style>
