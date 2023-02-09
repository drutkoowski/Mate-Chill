<template>
  <div class="wrapper">
    <div class="product-image-container">
      <ProductGallery
        :slides="[
          'https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_10.jpg',
          'https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_1.png',
          'https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_2.jpg',
          'https://www.yerbamarket.com/pol_pm_Yerba-Mate-Laranjeiras-Yari-terere-limao-siciliano-500-g-15104_1.png',
        ]"
      />
    </div>
    <div class="product-info-container">
      <h1>Yerba Mate Laranjeiras Yari terere - limao siciliano 500 g</h1>
      <div class="product-info-container__rating">
        <v-rating v-model="rating" readonly color="white" />
        <span>3.2/5.00 <span class="text-stone-50">(3 opinie)</span></span>
      </div>
      <div class="product-info-container__description mt-10">
        <p>Producent: Asadas</p>
        <p>Dostępność: <span>Bardzo duża ilość</span></p>
        <p>Kraj producenta: Polska</p>
        <p>
          Opis: Brazylijska yerba mate zawierająca listki i patyczki z porcją
          naturalnego aromatu cytrynowego. Idealna do przygotowywania na zimno
        </p>
      </div>

      <div class="product-info-container__customizable">
        <filterInput
          class="mt-2"
          :type="'select'"
          :text="'Rozmiar'"
          :multiple="false"
          :items="['25g', '500g', '1000g']"
        />
      </div>
      <div class="product-info-container__customizable">
        <filterInput
          :type="'select'"
          :text="'Rozmiar'"
          :multiple="false"
          :items="['25g', '500g', '1000g']"
        />
      </div>
      <h3 class="product-info-container__price">
        24,99 zł <small>brutto / szt.</small>
      </h3>
      <div class="product-info-container__actions">
        <div class="product-info-container__actions__counter px-5 py-2">
          <v-icon class="mr-auto" color="red">mdi-minus</v-icon>

          <h5 class="text-center font-weight-bold text-h5">0</h5>

          <v-icon class="ml-auto">mdi-plus</v-icon>
        </div>
        <Button :text="'Dodaj do koszyka'" />
      </div>
    </div>
  </div>
</template>

<script>
import ProductGallery from "@/components/products/ProductGallery.vue";
import filterInput from "@/components/filters/filterInput.vue";
import Button from "@/components/Button.vue";
export default {
  name: "ProductDetailView",
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { Button, ProductGallery, filterInput },
  data: () => ({
    rating: 3,
  }),
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
  padding: 0 2rem;
  height: 100%;
  width: 30rem;
  justify-self: center;
}
.product-info-container {
  &__rating {
    display: flex;
    align-items: center;
  }
  &__customizable {
    display: flex;
    align-items: center;
    width: 15rem;
  }
  &__price {
    font-size: 2rem;
    font-weight: bold;
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
    width: 15rem;
    border-radius: 5px;
    background-color: var(--white);
    h5 {
      color: var(--color-background);
    }
    .v-icon {
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
