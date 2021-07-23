import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
    financialData: [],
    groupedData: {},
  },
  mutations: {
    // set loading status
    SET_LOADING_STATUS(state, payload) {
      state.loading = payload;
    },

    // set financial data
    SET_FINANCIAL_DATA(state, payload) {
      state.financialData = payload;
    },

    // set grouped data
    SET_GROUPED_DATA(state, payload) {
      state.groupedData = payload;
    },
  },
  actions: {
    // fetch financial data
    FETCH_FINANCIAL_DATA(context) {
      return new Promise((resolve, reject) => {
        context.commit('SET_LOADING_STATUS', true);
        axios
          .get(`http://127.0.0.1:8000/sample-data`)
          .then((res) => {
            context.commit('SET_LOADING_STATUS', false);
            context.commit('SET_FINANCIAL_DATA', res.data);
            resolve(res);
          })
          .catch((err) => {
            context.commit('SET_LOADING_STATUS', false);
            console.log(err);
            reject(err);
          });
      });
    },

    // fetch grouped data
    FETCH_GROUPED_DATA(context) {
      return new Promise((resolve, reject) => {
        context.commit('SET_LOADING_STATUS', true);
        axios
          .get(`http://127.0.0.1:8000/sample-data/sales`)
          .then((res) => {
            context.commit('SET_LOADING_STATUS', false);
            context.commit('SET_GROUPED_DATA', res.data);
            resolve(res);
          })
          .catch((err) => {
            context.commit('SET_LOADING_STATUS', false);
            console.log(err);
            reject(err);
          });
      });
    },
  },
});
