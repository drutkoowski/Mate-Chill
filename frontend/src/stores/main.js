import { defineStore } from "pinia";
import cookies from "@/utils/cookies";

export default defineStore("main", {
  state: () => ({
    isLoading: false,
    isPolicyAccepted: false,
    cartItems: JSON.parse(cookies.getCookie("cartItems")) || [],
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
  },
});
