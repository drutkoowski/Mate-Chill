<template>
  <nav>
    <ul>
      <li><img src="/logo.svg" alt="Site logo" class="logo" /></li>
      <li>Mate <span class="primary-green">&</span> Chill</li>
      <li></li>
      <li>Zaloguj</li>
      <li>Zarejestruj</li>
      <li>Produkty</li>
      <li>
        <img class="cart-logo" src="/bag.svg" alt="Shopping cart logo" />
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
  height: 100%;
}

.cart-logo {
  height: 2rem;
}
ul {
  list-style: none;
  display: table;

  border-collapse: separate;
  border-spacing: 10px;
  -webkit-border-horizontal-spacing: 30px;
  li {
    display: table-cell;
    vertical-align: middle;
    height: 5rem;
    white-space: nowrap;
    font-size: 1.5rem;
    transition: all 0.3s ease-in;
  }
  li:nth-of-type(2) {
    font-size: 2rem;
    color: var(--primary-white);
  }
  li:nth-of-type(3) {
    width: 100%;
  }
}

ul li:not(:nth-of-type(3)) {
  cursor: pointer;
}

ul li:nth-of-type(4) {
  color: var(--primary-white);
}

ul li:nth-of-type(5) {
  color: var(--primary-white);
}
ul li:nth-of-type(6) {
  color: var(--primary-white);
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

ul li:nth-of-type(6):after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: var(--primary-green);
  transition: width 0.3s;
}

ul li:nth-of-type(4):hover::after {
  width: 100%;
}

ul li:nth-of-type(5):hover::after {
  width: 100%;
}

ul li:nth-of-type(6):hover::after {
  width: 100%;
}

ul li:hover {
  transform: scale(1.05);
}
</style>
