<template>
  <div v-if="isDisplayed">
    <ul>
      <li v-for="element in elements" :key="element">{{ element }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ExpandableCard.vue",
  props: ["isDisplayed", "elements"],
};
</script>

<style scoped lang="scss"></style>
