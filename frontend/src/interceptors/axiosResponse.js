import axios from "axios";
import useUserStore from "@/stores/user";

const axiosConfigResponse = axios.interceptors.response.use(
  function (response) {
    if (response.status === 401) {
      const userStore = useUserStore();
      userStore.isAuthenticated = false;
    }
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigResponse;
