<template>
  <v-select
    v-if="type === 'select'"
    :label="text"
    :items="items"
    :multiple="multiple"
    bg-color="white"
  />
  <v-text-field :type="type" :label="text" bg-color="white" v-else />
</template>

<script>
export default {
  name: "filterInput",
  props: {
    type: {
      type: String,
      default: "text",
    },
    text: String,
    items: Array,
    multiple: {
      type: Boolean,
      default: true,
      required: false,
    },
  },
};
</script>

<style scoped></style>
