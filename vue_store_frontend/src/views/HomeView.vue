<template>
  <div class="home">
    <div class="product-container">
      <div
        class="product-item"
        v-for="product in latestProducts"
        :key="product.id"
      >
        <img class="prod-img" :src="product.image_url" alt="" />
        <h2>{{ product.name }}</h2>
        <p>{{ product.price }}</p>
        <div>
          <a :href="'/' + product.category.slug + '/' + product.slug">
            <button>View Item</button></a
          >
        </div>
      </div>
    </div>
    <router-view />
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
        .get("/api/v1/product/latest-products/")
        .then(
          (response) => (
            (this.latestProducts = response.data), console.log(response.data)
          )
        )
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
  margin: 20px;
  box-shadow: 1px 1px 3px gainsboro;
  padding: 20px;
}

.product-container {
  display: grid;
  justify-content: center;
  align-items: center;
  margin: 20px;
  height: auto;
  grid-template-columns: 1fr 1fr;
}

.prod-img {
  width: 200px;
  height: 250px;
}
</style>
