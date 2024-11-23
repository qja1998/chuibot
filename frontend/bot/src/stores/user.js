import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000';
  const router = useRouter();

  const token = ref(null);
  const loginUsername = ref('');
  const loginNickname = ref('');
  const loginIndustry = ref('');
  const loginCompany = ref('');
  const loginDomain = ref('');
  const isLoggedIn = ref(false); // 로그인 상태 관리 변수 추가

  const userPayload = ref({
    username: loginUsername.value,
    nickname: loginNickname.value,
    industry: loginIndustry.value,
    company: loginCompany.value,
    domain: loginDomain.value
  });
  axios.defaults.withCredentials = true; // 쿠키 포함


  const login = async (payload) => {
    const { username, password } = payload;

    // const csrfToken = getCookie('csrftoken');
    // console.log(csrfToken)

    try {
      const response = await axios.post(`${API_URL}/auth/login/`, {
        username: username,
        password: password
      });

      console.log('response:', response);
      console.log('token:', response.data.key)
      token.value = response.data.key
      const user = await axios.get(`${API_URL}/auth/user/`,{
        headers: {
          'Authorization': `Token ${response.data.key}`, // 토큰 추가
        },
      })
      console.log('user:', user, (await user).data)

      // user 정보 업데이트
      fetchUserInfo(token);

      isLoggedIn.value = true; // 로그인 성공 시 상태 업데이트

      router.push('/');
    } catch (error) {
      console.log("error:", error);
    }
  };

  const signUp = async (payload) => {
    const { username, password1, password2, nickname, industry, company, domain } = payload;

    try {
      const response = await axios.post(`${API_URL}/auth/registration/`, {
        username: username,
        password1: password1,
        password2: password2,
        nickname: nickname,
        industry: industry,
        company: company,
        domain: domain
      });

      console.log('response:', response);
      alert('회원가입 성공');
      await login({
        username,
        password: password1,
        nickname: nickname,
        industry: industry,
        company: company,
        domain: domain
      }); // 로그인 후 호출
    } catch (error) {
      console.log("error:", error);
    }
  };

  const logout = async () => {
    try {
      await axios.post(`${API_URL}/auth/logout/`, {}, {
        headers: {
          Authorization: `Token ${token.value}`, // 현재 토큰을 헤더에 추가
        },
      });
      // 로그아웃 성공 후 상태 초기화
      token.value = null; 
      loginUsername.value = ''; 
      isLoggedIn.value = false; 
      router.push('/login'); // 로그인 페이지로 리다이렉트
    } catch (error) {
      console.log("Logout error:", error);
    }
  };

  const fetchUserInfo = async (token) => {
    console.log('token(fetch)', token.value)
    try {
      const response = await axios.get(`${API_URL}/auth/user/`, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
  
      console.log('response:', response);
  
      // 받은 정보를 저장
      loginUsername.value = response.data.username;
      loginNickname.value = response.data.nickname;
      loginIndustry.value = response.data.industry;
      loginCompany.value = response.data.company;
      loginDomain.value = response.data.domain;
      
      // userPayload를 새 객체로 업데이트
      userPayload.value = {
        username: loginUsername.value,
        nickname: loginNickname.value,
        industry: loginIndustry.value,
        company: loginCompany.value,
        domain: loginDomain.value
      };

      console.log(userPayload.data)
    } catch (error) {
      console.log("Error fetching user info:", error);
    }
  };

  return { token, userPayload, isLoggedIn, login, signUp, logout };
}, { persist: true });
