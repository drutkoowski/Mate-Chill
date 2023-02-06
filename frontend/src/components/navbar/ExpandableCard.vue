<template>
  <v-menu open-on-hover>
    <template v-slot:activator="{ props }">
      <li v-bind="props">{{ text }}</li>
    </template>
    <v-list>
      <v-list-item v-for="(item, index) in items" :key="index" :value="index">
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: "ExpandableCard",
  props: {
    text: String,
  },
  data: () => ({
    items: [
      { title: "Element 1" },
      { title: "Element 2" },
      { title: "Element 3" },
      { title: "Element 4" },
    ],
  }),
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
</style>
