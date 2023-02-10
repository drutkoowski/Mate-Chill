<template>
  <div class="policy" v-if="!mainStore.isPolicyAccepted">
    <p>
      Używamy niezbędnych plików cookie, aby nasza strona mogła działać. <br />
      Korzystając z niej, automatycznie zgadzasz się na wykorzystanie plików
      cookie zgodnie z opisem w naszej Polityce Cookies.
    </p>
    <Button
      :text="'Akceptuj'"
      class="policy__accept"
      @click.prevent="mainStore.acceptPolicy"
    />
  </div>
</template>

<script>
import useMainStore from "@/stores/main";
import Button from "@/components/Button.vue";

export default {
  name: "PolicyAcceptance",
  // eslint-disable-next-line vue/no-reserved-component-names
  components: { Button },
  setup() {
    const mainStore = useMainStore();
    return { mainStore };
  },
};
</script>

<style scoped lang="scss">
.policy {
  position: fixed;
  bottom: 20px;
  width: 40rem;
  padding: 1rem 2rem;
  font-size: 1rem;
  background-color: var(--primary-white);
  color: var(--primary-green);
  border-radius: 10px;
  &__accept {
    float: right;
  }
}
</style>
