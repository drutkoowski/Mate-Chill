<template>
  <Carousel />
  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <PopularCategories
        :categories="[
          {
            name: 'Yerba mate',
            url: '/logo.svg',
          },
          {
            name: 'Naczynka',
            url: '/naczynka-icon.svg',
          },
          {
            name: 'Bombille',
            url: '/bombilla-icon.svg',
          },
          {
            name: 'Zestawy',
            url: '/zestawy-icon.svg',
          },
        ]"
      />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <Section :headerText="'Nowości'" :items="latestProducts" />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <Section :headerText="'Bestsellery'" :items="latestProducts" />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <About />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <WebsiteFooter />
    </v-lazy>
  </v-sheet>

  <PolicyAcceptance />
</template>

<script>
import Carousel from "@/components/home/Carousel.vue";
import Section from "@/components/home/Section.vue";
import WebsiteFooter from "@/components/home/Footer.vue";
import About from "@/components/home/About.vue";
import PopularCategories from "@/components/home/PopularCategories.vue";
import PolicyAcceptance from "@/components/home/PolicyAcceptance.vue";
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    About,
    // eslint-disable-next-line vue/no-reserved-component-names
    Section,
    Carousel,
    WebsiteFooter,
    PopularCategories,
    PolicyAcceptance,
  },
  async beforeMount() {
    const latestProductsResponse = await axios.get("products/latest");
    this.latestProducts = latestProductsResponse.data;
  },
};
</script>

<style scoped lang="scss">
.slide-y-enter-active,
.slide-y-leave-active {
  transition: transform 1.2s cubic-bezier(0.25, 0.8, 0.5, 1), opacity 1.8s;
  opacity: 1;
}

.slide-y-enter-from,
.slide-y-leave-to {
  opacity: 0;
}

.slide-y-enter-from {
  transform: translateY(100px);
}

.slide-y-leave-to {
  transform: translateY(-100px);
}
</style>
