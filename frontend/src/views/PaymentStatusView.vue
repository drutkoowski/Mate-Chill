<template>
  <div class="order-response-wrapper" v-if="isSuccess">
    <v-icon size="200" color="#04b60e">mdi-check-circle</v-icon>
    <h3 class="primary-green">Twoje zamówienie zostało opłacone pomyślnie!</h3>
    <p>
      Dziękujemy za zakupy oraz zaufanie, proces wysyłania produktu właśnie się
      rozpoczął.
    </p>
    <h5>Sprawdź swoje zamówienia</h5>
  </div>
  <div class="order-response-wrapper" v-else>
    <v-icon size="200" color="#EE0D0DFF">mdi-alert-circle</v-icon>
    <h3 class="primary-red">Twoje zamówienie nie zostało jeszcze opłacone!</h3>
    <p>
      Prosimy o jak najszybsze uregulowanie zamówienia, abyśmy byli w stanie
      wysłać produkty. <br />W razie problemów z płatnością, skontaktuj się z
      działem pomocy.
    </p>
    <Button :text="'Sprawdź swoje zamówienia'" class="button" />
  </div>
</template>

<script>
import axios from "axios";
import Button from "@/components/Button.vue";

export default {
  name: "PaymentStatus",
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { Button },
  data() {
    return {
      isSuccess: false,
    };
  },
  async beforeCreate() {
    const orderId = this.$route.params.orderId;
    const response = await axios.get(`orders/${orderId}`);
    this.isSuccess = response.data.status === "opłacone";
    response.data.status === "zakończone"
      ? this.$router.push({ name: "home" })
      : null;
  },
};
</script>

<style scoped lang="scss">
.order-response-wrapper {
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
    font-size: 1.25rem;
    text-align: center;
  }
  .button {
    margin-top: 3rem;
  }
}
</style>
