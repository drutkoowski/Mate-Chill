import axios from "axios";
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";

const axiosConfigResponse = axios.interceptors.response.use(
  function (response) {
    if (response.status === 401) {
      const userStore = useUserStore();
      const toastStore = useToastStore();
      toastStore.displayToast("Wylogowano automatycznie.", "#E85959FF");
      this.router.push({ name: "home" });
      userStore.isAuthenticated = false;
    }
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigResponse;
