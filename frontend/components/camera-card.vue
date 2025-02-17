<template>
    <v-card
        elevation="12"
        class="mx-5 my-5"
        height="350"
        width="350"
        v-for="camera in security_cameras"
        :key="camera.id"
    >
        <v-img
            src="./../public/Immersive_Zone_Fone0.png"
        >
        <v-card-title
            class="text-grey">
            {{ camera.name }}
        </v-card-title>
        </v-img>
        <v-card-subtitle>
            {{ camera.description }}
        </v-card-subtitle>
        <div class="mx-5">
            Status: {{ camera.status }}
            <br>
            IP: {{ camera.ip }}
        </div>
        <v-card-actions>
            <NuxtLink :to="`/security/camera-${camera.ip}`">
                <v-btn variant="tonal">
                    Open camera
                </v-btn>
            </NuxtLink>
        </v-card-actions>
    </v-card>
</template>

<script setup>
    import { ref } from 'vue'
    const security_cameras = ref([])

    // Используем useFetch для получения данных с сервера
    const { data } = await useFetch('http://localhost:8000/api/security_cameras', {
        method: 'GET'
    })

    if (data.value) {
        security_cameras.value = Object.values(data.value)
    } else {
        console.error("Failed to fetch security cameras")
    }
</script>
