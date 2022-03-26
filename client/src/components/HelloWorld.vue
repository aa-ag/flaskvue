<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
  export default {
    name: 'hello',
    data() {
      return {
        msg: 'world!',
      };
    },
  };
</script>