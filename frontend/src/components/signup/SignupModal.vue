<template>
  <div class="signup">
    <h3>Załóż konto</h3>
    <form @submit.prevent="submit">
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
        bg-color="white"
        color="green-darken-1"
        hint="Numer telefonu powinien składać się z 9 cyfr."
        label="Telefon"
      ></v-text-field>

      <v-text-field
        v-model="email.value.value"
        :error-messages="email.errorMessage.value"
        bg-color="white"
        color="green-darken-1"
        hint="Pole powinno zawierać poprawny adres e-mail."
        label="E-mail"
      ></v-text-field>

      <v-text-field
        v-model="password.value.value"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        :error-messages="password.errorMessage.value"
        bg-color="white"
        color="green-darken-1"
        label="Hasło"
        hint="Hasło powinno zawierać conajmniej 8 znaków"
        counter
        @click:append="showPassword = !showPassword"
      ></v-text-field>

      <v-text-field
        v-model="passwordConfirm.value.value"
        :append-icon="showPasswordConfirm ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPasswordConfirm ? 'text' : 'password'"
        :error-messages="passwordConfirm.errorMessage.value"
        bg-color="white"
        color="green-darken-1"
        label="Potwierdź hasło"
        hint="Hasła powinny być identyczne."
        counter
        @click:append="showPasswordConfirm = !showPasswordConfirm"
      ></v-text-field>

      <div class="mt-5">
        <Button :text="'Załóż konto'" class="button" type="submit" />
        <Button :text="'Wyczyść'" class="button" @click.prevent="handleReset" />
      </div>
    </form>
  </div>
</template>

<script>
import { useField, useForm } from "vee-validate";
import Button from "@/components/Button.vue";

export default {
  name: "SignupModal",
  data() {
    return {
      showPassword: false,
      showPasswordConfirm: false,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
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
        email(value) {
          if (/^[a-z.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) return true;

          return "Pole musi zawierać poprawny adres e-mail.";
        },
        password(value) {
          if (value?.length >= 3) return true;

          return "Hasło musi składać się z conajmniej trzech znaków.";
        },

        passwordConfirm(value) {
          if (value?.length >= 3) return true;

          return "Hasła muszą być identyczne.";
        },
      },
    });
    const fname = useField("fname");
    const lname = useField("lname");
    const phone = useField("phone");
    const email = useField("email");
    const password = useField("password");
    const passwordConfirm = useField("passwordConfirm");

    const submit = handleSubmit((values) => {
      alert(JSON.stringify(values, null, 2));
    });

    return {
      fname,
      lname,
      phone,
      email,
      password,
      passwordConfirm,
      submit,
      handleReset,
    };
  },
};
</script>

<style scoped lang="scss">
.signup {
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
