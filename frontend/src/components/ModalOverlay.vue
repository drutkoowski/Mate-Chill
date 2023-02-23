<template>
  <div
    class="modal-overlay"
    tabindex="0"
    @keydown.esc="$emit('closeModal')"
    ref="modalOverlay"
  >
    <Transition name="fade" appear>
      <div class="modal">
        <slot @closeModal="$emit('closeModal')"></slot>
        <span class="modal__close" @click.prevent="$emit('closeModal')"
          >&#10005;</span
        >
      </div>
    </Transition>
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
  z-index: 1232132112;
  max-width: 100vw;
  max-height: 100vh;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.95);
}

.modal {
  text-align: center;
  position: relative;
  border-radius: 30px;
  background-color: var(--color-background);
  padding: 3rem 5rem;
  -webkit-box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);
  -moz-box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);
  box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);

  @include respond(phone-lg) {
    padding: 1rem 2rem;
  }
  @include respond(phone-sm) {
    padding: 1rem 1rem;
  }

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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
