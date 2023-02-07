<template>
  <div
    class="modal-overlay"
    tabindex="0"
    @keydown.esc="$emit('close-modal')"
    ref="modalOverlay"
  >
    <div class="modal">
      <slot @closeModal="$emit('close-modal')"></slot>
      <span class="modal__close" @click.prevent="$emit('close-modal')"
        >&#10005;</span
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalOverlay",
  created() {
    document.body.style.overflow = "hidden!important";
    document.body.style.position = "fixed";
  },
  mounted() {
    this.$refs.modalOverlay.focus();
  },
  unmounted() {
    document.body.style.removeProperty("overflow");
    document.body.style.removeProperty("position");
  },
};
</script>

<style scoped lang="scss">
.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000000da;
}

.modal {
  text-align: center;
  background-color: var(--white);
  padding: 60px 0;
  border-radius: 20px;
  position: relative;

  &__close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    transition: all 0.3s ease-in;
    cursor: pointer;
    &:hover {
      transform: scale(1.25);
    }
  }
}
</style>
