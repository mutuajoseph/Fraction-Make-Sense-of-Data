<template>
  <div id="visualization">
    <v-card class="px-4 py-4" v-if="!xData && !yData && !x2Data">
      <p class="text-center">Getting Data</p>
      <v-progress-linear
        color="deep-purple accent-4"
        :active="loading"
        :indeterminate="loading"
        rounded
        height="6"
      ></v-progress-linear>
    </v-card>
    <div v-else>
      <Chart :xData="xData" :yData="yData" :x2Data="x2Data" />
    </div>
  </div>
</template>

<script>
import Chart from "../components/Chart.vue";
import { mapActions, mapState } from "vuex";
export default {
  components: {
    Chart,
  },
  computed: {
    ...mapState({
      loading: state => state.loading
    }),
    xData() {
      // this.xData = this.$store.state.groupedData.labels
      return this.$store.state.groupedData.labels;
    },

    yData() {
      return this.$store.state.groupedData.total_sales;
    },

    x2Data() {
      return this.$store.state.groupedData.total_cogs;
    },
  },

  mounted() {
    this.FETCH_GROUPED_DATA();
  },


  methods: {
    ...mapActions(["FETCH_GROUPED_DATA"]),
  },
};
</script>

<style></style>
