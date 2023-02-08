<template>
  <v-card
    class="mx-auto products-container__products__container__wrapper__product-card"
  >
    <div class="image" ref="image"></div>
    <h3 class="text-center">{{ name }}</h3>

    <p>{{ price }} zł</p>
  </v-card>
</template>

<script>
export default {
  name: "ProductCard",
  props: {
    name: String,
    price: Number,
    photoUrl: String,
    detailsUrl: String,
  },
  mounted() {
    this.$refs.image.style.backgroundImage = `url(${this.photoUrl})`;
  },
};
</script>

<style scoped lang="scss">
.products-container__products__container__wrapper__product-card {
  height: 100%;
  width: 100%;
  padding: 10px 0;
  -webkit-box-shadow: 0px 0px 13px 2px rgba(208, 205, 205, 1);
  -moz-box-shadow: 0px 0px 13px 2px rgba(208, 205, 205, 1);
  box-shadow: 0px 0px 13px 2px rgba(208, 205, 205, 1);
}
.image {
  height: 70%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
}

h3,
p {
  padding: 0 0.5rem;
}

p {
  float: right;
  color: var(--primary-green);
}
</style>
