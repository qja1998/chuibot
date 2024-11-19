import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

// useRoute: 받을 때
// useRouter: 보낼 때
import { useRoute, useRouter } from "vue-router";

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const token = ref(null)
  const loginUsername = ref('')

  const login = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/login/`,
      data: {
        username,
        password
      }
    })
    .then((response) => {
      console.log('response:', response)
      token.value = response.data.key
      loginUsername.value = username
      
      router.push('/')
    })
    .catch((error) => {
      console.log("error:", error)
    })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/registration/`,
      data: {
        username,
        password1,
        password2
      }
    })
    .then((response) => {
      console.log('response:', response)
      alert('회원가입 성공')
      login({ username, password: password1})
    })
    .catch((error) => {
      console.log("error:", error)
    })
  }

  return { loginUsername, login, signUp }
}, { persist: true })