<template>
  <div class="board-container">
    <!-- 배경 -->
    <div class="background-overlay"></div>

    <!-- 콘텐츠 -->
    <div class="content-container">
      <!-- 헤더 -->
      <header class="header">
        <h1 class="title">Community</h1>
        <button class="add-thread-btn">
          <span>Add a new thread</span>
          <span class="add-icon">+</span>
        </button>
      </header>

      <!-- 게시물 목록 -->
      <section class="post-list">
        <div v-for="post in posts" :key="post.id" class="post-item">
          <PostItem :post="post" />
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import PostItem from '@/components/board/PostItem.vue';

export default {
  components: { PostItem },
  data() {
    return {
      posts: [
        {
          id: 1,
          title: 'Lecture Rescheduling',
          author: 'Elisabeth May',
          content:
            'Hi mates, so I talked with Dr Hellen and because of her illness we need to reschedule upcoming Lecture...',
          category: ['Accounting'],
          time: '6h ago',
          avatar: 'https://via.placeholder.com/48',
          responses: 11,
        },
        {
          id: 2,
          title: 'Date of the final exams',
          author: 'Dr Ronald Jackson',
          content:
            'Dear Students, after 6 months of our cooperation it is necessary to test your knowledge by the final exam...',
          category: ['Accounting', 'Corporate law'],
          time: '3d ago',
          avatar: 'https://via.placeholder.com/48',
          responses: 3,
        },
      ],
    };
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
</style>
