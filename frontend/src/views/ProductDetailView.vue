<template>
  <div class="wrapper">
    <div class="product-image-container">
      <ProductGallery />
    </div>
    <div class="product-info-container">2</div>
  </div>
</template>

<script>
import ProductGallery from "@/components/products/ProductGallery.vue";
export default {
  name: "ProductDetailView",
  components: { ProductGallery },
};
</script>

<style scoped lang="scss">
.wrapper {
  flex-grow: 1;
  display: grid;
  grid-template-columns: 0.7fr 1fr;
  padding: 0 5rem;
  grid-column-gap: 5rem;
  justify-items: center;
  align-items: center;
  margin-top: 5rem;
}
.product-image-container {
  padding: 0 2rem;
  height: 100%;
  width: 30rem;
}
.product-info-container {
}
</style>
