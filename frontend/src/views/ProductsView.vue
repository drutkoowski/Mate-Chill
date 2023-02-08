<template>
  <div class="wrapper">
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
              :text="'Podkategorie'"
              :items="['Prezentowe', 'Dla par', 'Na początek']"
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
      <div class="products-container__products"></div>
    </div>
  </div>
</template>

<script>
import filterInput from "@/components/filters/filterInput.vue";
import Button from "@/components/Button.vue";

export default {
  name: "ProductsView",
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    filterInput,
  },
  methods: {
    resetFilters() {
      this.$refs.form.reset();
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapper {
  padding: 0 5rem;
}
.products-container {
  grid-column: 2/3;
  margin: 10rem 0;

  display: grid;
  grid-template-columns: 0.4fr 1fr;
  grid-column-gap: 5rem;
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
  min-height: 35rem;
  height: 55vh;

  background-color: var(--primary-white);
  border-radius: 10px;
}
</style>
