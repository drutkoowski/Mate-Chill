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
    @include respond(tab-md) {
      height: 10rem;
      width: 10rem;
    }
    @include respond(tab-sm) {
      height: 7rem;
      width: 7rem;
    }
    @include respond(phone-lg) {
      height: 5rem;
      width: 5rem;
    }
    @include respond(phone-md-lg) {
      height: 3.5rem;
      width: 3.5rem;
      justify-self: center;
      margin: 0 auto;
    }
  }
  p {
    color: var(--primary-white);
  }
}
</style>
