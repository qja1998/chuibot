<script setup>
// 화면에 반영할 변수
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';
const store = useUserStore()

const username = ref('')
const password = ref('')

const login = function () {
  
  console.log(username.value, password.value)

  // 서버로 요청 보내도록 작성
  const payload = {
    username: username.value,
    password: password.value
  }

  store.login(payload)
}
</script>

<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username"> username: </label>
        <input type="text" id="username" v-model="username">
      </div>

      <div>
        <label for="password"> password: </label>
        <input type="password" id="password" v-model="password">
      </div>

      <input type="submit" value="login">

    </form>
  </div>
</template>

<style scoped>

</style>