<template>
  <v-select
    :label="text"
    :items="items"
    v-model="selectValue"
    bg-color="white"
    @update:modelValue="redirect"
  />
</template>

<script>
export default {
  name: "variationFilter",
  data() {
    return {
      selectValue: null,
    };
  },
  props: {
    text: String,
    items: Array,
  },
  methods: {
    redirect(e) {
      this.selectValue = null;
      this.$emit("handleRedirect", e);
    },
  },
};
</script>

<style scoped></style>
