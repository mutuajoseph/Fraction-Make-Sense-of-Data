<template>
  <div id="view-data">
    <v-container>
      <div class="csv-button mt-3" title="Download data as csv">
        <JsonCSV
          class="btn btn-default"
          :data="financeData"
          type="csv"
          name="finance-data.csv"
        >
          Export CSV
        </JsonCSV>
      </div>
      <v-card class="mt-2">
        <v-card-title class="header-text">
          Financial <span class="font"> Data</span>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Enter product or department to filter records"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="financeData"
          :search="search"
          :loading="loading"
          loading-text="Loading... Please wait"
          class="header-text"
        ></v-data-table>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import JsonCSV from "vue-json-csv";
export default {
  components: {
    JsonCSV,
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Product Name",
          align: "start",
          sortable: false,
          value: "product",
        },
        { text: "Department", value: "department" },
        { text: "Sales", value: "sales" },
        { text: "COGS", value: "cogs" },
        { text: "Profit", value: "profit" },
      ],
      financeData: [],
    };
  },

  computed: {
    ...mapState({ loading: (state) => state.loading }),
  },

  created() {
    this.FETCH_FINANCIAL_DATA().then((res) => {
      this.financeData = res.data;
    });
  },

  methods: {
    ...mapActions(["FETCH_FINANCIAL_DATA"]),
  },
};
</script>

<style scoped>
.font {
  color: #006d77;
  margin-left: 0.2rem;
}

.header-text {
  font-family: "Ubuntu", sans-serif;
}

.csv-button {
    width: 90px;
    padding: .3rem .7rem;
    cursor: pointer;
    background: #006d77;
    color: #fff;
    font-size: 12px;
    font-family: 'Ubuntu', sans-serif;
    font-weight: 600;
    border-radius: 6px;
}
</style>
