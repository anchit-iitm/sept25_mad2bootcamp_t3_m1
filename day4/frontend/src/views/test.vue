<template>
    <div class="test_page">
        <h1>Test Page</h1>
        <TestComp1 />
        <input type="text" placeholder="Enter something..." v-model="this.theInput" />
        <p>You entered: {{ this.theInput }}</p>
    </div>
</template>

<script>
import TestComp1 from '../components/testComp.vue'
export default {
  name: 'TestPage',
  components: {
    TestComp1
  },
  data() {
    return {
      theInput: null
    }
  }
}
</script>