<template>
    <div>
      <div class="top-bar">
        <span class="logo">Hitoha's Library</span>
        <button class="home-button" @click="goToHomepage">Home</button>
      </div>
      <div class="manage-users-page">
        <h1 class="title">Manage Users</h1>
        <div class="search-container">
          <input type="text" v-model="searchQuery" placeholder="Enter username">
          <button @click="findUsers">Find</button>
        </div>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Username</th>
              <th>Role ID</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.email">
              <td>{{ user.email }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.role_id }}</td>
              <td>
                <button @click="deleteUser(user.email)">Delete</button>
                <button @click="upgradeUser(user.email)">Upgrade</button>
              </td>
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
        searchQuery: '',
        users: []
      };
    },
    methods: {
      goToHomepage() {
        this.$router.push('/homepage');
      },
      findUsers() {
        const jsonData = {
          name: this.searchQuery
        };
  
        // Send JSON data to the backend
        // Replace the URL with your actual backend endpoint
        axios.post('http://127.0.0.1:5000/api/query/search_username', jsonData)
          .then(response => {
            // Handle the response from the backend
            this.users = response.data.data;
          })
          .catch(error => {
            // Handle any errors
            console.error(error);
          });
      },
      deleteUser(email) {
        const jsonData = {
          email: email
        };
  
        // Send JSON data to the backend for deleting a user
        // Replace the URL with your actual backend endpoint
        axios.post('http://127.0.0.1:5000/api/admin/delete_user', jsonData)
          .then(response => {
            // Handle the response from the backend
            console.log(response.data);
            // Refresh the user list or perform any other action as needed
          })
          .catch(error => {
            // Handle any errors
            console.error(error);
          });
      },
      upgradeUser(email) {
        const jsonData = {
          ok: 'y',
          email: email
        }; // Upgrade value
  
        // Send JSON data to the backend for upgrading a user
        // Replace the URL with your actual backend endpoint
        axios.post('http://127.0.0.1:5000/api/admin/upgrade', jsonData)
          .then(response => {
            // Handle the response from the backend
            console.log(response.data);
            // Refresh the user list or perform any other action as needed
          })
          .catch(error => {
            // Handle any errors
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
  
  .manage-users-page {
    padding: 20px;
  }
  
  .title {
    text-align: center;
  }
  
  .search-container {
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th,
  td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  th {
    background-color: #f2f2f2;
  }
  
  button {
    padding: 5px 10px;
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
  