<template>
  <div class="post-details fixed top-0 left-0 w-full h-full bg-gray-900 bg-opacity-50 flex items-center justify-center">
    <div class="bg-white p-6 rounded-lg shadow-lg w-3/4 max-w-2xl">
      <button class="text-gray-400 float-right" @click="$emit('close')">✖</button>
      <h2 class="text-xl font-bold mb-2">{{ post.title }}</h2>
      <p class="text-gray-500 mb-4">{{ post.author }} · {{ post.time }}</p>
      <span class="text-sm text-blue-600">{{ post.category }}</span>
      <p class="mt-4">{{ post.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: Object,
  },
};
</script>

<style scoped>
.post-details {
  z-index: 1000;
}
</style>
