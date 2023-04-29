<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
</script>

<template>
  <header>
    <div class="topnav">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/dashboard">Dashboard</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </div>
    <div class="wrapper">
      <RouterView />
    </div>
  </header>

</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

@media (min-width: 1024px) {

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

/* Add a black background color to the top navigation */
.topnav {
  background-color: #333;
  overflow: hidden;

  /* position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9999; */
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #04aa6d;
  color: white;
}
</style>
