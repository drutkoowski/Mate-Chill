<template>
  <!--	navbar-->
  <Navbar @openModalLogin="openModalLogin" @openModalSignup="openModalSignup" />

  <!--	view-->
  <RouterView />

  <!--  account actions modal-->
  <ModalOverlay
    v-if="modalLoginVisible || modalSignupVisible"
    @closeModal="closeModal"
  >
    <LoginModal v-if="modalLoginVisible" @closeModal="closeModal" />
    <SignupModal v-if="modalSignupVisible" @closeModal="closeModal" />
  </ModalOverlay>

  <!--  toast-->
  <Toast />

  <!--  loader-->
  <PageOverlay v-if="mainStore.isLoading">
    <v-progress-circular indeterminate color="green" size="50" width="4" />
  </PageOverlay>
</template>

<script>
import Navbar from "@/components/navbar/Navbar.vue";
import ModalOverlay from "@/components/ModalOverlay.vue";
import PageOverlay from "@/components/PageOverlay.vue";
import LoginModal from "./components/login/LoginModal.vue";
import SignupModal from "@/components/signup/SignupModal.vue";
import Toast from "@/components/Toast.vue";
import useMainStore from "@/stores/main";
import userAuth from "@/utils/userAuth";

export default {
  name: "App",
  setup() {
    const mainStore = useMainStore();
    mainStore.getCartItems();
    return { mainStore };
  },
  async created() {
    await userAuth.getCurrentUser();
  },
  data() {
    return {
      modalLoginVisible: false,
      modalSignupVisible: false,
    };
  },
  components: {
    LoginModal,
    ModalOverlay,
    Navbar,
    SignupModal,
    Toast,
    PageOverlay,
  },
  methods: {
    openModalLogin() {
      this.modalLoginVisible = true;
      this.modalSignupVisible = false;
    },
    openModalSignup() {
      this.modalSignupVisible = true;
      this.modalLoginVisible = false;
    },
    closeModal() {
      this.modalSignupVisible = false;
      this.modalLoginVisible = false;
    },
  },
};
</script>

<style scoped lang="scss">
@import "./assets/utils.scss";
</style>
