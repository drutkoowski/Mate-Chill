<template>
  <PageOverlay :closeAvailable="true">
    <img src="/logo.svg" alt="Site logo" class="page-overlay__logo" />
    <div class="navbar">
      <p>
        <router-link :to="{ name: 'products' }">Produkty</router-link>
      </p>
      <p
        @click.prevent="this.$emit('openModal', 'login')"
        v-if="!userStore.isAuthenticated"
      >
        Zaloguj
      </p>
      <p
        @click.prevent="this.$emit('openModal', 'signup')"
        v-if="!userStore.isAuthenticated"
      >
        Zarejestruj
      </p>
      <p v-if="userStore.isAuthenticated">
        <router-link :to="{ name: 'profile' }">Twój Panel</router-link>
      </p>
      <p @click.prevent="userLogout" v-if="userStore.isAuthenticated">
        Wyloguj
      </p>

      <div class="cart">
        <p>Koszyk</p>
        <div>
          <img class="cart-logo" src="/bag.svg" alt="Shopping cart logo" />
          <div>
            <span>{{ mainStore.cartItems.length }}</span>
          </div>
        </div>
      </div>
    </div>
    <span class="page-overlay__close" @click.prevent="this.$emit('hideOverlay')"
      >&#10005;</span
    >
  </PageOverlay>
</template>

<script>
import PageOverlay from "@/components/PageOverlay.vue";
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import useMainStore from "@/stores/main";
import userAuth from "@/utils/userAuth";
export default {
  name: "NavbarOverlay",
  components: { PageOverlay },
  setup() {
    const userStore = useUserStore();
    const mainStore = useMainStore();
    return { userStore, mainStore };
  },
  emits: ["openModal"],
  methods: {
    async userLogout() {
      await userAuth.logoutUser();
      const toastStore = useToastStore();
      toastStore.displayToast("Wylogowano z konta.", "red-lighten-1");
    },
  },
};
</script>

<style scoped lang="scss">
.navbar {
  display: flex;
  flex-direction: column;
  row-gap: 1.5rem;
  width: 30rem;
  p {
    font-size: 2rem;
    text-align: center;
  }
  &__categories {
    font-size: 0.75rem;
  }
}

.cart {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  div {
    img {
      margin-left: 1rem;
      height: 2rem;
    }
    div {
      display: flex;
      justify-content: center;
      align-content: center;
      position: absolute;
      top: 75%;
      left: 75%;
      background-color: var(--primary-green);
      width: 20px;
      height: 20px;
      border-radius: 20px;
      span {
        font-size: 0.85rem;
        font-weight: bold;
        color: var(--primary-white);
      }
    }
  }
}
.page-overlay__close {
  position: fixed;
  top: 2%;
  right: 5%;
}

.page-overlay__logo {
  position: fixed;
  top: 2%;
  left: 5%;
  height: 3rem;
  width: 2rem;
}
</style>
