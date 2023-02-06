<template>
  <div class="lower-nav__wrapper">
    <ul>
      <ExpandableCard
        :text="'Yerba Mate'"
        :cols="3"
        :items="{
          countries: ['Urugwaj', 'Argentyna', 'Brazylia', 'Peru'],
          type: ['Klasyczne', 'Pobudzające', 'Smakowe', 'Ziołowe'],
          brand: ['Producent1', 'Producent2', 'Producent3', 'Producent4'],
        }"
      />
      <ExpandableCard
        :text="'Bombille'"
        :cols="1"
        :items="[
          { title: 'Paragwaj' },
          { title: 'Urugwaj' },
          { title: 'Argentyna' },
          { title: 'Brazylia' },
          { title: 'Peru' },
        ]"
      />
      <ExpandableCard
        :text="'Naczynka'"
        :cols="1"
        :items="[
          { title: 'Paragwaj' },
          { title: 'Urugwaj' },
          { title: 'Argentyna' },
          { title: 'Brazylia' },
          { title: 'Peru' },
        ]"
      />
      <ExpandableCard
        :text="'Zestawy'"
        :cols="1"
        :items="[
          { title: 'Paragwaj' },
          { title: 'Urugwaj' },
          { title: 'Argentyna' },
          { title: 'Brazylia' },
          { title: 'Peru' },
        ]"
      />
      <ExpandableCard
        :text="'Kawy'"
        :cols="1"
        :items="[
          { title: 'Paragwaj' },
          { title: 'Urugwaj' },
          { title: 'Argentyna' },
          { title: 'Brazylia' },
          { title: 'Peru' },
        ]"
      />
      <ExpandableCard
        :text="'Herbaty'"
        :cols="1"
        :items="[
          { title: 'Paragwaj' },
          { title: 'Urugwaj' },
          { title: 'Argentyna' },
          { title: 'Brazylia' },
          { title: 'Peru' },
        ]"
      />
    </ul>
  </div>
</template>

<script>
import ExpandableCard from "./ExpandableCard.vue";
export default {
  name: "LowerNav.vue",
  data() {
    return {
      isExpanded: false,
    };
  },
  components: {
    ExpandableCard,
  },
};
</script>

<style scoped lang="scss">
.lower-nav__wrapper {
  display: grid;
  grid-template-columns: 0.3fr auto 0.3fr;
}
ul {
  grid-column: 2/3;
  display: inline-flex;
  justify-content: space-between;
  list-style: none;
  color: var(--primary-white);
}
</style>
