<template>
  <div class="lower-nav__wrapper">
    <ul>
      <ExpandableCard
        v-for="category in categories"
        :key="category"
        :text="category.name"
        :items="category.subcategories"
      />
    </ul>
  </div>
</template>

<script>
import ExpandableCard from "./ExpandableCard.vue";
import axios from "axios";
export default {
  name: "LowerNav.vue",
  data() {
    return {
      isExpanded: false,
      categories: [],
    };
  },
  async beforeMount() {
    const response = await axios.get("categories/main");
    this.categories = response.data;
  },
  components: {
    ExpandableCard,
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
