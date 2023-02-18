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
        <p class="text-3xl">
          Cena do zapłaty: <b>{{ itemsPriceSum + shippingCost }}</b> zł
        </p>
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
import { useField, useForm } from "vee-validate";
import axios from "axios";
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
    const paymentMethod = useField("paymentMethod");

    const userStore = useUserStore();
    fname.value.value = userStore.user.first_name;
    lname.value.value = userStore.user.last_name;
    phone.value.value = userStore.user.phone;

    const submit = handleSubmit(async function (values) {
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
      const orderResponse = await axios.post("order/create", payload);
      const response = await axios.post("payments/create-session/", {
        data: items.value,
        shippingCost: shippingCost.value,
        orderId: orderResponse.data.id,
      });
      console.log(response);
      sessionId.value = response.data.session.id;
      sessionUrl.value = response.data.session.url;
      // window.location.href = sessionUrl.value;
      window.open(sessionUrl.value, "_blank");
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
      paymentMethod,
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
}
.order__contact {
  display: flex;
  flex-direction: column;
  grid-column: 1/2;
  color: var(--primary-white);
  h3 {
    color: var(--primary-green);
  }
  .v-text-field {
    margin-top: 1rem;
    width: 25rem;
  }
  &__city {
    display: flex;
    column-gap: 2rem;
    .v-text-field:first-of-type {
      width: 10rem;
    }
    .v-text-field:nth-of-type(2) {
      width: 13rem;
    }
  }
}
.order__resume {
  color: var(--primary-white);
  ul {
    margin-top: 2rem;
    li {
      font-size: 1rem;
      span {
        font-size: 1.5rem;
      }
    }
  }
  p:first-of-type {
    margin-top: 2rem;
  }
  h3 {
    font-size: 2.5rem;
  }
}
.order__submit {
  height: 3rem !important;
}
</style>
