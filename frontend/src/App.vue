<template>
  <Navbar @openModal="openModal" />
  <RouterView />
  <ModalOverlay
    v-if="modalLoginVisible || modalSignupVisible"
    @closeModal="closeModal"
  >
    <LoginModal v-if="modalLoginVisible" />
    <SignupModal v-if="modalSignupVisible" />
  </ModalOverlay>
</template>

<script>
import Navbar from "@/components/navbar/Navbar.vue";
import ModalOverlay from "@/components/ModalOverlay.vue";
import LoginModal from "./components/login/LoginModal.vue";
import SignupModal from "@/components/signup/SignupModal.vue";

export default {
  name: "App",
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
  },
  methods: {
    openModal(type) {
      type === "login"
        ? (this.modalLoginVisible = true)
        : (this.modalSignupVisible = true);
    },
    closeModal() {
      this.modalSignupVisible = false;
      this.modalLoginVisible = false;
    },
  },
};
</script>

<style scoped></style>
