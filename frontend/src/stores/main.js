import { defineStore } from "pinia";
import cookies from "@/utils/cookies";

export default defineStore("main", {
  state: () => ({
    isLoading: false,
    isPolicyAccepted: false,
    cartItems: [],
  }),
  actions: {
    on() {
      this.isLoading = true;
    },
    off() {
      setTimeout(() => {
        this.isLoading = false;
      }, 1200);
    },
    acceptPolicy() {
      this.isPolicyAccepted = true;
    },
    setCartItems(items) {
      this.cartItems = items;
    },
    getCartItems() {
      const cartCookie = cookies.getCookie("cartItems");
      this.cartItems = cartCookie ? JSON.parse(cartCookie) : [];
    },
    clearCartItems() {
      this.cartItems = [];
    },
  },
});
