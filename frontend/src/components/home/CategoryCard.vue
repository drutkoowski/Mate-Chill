<template>
  <div>
    <img :src="category.url" :alt="category.name" />
    <p class="text-center mt-10">{{ category.name }}</p>
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
