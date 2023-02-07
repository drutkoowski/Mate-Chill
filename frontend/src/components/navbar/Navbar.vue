<template>
  <nav>
    <ul>
      <li>
        <router-link :to="{ name: 'home' }"
          ><img src="/logo.svg" alt="Site logo" class="logo"
        /></router-link>
      </li>

      <li>
        <router-link :to="{ name: 'home' }"
          >Mate <span class="primary-green">&</span> Chill</router-link
        >
      </li>

      <li @click.prevent="this.$emit('openModal', 'login')">Zaloguj</li>
      <li @click.prevent="this.$emit('openModal', 'signup')">Zarejestruj</li>

      <li>
        <router-link :to="{ name: 'products' }">Produkty</router-link>
      </li>

      <li class="cart">
        <img class="cart-logo" src="/bag.svg" alt="Shopping cart logo" />
        <div>
          <span>1</span>
        </div>
      </li>
    </ul>
    <LowerNav />
  </nav>
</template>

<script>
import LowerNav from "./LowerNav.vue";
export default {
  name: "Navbar",
  components: {
    LowerNav,
  },
};
</script>

<style scoped lang="scss">
.logo {
  height: 5rem;
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
    span {
      font-size: 1rem;
      font-weight: bold;
      color: var(--primary-white);
    }
  }
}

.cart-logo {
  height: 2rem;
}

ul {
  list-style: none;
  display: flex;
  align-items: center;
  column-gap: 30px;
  height: 5rem;
  li {
    align-self: center;
    white-space: nowrap;
    font-size: 1.5rem;
    transition: all 0.3s ease-in;
  }
  li:nth-of-type(2) {
    font-size: 2rem;
    color: var(--primary-white);
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
</style>
