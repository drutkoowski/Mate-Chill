<template>
  <v-snackbar
    v-model="store.isActive"
    :timeout="timeout"
    :color="store.color"
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
    timeout: 25000,
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
}
.toast-close {
  position: absolute;
  top: 3%;
  right: 1%;
}
</style>
