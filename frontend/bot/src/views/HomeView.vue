<template>
  <div id="chat-app">
    <h1>ChatGPT</h1>
    <div class="messages">
      <div v-for="(msg, index) in messages" :key="index" class="message">
        <div :class="msg.sender">
          <strong>{{ msg.sender }}:</strong> {{ msg.text }}
        </div>
      </div>
    </div>
    <div class="input">
      <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userMessage: '',
      messages: [],
    };
  },
  methods: {
    async sendMessage() {
      if (this.userMessage.trim() === '') return;

      // 사용자 메시지 추가
      this.messages.push({ sender: 'User', text: this.userMessage });
      
      // API 호출
      try {
        const response = await axios.post('http://localhost:3000/chat', {
          message: this.userMessage,
        });
        const botReply = response.data.reply;

        // 봇의 응답 메시지 추가
        this.messages.push({ sender: 'Bot', text: botReply });
      } catch (error) {
        console.error(error);
        this.messages.push({ sender: 'Bot', text: 'Sorry, something went wrong!' });
      }

      // 입력 필드 초기화
      this.userMessage = '';
    }
  }
};
</script>

<style scoped>
#chat-app {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
}

.messages {
  margin-bottom: 20px;
  max-height: 400px;
  overflow-y: scroll;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #fff;
}

.message {
  margin-bottom: 10px;
}

.message .User {
  text-align: left;
  color: blue;
}

.message .Bot {
  text-align: right;
  color: green;
}

.input {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.input input {
  flex: 1;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.input button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.input button:hover {
  background-color: #45a049;
}
</style>
