<template>
  <div>
    <h1 class="text-center">{{ headerText }}</h1>
    <div class="wrapper">
      <div class="section-container">
        <SectionCard v-for="item in items" :key="item.id" :item="item" />
      </div>
    </div>
  </div>
</template>

<script>
import SectionCard from "./SectionCard.vue";
export default {
  // eslint-disable-next-line vue/no-reserved-component-names
  name: "Section",
  props: {
    headerText: String,
    items: Array,
  },
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
  @include respond(md-desktop) {
    grid-template-columns: 1fr;
  }
}
.section-container {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: repeat(4, 1fr);
  grid-column: 2/3;
  grid-column-gap: 2rem;
  @include respond(md-desktop) {
    grid-column: 1/2;
  }
  @include respond(tab-md) {
    grid-template-columns: repeat(2, 1fr);
    grid-row-gap: 3rem;
  }
  @include respond(phone-md) {
    grid-template-columns: 1fr;
  }
}
h1 {
  color: var(--primary-white);
  font-size: 3rem;
  margin-top: 5rem;
  @include respond(tab-sm) {
    font-size: 2rem;
  }
}
</style>
