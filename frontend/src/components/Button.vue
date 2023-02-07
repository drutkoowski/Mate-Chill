<template>
  <v-btn>{{ text }}</v-btn>
</template>

<script>
export default {
  // eslint-disable-next-line vue/no-reserved-component-names
  name: "Button",
  props: {
    text: String,
  },
};
</script>

<style scoped lang="scss">
.v-btn {
  background-color: var(--primary-green);
  color: var(--primary-white);
  transition: all 0.3s ease-in-out;
  &:hover {
    transform: scale(1.02);
  }
}
</style>
