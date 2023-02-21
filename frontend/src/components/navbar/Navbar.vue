<template>
  <nav>
    <ul>
      <li>
        <router-link :to="{ name: 'home' }"
          ><img src="/logo.svg" alt="Site logo" class="logo"
        /></router-link>
      </li>

      <li class="site-name">
        <router-link :to="{ name: 'home' }"
          >Mate <span class="primary-green">&</span> Chill</router-link
        >
      </li>
      <li>
        <router-link :to="{ name: 'products' }">Produkty</router-link>
      </li>
      <li
        @click.prevent="this.$emit('openModal', 'login')"
        v-if="!userStore.isAuthenticated"
      >
        Zaloguj
      </li>
      <li
        @click.prevent="this.$emit('openModal', 'signup')"
        v-if="!userStore.isAuthenticated"
      >
        Zarejestruj
      </li>
      <li v-if="userStore.isAuthenticated">
        <router-link :to="{ name: 'profile' }">Twój Panel</router-link>
      </li>
      <li @click.prevent="userLogout" v-if="userStore.isAuthenticated">
        Wyloguj
      </li>

      <li class="cart">
        <router-link :to="{ name: 'cart' }"
          ><img class="cart-logo" src="/bag.svg" alt="Shopping cart logo" />
          <div>
            <span>{{ mainStore.cartItems.length }}</span>
          </div></router-link
        >
      </li>
    </ul>
    <LowerNav />
  </nav>
  <div class="navbar__phone">
    <router-link :to="{ name: 'home' }"
      ><img src="/logo.svg" alt="Site logo" class="logo"
    /></router-link>
    <h3>
      <router-link :to="{ name: 'home' }"
        >Mate <span class="primary-green">&</span> Chill</router-link
      >
    </h3>

    <svg
      @click.prevent="isHamburgerClicked = !isHamburgerClicked"
      height="34px"
      id="Layer_1"
      version="1.1"
      viewBox="0 0 28 28"
      width="40px"
      fill="currentColor"
      xml:space="preserve"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
    >
      <path
        d="M4,10h24c1.104,0,2-0.896,2-2s-0.896-2-2-2H4C2.896,6,2,6.896,2,8S2.896,10,4,10z M28,14H4c-1.104,0-2,0.896-2,2 s0.896,2,2,2h24c1.104,0,2-0.896,2-2S29.104,14,28,14z M28,22H4c-1.104,0-2,0.896-2,2s0.896,2,2,2h24c1.104,0,2-0.896,2-2 S29.104,22,28,22z"
      />
    </svg>
    <NavbarOverlay
      v-if="isHamburgerClicked"
      @openModal="
        this.$emit('openModal', type);
        isHamburgerClicked = !isHamburgerClicked;
      "
    />
  </div>
</template>

<script>
import LowerNav from "./LowerNav.vue";
import useUserStore from "@/stores/user";
import useToastStore from "@/stores/toast";
import useMainStore from "@/stores/main";
import userAuth from "@/utils/userAuth";
import NavbarOverlay from "@/components/navbar/NavbarOverlay.vue";

export default {
  name: "Navbar",
  components: {
    NavbarOverlay,
    LowerNav,
  },
  data() {
    return {
      isHamburgerClicked: false,
    };
  },
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
nav {
  @include respond(phone-lg) {
    display: none;
  }
}
.logo {
  height: 5rem;
  @include respond(tab-md) {
    height: 3rem;
  }
  @include respond(phone-md) {
    height: 2rem;
  }
}

.site-name {
  a,
  span {
    font-family: "Pacifico", cursive;
  }
}

.cart {
  position: relative;
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
    @include respond(tab-md) {
      width: 15px;
      height: 15px;
    }
    @include respond(phone-lg) {
      width: 12px;
      height: 12px;
    }
    span {
      font-size: 0.85rem;
      font-weight: bold;
      color: var(--primary-white);
      @include respond(tab-md) {
        font-size: 0.72rem;
      }
      @include respond(phone-lg) {
        text-align: center;
        font-size: 0.52rem;
      }
    }
  }
}

.cart-logo {
  height: 2rem;
  @include respond(tab-md) {
    height: 1.5rem;
  }
  @include respond(tab-md) {
    height: 1.25rem;
  }
}

ul {
  list-style: none;
  display: flex;
  align-items: center;
  column-gap: 30px;
  height: 5rem;
  @include respond(tab-md) {
    height: 3rem;
    margin-bottom: 2rem;
  }
  @include respond(tab-sm) {
    column-gap: 10px;
  }
  li {
    align-self: center;
    white-space: nowrap;
    font-size: 1.5rem;
    transition: all 0.3s ease-in;
    @include respond(tab-md) {
      font-size: 1rem;
    }
  }
  li:nth-of-type(2) {
    font-size: 2rem;
    color: var(--primary-white);
    @include respond(tab-md) {
      font-size: 1.5rem;
    }
    @include respond(phone-lg) {
      font-size: 1.25rem;
    }
    @include respond(phone-md) {
      font-size: 1rem;
    }
  }
}

ul li:nth-of-type(3) {
  color: var(--primary-white);
  margin-left: auto;
  cursor: pointer;
}

ul li:nth-of-type(4) {
  color: var(--primary-white);
  cursor: pointer;
}
ul li:nth-of-type(5) {
  color: var(--primary-white);
  cursor: pointer;
}

ul li:nth-of-type(6) {
  cursor: pointer;
}

ul li:nth-of-type(3):after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: var(--primary-green);
  transition: width 0.3s;
}

ul li:nth-of-type(4):after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: var(--primary-green);
  transition: width 0.3s;
}

ul li:nth-of-type(5):after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: var(--primary-green);
  transition: width 0.3s;
}

ul li:nth-of-type(3):hover::after {
  width: 100%;
}

ul li:nth-of-type(4):hover::after {
  width: 100%;
}

ul li:nth-of-type(5):hover::after {
  width: 100%;
}

ul li:hover {
  transform: scale(1.05);
}

.navbar__phone {
  display: none;
  @include respond(phone-lg) {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    position: fixed;
    z-index: 15;
    top: 0;
    left: 0;
    right: 0;
    padding: 10px 10px;
    background-color: var(--color-background);
    font-size: 2rem;
    color: var(--primary-white);
    column-gap: 1rem;
    img {
      width: 4rem;
      height: 4rem;
    }
    svg {
      height: 2rem;
      width: 2rem;
      margin-left: auto;
    }
    h3 {
      a,
      span {
        font-family: "Pacifico", cursive;
      }
    }
  }
}
</style>
