<template>
    <div>
        <header
        align="center"
        class="my-2"
        >
            
            <v-btn @click="toggleTheme"            
                class="mx-10 my-auto"
                rounded="LG"
                elevation="0"
                size="large"
            >toggle theme
            </v-btn>

            <NuxtLink to="/">
                <v-btn
                    class="mx-10 my-auto"
                    rounded="LG"
                    elevation="0"
                    variant="tonal"
                    size="large"
                    color="orange"
                >
                    Home
                </v-btn>
            </NuxtLink>
            <header_menu/>
        </header>

        <div class="container py-5">
            <slot />
        </div>

        <footer
        class="my-5">
            <v-divider :thickness="1"></v-divider>
            <div class="d-flex flex-wrap justify-space-evenly">
                <v-card
                    title="Contact info:"
                    width="350"
                    elevation="12"
                    class="mx-10 my-5 pb-5 px-5"
                >
                    <v-divider :thickness="3" class="my-2"></v-divider>
                    number: +7(***)***-**-** <br>
                    email: firewatch@org.com <br>
                    address: ----------
                </v-card>
            </div>
        </footer>
    </div>
</template>

<script setup>
import { useTheme } from 'vuetify'
import Header_menu from '~/components/header_menu.vue';

const theme = useTheme()

function toggleTheme () {
  theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
}

</script>