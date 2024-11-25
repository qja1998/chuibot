<template>

  <nav class="navbar">
    <div class="logo">CHuiZZK</div>
    <div v-if="!userStore.isLoggedIn">
      <ul class="nav-links">
        <li>
          <RouterLink to="/login" class="nav-link">로그인</RouterLink>
        </li>
        <li>
          <RouterLink to="/signup" class="nav-link">회원가입</RouterLink>
        </li>
      </ul>
    </div>

    <div v-else>
      <ul class="nav-links">
        <li>
          <RouterLink to="/" class="nav-link">메인페이지</RouterLink>
        </li>
        <li>
          <RouterLink to="/board" class="nav-link">게시판</RouterLink>
        </li>
        <li>
          <button @click="logout">로그아웃</button>
        </li>
      </ul>
    </div>
  </nav>

  <RouterView />
</template>

<script setup>
import { useUserStore } from './stores/user';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();

onMounted(() => {
  if (!userStore.isLoggedIn) {
    router.push('/login'); // 로그인하지 않았다면 /login으로 리다이렉트
  }
});

const logout = () => {
  userStore.logout(); // 로그아웃 처리
  router.push('/login'); // 로그인 페이지로 리다이렉트
};

</script>

<style scoped>
@font-face {
  font-family: 'main';
  src: url("./assets/fonts/Jalnan2TTF.ttf");
}
@font-face {
  font-family: 'maingothic';
  src: url("./assets/fonts/JalnanGothicTTF.ttf");
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2c2c2c; /* 배경 색상 */
  padding: 15px 30px; /* 패딩 */
  font-family: 'main';
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: white; /* 로고 색상 */
}

.nav-links {
  list-style: none;
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  flex: 1; /* 남은 공간을 차지 */
  gap: 10%; /* 링크 간 간격 */
}

.nav-links li {
  display: inline;
}

.nav-link {
  text-decoration: none;
  color: white; /* 링크 색상 */
  font-size: 16px; /* 링크 글자 크기 */
}

.nav-link:hover {
  text-decoration: underline; /* 호버 시 밑줄 추가 */
}

.contact-button {
  background-color: #00bcd4; /* 버튼 배경 색상 */
  color: white; /* 버튼 글자 색상 */
  border: none;
  border-radius: 5px; /* 둥근 모서리 */
  padding: 10px 20px; /* 패딩 */
  cursor: pointer;
  font-size: 16px; /* 버튼 글자 크기 */
}

.contact-button:hover {
  background-color: #0097a7; /* 호버 시 색상 변화 */
}
</style>
