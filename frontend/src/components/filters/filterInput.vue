<template>
  <v-select v-if="type === 'select'" :label="text" :items="items" multiple />
  <v-text-field :type="type" :label="text" v-else />
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
