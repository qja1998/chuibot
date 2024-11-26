<template>
  <div v-if="!loading">
    <div class="post-contianer">
      <div class="post-detail-container">
        <div class="post-title">
          <h1>{{ post.title }}</h1>
        </div>
        <div class="post-author">
          <img src="@/assets/avatar.png" alt="Avatar" class="avatar" />
          <div>
            <p class="author-name">{{ post.writer.username }}</p>
            <p class="post-time">{{ post.created_at }}</p>
          </div>
        </div>
        <div class="post-contnet-container">
          <p class="post-content">{{ post.content }}</p>
        </div>
        <div class="post-tags">
          <span v-for="tag in [...post.companies, ...post.domains]" :key="tag" class="tag">{{ tag.name }}</span>
        </div>
      </div>
      <div class="comments-section">
        <h3>댓글</h3>
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <div class="comment">
            <div class="comment-header">
              <span class="comment-author">{{ comment.writer.username }}</span>
              <span class="comment-date">{{ date }}</span>
            </div>
            <div class="comment-body">
              <p>{{ comment.content }}</p>
            </div>
          </div>
        </div>
  
        <div>
          <textarea v-model="newComment" placeholder="댓글을 입력하세요" class="form-input"></textarea>
        </div>
        <button class="comment-bnt" @click="addComment">댓글 추가</button>
      </div>
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

    const post = ref({}); // 게시물 정보 저장
    const comments = ref([]); // 댓글 정보 저장
    const newComment = ref(''); // 새 댓글 내용
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

    const fetchComments = async () => {
      try {
        const response = await axios.get(`${API_URL}/api/v1/board/${post.value.id}/comments/`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        comments.value = response.data;
      } catch (error) {
        console.error("Error fetching comments:", error);
      }
    };

    const addComment = async () => {
      try {
        console.log(post.value.id)
        const response = await axios.post(`${API_URL}/api/v1/board/${post.value.id}/comments/`, {
          content: newComment.value,
        }, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        comments.value.push(response.data);
        newComment.value = ''; // 입력 필드 초기화
      } catch (error) {
        console.error("Error adding comment:", error);
      }
    };

    onMounted(async () => {
      await fetchPost();
      await fetchComments();
    });

    return { post, comments, newComment, loading, addComment };
  },
};
</script>


<style scoped>
/* 스타일을 추가하세요 */

.post-contianer {
  margin: 20px;
}
.post-detail-container {
  font-size: medium;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 20px 20px 20px;
  padding: 20px;
}

.post-author {
  display: flex;
  align-items: center;
}

.post-title {
  font-family: 'main';
}

.avatar {
  margin: 20px;
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
  font-size: 10px;
  color: #6b7280;
}

.post-content {
  font-size: 15px;
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

.comments-section {
  margin: 20px;
  font-size: medium;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 20px 20px 20px;
  padding: 20px;
}

.form-input {
  width: 100%;
  padding: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
}

.comment {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
  background-color: #f9f9f9;

  font-size: medium;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  width: 100%;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  margin: 20px 20px 20px 20px;
  padding: 20px;
  font-family: 'main';
}

.comment-header {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}

.comment-body {
  margin-top: 5px;
  
}

.comment-bnt {
  height: 30px;
  display: flex;
  align-items: center;
  font-size: medium;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  
  color: white;
  border: 1px solid rgba(255, 255, 255, 0); /* 투명 테두리 */
  font-family: 'main';
  margin-top: 20px;
}

</style>
