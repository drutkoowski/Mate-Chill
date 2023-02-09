<template>
  <div class="page-overlay" tabindex="0" ref="pageOverlay">
    <div class="spinner">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageOverlay",
  created() {
    document.body.style.overflow = "hidden!important";
    document.body.style.position = "fixed";
  },
  mounted() {
    this.$refs.pageOverlay.focus();
  },
  unmounted() {
    document.body.style.removeProperty("overflow");
    document.body.style.removeProperty("position");
  },
};
</script>

<style scoped lang="scss">
.page-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  max-width: 100vw;
  max-height: 100vh;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.95);
  z-index: 5005050;
}

.loader {
  text-align: center;
  padding: 3rem 5rem;
  -webkit-box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);
  -moz-box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);
  box-shadow: 0px 0px 17px -14px rgba(255, 255, 255, 1);
}
</style>
