<template>
  <div>
    <div class="top-bar">
      <span class="logo">Hitoha's Library</span>
      <router-link to="/homepage" class="home-button">Home</router-link>
    </div>
    <div class="add-book-page">
      <h1 class="title">Add Book</h1>
      <div class="form-container">
        <div class="input-container">
          <label for="title">Title:</label>
          <input type="text" id="title" v-model="book.title" required>
        </div>
        <div class="input-container">
          <label for="isbn">ISBN:</label>
          <input type="text" id="isbn" v-model="book.isbn" required>
        </div>
        <div class="input-container">
          <label for="author">Author:</label>
          <input type="text" id="author" v-model="book.author" required>
        </div>
        <div class="input-container">
          <label for="totalStock">Total Stock:</label>
          <input type="number" id="totalStock" v-model="book.total_stock" required>
        </div>
      </div>
      <button class="add-button" @click="addBook">Add</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {
        title: '',
        isbn: '',
        author: '',
        total_stock: 0
      }
    };
  },
  methods: {
    addBook() {
      axios.post('http://127.0.0.1:5000/api/admin/add_book', this.book)
        .then(response => {
          // 处理添加成功后的逻辑
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
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

.home-button:hover {
  background-color: #0056b3;
}

.add-book-page {
  padding: 20px;
}

.title {
  text-align: center;
  margin-top: 0;
}

.form-container {
  margin-top: 20px;
}

.input-container {
  margin-bottom: 10px;
}

label {
  display: block;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.add-button {
  display: block;
  margin-top: 20px;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #0056b3;
}
</style>
