<template>
  <Carousel />
  <v-lazy
    transition="fade-transition"
    v-model="sectionPopularVisible"
    min-height="5"
    :options="{
      threshold: 3,
    }"
  >
    <Section />
  </v-lazy>
  <v-lazy
    transition="fade-transition"
    v-model="isActive"
    min-height="5"
    :options="{
      threshold: 3,
    }"
  >
    <h1>EAEAEA</h1>
  </v-lazy>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import Section from "../components/Section.vue";
export default {
  name: "HomeView",
  data() {
    return {
      isActive: false,
      sectionPopularVisible: false,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Section,
    Carousel,
  },
};
</script>

<style scoped lang="scss"></style>
