<template>
  <div v-if="locations">
    <v-sheet
    class="pa-5 text-center mx-auto"
    elevation="12"
    max-width="700"
    rounded="lg"
    width="100%"
    >
      <h1 align="center">Выбор локации</h1>
      <v-divider :thickness="5"></v-divider>
      <v-table>
        <thead>
          <tr>
            <th class="text-center">Name</th>
            <th class="text-center">Description</th>
            <th class="text-center">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="location in locations"
            :key="location.id"
            :class="`${location.color}`"
            >
            <td>
              <NuxtLink :to="`/locations_monitor/${location.name}`">
                <v-btn
                  color="black"
                  variant="tonal"
                >
                  {{ location.name }}
                </v-btn>
              </NuxtLink>
            </td>
            <td>{{ location.description }}</td>
            <td>{{ location.status }}</td>
          </tr>
        </tbody>
      </v-table>
    </v-sheet>
  </div>
  <p v-else align="center"><load /></p>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue'

  const locations = ref([])

  async function fetchLocations() {
    const response = await fetch('http://localhost:8000/api/locations')
    if (response.ok) {
      const data = await response.json()
      locations.value = Object.values(data)
    } else {
      console.error("Failed to fetch locations")
    }
  }

  onMounted(() => {
    // Загрузить локации при загрузке компонента
    fetchLocations()

    // Обновлять локации каждые 1 минуту
    setInterval(fetchLocations, 1000)
  })
</script>