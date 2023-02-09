import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import ProductsView from "@/views/ProductsView.vue";
import ProductDetailView from "@/views/ProductDetailView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/produkty",
      name: "products",
      component: ProductsView,
    },
    {
      path: "/produkty/:productSlug",
      name: "product-detail",
      params: true,
      component: ProductDetailView,
    },
  ],
});

export default router;
