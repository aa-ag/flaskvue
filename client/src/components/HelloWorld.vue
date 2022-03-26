<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script>
  export default {
    name: 'hello',
    data() {
      return {
        message: 'world!',
      };
    },
  };
</script>