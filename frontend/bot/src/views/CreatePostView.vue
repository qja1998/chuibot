<template>
  <div class="create-post-container">
    <h1>글 작성하기</h1>
    <form @submit.prevent="submitPost">
      <div class="form-group">
        <label for="title">제목</label>
        <input type="text" v-model="title" id="title" required class="form-input" />
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea v-model="content" id="content" required class="form-textarea"></textarea>
      </div>
      <div class="form-group">
        <label>회사 선택</label>
        <input
          type="text"
          v-model="newCompany"
          placeholder="회사 입력"
          class="form-input"
          @input="filterCompanies"
        />
        <ul v-if="filteredCompanies.length" class="dropdown">
          <li
            v-for="(company, index) in filteredCompanies"
            :key="index"
            @click="selectCompany(company)"
          >
            {{ company }}
          </li>
        </ul>
        <div class="selected-items">
          <span
            v-for="(company, index) in selectedCompanies"
            :key="index"
            class="selected-item"
          >
            {{ company }} <button @click="removeCompany(company)">X</button>
          </span>
        </div>
        <button type="button" @click="addCompany" class="add-button">회사 추가</button>
      </div>
      <div class="form-group">
        <label>도메인 선택</label>
        <input
          type="text"
          v-model="newDomain"
          placeholder="도메인 입력"
          class="form-input"
          @input="filterDomains"
        />
        <ul v-if="filteredDomains.length" class="dropdown">
          <li
            v-for="(domain, index) in filteredDomains"
            :key="index"
            @click="selectDomain(domain)"
          >
            {{ domain }}
          </li>
        </ul>
        <div class="selected-items">
          <span
            v-for="(domain, index) in selectedDomains"
            :key="index"
            class="selected-item"
          >
            {{ domain }} <button @click="removeDomain(domain)">X</button>
          </span>
        </div>
        <button type="button" @click="addDomain" class="add-button">도메인 추가</button>
      </div>
      <button type="submit" class="submit-button">제출</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'; // axios 임포트
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

const API_URL = 'http://127.0.0.1:8000/api/v1/board/'; // API URL

export default {
  setup() {
    const store = useUserStore();
    const token = store.token; // Token을 setup에서 가져옵니다
    const router = useRouter();
    return { token }; // token을 반환하여 메서드에서 사용 가능하게 합니다
  },
  data() {
    return {
      title: '',
      content: '',
      companies: ['삼성', 'LG', '네이버'], // 기본 회사 목록
      domains: ['IT', '개발자', 'AI', 'Backend', 'Frontend'], // 기본 도메인 목록
      newCompany: '',
      newDomain: '',
      filteredCompanies: [],
      filteredDomains: [],
      selectedCompanies: [],
      selectedDomains: [],
    };
  },
  methods: {
    filterCompanies() {
      this.filteredCompanies = this.companies.filter(company =>
        company.toLowerCase().includes(this.newCompany.toLowerCase())
      );
    },
    filterDomains() {
      this.filteredDomains = this.domains.filter(domain =>
        domain.toLowerCase().includes(this.newDomain.toLowerCase())
      );
    },
    selectCompany(company) {
      if (!this.selectedCompanies.includes(company)) {
        this.selectedCompanies.push(company);
      }
      this.newCompany = ''; // 입력 필드 초기화
      this.filteredCompanies = []; // 드롭다운 초기화
    },
    selectDomain(domain) {
      if (!this.selectedDomains.includes(domain)) {
        this.selectedDomains.push(domain);
      }
      this.newDomain = ''; // 입력 필드 초기화
      this.filteredDomains = []; // 드롭다운 초기화
    },
    addCompany() {
      if (this.newCompany && !this.selectedCompanies.includes(this.newCompany)) {
        this.selectedCompanies.push(this.newCompany);
        this.newCompany = ''; // 입력 필드 초기화
      }
    },
    addDomain() {
      if (this.newDomain && !this.selectedDomains.includes(this.newDomain)) {
        this.selectedDomains.push(this.newDomain);
        this.newDomain = ''; // 입력 필드 초기화
      }
    },
    removeCompany(company) {
      this.selectedCompanies = this.selectedCompanies.filter(c => c !== company);
    },
    removeDomain(domain) {
      this.selectedDomains = this.selectedDomains.filter(d => d !== domain);
    },
    async submitPost() {
      console.log(this.token)
      try {
        const response = await axios.post(API_URL, {
          title: this.title,
          content: this.content,
          companies: this.selectedCompanies,
          domains: this.selectedDomains,
        }, {
          headers: {
            Authorization: `Token ${this.token}`, // 현재 토큰을 헤더에 추가
          }
        });
        console.log("글이 성공적으로 작성되었습니다:", response.data);
        alert("글이 성공적으로 작성되었습니다!");
        this.router.push('/board'); // /board로 라우팅
      } catch (error) {
        console.error("글 작성 중 오류 발생:", error);
      }
    },
  },
};
</script>

<style scoped>
.create-post-container {
  padding: 20px;
  border-radius: 8px;
  background-color: #ffffff; /* 배경색 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  max-width: 600px;
  margin: auto;
}

h1 {
  color: #333;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
}

.form-textarea {
  resize: vertical;
}

.dropdown {
  border: 1px solid #ddd;
  border-radius: 5px;
  max-height: 150px;
  overflow-y: auto;
  background: white;
  position: absolute;
  z-index: 1000;
  width: 100%;
}

.dropdown li {
  padding: 10px;
  cursor: pointer;
}

.dropdown li:hover {
  background-color: #e2e8f0; /* hover 색상 */
}

.selected-items {
  margin-top: 10px;
}

.selected-item {
  display: inline-block;
  padding: 5px 10px;
  background-color: #4f46e5;
  color: white;
  border-radius: 5px;
  margin-right: 5px;
  margin-bottom: 5px;
}

.selected-item button {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  margin-left: 5px;
}

.add-button {
  margin-top: 5px;
  padding: 5px 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #218838; /* hover 색상 */
}

.submit-button {
  padding: 10px 15px;
  background-color: #4f46e5; /* 제출 버튼 색상 */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #4338ca; /* 마우스 오버 색상 */
}
</style>
