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
        <div>
          <textarea v-model="content" id="content" required class="form-input"></textarea>
        </div>
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
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

const API_URL = 'http://127.0.0.1:8000/api/v1/board/';

export default {
  setup() {
    const store = useUserStore();
    const token = store.token;
    const router = useRouter();
    return { token, router };
  },
  data() {
    return {
      title: '',
      content: '',
      companies: ['삼성', 'LG', '네이버'],
      domains: ['IT', '개발자', 'AI', 'Backend', 'Frontend'],
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
      this.newCompany = '';
      this.filteredCompanies = [];
    },
    selectDomain(domain) {
      if (!this.selectedDomains.includes(domain)) {
        this.selectedDomains.push(domain);
      }
      this.newDomain = '';
      this.filteredDomains = [];
    },
    addCompany() {
      if (this.newCompany && !this.selectedCompanies.includes(this.newCompany)) {
        this.selectedCompanies.push(this.newCompany);
        this.newCompany = '';
      }
    },
    addDomain() {
      if (this.newDomain && !this.selectedDomains.includes(this.newDomain)) {
        this.selectedDomains.push(this.newDomain);
        this.newDomain = '';
      }
    },
    removeCompany(company) {
      this.selectedCompanies = this.selectedCompanies.filter(c => c !== company);
    },
    removeDomain(domain) {
      this.selectedDomains = this.selectedDomains.filter(d => d !== domain);
    },
    async submitPost() {
      try {
        const response = await axios.post(API_URL, {
          title: this.title,
          content: this.content,
          companies: this.selectedCompanies,
          domains: this.selectedDomains,
        }, {
          headers: {
            Authorization: `Token ${this.token}`,
          }
        });
        alert("글이 성공적으로 작성되었습니다!");
        this.router.push('/board');
      } catch (error) {
        console.error("글 작성 중 오류 발생:", error);
      }
    },
  },
};
</script>

<style scoped>
.create-post-container {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0);
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

h1 {
  color: white;
  text-align: center;
}

.form-group {
  padding: 29px;
  margin-bottom: 15px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: black;
  border: 1px solid rgba(255, 255, 255, 0);
  margin: 20px;
  font-family: 'main';
}

.form-input {
  width: 100%;
  padding: 10px 0;
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
  background-color: #e2e8f0;
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
  height: 32px;
  margin-top: 5px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: black;
  border: 1px solid rgba(255, 255, 255, 0);
  font-family: 'main';
}

.add-button:hover {
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1),
              0px 2px 2px rgba(255, 255, 255, 0.3);
}

.submit-button {
  width: 68px;
  height: 37px;
  margin: 20px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  box-shadow: 0px 7px 7px rgba(0, 0, 0, 0.1),
              1px 2px 5px rgba(255, 255, 255, 0.3);
  color: black;
  border: 1px solid rgba(255, 255, 255, 0);
  margin: 20px 6px 20px 20px;
  font-family: 'main';
}

.submit-button:hover {
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1),
              0px 2px 2px rgba(255, 255, 255, 0.3);
}
</style>
