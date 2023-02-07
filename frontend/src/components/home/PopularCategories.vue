<template>
  <div class="wrapper">
    <h1 class="text-center mt-20 mb-10 text-5xl">Popularne Kategorie</h1>
    <div class="category-container">
      <CategoryCard
        v-for="category in categories"
        :key="category"
        :category="category"
      />
    </div>
  </div>
</template>

<script>
import CategoryCard from "@/components/home/CategoryCard.vue";
export default {
  name: "PopularCategories",
  props: {
    categories: Array,
  },
  components: {
    CategoryCard,
  },
};
</script>

<style scoped lang="scss">
h1 {
  color: var(--primary-white);
}

.wrapper {
  display: grid;
  grid-template-columns: 0.15fr 1fr 0.15fr;
  h1 {
    grid-column: 2/3;
    grid-row: 1/2;
  }
  .category-container {
    grid-column: 2/3;
    grid-row: 2/3;
    display: flex;
    justify-content: space-between;
    margin-top: 5rem;
  }
}
</style>
