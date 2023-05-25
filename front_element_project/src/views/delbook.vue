<template>
    <div>
      <div class="top-bar">
        <span class="logo">Hitoha's Library</span>
        <button class="home-button" @click="goToHomepage">Home</button>
      </div>
      <div class="delete-book-page">
        <h1 class="title">Delete Book</h1>
        <div class="search-container">
          <input type="text" v-model="searchTitle" placeholder="Enter title">
          <button @click="searchBooks">Search</button>
        </div>
        <div v-if="bookList.length > 0">
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Author</th>
                <th>ISBN</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="book in bookList" :key="book.isbn">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>{{ book.isbn }}</td>
                <td>
                  <button @click="deleteBook(book.isbn)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchTitle: '',
        bookList: []
      };
    },
    methods: {
      goToHomepage() {
        this.$router.push('/homepage');
      },
      searchBooks() {
        const searchData = {
          title: this.searchTitle
        };
  
        axios.post('http://127.0.0.1:5000/api/query/search_title', searchData)
          .then(response => {
            this.bookList = response.data.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      deleteBook(isbn) {
        const deleteData = {
          isbn: isbn
        };
  
        axios.post('http://127.0.0.1:5000/api/admin/delete_book', deleteData)
          .then(response => {
            // 处理删除成功后的逻辑
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
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .title {
    text-align: center;
    margin-top: 0;
  }
  
  .search-container {
    margin-top: 20px;
    display: flex;
    align-items: center;
  }
  
  input[type="text"] {
    width: 200px;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    margin-left: 10px;
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  table {
    margin-top: 20px;
    border-collapse: collapse;
    width: 100%;
  }
  
  th,
  td {
    padding: 8px;
    border-bottom: 1px solid #ddd;
    text-align: left;
  }
  
  button {
    padding: 8px 16px;
    background-color: #dc3545;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #c82333;
  }
  </style>
  