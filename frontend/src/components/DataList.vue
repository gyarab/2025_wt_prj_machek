<script setup>
import { ref } from 'vue'


const polozky = ref([
    { id: 1, nazev: 'První testovací záznam', popis: 'Tohle jsou ukázková data pro projekt Machek.' },
    { id: 2, nazev: 'Druhý testovací záznam', popis: 'Vue.js automaticky překreslí stránku, když se pole změní.' },
    { id: 3, nazev: 'Třetí testovací záznam', popis: 'Tlačítkem níže mě můžeš smazat ze seznamu.' }
])

const smazatPolozku = (id) => {
    polozky.value = polozky.value.filter(polozka => polozka.id !== id)
}
</script>

<template>
  <div class="data-list-container">
    <h2>Přehled záznamů</h2>

    <div v-if="polozky.length > 0" class="cards-grid">
      <div v-for="polozka in polozky" :key="polozka.id" class="card">
        <h3>{{ polozka.nazev }}</h3>
        <p>{{ polozka.popis }}</p>
        <button class="btn-delete" @click="smazatPolozku(polozka.id)">
          Smazat
        </button>
      </div>
    </div>

    <div v-else class="empty-state">
      <p>Žádné položky k zobrazení. Všechno jsi smazal! 🚀</p>
    </div>
  </div>
</template>

<style scoped>
.data-list-container {
  margin-top: 20px;
}


.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 15px;
}

.card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card h3 {
  margin-bottom: 10px;
  font-size: 1.2rem;
}

.card p {
  color: #666;
  font-size: 0.95rem;
  margin-bottom: 15px;
  flex-grow: 1;
}


.btn-delete {
  background-color: #e74c3c;
  color: white;
  align-self: flex-start;
}

.btn-delete:hover {
  background-color: #c0392b;
}


.empty-state {
  text-align: center;
  padding: 40px;
  background: #eaeaea;
  border-radius: 8px;
  color: #555;
  font-style: italic;
}
</style>
