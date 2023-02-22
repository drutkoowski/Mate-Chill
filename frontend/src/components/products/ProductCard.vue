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
      <h3
        class="text-center products-container__products__container__wrapper__product-card__title"
      >
        {{ product.name }}
      </h3>
      <div
        class="products-container__products__container__wrapper__product-card__image"
        ref="image"
      ></div>
      <div
        class="products-container__products__container__wrapper__product-card__description"
      >
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
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 0.25fr 1fr 0.25fr;
  height: 15rem;
  padding: 5px 10px;
  border: 1px solid var(--primary-green);

  transition: all 0.3s ease-in;
  cursor: pointer;

  &:hover {
    transform: scale(1.05);
  }
  @include respond(tab-md) {
    height: 20rem;
  }
  @include respond(phone-sm) {
    height: 15rem;
  }
  &__title {
    font-weight: bolder;
    @include respond(tab-desktop) {
      font-size: 0.9rem;
    }
    @include respond(phone-md-lg) {
      font-size: 1.2rem;
    }
  }
}
.products-container__products__container__wrapper__product-card__image {
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
}

.products-container__products__container__wrapper__product-card__description {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  div {
    display: flex;
    align-items: center;
    margin-top: auto;
    position: relative;
    .button {
      height: 2rem;
      font-size: 0.85rem;
      margin-left: auto;
      @include respond(tab-desktop) {
        height: 1.75rem;
      }
      @include respond(tab-land) {
        height: 1.5rem;
        font-size: 0.75rem;
      }
      @include respond(phone-md-lg) {
        height: 2.3rem;
        font-size: 1.25rem;
      }
    }
  }
}
small {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 2px 5px;
  color: var(--color-background);
  font-weight: bold;
  font-size: 1.3rem;
  border-radius: 5px;
  @include respond(tab-desktop) {
    font-size: 1.1rem;
    position: unset;
    bottom: unset;
    left: unset;
  }
  @include respond(tab-land) {
    font-size: 1rem;
  }
  @include respond(phone-md-lg) {
    font-size: 1.4rem;
    font-weight: bold;
  }
}
</style>
