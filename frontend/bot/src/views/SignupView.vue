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
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username"> username: </label>
        <input type="text" id="username" v-model="username">
      </div>

      <div>
        <label for="password1"> password1: </label>
        <input type="password" id="password1" v-model="password1">
      </div>

      <div>
        <label for="password2"> password2: </label>
        <input type="password" id="password2" v-model="password2">
      </div>

      <div>
        <label for="nickname"> nickname: </label>
        <input type="text" id="nickname" v-model="nickname">
      </div>

      <div>
        <label for="industry"> industry: </label>
        <input type="text" id="industry" v-model="industry">
      </div>

      <div>
        <label for="company"> company: </label>
        <input type="text" id="company" v-model="company">
      </div>

      <div>
        <label for="domain"> domain: </label>
        <input type="text" id="domain" v-model="domain">
      </div>

      <input type="submit" value="회원가입">

    </form>
  </div>
</template>

<style scoped>

</style>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: rgba(0, 0, 0, 0);
}

.card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1),
              0 0 10px rgba(255, 255, 255, 0.3); /* 굴절 효과 */
  width: 300px;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin-bottom: 40%; /* 카드가 위로 올라가도록 조정 */
}

.input-group {
  margin: 15px 0;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
}

.input-field {
  width: 100%;
  padding: 10px 0px 10px 0px;
  border: none;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  outline: none;
  transition: background 0.3s;
}

.input-field::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.input-field:focus {
  background: rgba(255, 255, 255, 0.3);
}

.btn {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1),
              0 0 10px rgba(255, 255, 255, 0.3); /* 굴절 효과 */
  width: 300px;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
}

.btn:hover {
  background: rgba(0, 46, 24, 0.2);
}
</style>