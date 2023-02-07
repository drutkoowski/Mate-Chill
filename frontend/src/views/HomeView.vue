<template>
  <Carousel />
  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      :model="sectionPopularVisible"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <Section :headerText="'Popularne kategorie'" />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      :model="sectionNewVisible"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <Section :headerText="'Nowości'" />
    </v-lazy>
  </v-sheet>

  <v-sheet min-height="250" class="fill-height" color="transparent">
    <v-lazy
      transition="slide-y"
      :model="sectionBestsellerVisible"
      min-height="5"
      :options="{
        threshold: 0.5,
      }"
    >
      <Section :headerText="'Bestsellery'" />
    </v-lazy>
  </v-sheet>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import Section from "../components/Section.vue";
export default {
  name: "HomeView",
  data() {
    return {
      sectionPopularVisible: false,
      sectionNewVisible: false,
      sectionBestsellerVisible: false,
    };
  },
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Section,
    Carousel,
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
