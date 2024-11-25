<template>
  <div class="post-detail-container" v-if="!loading">
    <h1>{{ post.title }}</h1>
    <div class="post-author">
      <img :src="post.avatar" alt="Avatar" class="avatar" />
      <div>
        <p class="author-name">{{ post.writer.name }}</p>
        <p class="post-time">{{ post.created_at }}</p>
      </div>
    </div>
    <p class="post-content">{{ post.content }}</p>
    <div class="post-tags">
      <span v-for="tag in [...post.companies, ...post.domains]" :key="tag" class="tag">{{ tag.name }}</span>
    </div>
  </div>
  <div v-else>Loading...</div> <!-- 로딩 중일 때 메시지 -->
</template>

<script>
import axios from 'axios'; // axios 임포트
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';

const API_URL = 'http://127.0.0.1:8000';

export default {
  props: ['id'],
  setup(props) {
    const store = useUserStore();
    const token = store.token;

    console.log(props)

    const post = ref({}); // 게시물 정보 저장
    const loading = ref(true);

    const fetchPost = async () => {
      try {
        const response = await axios.get(`${API_URL}/api/v1/board/${props.id}/`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        post.value = response.data;
      } catch (error) {
        console.error("Error fetching post:", error);
      } finally {
        loading.value = false;
      }
    };

    onMounted(fetchPost);

    return { post, loading };
  },
};
</script>

<style scoped>
/* 스타일을 추가하세요 */
.post-detail-container {
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: auto;
}

.post-author {
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
}

.author-name {
  font-size: 16px;
  font-weight: bold;
}

.post-time {
  font-size: 12px;
  color: #6b7280;
}

.post-content {
  font-size: 14px;
  margin-top: 10px;
}

.post-tags {
  margin-top: 10px;
}

.tag {
  background-color: #f0f9ff;
  color: #3b82f6;
  padding: 4px 8px;
  border-radius: 12px;
  margin-right: 5px;
}
</style>
