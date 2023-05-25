<template>
  <div class="background-container">
    <div class="homepage">
      <div class="top-bar">
        <span class="logo">Hitoha's Library</span>
        <button class="logout-button" @click="logout">Logout</button>
      </div>
      <h1 class="title">Homepage</h1>
      <div class="buttons">
        <router-link to="/search" class="button">Search</router-link>
        <router-link to="/borrows" class="button">Current Borrows</router-link>
        <router-link to="/manage" class="button">Manage (Admin only)</router-link>
      </div>
      <!-- 其他页面内容 -->
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      // 执行登出操作，例如清除本地存储的用户信息等
      // 然后重定向到登录页面
      this.$router.push('/login');
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

.homepage {
  display: flex;
  flex-direction: column;
  align-items: center; /* 修改为居中对齐 */
  justify-content: center; /* 修改为居中对齐 */
  padding: 10px;
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

.logout-button {
  margin-left: auto;
  padding: 8px 16px;
  background-color: #dc3545;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.title {
  margin: 0;
  padding: 10px;
}

.buttons {
  display: flex;
  flex-direction: column;
  align-items: center; /* 居中对齐 */
  margin-top: 20px;
}

.button {
  width: 100%;
  margin-bottom: 10px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}

.button:hover {
  background-color: #0056b3;
}
</style>
