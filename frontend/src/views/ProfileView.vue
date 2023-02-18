<template>
  <div class="profile-wrapper">
    <div class="profile">
      <div class="profile__info">
        <h3>Informacje o mnie</h3>
        <form @submit.prevent="submit">
          <v-text-field
            v-model="fname.value.value"
            :error-messages="fname.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Imię powinno zawierać conajmniej 3 znaki."
            label="Imię"
          ></v-text-field>
          <v-text-field
            v-model="lname.value.value"
            :error-messages="lname.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Nazwisko powinno zawierać conajmniej 3 znaki."
            label="Nazwisko"
          ></v-text-field>
          <v-text-field
            v-model="phone.value.value"
            :counter="9"
            :error-messages="phone.errorMessage.value"
            bg-color="white"
            color="green-darken-1"
            hint="Numer telefonu powinien składać się z 9 cyfr."
            label="Telefon"
          ></v-text-field>
          <div class="profile__info__actions">
            <Button :text="'Edytuj'" type="submit" /><Button
              :text="'Zmień hasło'"
            />
          </div>
        </form>
      </div>
      <div class="profile__orders">
        <h3>Moje zamówienia</h3>
        <v-table fixed-header height="300px">
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left font-weight-bold">Produkty</th>
              <th class="text-left font-weight-bold">Cena</th>
              <th class="text-left font-weight-bold">Data</th>
              <th class="text-left font-weight-bold">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in orders" :key="order.id">
              <td>{{ order.id }}</td>
              <td>
                <ul v-for="product in order.products" :key="product.id">
                  <li>
                    <b>{{ product.product.name }}</b> x {{ product.count }}
                  </li>
                </ul>
              </td>
              <td>{{ order.summary_cost }} zł</td>
              <td>{{ order.created_at }}</td>
              <td>
                <Button
                  :text="'Opłać'"
                  v-if="order.status === 'nieopłacone'"
                  @click.prevent="handlePayment(order)"
                />
                <span v-else>{{ order.status }}</span>
              </td>
            </tr>
          </tbody>
        </v-table>
      </div>
    </div>
  </div>
</template>

<script>
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import Button from "@/components/Button.vue";
import { useField, useForm } from "vee-validate";
import axios from "axios";

export default {
  name: "ProfileView",
  data() {
    return {
      orders: [],
    };
  },
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { Button },
  setup() {
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        fname(value) {
          if (value?.length >= 3) return true;

          return "Imię musi składać się z conajmniej trzech znaków.";
        },
        lname(value) {
          if (value?.length >= 3) return true;

          return "Nazwisko musi składać się z conajmniej trzech znaków.";
        },
        phone(value) {
          if (value?.length === 9 && /[0-9-]+/.test(value)) return true;

          return "Numer telefonu powinien składać się z 9 cyfr.";
        },
      },
    });
    const fname = useField("fname");
    const lname = useField("lname");
    const phone = useField("phone");

    const submit = handleSubmit(async function (values) {
      await axios.patch("account/update", {
        first_name: values.fname,
        last_name: values.lname,
        phone: values.phone,
      });
      fname.value.value = values.fname;
      lname.value.value = values.lname;
      phone.value.value = values.phone;
      const toastStore = useToastStore();
      toastStore.displayToast(
        "Pomyślnie zaktualizowano informacje.",
        "success"
      );
    });
    const userStore = useUserStore();
    fname.value.value = userStore.user.first_name;
    lname.value.value = userStore.user.last_name;
    phone.value.value = userStore.user.phone;
    return { fname, lname, phone, submit, handleReset };
  },
  async created() {
    const ordersResponse = await axios.get("orders/");
    this.orders = ordersResponse.data;
  },
  methods: {
    async handlePayment(order) {
      const data = [];
      order.products.forEach((el) =>
        data.push({
          name: el.product.name,
          count: el.count,
          price: el.price,
        })
      );
      const response = await axios.post("payments/create-session/", {
        data: data,
        shippingCost: order.shipping_cost,
        orderId: order.id,
      });
      window.location.href = response.data.session.url;
    },
  },
};
</script>

<style scoped lang="scss">
.profile-wrapper {
  margin-top: 5rem;
  flex-grow: 1;
  display: grid;
  grid-template-columns: 0.15fr 1fr 0.15fr;
}
.profile {
  grid-column: 2/3;
  display: grid;
  grid-template-columns: 0.5fr 1fr;
  grid-column-gap: 5rem;
  justify-items: stretch;
  color: var(--primary-white);
}
.profile__info {
  h3 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  &__actions {
    display: flex;
    column-gap: 2rem;
  }
}

.profile__orders {
  display: flex;
  flex-direction: column;
  justify-self: stretch;
  h3 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  .v-table {
    border-radius: 10px;
  }
}
</style>
