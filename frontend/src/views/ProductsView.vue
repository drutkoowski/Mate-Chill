<template>
  <div class="products-container">
    <v-slide-x-transition>
      <div
        class="products-container__filters"
        v-if="isFilterVisible"
        @keyup.esc="isFilterVisible = false"
      >
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
        <span
          class="products-container__filters__close"
          @click.prevent="isFilterVisible = false"
          >&#10005;</span
        >
      </div>
    </v-slide-x-transition>

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
        <div class="products-container__products__container__filters-wrapper">
          <div
            class="products-container__products__container__filters"
            @click.prevent="openFilters"
          >
            <img src="/options.svg" alt="Filters icon" />
            <p>Filtry</p>
          </div>
          <small v-if="queryParamsCount > 0"
            >Aktywne ({{ queryParamsCount }})
            <ul>
              <li v-if="minPrice.value.value">Cena min.</li>
              <li v-if="maxPrice.value.value">Cena maks.</li>
              <li v-if="manufacturer.value.value">Producent</li>
              <li v-if="category.value.value">Kategoria</li>
              <li v-if="subCategory.value.value">Podkategoria</li>
              <li v-if="grams.value.value">Gramatura</li>
            </ul>
          </small>
        </div>

        <small class="mt-2 products-container__products__container__counter"
          >{{ pagination_count }} wyszukanych produktów</small
        >
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
import { ref } from "vue";

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
    const isFilterVisible = ref(false);
    function openFilters() {
      isFilterVisible.value = !isFilterVisible.value;
    }
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
      isFilterVisible.value = false;
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
      isFilterVisible,
      openFilters,
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
      queryParamsCount: 0,
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
      let products;
      if (this.$route.query) {
        products = await this.fetchData(this.$route.query, "products/");
        this.category.value.value = this.$route.query?.category;
        this.subCategory.value.value = this.$route.query?.subcategory;
        this.minPrice.value.value = this.$route.query?.minPrice;
        this.maxPrice.value.value = this.$route.query?.maxPrice;
        this.grams.value.value = this.$route.query?.grams;
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
      this.isFilterVisible = false;
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
      this.pagination.maxPages = Math.ceil(
        this.pagination_count / import.meta.env.VITE_PAGINATION_SIZE
      );
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
      this.minPrice.value.value = route.query?.minPrice;
      this.maxPrice.value.value = route.query?.maxPrice;
      this.grams.value.value = route.query?.grams;
      this.queryParamsCount = Object.keys(route.query).length;
      const response = await this.fetchData(route.query);
      this.fillCards(response);
    },
  },
};
</script>

<style lang="scss" scoped>
.products-container {
  width: 100%;

  padding: 0 5rem;
  margin-top: 2.5rem;
  @include respond(tab-desktop) {
    padding: 0;
  }
}

.products-container__filters {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  background-color: var(--color-background);
  z-index: 2;
  display: flex;
  flex-direction: column;
  padding: 1rem 2rem;
  border-radius: 10px;
  border-right: 3px solid var(--primary-green);
  &__close {
    position: absolute;
    top: 10px;
    right: 20px;
    color: var(--primary-white);
    transform: scale(1.5);
    cursor: pointer;
    transition: all 0.3s ease-in;
    &:hover {
      transform: translateX(5px);
    }
  }
  form {
    margin: auto 0;
    @include respond(tab-port) {
      width: 20rem;
    }
  }
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
    @include respond(phone-lg) {
      margin-top: 2rem;
    }
    &__counter {
      color: var(--primary-white);
    }
    &__wrapper {
      flex-grow: 1;
      display: grid;
      grid-template-rows: repeat(2, 1fr);
      grid-template-columns: repeat(4, 1fr);
      grid-column-gap: 2rem;
      grid-row-gap: 2rem;
      padding: 0.5rem 0;
      @include respond(tab-land) {
        grid-column-gap: 1rem;
      }
      @include respond(tab-md) {
        grid-template-columns: repeat(2, 1fr);
        grid-column-gap: 3rem;
      }
      @include respond(phone-lg) {
        grid-column-gap: 1rem;
      }
      @include respond(phone-md-lg) {
        grid-template-columns: 1fr;
      }
      &__no-results {
        grid-row: 1/-1;
        grid-column: 1/-1;
        img {
          width: 15rem;
          height: 15rem;
          margin: 0 auto;
          @include respond(tab-md) {
            width: 12rem;
            height: 12rem;
          }
          @include respond(tab-sm) {
            margin-top: 5rem;
            width: 10rem;
            height: 10rem;
          }
        }
      }
    }
    &__indicators {
      display: flex;
      column-gap: 2rem;
      @include respond(phone-lg) {
        margin-top: 7rem;
      }
      @include respond(phone-md-lg) {
        column-gap: 0.5rem;
      }
      @include respond(phone-md-sm) {
        flex-direction: column;
      }
      &--search {
        flex-grow: 1;
      }
      &--sorting {
        width: 15rem;
        @include respond(tab-sm) {
          width: 10rem;
        }
        @include respond(phone-md-lg) {
          width: 7rem;
        }
        @include respond(phone-md-sm) {
          width: 10rem;
        }
      }
    }
    &__filters-wrapper {
      display: flex;
      align-items: center;
      column-gap: 2rem;
      @include respond(tab-land) {
        margin: 1rem 0;
      }
      @include respond(tab-md) {
        flex-direction: column;
      }
      div {
        @include respond(tab-md) {
          margin-right: auto;
        }
      }
      small {
        display: flex;
        column-gap: 2rem;
        color: var(--primary-white);
        @include respond(phone-lg) {
          font-size: 1rem !important;
          flex-direction: column;
          margin-top: 1rem;
        }
        ul {
          display: flex;
          column-gap: 1rem;
          color: var(--primary-green);
          @include respond(phone-lg) {
            font-size: 0.6rem !important;
            flex-direction: column;
          }
        }
        @include respond(tab-md) {
          margin-top: 1rem;
          margin-right: auto;
        }
        @include respond(tab-sm) {
          column-gap: 0.5rem;
          font-size: 0.7rem;
        }
        @include respond(phone-lg) {
          font-size: 0.55rem;
        }
      }
    }
    &__filters {
      display: flex;
      align-items: center;
      width: 10rem;
      height: 2rem;
      color: var(--primary-white);
      font-weight: bolder;
      cursor: pointer;
      transition: all 0.3s ease-in;
      background-color: var(--color-background);
      border: 2px solid var(--primary-white);
      justify-content: center;
      border-radius: 5px;
      padding: 20px 0;
      column-gap: 10px;
      &:hover {
        transform: scale(1.03);
      }
      img {
        width: 2rem;
        height: 2rem;
      }
    }
  }
  &__paginator {
    background-color: var(--color-background);
  }
}
</style>
