<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { $fetch } from 'ofetch'

const router = useRouter()
const form = ref({ username: '', password: '' })
const loading = ref(false)
const error = ref(null)
const baseUrl = import.meta.env.VITE_API_BASE_URL

const login = async () => {
  loading.value = true
  error.value = null
  try {
    const data = await $fetch(`${baseUrl}/auth/login/`, {
      method: 'POST',
      body: form.value,
    })

    document.cookie = `access_token=${data.access}; path=/; Secure; SameSite=Strict`
    document.cookie = `refresh_token=${data.refresh}; path=/; Secure; SameSite=Strict`

    router.push('/events/')
  } catch (err) {
    error.value = err?.data?.error || 'Login failed'
  } finally {
    loading.value = false
  }
}

const goToSignup = () => {
  router.push('/signup')
}
</script>

<template>
  <div class="signin-container">
    <div class="hero-section">
      <div class="hero-content">
        <div class="logo">
          <div class="logo-icon">
            <span class="material-symbols-outlined">calendar_month</span>
          </div>
          <h1 class="logo-text"> <a>EventSync</a></h1>
        </div>

        <h2 class="hero-title">Welcome Back</h2>
        <p class="hero-subtitle">Sign in to manage your events efficiently</p>
      </div>
    </div>

    <div class="form-section">
      <div class="form-content">
        <h3 class="form-title">Sign In</h3>
        <p class="form-subtitle">Access your EventSync dashboard</p>

        <form @submit.prevent="login" class="signup-form">
          <div class="form-group">
            <label for="username">Username</label>
            <input 
              type="text" 
              id="username" 
              v-model="form.username" 
              placeholder="Enter your username"
              required
            >
          </div>

          <div class="form-group">
            <label for="password">Password</label>
            <input 
              type="password" 
              id="password" 
              v-model="form.password" 
              placeholder="Enter your password"
              required
            >
          </div>

          <button type="submit" class="submit-btn" :disabled="loading">
            <span v-if="!loading">Sign In</span>
            <span v-else>Signing In...</span>
          </button>

          <div v-if="error" class="error-message">
            <span class="material-symbols-outlined">error</span>
            {{ error }}
          </div>

          <div class="signin-link">
            Don't have an account? <a @click.prevent="goToSignup">Sign up here</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');

.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

.signin-container {
  display: flex;
  min-height: 100vh;
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(to bottom, #fff, #a6b9ea);
}

.hero-section {
  flex: 1;
  background: linear-gradient(to bottom right, #0031af, #002074);
  color: white;
  padding: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.hero-content {
  max-width: 600px;
  z-index: 1;
}

.logo {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 50px;
}

.logo-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(to bottom right, #fff, #a6b9ea);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-icon span {
  font-size: 32px;
  color: #0031af;
}

.logo-text {
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 32px;
}
.logo-text a {
  color: white; 
  text-decoration: none;
}

.logo-text a:visited {
  color: white; 
}

.logo-text a:hover {
  text-decoration: underline; 
}

.hero-title {
  font-family: 'Poppins', sans-serif;
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 20px;
}

.hero-subtitle {
  font-size: 20px;
  line-height: 1.6;
  opacity: 0.9;
  margin-bottom: 40px;
}

.form-section {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background: white;
}

.form-content {
  max-width: 450px;
  width: 100%;
}

.form-title {
  font-family: 'Poppins', sans-serif;
  font-size: 36px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 10px;
  background: linear-gradient(to right, #0031af, #002074);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.form-subtitle {
  font-size: 18px;
  color: #4b5563;
  margin-bottom: 40px;
}

.signup-form {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-size: 16px;
  font-weight: 500;
  color: #111827;
}

input {
  padding: 18px 24px;
  border: 1px solid #d1d5db;
  border-radius: 18px;
  font-size: 16px;
  transition: all 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #0031af;
  box-shadow: 0 0 0 4px rgba(0, 49, 175, 0.2);
}

.submit-btn {
  background: linear-gradient(to right, #0031af, #002074);
  color: white;
  border: none;
  padding: 18px;
  border-radius: 18px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 49, 175, 0.2);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.error-message {
  background: #fee2e2;
  color: #b91c1c;
  padding: 18px;
  border-radius: 14px;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.signin-link {
  text-align: center;
  margin-top: 20px;
  color: #4b5563;
  font-size: 16px;
}

.signin-link a {
  color: #0031af;
  text-decoration: none;
  font-weight: 600;
  cursor: pointer;
}

.signin-link a:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .signin-container {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 28px;
  }
  
  .form-title {
    font-size: 24px;
  }
}
</style>
