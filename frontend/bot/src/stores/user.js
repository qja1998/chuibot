import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000';
  const router = useRouter();

  const token = ref(null);
  const loginUsername = ref('');
  const isLoggedIn = ref(false); // 로그인 상태 관리 변수 추가

  const login = async (payload) => {
    const { username, password } = payload;

    try {
      const response = await axios.post(`${API_URL}/dj-rest-auth/login/`, {
        username,
        password,
      });

      console.log('response:', response);
      token.value = response.data.key;
      loginUsername.value = username;
      isLoggedIn.value = true; // 로그인 성공 시 상태 업데이트

      router.push('/');
    } catch (error) {
      console.log("error:", error);
    }
  };

  const signUp = async (payload) => {
    const { username, password1, password2 } = payload;

    try {
      const response = await axios.post(`${API_URL}/dj-rest-auth/registration/`, {
        username,
        password1,
        password2,
      });

      console.log('response:', response);
      alert('회원가입 성공');
      await login({ username, password: password1 }); // 로그인 후 호출
    } catch (error) {
      console.log("error:", error);
    }
  };

  return { token, loginUsername, isLoggedIn, login, signUp };
}, { persist: true });
