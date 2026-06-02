<script setup>
import { ref, onMounted } from 'vue'
import Navbar from './components/Navbar.vue'

const nadpis = ref('Pára')

onMounted(() => {
    console.log('Frontend aplikace je připravena!')
})
</script>

<template>
  <div class="app-container">
    <Navbar />

    <main class="main-content">
      <h1>{{ nadpis }}</h1>
      <p>Tento frontend běží na Vue.js a je připraven pro napojení na tvůj backend.</p>
      
      </main>
  </div>
</template>

<style scoped>

.app-container {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
.main-content {
  margin-top: 20px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}
</style>
