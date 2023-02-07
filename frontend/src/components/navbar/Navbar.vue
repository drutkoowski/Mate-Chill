<template>
  <nav>
    <ul>
      <li><img src="/logo.svg" alt="Site logo" class="logo" /></li>
      <li>Mate <span class="primary-green">&</span> Chill</li>
      <li @click.prevent="this.$emit('openModal', 'login')">Zaloguj</li>
      <li @click.prevent="this.$emit('openModal', 'signup')">Zarejestruj</li>
      <li>Produkty</li>
      <li class="cart">
        <img class="cart-logo" src="/bag.svg" alt="Shopping cart logo" />
        <span>0</span>
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
  span {
    position: absolute;
    top: 40%;
    left: 75%;
    font-size: 1.3rem;
    color: var(--primary-white);
    font-weight: bold;
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
