<template>
  <div>
    <h1 class="text-center mt-20 text-5xl">{{ headerText }}</h1>
    <div class="wrapper">
      <div class="section-container">
        <SectionCard />
        <SectionCard />
        <SectionCard />
        <SectionCard />
      </div>
    </div>
  </div>
</template>

<script>
import SectionCard from "./SectionCard.vue";
export default {
  // eslint-disable-next-line vue/no-reserved-component-names
  name: "Section",
  props: ["headerText"],
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
h1 {
  color: var(--primary-white);
}
</style>
