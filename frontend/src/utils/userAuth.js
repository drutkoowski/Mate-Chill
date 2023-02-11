import axios from "axios";
import useUserStore from "@/stores/user";
export default {
  async getCurrentUser() {
    try {
      const response = await axios.get("me/");
      const store = useUserStore();
      if (response.status === 200) {
        store.isAuthenticated = true;
        return;
      }
      store.isAuthenticated = false;
    } catch (error) {
      console.log(error);
    }
  },
  async logoutUser() {
    try {
      const response = await axios.post("auth/logout/");
      if (response.status === 200) {
        const store = useUserStore();
        store.isAuthenticated = false;
      }
    } catch (error) {
      console.log(error);
    }
  },
};
