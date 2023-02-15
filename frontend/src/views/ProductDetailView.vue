<template>
  <div class="wrapper">
    <div class="product-image-container">
      <ProductGallery :slides="images" />
    </div>
    <div class="product-info-container">
      <h1>{{ item.name }}</h1>
      <div class="product-info-container__rating">
        <v-rating v-model="rating" readonly color="white" />
        <span>3.2/5.00 <span class="text-stone-50">(3 opinie)</span></span>
      </div>
      <div class="product-info-container__description mt-5">
        <p>
          <span class="primary-green">Producent:</span>
          {{ item.manufacturer?.name }}
        </p>
        <p>
          <span class="primary-green">Dostępność:</span>
          {{ item.num_available }}
        </p>
        <p>
          <span class="primary-green">Kraj producenta:</span> {{ item.country }}
        </p>
        <p><span class="primary-green">Opis:</span> {{ item.description }}</p>
      </div>

      <div
        class="product-info-container__customizable"
        v-if="item.variants?.length > 0"
      >
        <variationFilter
          class="mt-2"
          :text="'Warianty'"
          :items="item.variants.map((item) => item.name)"
          @handleRedirect="changeRoute"
        />
      </div>
      <h3 class="product-info-container__price">
        {{ item.price }} <small>zł brutto / szt. </small>
      </h3>
      <div class="product-info-container__actions">
        <div class="product-info-container__actions__counter">
          <v-icon
            class="mr-auto"
            color="red"
            @click.prevent="itemCounter === 0 ? null : itemCounter--"
            >mdi-minus</v-icon
          >

          <h5 class="text-center font-weight-bold text-h5">
            {{ itemCounter }}
          </h5>

          <v-icon class="ml-auto" @click.prevent="itemCounter++"
            >mdi-plus</v-icon
          >
        </div>
        <Button :text="'Dodaj do koszyka'" />
      </div>
      <p class="mt-2">Suma {{ (itemCounter * item.price).toFixed(2) }} zł</p>
      <ShippingInfo />
    </div>
  </div>
</template>

<script>
import ProductGallery from "@/components/products/ProductGallery.vue";
import Button from "@/components/Button.vue";
import axios from "axios";
import VariationFilter from "@/components/filters/variationFilter.vue";
import ShippingInfo from "@/components/products/product/shippingInfo.vue";
export default {
  name: "ProductDetailView",
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { ShippingInfo, VariationFilter, Button, ProductGallery },
  async created() {
    await this.fetchData();
  },
  data: () => ({
    item: {},
    images: [],
    rating: 3,
    itemCounter: 0,
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
    async changeRoute(e) {
      this.$router.push({
        name: "product-detail",
        params: {
          productSlug: this.slugify(e),
        },
      });
    },
    async fetchData() {
      const productSlug = this.$route.params.productSlug;
      const response = await axios.get(`products/${productSlug}`);
      this.item = response.data;
      let images = [this.item.main_image];
      if (this.item.images.length > 0)
        images = [...this.item.images.map((element) => element.image)];
      this.images = images;
    },
  },
  watch: {
    async $route() {
      await this.fetchData();
    },
  },
};
</script>

<style scoped lang="scss">
.wrapper {
  flex-grow: 1;
  display: grid;
  grid-template-columns: 0.7fr 1fr;
  padding: 0 5rem;
  grid-column-gap: 5rem;
  margin-top: 5rem;
}
.product-image-container {
  height: 100%;
  width: 30rem;
  justify-self: center;
}
.product-info-container {
  &__description {
    p {
      margin-top: 0.5rem;
    }
  }

  &__rating {
    display: flex;
    align-items: center;
  }
  &__customizable {
    display: flex;
    align-items: center;
    width: 25rem;
  }
  &__price {
    font-size: 2rem;
    font-weight: bolder;
    color: var(--primary-green);
    small {
      font-weight: normal;
      font-size: 1rem;
      color: var(--primary-white);
    }
  }
  h1 {
    font-size: 2rem;
    font-weight: bold;
    color: var(--primary-green);
  }
  p {
    font-size: 1.2rem;
    color: var(--primary-white);
  }
}

.product-info-container__actions {
  display: flex;
  column-gap: 2rem;
  margin-top: 2rem;
  &__counter {
    display: flex;
    align-items: center;
    height: 3rem;
    width: 7rem;
    border-radius: 5px;
    background-color: var(--white);
    h5 {
      color: var(--color-background);
    }
    .v-icon {
      width: 2rem;
      cursor: pointer;
      transition: all 0.3s ease-in-out;
      &:hover {
        transform: scale(1.15);
      }
    }
  }
  button {
    height: 3rem;
  }
}
</style>
