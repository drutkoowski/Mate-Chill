<template>
  <v-pagination
    :model="pageNum"
    class="my-4"
    :length="length"
    size="small"
    total-visible="5"
    @update:modelValue="this.$emit('pageChange', $event)"
  />
</template>

<script>
export default {
  name: "Paginator",
  props: {
    pageNum: Number,
    length: Number,
  },
};
</script>

<style scoped lang="scss"></style>
