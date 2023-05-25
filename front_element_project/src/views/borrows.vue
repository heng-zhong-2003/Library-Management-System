<template>
  <div class="borrows-page">
    <div class="top-bar">
      <span class="logo">Hitoha's Library</span>
      <router-link to="/homepage" class="home-button">Home</router-link>
    </div>
    <h1 class="title">Borrows</h1>
    <table v-if="bookList.length > 0">
      <thead>
        <tr>
          <th>Title</th>
          <th>ISBN</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in bookList" :key="book.isbn">
          <td>{{ book.title }}</td>
          <td>{{ book.isbn }}</td>
          <td>
            <button @click="returnBook(book.isbn)">Return</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      currentUser: localStorage.getItem('currentUser'),
      bookList: []
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      const data = {
        email: this.currentUser
      };

      axios.post('http://127.0.0.1:5000/api/query/borrows', data)
        .then(response => {
          this.bookList = response.data.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    returnBook(isbn) {
      const data = {
        isbn: isbn,
        email: this.currentUser
      };

      axios.post('http://127.0.0.1:5000/api/borrow_return/return', data)
        .then(response => {
          // 处理返回结果
          // 可以在此更新书籍列表或执行其他操作
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
html,
body {
  height: 100%;
  margin: 0;
}

.borrows-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url('your-image.jpg');
  background-size: 100% 100%;
  background-position: center;
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
}

.logo {
  margin-left: 20px;
}

.home-button {
  margin-left: auto;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border: none;
  border-radius: 4px;
}

.title {
  text-align: center;
  margin-top: 100px;
  font-size: 32px;
  color: #fff;
}

table {
  margin: 20px auto;
  color: #000;
}

th,
td {
  padding: 8px;
  color: #000;
}

</style>

