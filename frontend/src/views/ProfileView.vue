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
            <Button :text="'Edytuj'" type="submit" />
            <Button
              :text="'Zmień hasło'"
              @click.prevent="passwordModalVisible = true"
            />
          </div>
        </form>
      </div>
      <div class="profile__orders">
        <h3>Moje zamówienia</h3>
        <v-table height="300px">
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left font-weight-bold">Produkty</th>
              <th class="text-left font-weight-bold">Cena</th>
              <th class="text-left font-weight-bold">Data</th>
              <th class="text-left font-weight-bold">Status</th>
              <th class="text-left font-weight-bold">Akcje</th>
            </tr>
          </thead>
          <tbody v-if="orders.length > 0">
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
              <td>{{ order.status }}</td>
              <td class="profile__orders__actions">
                <Button
                  :text="'Opłać'"
                  v-if="order.status === 'nieopłacone'"
                  :color="'#E85959FF'"
                  @click.prevent="handlePayment(order)"
                />
                <Button
                  :text="'Oceń'"
                  v-if="order.status === 'zakończone'"
                  @click.prevent="openReviewModal(order)"
                />
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td colspan="5">
                <h3 class="text-center mt-5">
                  Nie złożyłeś jeszcze żadnych zamówień.
                </h3>
              </td>
            </tr>
          </tbody>
        </v-table>
      </div>
    </div>
  </div>
  <!--	modal password change-->
  <ModalOverlay
    v-if="passwordModalVisible"
    @closeModal="passwordModalVisible = false"
  >
    <div class="password-change">
      <form @submit.prevent="handlePasswordChange">
        <v-text-field
          v-model="newPassword"
          bg-color="white"
          type="password"
          color="green-darken-1"
          label="Nowe hasło"
        ></v-text-field>
        <v-text-field
          v-model="newPassword2"
          bg-color="white"
          type="password"
          color="green-darken-1"
          label="Potwierdź hasło"
        ></v-text-field>
        <p v-if="passwordErrorMessage">{{ passwordErrorMessage }}</p>
        <Button
          :text="'Zmień hasło'"
          type="submit"
          class="password-change__button"
        />
      </form>
    </div>
  </ModalOverlay>

  <!--	modal review-->
  <OrderProductReview
    :order="commentedOrder"
    v-if="reviewModalVisible"
    @closeModal="reviewModalVisible = false"
    @isReviewPosted="reviewModalVisible = false"
  />
</template>

<script>
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import useMainStore from "@/stores/main";
import Button from "@/components/Button.vue";
import { useField, useForm } from "vee-validate";
import axios from "axios";
import ModalOverlay from "@/components/ModalOverlay.vue";
import OrderProductReview from "@/components/orders/OrderProductReview.vue";

export default {
  name: "ProfileView",
  data() {
    return {
      orders: [],
      passwordModalVisible: false,
      reviewModalVisible: false,
      newPassword2: "",
      newPassword: "",
      passwordErrorMessage: "",
      commentedOrder: {},
    };
  },
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { OrderProductReview, ModalOverlay, Button },
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

    const userStore = useUserStore();
    const submit = handleSubmit(async function (values) {
      const mainStore = useMainStore();
      const toastStore = useToastStore();
      try {
        await axios.patch("account/update", {
          first_name: values.fname,
          last_name: values.lname,
          phone: values.phone,
        });
        fname.value.value = values.fname;
        lname.value.value = values.lname;
        phone.value.value = values.phone;
        userStore.user.first_name = values.fname;
        userStore.user.last_name = values.fname;
        userStore.user.phone = values.phone;

        toastStore.displayToast(
          "Pomyślnie zaktualizowano informacje.",
          "success"
        );
      } catch (error) {
        toastStore.displayToast(
          "Nie udało się zaktualizować informacji.",
          "#E85959FF"
        );
      }
      mainStore.on();
    });

    fname.value.value = userStore.user.first_name;
    lname.value.value = userStore.user.last_name;
    phone.value.value = userStore.user.phone;
    return {
      fname,
      lname,
      phone,
      submit,
      handleReset,
    };
  },
  async created() {
    const ordersResponse = await axios.get("orders/");
    this.orders = ordersResponse.data;
  },
  methods: {
    openReviewModal(order) {
      this.reviewModalVisible = true;
      this.commentedOrder = order;
    },
    async handlePayment(order) {
      const toastStore = useToastStore();
      const data = [];
      order.products.forEach((el) =>
        data.push({
          name: el.product.name,
          count: el.count,
          price: el.price,
        })
      );
      try {
        const response = await axios.post("payments/create-session/", {
          data: data,
          shippingCost: order.shipping_cost,
          orderId: order.id,
        });
        window.location.href = response.data.session.url;
      } catch (error) {
        toastStore.displayToast("Operacja nie powiodła się.", "#E85959FF");
      }
    },
    async handlePasswordChange() {
      this.passwordErrorMessage = "";
      if (this.newPassword.length <= 3 || this.newPassword2.length <= 3) {
        this.passwordErrorMessage = "Hasło powinno być dłuższe od 3 znaków.";
        return;
      }
      if (this.newPassword !== this.newPassword2) {
        this.passwordErrorMessage = "Hasła nie są identyczne.";
        return;
      }
      await axios.patch("account/update", {
        password: this.password,
      });
      const toastStore = useToastStore();
      toastStore.displayToast("Pomyślnie zmieniono hasło", "success");
      this.passwordModalVisible = false;
      this.newPassword = "";
      this.newPassword2 = "";
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
  @include respond(md-desktop) {
    grid-template-columns: 1fr;
  }
}
.profile {
  grid-column: 2/3;
  display: grid;
  grid-template-columns: 0.5fr 1fr;
  grid-column-gap: 5rem;
  justify-items: stretch;
  color: var(--primary-white);
  @include respond(md-desktop) {
    grid-column: 1/2;
  }
  @include respond(tab-desktop) {
    grid-template-columns: 1fr;
  }
  @include respond(phone-lg) {
    margin-top: 3rem;
  }
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
  form {
    @include respond(tab-desktop) {
      width: 25rem;
    }
    @include respond(phone-md) {
      width: 20rem;
    }
    @include respond(phone-md-sm) {
      width: 16.5rem;
    }
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
  @include respond(tab-port) {
    overflow-x: auto;
  }
  .v-table {
    border-radius: 10px;
    @include respond(tab-port) {
      width: 55rem;
      overflow: auto !important;
      white-space: nowrap;
      display: unset;
      font-size: 0.65rem;
    }
    @include respond(phone-md-sm) {
      width: 25rem;
      font-size: 0.55rem;
    }
  }
  &__actions {
    button {
      width: 100%;
      @include respond(tab-port) {
        width: 1rem;
        height: 1rem;
        font-size: 0.5rem;
      }
    }
  }
}
.password-change {
  min-width: 25rem;
  @include respond(phone-lg) {
    margin-top: 3rem;
    width: 20rem;
    min-width: unset;
  }
  @include respond(phone-md-sm) {
    margin-top: 3rem;
    width: 16rem;
    min-width: unset;
  }
  p {
    height: 2rem;
  }
  &__button {
    margin-top: 1rem;
  }
}
.review-modal {
  h3 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  &__error {
    height: 2rem;
    font-size: 1.2rem;
    color: var(--primary-red);
  }
}
</style>
