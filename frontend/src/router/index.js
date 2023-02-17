import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import ProductsView from "@/views/ProductsView.vue";
import ProductDetailView from "@/views/ProductDetailView.vue";
import useMainStore from "@/stores/main";
import useUserStore from "@/stores/user";
import CartView from "@/views/CartView.vue";
import OrderView from "@/views/OrderView.vue";

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
    {
      path: "/koszyk",
      name: "cart",
      component: CartView,
    },
    {
      path: "/zamowienie",
      name: "order",
      component: OrderView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/:catchAll(.*)*",
      redirect: { name: "home" },
    },
  ],
});
router.beforeResolve((to, from, next) => {
  // If this isn't an initial page load.

  if (to.name) {
    const store = useMainStore();
    store.on();
    // Start the route progress bar.
  }
  next();
});

router.beforeEach(async (to, from, next) => {
  if (!to.meta.requiresAuth) {
    next();
    return;
  }
  const userStore = useUserStore();
  await userStore.checkAuth();
  if (!userStore.isAuthenticated) {
    next({ name: "home" });
  }
  next();
});

router.afterEach(() => {
  // Complete the animation of the route progress bar.

  const store = useMainStore();
  store.off();
});

export default router;
