<template>
  <v-select
    :label="text"
    :items="items"
    bg-color="white"
    @update:modelValue="redirect"
  />
</template>

<script>
export default {
  name: "variationFilter",
  props: {
    text: String,
    items: Array,
  },
  methods: {
    redirect(e) {
      this.$emit("handleRedirect", e);
    },
  },
};
</script>

<style scoped></style>
