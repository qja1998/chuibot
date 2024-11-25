<template>
  <router-link :to="{ name: 'post-detail', params: { id: post.id } }">
    <p>{{post.id}}</p>
    <div class="post-item">
      <!-- 제목 -->
      <h2 class="post-title">{{ post.title }}</h2>
  
      <!-- 작성자 정보 -->
      <div class="post-author">
        <img :src="post.avatar" alt="Avatar" class="avatar" />
        <div>
          <p class="author-name">{{ post.writer.username }}</p>
          <p class="post-time">{{ post.created_at }}</p>
        </div>
      </div>
  
      <!-- 본문 -->
      <p class="post-content">{{ post.content }}</p>
  
      <!-- 태그 -->
      <div class="post-tags">
        <span v-for="category in [...post.companies, ...post.domains]" :key="category" class="tag">{{ category.name }}</span>
      </div>
  
      <!-- 하단 메뉴 -->
      <div class="post-footer">
        <button class="footer-btn">
          <span class="material-icons-outlined">bookmark_border</span> Save
        </button>
        <button class="footer-btn">
          <span class="material-icons-outlined">chat_bubble_outline</span> Add Response
        </button>
        <div class="responses">
          <div v-for="i in post.responses" :key="i" class="response-avatar">
            <img :src="'https://via.placeholder.com/32/' + (50 + i * 10)" alt="User Avatar" />
          </div>
          <span class="response-count">+{{ post.responses }}</span>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    post: Object,
  },
};
</script>

<style scoped>
/* 게시물 카드 스타일 */
.post-item {
  background-color: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

.post-item:hover {
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}

.post-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 12px;
  color: #1f2937;
}

.post-author {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
}

.author-name {
  font-size: 14px;
  font-weight: bold;
  color: #4b5563;
}

.post-time {
  font-size: 12px;
  color: #6b7280;
}

.post-content {
  font-size: 14px;
  color: #374151;
  margin-bottom: 16px;
}

.post-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.tag {
  font-size: 12px;
  background-color: #f0f9ff;
  color: #3b82f6;
  padding: 4px 8px;
  border-radius: 12px;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-btn {
  background: none;
  border: none;
  color: #6b7280;
  font-size: 14px;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.footer-btn:hover {
  color: #3b82f6;
}

.responses {
  display: flex;
  align-items: center;
}

.response-avatar {
  margin-left: -8px;
  border: 2px solid white;
  border-radius: 50%;
  overflow: hidden;
}

.response-avatar img {
  width: 24px;
  height: 24px;
}

.response-count {
  font-size: 12px;
  color: #6b7280;
  margin-left: 8px;
}
</style>
