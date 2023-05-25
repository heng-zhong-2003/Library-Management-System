<template>
  <div class="background-container">
    <div class="search-page">
      <div class="top-bar">
        <span class="logo">Hitoha's Library</span>
        <button class="home-button" @click="goToHomepage">Home</button>
      </div>
      <h1 class="title">Search</h1>
      <div class="search-container">
        <input type="text" v-model="searchTerm" placeholder="Enter book title">
        <button @click="searchBooks">Search</button>
      </div>
      <table v-if="bookList.length > 0">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>ISBN</th>
            <th>Stock</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in bookList" :key="book.isbn">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.isbn }}</td>
            <td>{{ book.current_stock }}</td>
            <td><button @click="borrowBook(book.isbn)">Borrow</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchTerm: '',
      bookList: []
    };
  },
  methods: {
    searchBooks() {
      const searchData = {
        title: this.searchTerm
      };

      axios.post('http://127.0.0.1:5000/api/query/search_title', searchData)
        .then(response => {
          this.bookList = response.data.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    borrowBook(isbn) {
      const borrowData = {
        isbn: isbn,
        email: localStorage.getItem('currentUser')
      };

      axios.post('http://127.0.0.1:5000/api/borrow_return/borrow', borrowData)
        .then(response => {
          // 处理借阅成功后的逻辑
        })
        .catch(error => {
          console.error(error);
        });
    },
    goToHomepage() {
      this.$router.push('/homepage');
    }
  }
};
</script>

<style scoped>
body {
  margin: 0;
}

.background-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-image: url('./bk.jpg'); /* 修改为您本地图像的路径 */
  background-size: cover;
  background-position: center;
}

.search-page {
  display: flex;
  flex-direction: column;
  align-items: center; /* 修改为居中对齐 */
  justify-content: center; /* 修改为居中对齐 */
  padding: 20px;
  height: 100%;
}

.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #007bff;
  padding: 10px;
  color: #fff;
  font-size: 20px;
  text-align: left;
  display: flex;
  align-items: center;
  z-index: 1;
}

.logo {
  margin-left: 20px;
}

.home-button {
  margin-left: auto;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.title {
  margin-top: 0;
}

.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

input[type="text"] {
  padding: 8px;
  border: none;
  border-radius: 4px;
  margin-right: 10px;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px;
  border: 1px solid #ccc;
}

th {
  background-color: #f0f0f0;
}

button:hover {
  background-color: #0056b3;
}
</style>
