import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/HelloWorld.vue';

Vue.use(VueRouter);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/hello',
      name: 'hello',
      componen: HelloWorld,
    },
  ],
});
