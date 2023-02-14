<template>
  <router-link
    :to="{
      name: 'product-detail',
      params: {
        productSlug: product.slug,
      },
    }"
  >
    <v-card
      class="mx-auto products-container__products__container__wrapper__product-card"
    >
      <div
        class="products-container__products__container__wrapper__product-card__image"
        ref="image"
      ></div>
      <div
        class="products-container__products__container__wrapper__product-card__description"
      >
        <h3 class="text-center">{{ product.name }}</h3>
        <div>
          <small>{{ product.price }} zł</small
          ><Button :text="'Zobacz'" class="button" type="submit" />
        </div>
      </div>
    </v-card>
  </router-link>
</template>

<script>
import Button from "@/components/Button.vue";
export default {
  name: "ProductCard",
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  props: {
    product: Object,
  },
  mounted() {
    this.$refs.image.style.backgroundImage = `url(${
      import.meta.env.VITE_STATIC_ORGIN + this.product.main_image
    })`;
  },
};
</script>

<style scoped lang="scss">
.products-container__products__container__wrapper__product-card {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;

  padding: 5px 5px;
  border: 1px solid var(--primary-green);

  transition: all 0.3s ease-in;
  cursor: pointer;

  &:hover {
    transform: scale(1.05);
  }
}
.products-container__products__container__wrapper__product-card__image {
  height: 10rem;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
}

.products-container__products__container__wrapper__product-card__description {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  h3 {
    font-size: 0.85rem;
    font-weight: bold;
  }
  div {
    display: flex;
    align-items: center;
    margin-top: auto;
    .button {
      height: 1.5rem;
      font-size: 0.85rem;
      margin-left: auto;
    }
  }
}
small {
  color: var(--primary-red);
  font-weight: bold;
}
</style>
