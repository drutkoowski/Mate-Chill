<template>
  <div class="shipping-wrapper">
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-calendar</v-icon>
      <span>14 dni na darmowy zwrot</span>
    </div>
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-shield-check</v-icon>
      <span>Bezpieczne zakupy</span>
    </div>
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-truck</v-icon>
      <span>Darmowa przesyłka dla zamówień</span>
      +60 zł
    </div>
  </div>
</template>

<script>
export default {
  name: "shippingInfo",
};
</script>

<style scoped lang="scss">
.shipping-wrapper {
  display: table;
  color: var(--primary-white);
  @include respond(phone-md) {
    font-size: 0.75rem;
  }
  &__element {
    display: table-row;
    vertical-align: middle;
    span {
      margin-left: 5px;
    }
    .v-icon {
      margin-top: -5px;
    }
  }
}
</style>
