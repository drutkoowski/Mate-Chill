import axios from "axios";
import userAuth from "@/utils/userAuth";

const axiosConfigResponse = axios.interceptors.response.use(
  async function (response) {
    if (response.status === 401) {
      await userAuth.logoutUser();
    }
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigResponse;
