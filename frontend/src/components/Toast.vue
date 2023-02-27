<template>
  <v-snackbar
    transition="slide-x-reverse-transition"
    v-model="store.isActive"
    :timeout="timeout"
    :color="store.color"
    location="bottom right"
    class="toast"
  >
    <p class="toast-message text-center">{{ store.message }}</p>
    <span class="toast-close" @click.prevent="store.isActive = false"
      >&#10005;</span
    >
  </v-snackbar>
</template>

<script>
import useToastStore from "@/stores/toast";

export default {
  name: "Toast",
  props: ["color", "text"],
  data: () => ({
    snackbar: false,
    timeout: 5000,
  }),
  setup() {
    const store = useToastStore();
    return { store };
  },
};
</script>

<style scoped lang="scss">
.toast {
  position: relative;
}

.toast-message {
  font-size: 1rem;
  @include respond(phone-lg) {
    font-size: 0.75rem;
  }
}
.toast-close {
  position: absolute;
  top: 3%;
  right: 1%;
  cursor: pointer;
}

::v-deep .v-snackbar__wrapper {
  @include respond(phone-lg) {
    min-width: 200px !important;
  }
}
</style>
