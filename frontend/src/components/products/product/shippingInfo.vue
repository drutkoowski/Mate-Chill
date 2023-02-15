<template>
  <div class="shipping-wrapper">
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-calendar</v-icon> 14 dni na darmowy zwrot
    </div>
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-shield-check</v-icon> Bezpieczne zakupy
    </div>
    <div class="shipping-wrapper__element">
      <v-icon color="#04b60e">mdi-truck</v-icon> Darmowa przesyłka dla zamówień
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
  &__element {
    display: table-row;
    vertical-align: center;
  }
}
</style>
