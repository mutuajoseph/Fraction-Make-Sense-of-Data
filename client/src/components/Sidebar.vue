<template>
  <div id="sidebar">
    <v-card shaped class="mx-auto mt-4" width="200" height="400">
      <v-navigation-drawer dark width="200" color="#006d77">
        <v-list shaped>
          <v-list-item-group v-model="model">
            <v-list-item link v-for="(item, i) in items" :key="i" :title="item.title">
              <v-list-item-icon>
                <v-icon small v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content @click="change_route(item.link)">
                <v-list-item-title class="font">{{
                  item.text
                }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: [
        {
        icon: "assessment",
        text: "Visualization",
        link: { name: "Visualization" },
        title: "View data visualization"
      },
      {
        icon: "mdi-inbox",
        text: "Financial Data",
        link: { name: "ViewData" },
        title: "View Data table"
      }
    ],
    model: 0,
  }),

  methods: {
    change_route(object) {
      // eslint-disable-next-line handle-callback-err
      this.$router.push(object).catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.font {
  font-family: "Ubuntu", sans-serif;
  font-size: 14px;
}

.back {
  background: #006d77;
}
</style>
