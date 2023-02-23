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
      <FormMessage :text="errorMsg" />
      <div class="login__buttons">
        <Button :text="'Zaloguj'" class="button" type="submit" />
        <Button :text="'Wyczyść'" class="button" @click.prevent="handleClear" />
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
import FormMessage from "@/components/FormMessage.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "LoginModal",
  props: {
    next: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      showPassword: false,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    FormMessage,
  },
  emits: ["closeModal"],
  setup(props, context) {
    let errorMsg = ref("");
    const { handleSubmit, handleReset } = useForm({
      validationSchema: {
        email(value) {
          if (
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
              value
            )
          )
            return true;

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
    const router = useRouter();

    const submit = handleSubmit(async function (values) {
      try {
        const response = await axios.post("auth/login/", values);
        if (response.status === 200) {
          errorMsg.value = "";
          const userStore = useUserStore();
          const toastStore = useToastStore();
          toastStore.displayToast("Pomyślnie zalogowano.", "success");
          userStore.isAuthenticated = true;
          const currentUser = await axios.get("me/");
          userStore.user = currentUser.data;
          context.emit("closeModal");
          if (props.next) {
            router.push({ name: props.next });
          }
        }
      } catch (error) {
        error.response.status === 401
          ? (errorMsg.value = "Błędne dane do logowania.")
          : (errorMsg.value =
              "Nie udało się zalogować użytkownika z tymi danymi.");
      }
    });

    return { email, password, submit, handleReset, errorMsg };
  },
  methods: {
    handleClear() {
      this.errorMsg = "";
      this.handleReset();
    },
  },
};
</script>

<style scoped lang="scss">
.login {
  width: 35rem;
  padding: 0 2rem;
  @include respond(tab-sm) {
    width: 30rem;
    padding: 0 1rem;
  }
  @include respond(phone-lg) {
    width: 25rem;
    height: 20rem;
  }
  @include respond(phone-md) {
    width: 100%;
    height: 20rem;
  }
  h3 {
    font-size: 2rem;
    color: var(--primary-white);
    @include respond(phone-lg) {
      margin: 1rem 0;
    }
  }
  &__buttons {
    display: flex;
    justify-content: center;
  }
}
.button {
  margin: 0 1rem;
}
</style>
