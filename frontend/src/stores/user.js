import { defineStore } from "pinia";
import userAuth from "../utils/userAuth";

export default defineStore("user", {
  state: () => ({
    isAuthenticated: false,
    user: {},
  }),
  actions: {
    async checkAuth() {
      await userAuth.getCurrentUser();
    },
  },
});
