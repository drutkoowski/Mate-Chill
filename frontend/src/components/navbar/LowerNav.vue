<template>
  <div class="lower-nav__wrapper">
    <ul>
      <li @mouseenter="expandCard" @mouseleave="expandCard">
        Yerba Mate
        <ExpandableCard :isDisplayed="isExpanded" :elements="['123', '234']" />
      </li>
      <li>Naczynia</li>
      <li>Bombille</li>
      <li>Zestawy</li>
      <li>Akcesoria</li>
      <li>Kawy</li>
      <li>Herbaty</li>
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
  li {
    transition: all 0.3s ease-in;
    cursor: pointer;
    &:hover {
      transform: scale(1.03);
      color: var(--primary-green);
    }
  }
}
</style>
