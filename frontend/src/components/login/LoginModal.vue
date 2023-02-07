<template>
  <div class="login">
    <h3>Zaloguj się</h3>
    <form @submit.prevent="submit">
      <v-text-field
        v-model="email.value.value"
        :error-messages="email.errorMessage.value"
        label="E-mail"
      ></v-text-field>

      <v-text-field
        v-model="password.value.value"
        :error-messages="password.errorMessage.value"
        label="Password"
      ></v-text-field>

      <Button :text="'Zaloguj'" class="button" />
      <Button :text="'Wyczyść'" class="button" @click="handleReset" />
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useField, useForm } from "vee-validate";
import Button from "@/components/Button.vue";

export default {
  name: "LoginModal",
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  setup() {
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        email(value) {
          if (/^[a-z.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) return true;

          return "Mail must be a valid email.";
        },
      },
    });
    const email = useField("email");
    const password = useField("password");

    const items = ref(["Item 1", "Item 2", "Item 3", "Item 4"]);

    const submit = handleSubmit((values) => {
      alert(JSON.stringify(values, null, 2));
    });

    return { email, password, items, submit, handleReset };
  },
};
</script>

<style scoped lang="scss">
.login {
  width: 45rem;
  padding: 0 5rem;
  h3 {
    font-size: 2rem;
  }
}
.button {
  margin: 0 1rem;
}
</style>
