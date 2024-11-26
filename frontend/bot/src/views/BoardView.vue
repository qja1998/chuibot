<template>
  <div class="board-container">
    <div class="background-overlay"></div>

    <div class="content-container">
      <header class="header">
        <h1 class="title">게시판</h1>
        <router-link to="/create-post">
          <button class="add-thread-btn">
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
  
  min-height: 100vh;
  font-family: 'Arial', sans-serif;
  overflow: hidden;
}


/* 메인 콘텐츠 컨테이너 */
.content-container {
  padding: 10px;
  font-size: medium;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

/* 헤더 스타일 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  font-family: 'main';
}

.title {
  margin: 20px;
  font-size: 28px;
  font-weight: bold;
  color: white;
  font-family: 'main';
}

.add-thread-btn {
  display: flex;
  align-items: center;
  padding-left: 10px;
  font-size: medium;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

.add-thread-btn:hover {
  font-size: medium;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

.add-icon {
  width: 15px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border-radius: 50%;
  font-size: 16px;
  font-weight: bold;
  font-family: 'main';
  text-decoration: none;
}

/* 게시물 목록 */
.post-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  font-family: 'main';
}

.search-container {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  width: 87%;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

.search-input {
  width: 100%;
  background: rgba(0, 0, 0, 0);
  padding: 10px;
  border: 0px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s;
  font-family: 'main';
}

</style>
