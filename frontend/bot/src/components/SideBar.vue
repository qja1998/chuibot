<template>
  <div class="sidebar">
    <div class="profile">
      <img class="profile-image" src="../assets/avatar.png" alt="Profile" />
      <h2 class="profile-name">{{ nickname }}</h2>
    </div>
    <div class="interest-container">
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
    <div class="button-container">
      <div class="button-group">
        <button 
          v-for="(word, index) in posWords" 
          :key="index" 
          class="emotion-button positive" 
          @click="sendMessage(word)">
          {{ word }}
        </button>
      </div>
      <div class="button-group">
        <button 
          v-for="(word, index) in nagWords" 
          :key="index" 
          class="emotion-button negative" 
          @click="sendMessage(word)">
          {{ word }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { watch } from 'vue';
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


const props = defineProps(['pos_emotion', 'nag_emotion']);
const posWords = ref([]);
const nagWords = ref([]);

// pos_emotion과 nag_emotion이 변경될 때마다 버튼 업데이트
watch([() => props.pos_emotion, () => props.nag_emotion], ([newPosEmotion, newNagEmotion]) => {
  posWords.value = newPosEmotion;
  nagWords.value = newNagEmotion;
}, { immediate: true });

</script>

<style scoped>
.sidebar {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3), 1px 2px 7px rgba(255, 255, 255, 0.3);
  width: 100%;
  height: 25vh;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
}

.profile {
  display: flex;
  align-items: center;
  margin: 20px;
  padding: 5px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3), 1px 2px 7px rgba(255, 255, 255, 0.3);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0);
  overflow-y: auto;
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

.interest-container {
  font-family: 'main';
  margin: 20px;
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
  backdrop-filter: blur(10px);
  box-shadow: 1px 4px 3px rgba(0, 0, 0, 0.2), 1px 1px 2px rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0);
  font-family: 'main';
}

.interest-button:hover {
  filter: brightness(0.9); /* 호버 시 밝기 감소 */
}

.button-container {
  margin-top: 13vh;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3), 1px 2px 7px rgba(255, 255, 255, 0.3);
  width: 100%;
  height: 25vh;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
  overflow-y: auto;
  font-family: 'main';
}

.positive {
  background-color: lightblue; /* 긍정적 버튼 색상 */
  color: black;

  margin: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
  backdrop-filter: blur(10px);
  box-shadow: 1px 4px 3px rgba(0, 0, 0, 0.2), 1px 1px 2px rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0);
  font-family: 'main';
}

.negative {
  background-color: lightcoral; /* 부정적 버튼 색상 */
  color: black;

  margin: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
  backdrop-filter: blur(10px);
  box-shadow: 1px 4px 3px rgba(0, 0, 0, 0.2), 1px 1px 2px rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0);
  font-family: 'main';
}

.emotion-button:hover {
  filter: brightness(0.9); /* 호버 효과 */
}
</style>
