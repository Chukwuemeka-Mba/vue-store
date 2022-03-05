<template>
  <div class="home">
    <div
      class="products-container"
      v-for="product in latestProducts"
      :key="product.id"
    >
      <div class="product-item">
        <img :src="product.get_thumbnail" alt="" />
        <h2>{{ product.name }}</h2>
        <p>{{ prooduct.price }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products/")
        .then((response) => (this.latestProducts = response.data))
        .catch((error) => console.error(error));
    },
  },
};
</script>

<style scoped>
.home {
  font-family: "Fira Sans Extra Condensed", sans-serif;
}
.product-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.products-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 10px;
  box-shadow: 1px 1px 3px gainsboro;
}
</style>
