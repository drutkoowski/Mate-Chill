<template>
  <div class="order-wrapper">
    <form @submit.prevent="submit">
      <div class="order__contact">
        <h3>Informacje kontaktowe</h3>
        <v-text-field
          v-model="email.value.value"
          :error-messages="email.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Imię powinno zawierać conajmniej 3 znaki."
          counter
          label="Imię"
        ></v-text-field>
        <v-text-field
          v-model="email.value.value"
          :error-messages="email.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Nazwisko powinno zawierać conajmniej 3 znaki."
          counter
          label="Nazwisko"
        ></v-text-field>
        <v-text-field
          v-model="email.value.value"
          :counter="9"
          :error-messages="email.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Numer telefonu powinien składać się z 9 cyfr."
          label="Telefon"
        ></v-text-field>
        <h3>Adres dostawy</h3>
        <v-text-field
          v-model="email.value.value"
          :error-messages="email.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Adres dostawy."
          label="Nazwa ulicy"
        ></v-text-field>

        <v-text-field
          v-model="email.value.value"
          :error-messages="email.errorMessage.value"
          bg-color="white"
          color="green-darken-1"
          hint="Adres dostawy."
          label="Nazwa ulicy linia 2"
        ></v-text-field>

        <div class="order__contact__city">
          <v-text-field
            v-model="email.value.value"
            :error-messages="email.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Kod pocztowy."
            label="Kod pocztowy"
          ></v-text-field>
          <v-text-field
            v-model="email.value.value"
            :error-messages="email.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Miasto."
            label="Miasto"
          ></v-text-field>
        </div>
      </div>
      <div class="order__resume">
        <h3>Podsumowanie</h3>
        <hr />
        <ul>
          <li v-for="item in items" :key="item.id">
            <span>{{ item.name }}</span> ({{ item.price }} zł)
            {{ item.count }} szt.
          </li>
        </ul>
        <p>Dostawa: {{ shippingCost }} zł</p>
        <p>Cena końcowa: {{ itemsPriceSum + shippingCost }} zł</p>
        <v-select
          :label="'Metoda płatności'"
          :items="['tak']"
          bg-color="white"
        />
        <Button
          :text="'Przejdź do płatności'"
          class="order__submit"
          type="submit"
        />
      </div>
    </form>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";
import { useField, useForm } from "vee-validate";
import cookies from "@/utils/cookies";
import axios from "axios";

export default {
  name: "OrderView",
  data() {
    return {
      items: [],
      itemsPriceSum: 0,
      shippingCost: 0,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  setup() {
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        email(value) {
          if (/^[a-z0-9.]{1,64}@[a-z0-9.]{1,64}$/i.test(value)) return true;

          return "Pole musi zawierać poprawny adres e-mail.";
        },
      },
    });
    const email = useField("email");
    const password = useField("password");

    const submit = handleSubmit(async function (values) {
      console.log(values);
    });

    return {
      email,
      password,
      submit,
      handleReset,
    };
  },
  async created() {
    const cartCookie = cookies.getCookie("cartItems");
    if (!cartCookie) this.$router.push({ name: "cart" });
    let items = [];
    let parsedArray = JSON.parse(cartCookie);
    await parsedArray.map(async (item) => {
      const response = await axios.get(`product/${item.id}`);
      items.push({ ...response.data, count: item.count });
      this.itemsPriceSum += response.data.price * item.count;
      this.items = items;
      this.shippingCost = this.itemsPriceSum >= 60 ? 0 : 9.99;
    });
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
  .v-text-field {
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
