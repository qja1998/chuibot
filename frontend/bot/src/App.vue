<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <nav>
    <!-- RouterLink 에서 경로를 선택 -->
    <RouterLink to="/">메인페이지</RouterLink>
    |
    <RouterLink to="/login">로그인</RouterLink>
    |
    <RouterLink to="/signup">회원가입</RouterLink>
  </nav>

  <!-- RouterView 에 경로에 해당하는 컴포넌트 출력-->
  <RouterView />
</template>

<style scoped>
</style>
