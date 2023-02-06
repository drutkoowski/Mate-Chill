<template>
  <!--  navbar-->
  <Navbar />
  <RouterView />
</template>

<script>
import Navbar from "@/components/navbar/Navbar.vue";
export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style scoped></style>
