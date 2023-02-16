<template>
  <div class="cart-wrapper" v-if="this.items.length > 0">
    <div class="cart-wrapper__products">
      <div
        class="cart-wrapper__products__element"
        v-for="item in items"
        :key="item.id"
      >
        <div class="cart-wrapper__products__element__photo">
          <img :src="getPhotoUrl(item)" :alt="item.name" />
        </div>

        <div class="cart-wrapper__products__element__name">
          <h3>{{ item.name }}</h3>
          <p>
            Kategorie:
            <span
              v-for="category in item.category"
              :key="category.name"
              class="ml-2"
            >
              {{ category.name }}
            </span>
          </p>
          <p>Cena za szt: {{ item.price }} zł</p>
        </div>
        <div class="cart-wrapper__products__element__counter">
          <ProductCounter
            :itemCounter="item.count"
            @minus="handleMinus(item)"
            @plus="handlePlus(item)"
          />
        </div>

        <p class="cart-wrapper__products__element__actions">
          {{ (item.count * item.price).toFixed(2) }} zł
          <v-icon
            color="#EE0D0DFF"
            size="large"
            @click.prevent="
              isModalVisible = true;
              modalItem = item;
            "
            >mdi-trash-can</v-icon
          >
        </p>
      </div>
    </div>
    <div class="cart-wrapper__summary">
      <h3>Podsumowanie</h3>
      <hr />
      <p>Cena: {{ itemsPriceSum.toFixed(2) }} zł</p>
      <p>
        Dostawa: <span>{{ shippingCost }} zł</span>
      </p>
      <p>Cena końcowa: {{ totalPrice.toFixed(2) }} zł</p>
      <Button :text="'Przejdź do zakupu'" class="mt-8" />
    </div>
  </div>
  <div class="cart-wrapper__empty" v-else>
    <v-icon color="#EE0D0DFF" size="200">mdi-cart-off</v-icon>
    <h3 class="mt-10">Nie masz żadnych produktów w koszyku...</h3>
    <router-link :to="{ name: 'products' }"
      ><p>Przeglądaj produkty &#8594;</p></router-link
    >
  </div>
  <ModalOverlay
    v-if="isModalVisible"
    class="cart-confirm-modal"
    @closeModal="isModalVisible = false"
  >
    <h3>Potwierdź usunięcie produktu z koszyka</h3>
    <p>
      Czy na pewno chcesz usunąć <span>{{ modalItem.name }}</span> z koszyka?
    </p>
    <Button
      :text="'Potwierdź'"
      class="mt-8"
      @click.prevent="
        deleteCartItem(this.modalItem);
        this.items = this.items.filter((el) => el.id !== modalItem.id);
        isModalVisible = false;
        modalItem = {};
      "
    />
  </ModalOverlay>
</template>

<script>
import ProductCounter from "@/components/ProductCounter.vue";
import ModalOverlay from "@/components/ModalOverlay.vue";
import Button from "@/components/Button.vue";
import cookies from "@/utils/cookies";
import axios from "axios";
export default {
  name: "CartView",
  components: {
    ProductCounter,
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    ModalOverlay,
  },
  data() {
    return {
      items: [],
      itemsPriceSum: 0,
      shippingCost: 9.99,
      isModalVisible: false,
      modalItem: {},
    };
  },
  async created() {
    const cartCookie = cookies.getCookie("cartItems");
    let parsedArray = [];
    if (cartCookie) {
      parsedArray = JSON.parse(cartCookie);
      parsedArray = parsedArray.map(async (item) => {
        const response = await axios.get(`product/${item.id}`);
        this.items.push({ ...response.data, count: item.count });
        this.itemsPriceSum += response.data.price * item.count;
      });
    }

    return { parsedArray };
  },
  methods: {
    getPhotoUrl(item) {
      return import.meta.env.VITE_STATIC_ORGIN + item.main_image;
    },
    deleteCartItem(item) {
      const newCartItem = {
        id: item.id,
        count: item.count - 1,
      };
      cookies.changeCartItem(newCartItem);
      item.count -= 1;
      const sumArray = this.items.map((el) => el.count * el.price);
      let sum = 0;
      sumArray.forEach((el) => {
        sum += el;
      });
      this.itemsPriceSum = sum;
    },
    handleMinus(item) {
      if (item.count === 1) {
        this.isModalVisible = true;
        this.modalItem = item;
        return;
      }
      this.deleteCartItem(item);
    },
    handlePlus(item) {
      const newCartItem = {
        id: item.id,
        count: item.count + 1,
      };
      cookies.changeCartItem(newCartItem);
      item.count += 1;
      const sumArray = this.items.map((el) => el.count * el.price);
      let sum = 0;
      sumArray.forEach((el) => {
        sum += el;
      });
      this.itemsPriceSum = sum;
    },
  },
  watch: {
    itemsPriceSum() {
      this.shippingCost = this.itemsPriceSum >= 60 ? 0 : this.shippingCost;
    },
  },
  computed: {
    totalPrice() {
      return this.itemsPriceSum + this.shippingCost;
    },
  },
};
</script>

<style scoped lang="scss">
.cart-confirm-modal {
  color: var(--primary-white);
  h3 {
    font-size: 2rem;
  }
  p {
    span {
      color: var(--primary-green);
    }
  }
}
.cart-wrapper {
  margin-top: 5rem;
  flex-grow: 1;
  display: grid;
  grid-template-columns: 0.25fr 1fr 0.5fr 0.25fr;

  &__products {
    grid-column: 2/3;
    display: flex;
    flex-direction: column;
    row-gap: 2rem;
    min-height: 35rem;
    height: 65vh;
    max-height: 45rem;
    overflow-y: scroll;
    overflow-x: hidden;
    -ms-overflow-style: none;
    scrollbar-width: none;
    &::-webkit-scrollbar {
      display: none;
    }
    &__element {
      align-items: center;
      display: grid;
      grid-template-columns: auto 2fr auto 0.5fr;
      grid-column-gap: 2rem;
      &__actions {
        color: var(--primary-white);
        display: flex;
        .v-icon {
          margin-left: auto;
        }
      }
      &__photo {
        height: 5rem;
        width: 6rem;
        img {
          height: 100%;
          width: 100%;
          border: 3px solid var(--primary-green);
          cursor: pointer;
          transition: all 0.3s ease-in;
          &:hover {
            transform: scale(1.05);
          }
        }
      }
      &__name {
        display: flex;
        flex-direction: column;
        cursor: pointer;
        transition: all 0.3s ease-in;
        &:hover {
          transform: scale(1.05);
        }
        p {
          color: var(--primary-white);
        }
      }
      &__counter {
        display: flex;
        width: 7rem;
        height: 3rem;
        border-radius: 5px;
        outline: 1px solid var(--primary-white);
        padding: 0 5px;
        align-items: center;
        margin-left: auto;
      }
    }
  }
  &__summary {
    grid-column: 3/4;
    margin-left: 4rem;
    color: var(--primary-white);
    h3 {
      font-size: 2rem;
    }
    hr {
      color: var(--primary-green);
    }
    p:first-of-type {
      margin-top: 2rem;
    }
  }
}

.cart-wrapper__empty {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--primary-white);
  h3 {
    font-size: 2.5rem;
  }
  p {
    font-size: 1.5rem;
    transition: all 0.3s ease-in;
    &:hover {
      transform: scale(1.05);
      color: var(--primary-green);
    }
  }
}
</style>
