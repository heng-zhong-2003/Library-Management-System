<template>
    <div class="register-page">
      <h1 class="title">Register</h1>
      <div class="form-container">
        <div class="input-container">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="input-container">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="input-container">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <button @click="register">Register</button>
      </div>
      <button @click="goToLogin" class="back-button">Back</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        email: '',
        password: '',
        username: ''
      };
    },
    methods: {
      register() {
        const jsonData = {
          email: this.email,
          password: this.password,
          name: this.username
        };
  
        // Send JSON data to the backend
        // Replace the URL with your actual backend endpoint
        axios.post('http://127.0.0.1:5000/api/auth/register', jsonData)
          .then(response => {
            // Handle the response from the backend
            console.log(response.data);
          })
          .catch(error => {
            // Handle any errors
            console.error(error);
          });
      },
      goToLogin() {
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .register-page {
    padding: 20px;
  }
  
  .title {
    text-align: center;
  }
  
  .form-container {
    max-width: 400px;
    margin: 0 auto;
  }
  
  .input-container {
    margin-bottom: 10px;
  }
  
  label {
    display: block;
  }
  
  button {
    display: block;
    margin-top: 20px;
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .back-button {
    margin-top: 20px;
  }
  </style>
  