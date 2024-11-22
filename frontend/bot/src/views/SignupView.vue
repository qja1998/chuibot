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