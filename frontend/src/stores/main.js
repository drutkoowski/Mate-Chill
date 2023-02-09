import { defineStore } from "pinia";

export default defineStore("main", {
  state: () => ({
    isLoading: false,
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
  },
});
