<template>
  <div>
    <nav>
      <div>
        <router-link to="/"><h1 class="">Store</h1></router-link>
      </div>

      <div class="nav-links">
        <div class="nav-links">
          <router-link to="/summer">Summer</router-link>
          <router-link to="/winter">Winter</router-link>
        </div>
        <div class="nav-links">
          <router-link to="/login" class="login">Login</router-link>
          <router-link to="/cart" class="cart">
            <span><i class="fas fa-shopping-cart"></i></span>
            <span>Cart</span>
          </router-link>
        </div>
      </div>
      <!-- <div v-show="isMobile" @click="isMobile = !isMobile">
        <i class="fas fa-bars"></i>
      </div> -->
    </nav>
    <router-view />

    <div class="footer">
      <p>built with ❤️ by emeka</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMobile: false,
    };
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Fira+Sans+Extra+Condensed:wght@200&display=swap");
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(30, 33, 37);
  color: white;
  padding: 10px;
  margin: 0px;
  font-family: "Fira Sans Extra Condensed", sans-serif;
}
body {
  margin: 0px;
}
.nav-links {
  display: flex;
  gap: 20px;
  list-style-type: none;
}
.nav-links a {
  padding: 5px 10px;
  border-radius: 5px;
  color: white;
}
a {
  text-decoration: none;
}

nav h1 {
  color: green;
}

.cart {
  background-color: rgb(14, 138, 14);
}
.cart span {
  margin: 5px;
}
.login {
  background-color: rgb(124, 121, 121);
}

.footer {
  font-family: "Fira Sans Extra Condensed", sans-serif;
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 2.5rem; /* Footer height */
}

.footer p {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 10px 5px;
}
</style>
