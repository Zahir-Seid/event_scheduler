<template>
  <v-footer
    fixed
    height="auto"
    class="custom-footer pa-4"
  >
    <v-container fluid>
      <v-row
        align="center"
        justify="space-between"
        class="flex-wrap"
      >
        <!-- Logo and Name -->
        <v-col
          cols="12"
          md="4"
          class="d-flex align-center"
        >
          <div class="icon-bg d-flex align-center justify-center">
            <v-icon size="28" color="white">mdi-calendar-month</v-icon>
          </div>
          <span class="ml-3 text-h6 font-weight-bold white--text">EventSync</span>
        </v-col>

        <!-- Social Icons -->
        <v-col
          cols="12"
          md="4"
          class="d-flex align-center justify-center justify-md-end"
        >
          <v-btn icon href="mailto:zahirseid101@gmail.com" target="_blank" title="Email" class="footer-icon-btn">
            <v-icon size="24" color="#222">mdi-email</v-icon>
          </v-btn>

          <v-btn icon href="https://github.com/Zahir-Seid" target="_blank" title="GitHub" class="footer-icon-btn">
            <v-icon size="24" color="#222">mdi-github</v-icon>
          </v-btn>

          <v-btn icon href="https://www.linkedin.com/in/zahir-seid-518785294/" target="_blank" title="LinkedIn" class="footer-icon-btn">
            <v-icon size="24" color="#222">mdi-linkedin</v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-divider class="my-4" />

      <div class="text-caption white--text text-center" style="opacity: 0.6;">
        © 2025 EventSync Challenge Project. Built with <strong>Django 5</strong> + <strong>Vue JS</strong> + <strong>TypeScript</strong>.
      </div>
    </v-container>
  </v-footer>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
// Reactive footer show/hide using Vue directive
import { watchEffect } from 'vue'

const footer = ref(null)

watchEffect(() => {
  if (footer.value) {
    footer.value.style.transform = footerVisible.value ? 'translateY(0)' : 'translateY(100%)'
  }
})
const footerVisible = ref(true)
let lastScrollY = window.scrollY

function onScroll() {
  const currentScrollY = window.scrollY
  if (currentScrollY > lastScrollY && currentScrollY > 100) {
    // scrolling down - hide footer
    footerVisible.value = false
  } else {
    // scrolling up - show footer
    footerVisible.value = true
  }
  lastScrollY = currentScrollY
}

onMounted(() => {
  window.addEventListener('scroll', onScroll)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<style scoped lang="scss">
.custom-footer {
  background-color: #1a202c !important; /* bg-gray-900 */
  color: white !important;
  transition: transform 0.3s ease;
  z-index: 100;

  /* We'll toggle this transform to hide/show */
  transform: translateY(0);
}

.custom-footer[style*="display: none"] {
  transform: translateY(100%);
}

.icon-bg {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  border-radius: 0.5rem;
}

.footer-icon-btn {
  margin-left: 0.75rem;
  color: #cbd5e1; /* gray-400 */
  transition: color 0.2s ease;
}

.footer-icon-btn:hover {
  color: white !important;
}
</style>

