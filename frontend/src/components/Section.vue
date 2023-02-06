<template>
  <div class="wrapper">
    <div class="section-container">
      <SectionCard />
      <SectionCard />
      <SectionCard />
      <SectionCard />
    </div>
  </div>
</template>

<script>
import SectionCard from "./SectionCard.vue";
export default {
  // eslint-disable-next-line vue/no-reserved-component-names
  name: "Section",
  components: {
    SectionCard,
  },
};
</script>

<style scoped lang="scss">
.wrapper {
  display: grid;
  grid-template-columns: 0.15fr 1fr 0.15fr;
  margin-top: 5rem;
}
.section-container {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: repeat(4, 1fr);
  grid-column: 2/3;
}
</style>
