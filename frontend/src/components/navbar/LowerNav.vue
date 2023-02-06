<template>
  <div class="lower-nav__wrapper">
    <ul>
      <ExpandableCard :text="'Yerba Mate'" />
      <ExpandableCard :text="'Bombille'" />
      <ExpandableCard :text="'Zestawy'" />
      <ExpandableCard :text="'Akcesoria'" />
      <ExpandableCard :text="'Kawy'" />
      <ExpandableCard :text="'Herbaty'" />
    </ul>
  </div>
</template>

<script>
import ExpandableCard from "./ExpandableCard.vue";
export default {
  name: "LowerNav.vue",
  data() {
    return {
      isExpanded: false,
    };
  },
  components: {
    ExpandableCard,
  },
  methods: {
    expandCard(ev) {
      console.log(ev.target);
      this.isExpanded = !this.isExpanded;
    },
  },
};
</script>

<style scoped lang="scss">
.lower-nav__wrapper {
  display: grid;
  grid-template-columns: 0.3fr auto 0.3fr;
}
ul {
  grid-column: 2/3;
  display: inline-flex;
  justify-content: space-between;
  list-style: none;
  color: var(--primary-white);
}
</style>
