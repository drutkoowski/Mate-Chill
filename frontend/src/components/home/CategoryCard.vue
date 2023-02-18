<template>
  <div>
    <router-link
      :to="{
        name: 'products',
        query: {
          category: category.name,
        },
      }"
    >
      <img :src="category.url" :alt="category.name" />
      <p class="text-center mt-10">{{ category.name }}</p></router-link
    >
  </div>
</template>

<script>
export default {
  name: "CategoryCard",
  props: {
    category: Object,
  },
  data: () => ({
    show: false,
  }),
  methods: {
    slugify(string) {
      return string
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, "")
        .replace(/[\s_-]+/g, "-")
        .replace(/^-+|-+$/g, "");
    },
  },
};
</script>

<style scoped lang="scss">
div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  cursor: pointer;
  transition: all 0.3s ease-in;

  &:hover {
    transform: scale(1.05);
  }
  img {
    height: 15rem;
    width: 15rem;
  }
  p {
    color: var(--primary-white);
  }
}
</style>
