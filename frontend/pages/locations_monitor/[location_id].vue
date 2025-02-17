<template>
    <h1
    class="text-center my-10">
        {{ location_id }}
    </h1>
    <v-sheet
    class="pa-5 text-center mx-auto"
    elevation="12"
    max-width="700"
    rounded="lg"
    width="100%"
    >
        <v-table>
            <thead>
                <tr>
                    <th class="text-center">Time</th>
                    <th class="text-center">User-IMG</th>
                    <th class="text-center">User-Name</th>
                    <th class="text-center">Rang</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="location in locations"
                    :key="location.id"
                    :class="`${location.color}`"
                >
                    <td>
                        <!-- {{ time }} -->
                    </td>
                    <td>
                        <!-- <v-img :src="`${user.ing}`">
                        </v-img> -->
                    </td>
                    <td>
                        <NuxtLink :to="`/location/${location.name}`">
                            <v-btn
                            color="black"
                            variant="tonal"
                            >
                                User-Name
                            </v-btn>
                        </NuxtLink>
                    </td>
                </tr>
            </tbody>
        </v-table>
    </v-sheet>
</template>

<script setup>
    const { location_id } = useRoute().params

    import { ref } from 'vue'
    const users = ref([])

    // Используем useFetch для получения данных с сервера
    const { data } = await useFetch('http://localhost:8000/api/users', {
        method: 'GET'
    })

    if (data.value) {
        users.value = Object.values(data.value)
    } else {
        console.error("Failed to fetch security cameras")
    }

    // Используем useFetch для получения данных с сервера
    // const { data1 } = await useFetch('http://localhost:8000/api/locations', {
    //     method: 'GET'
    // })

    // if (data.value) {
    //     users.value = Object.values(data1.value)
    // } else {
    //     console.error("Failed to fetch security cameras")
    // }

</script>
