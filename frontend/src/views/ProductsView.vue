<template>
  <div class="products-container">
    <div class="products-container__filters">
      <v-form ref="form" lazy-validation>
        <div class="filter-element">
          <filterInput :type="'number'" :text="'Cena od'" />
          <filterInput :type="'number'" :text="'Cena do'" />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Producent'"
            :items="['Guarani', 'Verde Mate']"
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Kategorie'"
            :items="['Yerba Mate', 'Dla par', 'Na początek']"
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Gramatura'"
            :items="[
              'mniejsza',
              'do 250g',
              'do 500g',
              'do 1kg',
              '2kg i większe',
            ]"
          />
        </div>
        <div class="products-container__filters__buttons">
          <Button :text="'Szukaj'" class="button" type="submit" />
          <Button
            :text="'Wyczyść'"
            class="button"
            @click.prevent="resetFilters"
          />
        </div>
      </v-form>
    </div>
    <div class="products-container__products">
      <div class="products-container__products__container">
        <div class="products-container__products__container__indicators">
          <div
            class="products-container__products__container__indicators--search"
          >
            <v-text-field
              bg-color="white"
              label="Wyszukaj produkt"
              append-inner-icon="mdi-magnify"
            />
          </div>
          <div
            class="products-container__products__container__indicators--sorting"
          >
            <v-select
              bg-color="white"
              label="Sortuj"
              :items="['Cena rosnąco', 'Cena malejąco ']"
            />
          </div>
        </div>
        <small class="mb-2">{{ products.length }} wyszukanych produktów</small>
        <div class="products-container__products__container__wrapper">
          <ProductCard
            v-for="product in products"
            :key="product.id"
            :product="product"
          />
        </div>
      </div>
      <div class="products-container__products__paginator">
        <Paginator :pageNum="page" :length="maxPages" />
      </div>
    </div>
  </div>
</template>

<script>
import filterInput from "@/components/filters/filterInput.vue";
import Button from "@/components/Button.vue";
import Paginator from "@/components/Paginator.vue";
import ProductCard from "@/components/products/ProductCard.vue";
import axios from "axios";

export default {
  name: "ProductsView",
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    filterInput,
    Paginator,
    ProductCard,
  },
  data() {
    return {
      page: 1,
      maxPages: 15,
      products: [],
    };
  },
  async beforeMount() {
    try {
      const response = await axios.get("products");
      this.products = response.data;
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    resetFilters() {
      this.$refs.form.reset();
    },
  },
};
</script>

<style lang="scss" scoped>
.products-container {
  display: grid;
  grid-template-columns: 0.4fr 1fr;
  grid-column-gap: 5rem;
  width: 100%;

  padding: 0 5rem;
  margin-top: 5rem;
}

.products-container__filters {
  display: flex;
  flex-direction: column;
  height: fit-content;
  padding: 1rem 2rem;
  border-radius: 10px;

  .filter-element {
    display: flex;
    column-gap: 2rem;
  }

  &__buttons {
    display: flex;
    justify-content: center;
    column-gap: 2rem;
    margin-top: 2rem;
  }
}

.products-container__products {
  display: flex;
  flex-direction: column;

  background-color: var(--primary-white);
  border-radius: 10px;
  &__container {
    flex-grow: 1;
    background-color: var(--color-background);
    display: flex;
    flex-direction: column;

    &__wrapper {
      flex-grow: 1;
      display: grid;
      grid-template-rows: repeat(2, 1fr);
      grid-template-columns: repeat(4, 1fr);
      grid-column-gap: 2rem;
      grid-row-gap: 2rem;
      padding: 0.5rem 0.5rem;
    }
    &__indicators {
      display: flex;
      column-gap: 2rem;
      &--search {
        flex-grow: 1;
      }
      &--sorting {
        width: 10rem;
      }
    }
  }
  &__paginator {
    background-color: var(--color-background);
  }
}
</style>
