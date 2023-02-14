<template>
  <v-menu open-on-hover>
    <template v-slot:activator="{ props }">
      <li v-bind="props">
        <router-link
          :to="{
            name: 'products',
            query: {
              category: text,
            },
          }"
          >{{ text }}</router-link
        >
      </li>
    </template>
    <div class="card-container">
      <router-link
        v-for="(item, index) in items"
        :key="index"
        :to="{
          name: 'products',
          query: {
            category: text,
            subcategory: item.name,
          },
        }"
        >{{ item.name }}</router-link
      >
    </div>
  </v-menu>
</template>

<script>
export default {
  name: "ExpandableCard",
  props: {
    text: String,
    items: Object,
  },
};
</script>

<style scoped lang="scss">
li {
  transition: all 0.3s ease-in;
  cursor: pointer;
  &:hover {
    transform: scale(1.03);
    color: var(--primary-green);
  }
}
.card-container {
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(1, 1fr);
  background-color: var(--primary-white);
  padding: 1rem 2rem;
  border-radius: 5px;
  color: var(--color-background);
  p {
    cursor: pointer;
    &:hover {
      color: var(--primary-green);
    }
  }
}
</style>
