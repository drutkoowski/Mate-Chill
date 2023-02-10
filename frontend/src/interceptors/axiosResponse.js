import axios from "axios";

const axiosConfigResponse = axios.interceptors.response.use(
  function (response) {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigResponse;
