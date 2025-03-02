<template>
    <v-card
        elevation="12"
        class="mx-5 my-5"
        height="350"
        width="350"
        v-for="user in users"
        :key="user.id"
    >
        <v-img
            :src="'${user.img}'"
        >
        <v-card-title
            class="text-grey">
            {{ user.name }}
        </v-card-title>
        </v-img>
        <v-card-subtitle>
        </v-card-subtitle>
        <div class="mx-5">
            Status: {{ user.status }}
            <br>
            ID: 
        </div>
        <v-card-actions>
            <NuxtLink :to="`/users/${user.name}`">
                <v-btn variant="tonal">
                    Info
                </v-btn>
            </NuxtLink>
        </v-card-actions>
    </v-card>
</template>

<script setup>
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
</script>
