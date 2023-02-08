<template>
  <v-select
    v-if="type === 'select'"
    :label="text"
    :items="items"
    multiple
    bg-color="white"
  />
  <v-text-field :type="type" :label="text" bg-color="white" v-else />
</template>

<script>
export default {
  name: "filterInput",
  props: {
    type: String,
    text: String,
    items: Array,
  },
};
</script>

<style scoped></style>
