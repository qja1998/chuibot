<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

const store = useUserStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref('')
const industry = ref('')
const company = ref('')
const domain = ref('')

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    industry: industry.value,
    company: company.value,
    domain: domain.value,
  }
  store.signUp(payload)
}

</script>

<template>
  <div class="container">
    <div class="card">
      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="input-group">
          <label for="username"> username: </label>
          <input class="input-field" type="text" id="username" v-model="username">
        </div>
  
        <div class="input-group">
          <label for="password1"> password1: </label>
          <input class="input-field" type="password" id="password1" v-model="password1">
        </div>
  
        <div class="input-group">
          <label for="password2"> password2: </label>
          <input class="input-field" type="password" id="password2" v-model="password2">
        </div>
  
        <div class="input-group">
          <label for="nickname"> nickname: </label>
          <input class="input-field" type="text" id="nickname" v-model="nickname">
        </div>
  
        <div class="input-group">
          <label for="industry"> industry: </label>
          <input class="input-field" type="text" id="industry" v-model="industry">
        </div>
  
        <div class="input-group">
          <label for="company"> company: </label>
          <input class="input-field" type="text" id="company" v-model="company">
        </div>
  
        <div class="input-group">
          <label for="domain"> domain: </label>
          <input class="input-field" type="text" id="domain" v-model="domain">
        </div>
  
        <input type="submit" value="signup" class="btn">
  
      </form>
    </div>
  </div>
</template>

<style scoped>

</style>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  flex-direction: column; 
  align-items: center;
  height: 100vh;
  background: rgba(0, 0, 0, 0);
}

.logo {
  margin-bottom: 40px; /* 로고와 카드 사이의 간격 */
  width: 24%; /* 로고의 너비 조정 */
  height: auto; /* 비율 유지 */
}

.card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  padding: 20px;
  box-shadow: 4px 5px 6px rgba(0, 0, 0, 0.3),
              -3px -2px 7px rgba(255, 255, 255, 0.2); /* 굴절 효과 */
  width: 300px;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin-bottom: 40%; /* 카드가 위로 올라가도록 조정 */
  font-family: 'main';
}

.input-group {
  margin: 15px 0;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 6px;
  margin-top: 25px;
}

.input-field {
  width: 100%;
  padding: 10px 0px 10px 0px;
  border: none;
  border-radius: 5px;
  color: white;
  outline: none;
  transition: background 0.3s;

  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 4px rgba(255, 255, 255, 0.5),
            -4px -2px 6px rgba(0,0,0, 0.3); /* 굴절 효과 */
  width: 300px;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
}

.input-field::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.input-field:focus {
  background: rgba(255, 255, 255, 0.3);
}

.btn {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
  backdrop-filter: blur(10px);
  margin-top: 20px;
  padding: 10px;
  box-shadow: 0 4px 5px rgba(0, 0, 0, 0.6),
              0 0 3px rgba(255, 255, 255, 0.5); /* 굴절 효과 */
  width: 300px;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
}

.btn:hover {
  background: rgba(0, 46, 24, 0.1);
}
</style>