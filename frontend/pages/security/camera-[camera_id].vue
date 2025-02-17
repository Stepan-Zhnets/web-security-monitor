<template>
    <h2
    class="text-center my-10">
        {{ camera_id }}
    </h2>
    <v-sheet
    class="pa-4 text-center mx-auto text-black"
    elevation="12"
    max-width="600"
    rounded="lg"
    width="100%"
    border="lg opacity-15"
    >
        <v-img
            src="../../public/no-video.png"
            width="100"
            class="text-center mx-auto my-10"
            align="center"
        >
        </v-img>
        <h2>
            Camera
        </h2>
        <h1>
            Disconnect
        </h1>
    </v-sheet>
</template>

<script setup>
    const { camera_id } = useRoute().params
</script>