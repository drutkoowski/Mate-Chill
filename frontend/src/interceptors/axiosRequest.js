import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000" + "/api/";
axios.defaults.withCredentials = true;
// request interceptor
// const axiosConfigRequest = axios.interceptors.request.use(
//   function (config) {
//     // Do something before request is sent
//     return config;
//   },
//   (error) => {
//     return Promise.reject(error);
//   }
// );
// export default axiosConfigRequest;
