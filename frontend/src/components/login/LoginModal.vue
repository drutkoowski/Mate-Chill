<template>
  <div class="login">
    <h3>Zaloguj się</h3>
    <form @submit.prevent="submit">
      <v-text-field
        v-model="email.value.value"
        :error-messages="email.errorMessage.value"
        bg-color="white"
        color="green-darken-1"
        hint="Pole powinno zawierać poprawny adres e-mail."
        label="Adres Email"
      ></v-text-field>

      <v-text-field
        v-model="password.value.value"
        :error-messages="password.errorMessage.value"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        bg-color="white"
        color="green-darken-1"
        label="Hasło"
        hint="Hasło powinno zawierać conajmniej 8 znaków"
        counter
        @click:append="showPassword = !showPassword"
      ></v-text-field>
      <div class="mt-5">
        <Button :text="'Zaloguj'" class="button" type="submit" />
        <Button :text="'Wyczyść'" class="button" @click.prevent="handleReset" />
      </div>
    </form>
  </div>
</template>

<script>
import { useField, useForm } from "vee-validate";
import axios from "axios";
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import Button from "@/components/Button.vue";

export default {
  name: "LoginModal",
  data() {
    return {
      showPassword: false,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  emits: ["closeModal"],
  setup(props, context) {
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        email(value) {
          if (/^[a-z0-9.]{1,64}@[a-z0-9.]{1,64}$/i.test(value)) return true;

          return "Pole musi zawierać poprawny adres e-mail.";
        },
        password(value) {
          if (value?.length >= 8) return true;

          return "Hasło musi składać się z conajmniej 8 znaków.";
        },
      },
    });
    const email = useField("email");
    const password = useField("password");

    const submit = handleSubmit(async function (values) {
      const response = await axios.post("auth/login/", values);
      if (response.status === 200) {
        const userStore = useUserStore();
        const toastStore = useToastStore();
        toastStore.displayToast("Pomyślnie zalogowano.", "success");
        userStore.isAuthenticated = true;
        context.emit("closeModal");
      }
    });

    return { email, password, submit, handleReset };
  },
};
</script>

<style scoped lang="scss">
.login {
  width: 35rem;
  padding: 0 2rem;
  h3 {
    font-size: 2rem;
    color: var(--primary-white);
  }
}
.button {
  margin: 0 1rem;
}
</style>
