<template>
  <div class="background-container">
    <div class="top-bar">
      <span class="logo">Hitoha's Library</span>
      <router-link to="/homepage" class="home-button">Home</router-link>
    </div>
    <div class="management-page">
      <h1 class="title">Management</h1>
      <div class="button-container">
        <button @click="goToAddBook">Add Book</button>
        <button @click="goToDeleteBook">Delete Book</button>
        <button @click="goToManageUsers">Manage Users</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  mounted() {
    const currentUser = localStorage.getItem('currentUser');
    const jsonData = {
      email: currentUser
    };

    // 向后端发送包含当前用户的 JSON
    axios.post('http://127.0.0.1:5000/api/admin/manage', jsonData)
      .then(response => {
        const responseData = response.data.data;
        console.log(responseData.qualified);
        if (responseData.qualified !== 'y') {
          // 未满足资格，重定向回 homepage
          this.$router.push('/homepage');
        }
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    goToAddBook() {
      this.$router.push('/addbook');
    },
    goToDeleteBook() {
      this.$router.push('/delbook');
    },
    goToManageUsers() {
      this.$router.push('/manageusr');
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
  text-decoration: none;
  border: none;
  border-radius: 4px;
}

.home-button:hover {
  background-color: #0056b3;
}

.management-page {
  padding: 20px;
}

.title {
  text-align: center;
  margin-top: 0;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
