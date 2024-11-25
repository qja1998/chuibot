<template>
  <div class="reference-container">
    <h2>게시판</h2>
    <div v-for="post in filteredPosts" :key="post.id" class="reference-card">
      <h3 class="reference-title">{{ post.title }}</h3>
      <p class="reference-content">{{ post.content }}</p>
    </div>
    <button class="more-button">더 보기</button>
  </div>
</template>

<script>
import PostItem from '@/components/board/PostItem.vue';
import { useUserStore } from '@/stores/user';
import { computed } from 'vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  setup() {
    const store = useUserStore();
    const token = store.token;

    // 관심사를 통합하여 단일 배열로 변환하고 병합
    const combinedInterests = computed(() => {
      
      const jobRoles = userStore.userPayload.interest.job_roles.map(jobRole => ({
        name: jobRole.name,
        frequency: jobRole.frequency || 1 // 기본 빈도 1로 설정
      }));

      // 두 배열을 합치고 병합
      const allInterests = [...jobRoles];
      
      return allInterests.reduce((acc, current) => {
        const existing = acc.find(item => item.name === current.name);
        if (!existing) {
          acc.push(current);
        }
        return acc;
      }, []);
    });

    return { token, combinedInterests };
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
      const interestNames = this.combinedInterests.map(interest => interest.name.toLowerCase());

      this.filteredPosts = this.posts.filter(post => {
        const postTitle = post.title.toLowerCase();
        const postContent = post.content.toLowerCase();
        const postTags = post.tags ? post.tags.map(tag => tag.toLowerCase()) : [];

        // 관심사 단어가 제목, 내용 또는 태그에 포함되어 있는지 확인
        return (
          interestNames.some(interest => postTitle.includes(interest)) ||
          interestNames.some(interest => postContent.includes(interest)) ||
          postTags.some(tag => interestNames.includes(tag))
        );
      });
    },
  },
};
</script>

<style scoped>
.reference-container {
  padding: 16px;
  background-color: #f9f9f9;
  border-radius: 8px;
  max-width: 600px;
  margin: auto;
}

.reference-card {
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.reference-title {
  font-size: 18px;
  font-weight: bold;
  margin: 0 0 8px;
}

.reference-content {
  font-size: 14px;
  color: #555;
}

.more-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}

.more-button:hover {
  background-color: #0056b3;
}
</style>
