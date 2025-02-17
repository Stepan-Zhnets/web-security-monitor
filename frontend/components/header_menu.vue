<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-btn
                icon="mdi-dots-vertical"
                variant="text"
                v-bind="props"
            ></v-btn>
        </template>

        <v-list>
            <v-list-item
                v-for="item in items_menu"
                :key="item.id"
            >
                <v-list-item-title>
                    <NuxtLink :to="`${item.link}`">
                        <v-btn
                            rounded="LG"
                            elevation="0"
                            variant="tonal"
                            :color="`${item.color}`"
                        >
                            {{ item.name }}
                        </v-btn>
                    </NuxtLink>
                </v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script setup>
    import { NuxtLink } from '#components'
import { ref } from 'vue'
    const items_menu = ref([])

    // Используем useFetch для получения данных с сервера
    const { data } = await useFetch('http://localhost:8000/api/items_menu', {
        method: 'GET'
    })

    if (data.value) {
        items_menu.value = Object.values(data.value)
    } else {
        console.error("Failed to fetch security cameras")
    }
</script>
