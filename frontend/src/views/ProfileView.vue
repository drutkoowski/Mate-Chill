<template>
  <div class="profile-wrapper">
    <div class="profile-info">
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
        <div class="profile-info__actions">
          <Button :text="'Edytuj'" /><Button :text="'Zmień hasło'" />
        </div>
      </form>
    </div>
    <div class="profile-orders">
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
</template>

<script>
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
          if (/^[a-z0-9.]{1,64}@[a-z0-9.]{1,64}$/i.test(value)) return true;

          return "Pole musi zawierać poprawny adres e-mail.";
        },
        lname(value) {
          if (value?.length >= 8) return true;

          return "Hasło musi składać się z conajmniej 8 znaków.";
        },
        phone(value) {
          if (value?.length >= 8) return true;

          return "Hasło musi składać się z conajmniej 8 znaków.";
        },
      },
    });
    const fname = useField("fname");
    const lname = useField("lname");
    const phone = useField("phone");

    const submit = handleSubmit(async function (values) {
      console.log(values);
    });

    return { fname, lname, phone, submit, handleReset };
  },
  async created() {
    const ordersResponse = await axios.get("orders/");
    this.orders = ordersResponse.data;
    console.log(this.orders);
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
  grid-template-columns: 1fr 1fr;
  justify-items: center;
  color: var(--primary-white);
}
.profile-info {
  h3 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  &__actions {
    display: flex;
    justify-content: space-between;
  }
}

.profile-orders {
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
