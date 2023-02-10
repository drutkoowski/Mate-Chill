import axios from "axios";
import useUserStore from "@/stores/user";
export default {
  async getCurrentUser() {
    const response = await axios.get("me/");
    const store = useUserStore();
    if (response.status === 200) {
      store.isAuthenticated = true;
      return;
    }
    store.isAuthenticated = false;
  },
  async logoutUser() {
    const response = await axios.post("auth/logout/");
    if (response.status === 200) {
      const store = useUserStore();
      store.isAuthenticated = false;
    }
  },
};
