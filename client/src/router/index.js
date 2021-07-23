import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import ViewData from "../views/ViewData";
import Visualization from "../views/Visualization";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "visualization",
        name: "Visualization",
        component: Visualization,
      },
      {
        path: "view-data",
        name: "ViewData",
        component: ViewData,
      },
    ],
  },
  {
    path: "/visualization",
    name: "Visualization",
    component: Visualization,
  },
  {
    path: "/view-data",
    name: "ViewData",
    component: ViewData,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

router.push("/visualization");

export default router;
