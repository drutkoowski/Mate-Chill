import { defineStore } from "pinia";
import userAuth from "../utils/userAuth";

export default defineStore("user", {
  state: () => ({
    isAuthenticated: false,
  }),
  actions: {
    async checkAuth() {
      await userAuth.getCurrentUser();
    },
  },
});
