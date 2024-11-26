<template>
  <div class="background">
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
  </div>
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

.background {
  height: 100vh; /* 전체 화면 높이 */
  background: linear-gradient(90deg, rgba(0, 0, 0, 1) 30%, rgba(0, 46, 24, 1) 50%, rgba(0, 0, 0, 1) 70%);
  background-size: 300% 300%; /* 애니메이션을 위한 배경 크기 조정 */
  animation: gradientAnimation 50s ease infinite; /* 애니메이션 적용 */
}

@keyframes gradientAnimation {
  0% {
    background-position: 25% 50%; /* 시작 지점 */
    filter: brightness(1);
  }
  50% {
    background-position: 100% 50%; /* 중간 지점 */
    filter: brightness(1.5);
  }
  100% {
    background-position: 25% 50%; /* 끝 지점 */
    filter: brightness(1);
  }
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(0, 0, 0, 0); /* 배경 색상 */
  padding: 33px 7%; /* 패딩 */
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

</style>
