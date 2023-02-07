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
  setup() {
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        email(value) {
          if (/^[a-z.-]+@[a-z.-]+[0-9]\.[a-z]+$/i.test(value)) return true;

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

    const submit = handleSubmit((values) => {
      alert(JSON.stringify(values, null, 2));
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
