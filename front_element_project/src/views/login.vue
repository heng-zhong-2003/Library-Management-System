<template>
  <div class="background-container">
    <div class="top-bar">
      <span class="logo">Hitoha's Library</span>
    </div>
    <div class="login-container">
      <h1 class="title">Login</h1>
      <form @submit.prevent="login">
        <div class="input-container">
          <label for="email">Email:</label>
          <input type="text" id="email" v-model="email" required>
        </div>
        <div class="input-container">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
      <router-link to="/register" class="register-button">Register</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    };
  },
  methods: {
    login() {
      axios
        .post('http://127.0.0.1:5000/api/auth/login', {
          email: this.email,
          password: this.password
        })
        .then(response => {
          const responseData = response.data;

          if (responseData.success) {
            // 登录成功，重定向到homepage或其他页面
            this.$router.push('/homepage');
          } else {
            // 登录失败，显示错误信息
            this.error = 'Incorrect email or password.';
          }
        })
        .catch(error => {
          // 处理请求错误
          console.error(error);
        });
      localStorage.setItem('currentUser', this.email);
    }
  }
};
</script>

<style>
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
  z-index: 0; /* 修改为 0 */
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
  z-index: 1;
}

.logo {
  margin-left: 20px;
}

.login-container {
  max-width: 400px;
  margin: 80px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.8);
  overflow: hidden;
}

.title {
  margin-top: 0;
  text-align: left;
}

.input-container {
  margin-bottom: 10px;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
  text-align: left;
}

button {
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

.register-button {
  display: inline-block;
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #28a745;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}

.register-button:hover {
  background-color: #218838;
}
</style>
