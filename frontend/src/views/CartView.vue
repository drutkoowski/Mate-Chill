<template>
  <!--	cart-->
  <div class="cart-wrapper" v-if="this.items.length > 0">
    <div class="cart-wrapper__products">
      <div
        class="cart-wrapper__products__element"
        v-for="item in items"
        :key="item.id"
      >
        <div class="cart-wrapper__products__element__photo">
          <router-link
            :to="{
              name: 'product-detail',
              params: {
                productSlug: item.slug,
              },
            }"
          >
            <img :src="getPhotoUrl(item)" :alt="item.name"
          /></router-link>
        </div>

        <div class="cart-wrapper__products__element__name">
          <h3>
            <router-link
              :to="{
                name: 'product-detail',
                params: {
                  productSlug: item.slug,
                },
              }"
              >{{ item.name }}</router-link
            >
          </h3>
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
              isModalAcceptVisible = true;
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
      <Button
        :text="'Przejdź do zakupu'"
        class="mt-8"
        @click.prevent="handleCartForward"
      />
    </div>
  </div>

  <!--	empty cart information-->
  <div class="cart-wrapper__empty" v-else>
    <v-icon color="#EE0D0DFF" size="200">mdi-cart-off</v-icon>
    <h3>Nie masz żadnych produktów w koszyku...</h3>
    <router-link :to="{ name: 'products' }"
      ><p>Przeglądaj produkty &#8594;</p></router-link
    >
  </div>

  <ModalOverlay
    v-if="isModalLoginVisible"
    @closeModal="isModalLoginVisible = false"
  >
    <LoginModal @closeModal="isModalLoginVisible = false" :next="'order'" />
  </ModalOverlay>

  <!--	modal confirm delete-->
  <ModalOverlay
    v-if="isModalAcceptVisible"
    class="cart-confirm-modal"
    @closeModal="isModalAcceptVisible = false"
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
        isModalAcceptVisible = false;
        modalItem = {};
      "
    />
  </ModalOverlay>
</template>

<script>
import ProductCounter from "@/components/ProductCounter.vue";
import ModalOverlay from "@/components/ModalOverlay.vue";
import Button from "@/components/Button.vue";
import LoginModal from "@/components/login/LoginModal.vue";
import cookies from "@/utils/cookies";
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import axios from "axios";

export default {
  name: "CartView",
  components: {
    ProductCounter,
    LoginModal,
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    ModalOverlay,
  },
  data() {
    return {
      items: [],
      itemsPriceSum: 0,
      shippingCost: 9.99,
      isModalAcceptVisible: false,
      isModalLoginVisible: false,
      modalItem: {},
    };
  },
  setup() {
    const userStore = useUserStore();
    return { userStore };
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
        this.isModalAcceptVisible = true;
        this.modalItem = item;
        return;
      }
      this.deleteCartItem(item);
    },
    handlePlus(item) {
      if (item.count >= item.num_available) {
        const toastStore = useToastStore();
        toastStore.displayToast(
          "Wybrano maksymalną dostępną ilość produktu.",
          "#E85959FF"
        );
        return;
      }
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
    handleCartForward() {
      if (!this.userStore.isAuthenticated) {
        this.isModalLoginVisible = true;
        return;
      }
      this.$router.push({ name: "order" });
    },
  },
  watch: {
    itemsPriceSum() {
      this.shippingCost = this.itemsPriceSum >= 60 ? 0 : 9.99;
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
  @include respond(tab-desktop) {
    grid-template-columns: 1fr 0.5fr;
  }
  @include respond(tab-md) {
    grid-template-columns: 1fr;
    grid-template-rows: auto 1fr;
  }
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
    @include respond(tab-desktop) {
      grid-column: 1/2;
    }
    @include respond(tab-md) {
      height: unset;
      min-height: unset;
    }
    @include respond(phone-lg) {
      margin-top: 5rem;
    }
    &__element {
      align-items: center;
      display: grid;
      grid-template-columns: auto 2fr auto 0.5fr;
      grid-column-gap: 2rem;
      @include respond(tab-sm) {
        grid-template-columns: 0.25fr 1fr 0.25fr 0.25fr;
        grid-row-gap: 2rem;
        padding: 5px 5px;
      }
      &__actions {
        color: var(--primary-white);
        display: flex;
        white-space: nowrap;
        column-gap: 5px;
        .v-icon {
          margin-left: auto;
        }
        @include respond(phone-md-lg) {
          font-size: 0.85rem;
        }
      }
      &__photo {
        height: 5rem;
        width: 6rem;
        @include respond(tab-sm) {
          height: 6rem;
          width: 7rem;
        }
        @include respond(phone-md-lg) {
          height: 5rem;
          width: 6rem;
        }
        @include respond(phone-md-sm) {
          height: 5rem;
          width: 5rem;
        }
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
        @include respond(tab-sm) {
          grid-column: 2/5;
        }
        h3 {
          @include respond(tab-sm) {
            font-size: 1.1rem;
          }
          @include respond(phone-md-lg) {
            font-size: 1rem;
          }
        }
        &:hover {
          transform: scale(1.01);
        }
        p {
          color: var(--primary-white);
          @include respond(phone-md-lg) {
            font-size: 0.85rem;
          }
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
        @include respond(tab-sm) {
          grid-column: 1/4;
          margin-left: 0;
        }
        @include respond(phone-md-lg) {
          width: 6rem;
          height: 2rem;
        }
        @include respond(phone-md-sm) {
          grid-column: 1/3;
        }
      }
    }
  }
  &__summary {
    grid-column: 3/4;
    margin-left: 4rem;
    color: var(--primary-white);
    @include respond(tab-desktop) {
      grid-column: 2/3;
    }
    @include respond(tab-md) {
      grid-column: 1/2;
      grid-row: 2/3;
      margin-left: 0;
      margin-top: 4rem;
    }
    h3 {
      font-size: 2rem;
      @include respond(tab-md) {
        font-size: 3rem;
      }
      @include respond(phone-md-lg) {
        font-size: 2.5rem;
      }
      @include respond(phone-md-sm) {
        font-size: 2rem;
      }
    }
    hr {
      color: var(--primary-green);
      @include respond(tab-md) {
        width: 25rem;
      }
      @include respond(phone-md-lg) {
        width: 20rem;
      }
      @include respond(phone-md-sm) {
        width: 15rem;
      }
    }
    p:first-of-type {
      margin-top: 2rem;
    }
    p {
      @include respond(tab-md) {
        font-size: 1.5rem;
      }
      @include respond(tab-sm) {
        font-size: 1.25rem;
      }
      @include respond(phone-md-sm) {
        font-size: 1rem;
      }
    }
    button {
      @include respond(tab-md) {
        font-size: 1.3rem;
        height: 3.5rem;
      }
      @include respond(tab-sm) {
        font-size: 1rem;
        height: 3rem;
      }
      @include respond(phone-md-sm) {
        font-size: 0.75rem;
        height: 2.5rem;
      }
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
  i {
    @include respond(tab-land) {
      transform: scale(0.9);
    }
    @include respond(tab-sm) {
      transform: scale(0.7);
    }
    @include respond(phone-md) {
      transform: scale(0.5);
    }
  }
  h3 {
    margin-top: 1rem;
    font-size: 2.5rem;
    @include respond(tab-land) {
      font-size: 2rem;
    }
    @include respond(tab-sm) {
      font-size: 1.65rem;
      margin-top: 0;
    }
    @include respond(phone-lg) {
      font-size: 1.2rem;
    }
    @include respond(phone-md) {
      font-size: 1rem;
      margin-top: -1rem;
    }
    @include respond(phone-sm) {
      font-size: 0.85rem;
    }
  }
  p {
    font-size: 1.5rem;
    transition: all 0.3s ease-in;
    @include respond(tab-land) {
      font-size: 1.25rem;
    }
    @include respond(tab-sm) {
      font-size: 1rem;
    }
    @include respond(phone-lg) {
      font-size: 0.75rem;
    }
    @include respond(phone-md) {
      font-size: 0.65rem;
    }
    @include respond(phone-sm) {
      font-size: 0.55rem;
    }
    &:hover {
      transform: scale(1.05);
      color: var(--primary-green);
    }
  }
}
</style>
