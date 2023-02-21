<template>
  <div class="wrapper">
    <div class="product-image-container">
      <ProductGallery :slides="images" />
    </div>
    <div class="product-info-container">
      <h1>{{ item.name }}</h1>
      <div class="product-info-container__rating" v-if="item.reviews">
        <v-rating v-model="item.rating" readonly color="white" />
        <span
          >{{ item.rating.toFixed(2) }}/5.00
          <span
            class="text-stone-50 product-info-container__rating__counter"
            @click.prevent="openReviewModal"
            >({{ item.reviews?.length }} opinie)</span
          ></span
        >
      </div>
      <div class="product-info-container__description mt-5">
        <p>
          <span class="primary-green">Producent: </span>
          {{ item.manufacturer?.name }}
        </p>
        <p>
          <span class="primary-green">Dostępność: </span>
          <v-icon :color="counterColor" size="16">mdi-circle</v-icon>
          {{ item.num_available }}
        </p>
        <p>
          <span class="primary-green">Kraj producenta: </span>
          {{ item.country }}
        </p>
        <p><span class="primary-green">Opis: </span> {{ item.description }}</p>
      </div>

      <div class="product-info-container__customizable" v-if="hasVariants">
        <variationFilter
          class="mt-2"
          :text="'Warianty'"
          :items="variants"
          @handleRedirect="changeRoute"
        />
      </div>
      <h3 class="product-info-container__price">
        {{ item.price }} <small>zł brutto / szt. </small>
      </h3>
      <div class="product-info-container__actions">
        <div class="product-info-container__actions__counter">
          <ProductCounter
            :itemCounter="itemCounter"
            @minus="itemCounter--"
            @plus="handlePlus"
          />
        </div>
        <Button :text="'Dodaj do koszyka'" @click.prevent="addToCart" />
      </div>
      <p class="mt-2">Suma {{ (itemCounter * item.price).toFixed(2) }} zł</p>
      <ShippingInfo />
    </div>
  </div>
  <ModalOverlay @closeModal="hideReviewModal" v-if="reviewModalVisible">
    <div class="review-modal">
      <h3>Opinie do produktu {{ item.name }}</h3>
      <ReviewsList :reviews="item.reviews" v-if="item.reviews.length > 0" />
      <p class="my-auto text-stone-200" v-else>Brak dodanych opinii.</p>
      <div class="review-modal__add" v-if="isBuyer">
        <form @submit="reviewProduct">
          <v-textarea
            label="Treść Twojej opinii"
            bg-color="white"
            v-model="reviewContent.value.value"
          />
          <p class="review-modal__error">{{ reviewErrorMessage }}</p>
          <div>
            <v-rating
              color="#04b60e"
              hover
              v-model="starsCount.value.value"
            ></v-rating>
          </div>
          <Button :text="'Dodaj opinię'" type="submit" />
        </form>
      </div>
      <span v-else
        >Tylko zalogowani użytkownicy, którzy zakupili produkt, mogą dodać
        opinię.</span
      >
    </div>
  </ModalOverlay>
</template>

<script>
import ProductGallery from "@/components/products/ProductGallery.vue";
import Button from "@/components/Button.vue";
import VariationFilter from "@/components/filters/variationFilter.vue";
import ShippingInfo from "@/components/products/product/shippingInfo.vue";
import ProductCounter from "@/components/ProductCounter.vue";
import ModalOverlay from "@/components/ModalOverlay.vue";
import ReviewsList from "@/components/reviews/ReviewsList.vue";
import cookies from "@/utils/cookies";
import useToastStore from "@/stores/toast";
import useUserStore from "@/stores/user";
import axios from "axios";
import { useField, useForm } from "vee-validate";
import { ref } from "vue";

export default {
  name: "ProductDetailView",
  components: {
    ModalOverlay,
    ProductCounter,
    ShippingInfo,
    VariationFilter,
    ReviewsList,
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
    ProductGallery,
  },
  setup() {
    const reviewErrorMessage = ref("");
    const reviewModalVisible = ref(false);
    const isBuyer = ref(false);
    const userStore = ref(useUserStore());
    const item = ref({});
    const reviewContent = useField("reviewContent");
    const starsCount = useField("starsCount");
    const { handleSubmit, handleReset } = useForm({});
    const openReviewModal = function () {
      isBuyer.value =
        userStore.value.user.products_bought?.filter(
          (obj) => obj.id === item.value.id
        ).length > 0;
      if (item.value.reviews.length > 0 || isBuyer.value) {
        reviewModalVisible.value = true;
      } else {
        const toastStore = useToastStore();
        toastStore.displayToast(
          "Tylko zalogowani użytkownicy, którzy zakupili produkt, mogą dodać opinię.",
          "#E85959FF"
        );
      }
    };
    const hideReviewModal = function () {
      reviewModalVisible.value = false;
    };
    const reviewProduct = handleSubmit(async function () {
      reviewErrorMessage.value = "";
      if (starsCount.value.value && reviewContent.value.value.length > 3) {
        const toastStore = useToastStore();
        try {
          await axios.post("reviews/create", {
            product: item.value.id,
            content: reviewContent.value.value,
            stars: starsCount.value.value,
          });
          toastStore.displayToast("Opinia została dodana pomyślnie", "success");
        } catch (error) {
          toastStore.displayToast(
            "Dodawanie opinii nie powiodło się.",
            "#E85959FF"
          );
        }
        hideReviewModal();
        return;
      }
      return (reviewErrorMessage.value =
        "Pole komentarza powinno zawierać conajmniej 3 znaki.");
    });
    return {
      isBuyer,
      userStore,
      item,
      reviewModalVisible,
      starsCount,
      reviewContent,
      reviewErrorMessage,
      reviewProduct,
      handleReset,
      openReviewModal,
      hideReviewModal,
    };
  },
  async created() {
    await this.fetchData();
  },
  data: () => ({
    images: [],
    itemCounter: 1,
    maxAvailable: 0,
    counterColor: "green",
    hasVariants: false,
    variants: [],
  }),
  methods: {
    handlePlus() {
      const toastStore = useToastStore();
      this.itemCounter < this.maxAvailable
        ? this.itemCounter++
        : toastStore.displayToast(
            "Wybrano maksymalną dostępną ilość produktu.",
            "#E85959FF"
          );
    },
    slugify(string) {
      return string
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, "")
        .replace(/[\s_-]+/g, "-")
        .replace(/^-+|-+$/g, "");
    },
    async changeRoute(e) {
      this.$router.push({
        name: "product-detail",
        params: {
          productSlug: this.slugify(e),
        },
      });
    },
    async fetchData() {
      try {
        const productSlug = this.$route.params.productSlug;
        const response = await axios.get(`products/${productSlug}`);
        this.item = response.data;
        this.maxAvailable = response.data.num_available;
        if (response.data.num_available < 5) this.counterColor = "#EE0D0DFF";
        else if (
          response.data.num_available >= 5 &&
          response.data.num_available <= 15
        )
          this.counterColor = "#ff8604";
        else {
          this.counterColor = "#04B60EFF";
        }
        let images = [this.item.main_image];
        if (this.item.images.length > 0)
          images = [...this.item.images.map((element) => element.image)];
        this.images = images;
      } catch (error) {
        this.$router.push({ name: "products" });
      }
    },
    addToCart() {
      const store = useToastStore();
      if (this.itemCounter > 0) {
        cookies.setCartCookie({
          id: this.item.id,
          count: this.itemCounter,
        });
        this.itemCounter = 1;
        store.displayToast("Produkt dodany do koszyka", "success");
      } else {
        store.displayToast("Wybierz ilość produktu", "#E85959FF");
      }
    },
    getVariants() {
      const variants = [];
      this.item?.variants.forEach((item) => variants.push(item.name));
      this.item?.parent ? variants.push(this.item?.parent.name) : null;
      this.item?.parent?.variants.forEach((item) => {
        if (item.name !== this.item.name) variants.push(item.name);
      });
      this.variants = variants;
    },
  },
  watch: {
    async $route() {
      await this.fetchData();
    },
    item() {
      const variantsCount =
        this.item?.variants.length +
        (this.item?.parent ? 1 : 0) +
        (this.item?.parent?.variants.length
          ? this.item?.parent?.variants.length
          : 0);
      if (variantsCount > 0) {
        this.getVariants();
        this.hasVariants = true;
        return;
      }
      this.hasVariants = false;
    },
  },
};
</script>

<style scoped lang="scss">
.wrapper {
  flex-grow: 1;
  display: grid;
  grid-template-columns: 0.7fr 1fr;
  padding: 0 5rem;
  grid-column-gap: 5rem;
  margin-top: 5rem;
}
.product-image-container {
  height: 100%;
  width: 30rem;
  justify-self: center;
}
.product-info-container {
  &__description {
    p {
      margin-top: 0.5rem;
    }
  }

  &__rating {
    display: flex;
    align-items: center;
    &__counter {
      cursor: pointer;
      transition: all 0.3s ease-in;
    }
  }
  &__customizable {
    display: flex;
    align-items: center;
    width: 25rem;
  }
  &__price {
    font-size: 2rem;
    font-weight: bolder;
    color: var(--primary-green);
    small {
      font-weight: normal;
      font-size: 1rem;
      color: var(--primary-white);
    }
  }
  h1 {
    font-size: 2rem;
    font-weight: bold;
    color: var(--primary-green);
  }
  p {
    font-size: 1.2rem;
    color: var(--primary-white);
  }
}

.product-info-container__actions {
  display: flex;
  column-gap: 2rem;
  margin-top: 2rem;
  &__counter {
    display: flex;
    align-items: center;
    height: 3rem;
    width: 7rem;
    border-radius: 5px;
    padding: 0 5px;
    outline: 1px solid var(--primary-white);
    h5 {
      color: var(--color-background);
    }
    .v-icon {
      width: 2rem;
      cursor: pointer;
      transition: all 0.3s ease-in-out;
      &:hover {
        transform: scale(1.15);
      }
    }
  }
  button {
    height: 3rem;
  }
}
.review-modal {
  width: 45rem;
  height: 35rem;
  overflow-y: scroll;
  -ms-overflow-style: none; /* Internet Explorer 10+ */
  scrollbar-width: none;
  display: flex;
  flex-direction: column;
  &::-webkit-scrollbar {
    display: none; /* Safari and Chrome */
  }
  .review-list {
    flex-grow: 1;
    overflow-y: scroll;
    -ms-overflow-style: none; /* Internet Explorer 10+ */
    scrollbar-width: none;
    margin-bottom: 0.5rem;
  }
  .review-list::-webkit-scrollbar {
    display: none; /* Safari and Chrome */
  }
  &__add {
    margin-top: auto;
  }
}

.review-modal__error {
  height: 2rem;
}
</style>
