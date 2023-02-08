import { defineStore } from "pinia";

export default defineStore("toast", {
  state: () => ({
    isActive: false,
    message: "",
    color: "",
  }),
  actions: {
    displayToast(msg, color) {
      this.isActive = true;
      this.message = msg;
      this.color = color;
    },
  },
});
