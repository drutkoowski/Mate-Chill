import axios from "axios";

axios.defaults.baseURL = import.meta.env.VITE_DEVELOPMENT_API_URL;
axios.defaults.withCredentials = true;

const axiosConfigRequest = axios.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigRequest;
