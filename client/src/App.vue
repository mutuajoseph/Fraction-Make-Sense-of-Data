<template>
  <v-app>
    <v-app-bar dense app color="#006d77" dark>
      <v-toolbar-title class="text-subtitle-1"
        >Fraction Financial Data Analytics</v-toolbar-title
      >
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
