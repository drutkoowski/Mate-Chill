import { defineStore } from "pinia";

export default defineStore("main", {
  state: () => ({
    isLoading: false,
    isPolicyAccepted: false,
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
