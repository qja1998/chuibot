<template>
  <div class="board-container">
    <div class="background-overlay"></div>

    <div class="content-container">
      <header class="header">
        <h1 class="title">Community</h1>
        <router-link to="/create-post">
          <button class="add-thread-btn">
            <span>Add a new thread</span>
            <span class="add-icon">+</span>
          </button>
        </router-link>
      </header>

      <!-- 검색 입력 필드 -->
      <div class="search-container">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Search by title, content, or tags..."
          class="search-input"
          @input="filterPosts"
        />
      </div>

      <!-- 게시물 목록 -->
      <section class="post-list">
        <div v-for="post in filteredPosts" :key="post.id" class="post-item">
          <PostItem :post="post" />
        </div>
      </section>
    </div>
  </div>
</template>


<script>
import PostItem from '@/components/board/PostItem.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  setup() {
    const store = useUserStore();
    const token = store.token;

    return { token };
  },
  components: { PostItem },
  data() {
    return {
      posts: [],
      searchQuery: '',
      filteredPosts: [],
    };
  },
  async mounted() {
    try {
      const response = await axios.get(`${API_URL}/api/v1/board/`, {
        headers: {
          Authorization: `Token ${this.token}`,
        },
      });
      this.posts = response.data; // 응답 데이터를 posts에 할당
      this.filteredPosts = this.posts; // 초기 필터링된 게시물 목록 설정
    } catch (error) {
      console.log("Logout error:", error);
    }
  },
  methods: {
    filterPosts() {
      const query = this.searchQuery.toLowerCase();
      this.filteredPosts = this.posts.filter(post => {
        return (
          post.title.toLowerCase().includes(query) ||
          post.content.toLowerCase().includes(query) ||
          (post.tags && post.tags.some(tag => tag.toLowerCase().includes(query)))
        );
      });
    },
  },
};
</script>



<style scoped>
/* 전체 배경 */
.board-container {
  position: relative;
  width: 100%;
  min-height: 100vh;
  font-family: 'Arial', sans-serif;
  overflow: hidden;
}

/* 배경 그라데이션 */
.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f5f7fa, #dfe7f5, #f8f9fc);
  z-index: 1;
}

/* 메인 콘텐츠 컨테이너 */
.content-container {
  position: relative;
  z-index: 2;
  margin: 32px auto;
  padding: 24px;
  max-width: 800px;
  background: rgba(255, 255, 255, 0.7); /* 반투명 흰색 */
  backdrop-filter: blur(12px); /* 블러 효과 */
  border-radius: 16px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* 헤더 스타일 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.title {
  font-size: 28px;
  font-weight: bold;
  color: #374151;
}

.add-thread-btn {
  display: flex;
  align-items: center;
  background-color: #4f46e5;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 50px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  box-shadow: 0 4px 6px rgba(79, 70, 229, 0.3);
  transition: background-color 0.3s, box-shadow 0.3s;
}

.add-thread-btn:hover {
  background-color: #4338ca;
  box-shadow: 0 6px 8px rgba(67, 56, 202, 0.4);
}

.add-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  color: #4f46e5;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  margin-left: 10px;
  font-size: 16px;
  font-weight: bold;
}

/* 게시물 목록 */
.post-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.search-container {
  margin: 16px 0;
}

.search-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.search-input:focus {
  border-color: #4f46e5; /* 포커스 시 테두리 색상 */
  outline: none; /* 기본 아웃라인 제거 */
}
</style>
