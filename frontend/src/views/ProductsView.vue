<template>
  <div class="products-container">
    <div class="products-container__filters">
      <form ref="form" lazy-validation @submit.prevent="submitFilters">
        <div class="filter-element">
          <filterInput
            :type="'number'"
            :text="'Cena od'"
            v-model="minPrice.value.value"
          />
          <filterInput
            :type="'number'"
            :text="'Cena do'"
            v-model="maxPrice.value.value"
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Producent'"
            v-model="manufacturer.value.value"
            :items="manufacturers"
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Kategorie'"
            v-model="category.value.value"
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
            v-model="grams.value.value"
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
      </form>
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
        <small class="mb-2">{{ pagination_count }} wyszukanych produktów</small>
        <div class="products-container__products__container__wrapper">
          <ProductCard
            v-for="product in products"
            :key="product.id"
            :product="product"
          />
        </div>
      </div>
      <div class="products-container__products__paginator">
        <Paginator
          :pageNum="pagination.page"
          :length="pagination.maxPages"
          @pageChange="paginate"
        />
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
import { useField, useForm } from "vee-validate";

export default {
  name: "ProductsView",
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    filterInput,
    Paginator,
    ProductCard,
  },
  setup() {
    const { handleSubmit, handleReset } = useForm({});
    const minPrice = useField("minPrice");
    const maxPrice = useField("maxPrice");
    const manufacturer = useField("manufacturer");
    const category = useField("category");
    const grams = useField("grams");
    const submit = handleSubmit(async function (values) {
      const manufacturerString = values.manufacturer
        ? values.manufacturer.toString()
        : values.manufacturer;
      const categoryString = values.category
        ? values.category.toString()
        : values.category;
      const gramsString = values.grams ? values.grams.toString() : values.grams;
      return await axios.get("products/", {
        params: {
          minPrice: values.minPrice,
          maxPrice: values.maxPrice,
          manufacturer: manufacturerString,
          category: categoryString,
          grams: gramsString,
        },
      });
    });
    return {
      minPrice,
      maxPrice,
      manufacturer,
      grams,
      category,
      submit,
      handleReset,
    };
  },
  data() {
    return {
      pagination: {
        page: 1,
        maxPages: 1,
        prevUrl: "",
        nextUrl: "",
      },
      filters: {
        min: "",
        max: "",
        category: "",
        manufacturer: "",
        grams: "",
      },
      products: [],
      pagination_count: 0,
      manufacturers: [],
    };
  },
  async beforeMount() {
    try {
      const products = await axios.get("products/");
      const categories = await axios.get("categories/");
      this.manufacturers = categories.data.map((item) => item.name);
      this.fillCards(products);
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    async submitFilters(event) {
      const response = await this.submit(event);
      this.fillCards(response);
    },
    resetFilters() {
      this.$refs.form.reset();
    },
    fillCards(response) {
      this.pagination.nextUrl = response.data.next;
      this.pagination.prevUrl = response.data.previous;
      this.products = response.data.results;
      this.pagination_count = response.data.count;
      this.pagination.maxPages = Number(this.pagination_count % 8) + 1;
    },
    async paginate(page) {
      let url;
      if (page > this.pagination.page) {
        url = this.pagination.nextUrl;
      } else if (page <= this.pagination.page) {
        url = this.pagination.prevUrl;
      }
      try {
        const response = await axios.get(url);
        this.fillCards(response);
      } catch (error) {
        console.log(error);
      }
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
