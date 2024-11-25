<template>
  <div class="wrapper">
      <!--<h1 class="heading">OpenAI Chat Bot</h1>-->
      <div class="messages">
          <div
              v-for="(message, index) in messages"
              :key="index"
          >
              <div
                  :class="message.from == 'user' ? 'user-message--wrapper' : 'bot-message--wrapper'"
              >
                  <div
                      :class="message.from == 'user' ? 'user-message--content' : 'bot-message--content'"
                  >{{ message.data }}</div>
              </div>
          </div>
          <div
              v-if="messageLoading"
              class="message-loading"
          >생각중...</div>
      </div>
      <div class="footer">
          <input
              v-model="currentMessage"
              type="text"
              class="input-field"
              placeholder="Ask me something."
              @keyup.enter="submitMessage(currentMessage)"
          />
          <button
              @click="submitMessage(currentMessage)"
              class="button"
          >Send</button>
      </div>
  </div>
</template>

<script setup>
import { ref, watch  } from 'vue'
import { defineEmits } from 'vue';
import { useUserStore } from '@/stores/user';

const currentMessage = ref('');
const messageLoading = ref(false);
const API_URL = 'http://127.0.0.1:8000';
const userStore = useUserStore();
const token = userStore.token;
const news_sources = ref([]);
const recruit_sources = ref([]);

const props = defineProps(['messages']);
const messages = ref([]); // 로컬 상태

// emit 정의
const emit = defineEmits(['update-sources']);

// 메타데이터를 부모에게 emit
const updateSources = () => {
  emit('update-sources', {
    news_sources: news_sources.value,
    recruit_sources: recruit_sources.value,
  });
};

watch(
  news_sources,
  () => {
    updateSources();
  },
  { deep: true, immediate: true }
);

watch(
  recruit_sources,
  () => {
    updateSources();
  },
  { deep: true, immediate: true }
);


// messages 업데이트 (props.messages 변경 시 동기화)
const isProcessing = ref(false); // 메시지 처리 중인지 확인
const isInitialized = ref(false); // 첫 실행 여부 확인

watch(
  () => props.messages,
  (newMessages) => {
    // 첫 실행 무시
    if (!isInitialized.value) {
      isInitialized.value = true;
      return;
    }

    console.log(props.messages)
    submitMessage(props.messages)
  },
  { deep: true, immediate: true } // 깊은 감시와 즉시 실행 활성화
);




async function submitMessage(message) {
  console.log('message:', message)
  if (!message.trim()) return; // 빈 메시지 전송 방지
  await addToMessageArray('user', message);
  messageLoading.value = true;

  try {
    const response = await fetch(`${API_URL}/api/v1/chat/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
      body: JSON.stringify({ question: message })
    });

    const data = await response.json();
    if (data) {
      news_sources.value = data.source.news_src;
      recruit_sources.value = data.source.recruit_src;
      await addToMessageArray('chatGpt', data.answer);
      updateMessageStatus('success');
      await userStore.fetchUserInfo()
    }
  } catch (error) {
    console.error('Error submitting message:', error);
    messageLoading.value = false;
  }
  
  updateMessageStatus();
}

function addToMessageArray(from, data) {
  messages.value.push({
      from,
      data
  });
  scrollToBottom();
}

// 마지막 대화 다 나올 수 있도록 수정 필요
function scrollToBottom() {
  const messagesContainer = document.querySelector('.messages');
  messagesContainer.scrollTop = messagesContainer.scrollHeight; // 전체 메시지의 높이로 스크롤
}

function updateMessageStatus(status) {
  if (status === 'success') {
      currentMessage.value = ''
  }
  messageLoading.value = false;
}

</script>


<style scoped>
.wrapper {
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  height: 80vh;
}

.heading,
.user-message--content,
.footer {
  background-color: #0098e0;
}

.heading,
.footer,
.messages {
  padding: 1rem;
}

.bot-message--wrapper,
.user-message--wrapper {
  display: flex;
}

.user-message--wrapper {
  justify-content: flex-end;
}

.bot-message--wrapper {
  justify-content: flex-start;
}

.bot-message--content,
.message-loading,
.user-message--content {
  border-radius: 1rem;
  margin-bottom: 1rem;
  max-width: 70%;
  padding: 1rem;
  white-space: break-spaces;
  width: fit-content;
}

.bot-message--content {
  background-color: #323232;
  color: white;
}

.bot-message--content,
.heading,
.user-message--content {
  color: #fefefe;
}

.message-loading {
  background-color: #e8e8e8;
  color: #323232;
}

.messages {
  margin-bottom: 5rem;
  overflow-y: auto; /* 세로 스크롤 가능 */
  flex-grow: 1; /* 가능한 공간을 모두 차지하도록 설정 */
}

/* footer */
.footer {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  border-radius: 1rem;
  background-color: #0098e0;
  margin-top: auto;
  height: 4%;
}

.footer .input-field {
  flex: 1;
  border-radius: 1rem;
  padding: 1rem;
  border: none;
  height: auto;
}

.footer .button {
  padding: 0.5rem 1rem;
  border-radius: 1rem;
  border: none;
  background-color: #007acc;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-left: 0.5rem;
}

.footer .button:hover {
  background-color: #005f99;
}
</style>
