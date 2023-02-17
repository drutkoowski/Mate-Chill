import axios from "axios";
import useUserStore from "@/stores/user";
export default {
  async getCurrentUser() {
    try {
      const response = await axios.get("me/");
      const store = useUserStore();
      if (response.status === 200) {
        store.isAuthenticated = true;
        store.user = response.data;
        return;
      }
      store.isAuthenticated = false;
      store.user = {};
    } catch (error) {
      console.log(error);
    }
  },
  async logoutUser() {
    try {
      const response = await axios.post("auth/logout/");
      if (response.status === 200) {
        const store = useUserStore();
        store.user = {};
        store.isAuthenticated = false;
      }
    } catch (error) {
      console.log(error);
    }
  },
};
