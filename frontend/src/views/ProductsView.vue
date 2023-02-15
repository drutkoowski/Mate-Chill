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
            multiple
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Kategorie'"
            v-model="category.value.value"
            :items="mainCategories.map((item) => item.name)"
          />
        </div>
        <div class="filter-element" v-if="category.value.value">
          <filterInput
            :type="'select'"
            :text="`Podkategorie
           ${category.value.value}`"
            v-model="subCategory.value.value"
            :items="getSubCategories(category.value.value)"
            multiple
          />
        </div>
        <div class="filter-element">
          <filterInput
            :type="'select'"
            :text="'Gramatura'"
            :items="['25g', '50g', '250g', '500g', '1000g', 'większe']"
            v-model="grams.value.value"
            multiple
          />
        </div>
        <div class="products-container__filters__buttons">
          <Button :text="'Szukaj'" class="button" type="submit" />
          <Button
            :text="'Wyczyść'"
            class="button"
            @click.prevent="handleClear"
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
              v-model="query"
              ><template v-slot:append-inner>
                <v-icon
                  color="#04b60e"
                  size="large"
                  @click.prevent="submitSearch"
                  @keyup.enter="submitSearch"
                  >mdi-magnify</v-icon
                >
              </template></v-text-field
            >
          </div>
          <div
            class="products-container__products__container__indicators--sorting"
          >
            <v-select
              bg-color="white"
              label="Sortuj"
              :items="['Cena rosnąco', 'Cena malejąco']"
              @update:modelValue="setSorting"
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
          <div
            v-if="products.length === 0"
            class="products-container__products__container__wrapper__no-results"
          >
            <img src="/no-results.svg" alt="No results icon" />
            <h3 class="text-center my-10">
              Niestety, nie znaleziono wyników spełniających Twoje wymogi.
            </h3>
          </div>
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
    const subCategory = useField("subcategory");
    const grams = useField("grams");
    const submit = handleSubmit(async function (values) {
      const manufacturerString = values.manufacturer
        ? values.manufacturer.toString()
        : values.manufacturer;
      const categoryString = values.category
        ? values.category.toString()
        : values.category;
      const subCategoryString = values.subcategory
        ? values.subcategory.toString()
        : values.subcategory;
      const gramsString = values.grams ? values.grams.toString() : values.grams;
      return {
        minPrice: values.minPrice,
        maxPrice: values.maxPrice,
        manufacturer: manufacturerString,
        category: categoryString,
        subcategory: subCategoryString,
        grams: gramsString,
      };
    });
    return {
      minPrice,
      maxPrice,
      manufacturer,
      grams,
      category,
      subCategory,
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
      products: [],
      pagination_count: 0,
      manufacturers: [],
      categories: [],
      mainCategories: [],
      query: "",
    };
  },
  async beforeMount() {
    try {
      const manufacturers = await axios.get("manufacturers/");
      const categories = await axios.get("categories/");
      this.manufacturers = manufacturers.data.map((item) => item.name);
      this.categories = categories.data;
      this.mainCategories = categories.data.filter(
        (item) => item.subcategories.length > 0
      );
      // categories.data.some((item) => item.name === this.$route.query.category)
      let products;
      if (this.$route.query) {
        products = await this.fetchData(this.$route.query, "products/");
        this.category.value.value = this.$route.query.category;
        this.subCategory.value.value = this.$route.query?.subcategory;
      } else {
        products = await this.fetchData({}, "products/");
      }
      this.fillCards(products);
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    submitSearch() {
      let queryParams = this.$route.query;
      this.$router.replace({
        query: { ...queryParams, q: this.query },
      });
      this.query = "";
    },
    setSorting(value) {
      let query = this.$route.query;
      this.$router.replace({
        query: { ...query, sorting: value === "Cena rosnąco" ? 0 : 1 },
      });
    },
    handleClear(event) {
      this.handleReset(event);
      this.$router.replace({ query: {} });
    },
    async submitFilters(event) {
      const params = await this.submit(event);
      this.$router.replace({ query: params });
    },
    async fetchData(filters, url = "products/") {
      return await axios.get(url, { params: filters });
    },
    fillCards(response) {
      this.pagination.nextUrl = response.data.next;
      this.pagination.prevUrl = response.data.previous;
      this.products = response.data.results;
      this.pagination_count = response.data.count;
      this.pagination.maxPages = Math.ceil(this.pagination_count / 8);
    },
    async paginate(page) {
      let url;
      if (page > this.pagination.page) {
        url = this.pagination.nextUrl;
      } else if (page <= this.pagination.page) {
        url = this.pagination.prevUrl;
      }
      try {
        const response = await this.fetchData({}, url);
        this.fillCards(response);
      } catch (error) {
        console.log(error);
      }
    },
    getSubCategories(name) {
      return this.categories
        .filter((item) => item.name === name)[0]
        ["subcategories"].map((item) => item.name);
    },
  },
  watch: {
    async $route(route) {
      this.category.value.value = route.query?.category;
      this.subCategory.value.value = route.query?.subcategory;
      const response = await this.fetchData(route.query);
      this.fillCards(response);
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
      &__no-results {
        grid-row: 1/-1;
        grid-column: 1/-1;
        img {
          width: 15rem;
          height: 15rem;
          margin: 0 auto;
        }
      }
    }
    &__indicators {
      display: flex;
      column-gap: 2rem;
      &--search {
        flex-grow: 1;
      }
      &--sorting {
        width: 15rem;
      }
    }
  }
  &__paginator {
    background-color: var(--color-background);
  }
}
</style>
