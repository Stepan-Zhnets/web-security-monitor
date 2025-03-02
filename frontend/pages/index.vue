<template>
  <div>
            <div align="center">
                <v-img
                    class="my-10"
                    :width="600"
                    aspect-ratio="16/9"
                    cover
                    src="./../public/WSM_Logo.png"
                ></v-img>
            </div>
    <v-sheet
    class="pa-5 text-center mx-auto"
    elevation="12"
    max-width="1350"
    width="100%"
    rounded="lg"
    >
      <NuxtLink to="security">
        <v-btn
          class="mx-10 my-2"
          rounded="LG"
          elevation="0"
          variant="tonal"
          size="x-large"
          color="green"
        >
        Surveillance cameras
        </v-btn>
      </NuxtLink>
      <NuxtLink to="locations_monitor">
        <v-btn
          class="mx-10 my-2"
          rounded="LG"
          elevation="0"
          variant="tonal"
          size="x-large"
          color="orange"
        >
          Locations Monitor
        </v-btn>
      </NuxtLink>
      <NuxtLink to="info">
        <v-btn
          class="mx-10 my-2"
          rounded="LG"
          elevation="0"
          variant="tonal"
          size="x-large"
          color="blue"
        >
          Informations
        </v-btn>
      </NuxtLink>
      <NuxtLink to="users">
        <v-btn
          class="mx-10 my-2"
          rounded="LG"
          elevation="0"
          variant="tonal"
          size="x-large"
          color="lime"
        >
          Users list
        </v-btn>
      </NuxtLink>
    </v-sheet>
  </div>
</template>
  
