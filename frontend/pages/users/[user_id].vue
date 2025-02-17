<template>
    <h2
    class="text-center my-10">
        {{ user_id }}
    </h2>
    <v-sheet
    class="pa-4 text-center mx-auto text-black"
    elevation="12"
    max-width="600"
    rounded="lg"
    width="100%"
    border="lg opacity-15"
    >
    </v-sheet>
</template>

<script setup>
    const { user_id } = useRoute().params
</script>