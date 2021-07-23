<template>
  <div id="charts">
    <p class="text-h6 mt-4">Total sales and COGS per product</p>
    <apexcharts
      width="900"
      height="350"
      type="bar"
      :options="chartOptions"
      :series="series"
    ></apexcharts>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
export default {
  components: {
    apexcharts: VueApexCharts,
  },
  data: function () {
    return {
      chartOptions: {
        chart: {
          id: "basic-bar",
        },
        xaxis: {
          categories: this.xData,
          // categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        },
      },
      series: [
        {
          name: "total-sales",
          data: this.yData,
          // data: [30, 40, 45, 50, 49, 60, 70, 91]
        },
        {
          name: "total-cogs",
          data: this.x2Data
        }
      ],
    };
  },

  props: ["xData", "yData", "x2Data"],
};
</script>

<style>
</style>