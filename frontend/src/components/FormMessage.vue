<template>
  <p class="text-center text-red-500">{{ text }}</p>
</template>

<script>
export default {
  name: "FormMessage",
  props: {
    text: String,
  },
};
</script>

<style scoped lang="scss">
p {
  min-height: 1.35rem;
}
</style>
