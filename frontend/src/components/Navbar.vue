<script setup>
</script>

<template>
  <nav class="navbar">
    <div class="logo">PrjMachek</div>
    <ul class="nav-links">
      <li><a href="#">Domů</a></li>
      <li><a href="#">Přehled</a></li>
      <li><a href="#">Správa</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
}
.nav-links {
  list-style: none;
  display: flex;
  gap: 15px;
}
.nav-links a {
  color: white;
  text-decoration: none;
}
.nav-links a:hover {
  text-decoration: underline;
}
</style>
