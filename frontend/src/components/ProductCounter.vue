<template>
  <v-icon
    class="mr-auto icon"
    color="red"
    @click.prevent="itemCounter === 0 ? null : this.$emit('minus')"
    >mdi-minus</v-icon
  >

  <h5 class="text-center font-weight-bold text-h5">
    {{ itemCounter }}
  </h5>

  <v-icon class="ml-auto icon" @click.prevent="this.$emit('plus')"
    >mdi-plus</v-icon
  >
</template>

<script>
export default {
  name: "ProductCounter",
  props: ["itemCounter"],
  emits: ["plus", "minus"],
};
</script>

<style scoped lang="scss">
h5 {
  color: var(--primary-white);
  @include respond(phone-sm) {
    font-size: 0.95rem;
  }
}
.icon {
  transition: all 0.3s ease-in;
  &:hover {
    transform: scale(1.1);
  }
  @include respond(phone-sm) {
    width: 0.5rem;
    height: 0.5rem;
  }
}
</style>
