<template>
  <div id="Homepage">
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="3">
          <Sidebar />
        </v-col>
        <v-col cols="12" md="9">
          <router-view></router-view>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
export default {
  name: "Home",
  components: {
    Sidebar,
  },
};
</script>
