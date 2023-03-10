<template>
  <div class="order-wrapper">
    <form @submit.prevent="submit">
      <div class="order__contact">
        <h3>Informacje kontaktowe</h3>
        <v-text-field
          v-model="fname.value.value"
          :error-messages="fname.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Imię powinno zawierać conajmniej 3 znaki."
          counter
          label="Imię"
        ></v-text-field>
        <v-text-field
          v-model="lname.value.value"
          :error-messages="lname.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Nazwisko powinno zawierać conajmniej 3 znaki."
          counter
          label="Nazwisko"
        ></v-text-field>
        <v-text-field
          v-model="phone.value.value"
          :counter="9"
          :error-messages="phone.errorMessage.value"
          type="number"
          bg-color="white"
          color="green-darken-1"
          hint="Numer telefonu powinien składać się z 9 cyfr."
          label="Telefon"
        ></v-text-field>
        <h3>Adres dostawy</h3>
        <v-text-field
          v-model="streetAddress.value.value"
          :error-messages="streetAddress.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          label="Nazwa ulicy"
        ></v-text-field>

        <v-text-field
          v-model="streetAddress2.value.value"
          bg-color="white"
          color="green-darken-1"
          label="Nazwa ulicy linia 2"
        ></v-text-field>

        <div class="order__contact__city">
          <v-text-field
            v-model="cityCode.value.value"
            :error-messages="cityCode.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Pole powinno zawierać poprawny kod pocztowy, np. 37-682."
            label="Kod pocztowy"
          ></v-text-field>
          <v-text-field
            v-model="city.value.value"
            :error-messages="city.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            label="Miasto"
          ></v-text-field>
        </div>
      </div>
      <div class="order__resume">
        <h3>Podsumowanie</h3>
        <hr />
        <ul>
          <li v-for="item in items" :key="item.id">
            <span class="primary-green">{{ item.name }}</span> ({{
              item.price
            }}
            zł) {{ item.count }} szt.
          </li>
        </ul>
        <p>Dostawa: {{ shippingCost }} zł</p>
        <p class="order__resume__price">
          Cena do zapłaty:
          <b>{{ (itemsPriceSum + shippingCost).toFixed(2) }}</b> zł
        </p>
        <h5 class="mt-12">Metody płatności</h5>
        <div class="order__resume__payment-methods">
          <img src="/blik.svg" alt="Visa" />
          <img src="/visa.svg" alt="Mastercard" />
          <img src="/mastercard.svg" alt="Blik" />
        </div>
        <Button
          :text="'Zatwierdź kupno i przejdź do płatności'"
          class="order__submit mt-8"
          type="submit"
        />
      </div>
    </form>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";
import cookies from "@/utils/cookies";
import useUserStore from "@/stores/user";
import useMainStore from "@/stores/main";
import useToastStore from "@/stores/toast";
import axios from "axios";
import { useField, useForm } from "vee-validate";
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "OrderView",
  data() {
    return {
      publishableKey: import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  setup() {
    const items = ref([]);
    const itemsPriceSum = ref(0);
    const shippingCost = ref(0);
    const cartCookie = ref(cookies.getCookie("cartItems"));
    const router = useRouter();
    if (!cartCookie.value) router.push({ name: "cart" });
    let parsedArray = JSON.parse(cartCookie.value);
    const cookieItems = [];
    parsedArray.map(async (item) => {
      const response = await axios.get(`product/${item.id}`);
      cookieItems.push({ ...response.data, count: item.count });
      itemsPriceSum.value += response.data.price * item.count;
      items.value = cookieItems;
      shippingCost.value = itemsPriceSum.value >= 60 ? 0 : 9.99;
    });
    const sessionId = ref("");
    const sessionUrl = ref("");

    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        fname(value) {
          if (value?.length >= 3) return true;

          return "Imię powinno zawierać conajmniej 3 znaki.";
        },
        lname(value) {
          if (value?.length >= 3) return true;

          return "Nazwisko powinno zawierać conajmniej 3 znaki.";
        },
        phone(value) {
          if (value?.length === 9) return true;
          return "Numer telefonu powinien składać się z 9 cyfr.";
        },
        streetAddress(value) {
          if (value?.length >= 3) return true;
          return "Pole powinno zawierać nazwę ulicy dłuższą od 5 znaków";
        },
        cityCode(value) {
          if (/^[0-9]{2}-[0-9]{3}$/.test(value)) return true;
          return "Pole powinno zawierać poprawny kod pocztowy";
        },
        city(value) {
          if (value?.length >= 3) return true;
          return "Nazwa miasta powinna zawierać conajmniej 3 znaki.";
        },
      },
    });

    const fname = useField("fname");
    const lname = useField("lname");
    const phone = useField("phone");
    const streetAddress = useField("streetAddress");
    const streetAddress2 = useField("streetAddress2");
    const cityCode = useField("cityCode");
    const city = useField("city");

    const userStore = useUserStore();
    fname.value.value = userStore.user.first_name;
    lname.value.value = userStore.user.last_name;
    phone.value.value = userStore.user.phone;

    const submit = handleSubmit(async function (values) {
      const mainStore = useMainStore();
      mainStore.on();
      cookies.deleteCookie("cartItems");
      mainStore.clearCartItems();
      const payload = {
        data: {
          city: values.city,
          city_code: values.cityCode,
          additional_address: values.streetAddress2,
          address: values.streetAddress,
          last_name: values.lname,
          first_name: values.fname,
        },
        products: parsedArray,
      };
      try {
        const orderResponse = await axios.post("order/create", payload);
        const response = await axios.post("payments/create-session/", {
          data: items.value,
          shippingCost: shippingCost.value,
          orderId: orderResponse.data.id,
        });
        sessionId.value = response.data.session.id;
        sessionUrl.value = response.data.session.url;
        window.location.href = sessionUrl.value;
      } catch (error) {
        const toastStore = useToastStore();
        toastStore.displayToast("Płatność nie powiodła się.", "#E85959FF");
      }
      mainStore.off();
    });

    return {
      fname,
      lname,
      phone,
      userStore,
      streetAddress,
      streetAddress2,
      cityCode,
      city,
      sessionId,
      sessionUrl,
      items,
      itemsPriceSum,
      shippingCost,
      handleReset,
      submit,
    };
  },
};
</script>

<style scoped lang="scss">
.order-wrapper {
  margin-top: 5rem;
  flex-grow: 1;
  justify-items: center;
}
form {
  justify-items: center;
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  @include respond(md-desktop) {
    grid-template-columns: 0.5fr 1fr;
  }
  @include respond(tab-desktop) {
    grid-template-columns: 1fr;
    justify-items: start;
  }
  @include respond(phone-sm) {
    justify-items: center;
  }
}
.order__contact {
  display: flex;
  flex-direction: column;
  grid-column: 1/2;
  color: var(--primary-white);
  @include respond(tab-desktop) {
    display: grid;
    grid-template-columns: repeat(2, auto);
    grid-column-gap: 1rem;
  }
  @include respond(tab-port) {
    grid-template-columns: unset;
  }
  @include respond(phone-lg) {
    margin-top: 5rem;
  }

  h3 {
    color: var(--primary-green);
    @include respond(tab-desktop) {
      grid-column: 1/-1;
    }
  }
  .v-text-field {
    margin-top: 1rem;
    width: 25rem;
    @include respond(tab-port) {
      width: 15rem;
    }
    @include respond(phone-sm) {
      justify-self: center;
    }
  }
  &__city {
    display: flex;
    column-gap: 2rem;
    @include respond(phone-lg) {
      flex-direction: column;
    }
    .v-text-field:first-of-type {
      width: 10rem;
      @include respond(phone-lg) {
        width: 15rem;
      }
    }
    .v-text-field:nth-of-type(2) {
      width: 13rem;
      @include respond(phone-lg) {
        width: 15rem;
      }
    }
  }
}
.order__resume {
  color: var(--primary-white);
  @include respond(phone-sm) {
    display: flex;
    flex-direction: column;
    justify-items: center;
  }
  &__price {
    font-size: 2.5rem;
    @include respond(tab-desktop) {
      font-size: 2rem;
    }
    @include respond(tab-desktop) {
      font-size: 1.75rem;
    }
    @include respond(tab-desktop) {
      font-size: 1.5rem;
    }
    @include respond(phone-sm) {
      font-size: 1.35rem;
    }
  }
  hr {
    @include respond(phone-md) {
      width: 15rem;
      margin: 0 auto;
    }
  }
  ul {
    margin-top: 2rem;
    li {
      font-size: 1rem;
      @include respond(phone-md-lg) {
        font-size: 0.85rem;
      }
      @include respond(phone-lg) {
        font-size: 0.75rem;
      }
      @include respond(tab-desktop) {
        font-size: 0.65rem;
      }
      span {
        font-size: 1.5rem;
        @include respond(phone-md-lg) {
          font-size: 1.25rem;
        }
        @include respond(phone-lg) {
          font-size: 1rem;
        }
        @include respond(tab-desktop) {
          font-size: 0.9rem;
        }
      }
    }
  }
  p:first-of-type {
    margin-top: 2rem;
  }
  h3 {
    font-size: 2.5rem;
    @include respond(phone-md-lg) {
      font-size: 2rem;
    }
    @include respond(phone-sm) {
      text-align: center;
    }
  }
  &__payment-methods {
    display: flex;
    column-gap: 1rem;
    align-items: center;
    img {
      width: 3rem;
      height: 3rem;
    }
  }
}
.order__submit {
  height: 3rem !important;
  @include respond(phone-md) {
    height: 4rem;
    font-size: 0.75rem;
  }
  @include respond(phone-sm) {
    height: 5rem;
    font-size: 0.65rem;
  }
}
</style>
