<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { $fetch } from 'ofetch'

const router = useRouter()
const baseUrl = import.meta.env.VITE_API_BASE_URL
const form = ref({ username: '', password: '' })
const loading = ref(false)
const error = ref(null)
const success = ref(null)

const register = async () => {
  loading.value = true
  error.value = null
  success.value = null
  try {
    const data = await $fetch(`${baseUrl}/auth/register/`, {
      method: 'POST',
      body: form.value,
    })
    success.value = data.message || 'Registration successful! You can now sign in.'
    setTimeout(() => {
      router.push('/signin')
    }, 2000)
  } catch (err) {
    error.value = err?.data?.error || 'Registration failed. Please try again.'
  } finally {
    loading.value = false
  }
}

const goToSignin = () => {
  router.push('/signin')
}
</script>

<template>
  <div class="signup-container">
    <div class="hero-section">
      <div class="hero-content">
        <div class="logo">
          <div class="logo-icon">
            <span class="material-symbols-outlined">calendar_month</span>
          </div>
          <h1 class="logo-text"> <a href="/">EventSync</a></h1>
        </div>
        
        <h2 class="hero-title">Create Your Account</h2>
        <p class="hero-subtitle">Join thousands of users managing their schedules with precision</p>
        
        <div class="features">
          <div class="feature">
            <div class="feature-icon">
              <span class="material-symbols-outlined">event</span>
            </div>
            <p class="feature-text">Advanced recurrence patterns</p>
          </div>
          <div class="feature">
            <div class="feature-icon">
              <span class="material-symbols-outlined">calendar_view_month</span>
            </div>
            <p class="feature-text">Multiple calendar views</p>
          </div>
          <div class="feature">
            <div class="feature-icon">
              <span class="material-symbols-outlined">security</span>
            </div>
            <p class="feature-text">Secure user authentication</p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="form-section">
      <div class="form-content">
        <h3 class="form-title">Get Started</h3>
        <p class="form-subtitle">Create your EventSync account</p>
        
        <form @submit.prevent="register" class="signup-form">
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
              placeholder="Create a password"
              required
            >
          </div>
          
          <button type="submit" class="submit-btn" :disabled="loading">
            <span v-if="!loading">Create Account</span>
            <span v-else>Creating Account...</span>
          </button>
          
          <div v-if="error" class="error-message">
            <span class="material-symbols-outlined">error</span>
            {{ error }}
          </div>
          
          <div v-if="success" class="success-message">
            <span class="material-symbols-outlined">check_circle</span>
            {{ success }}
          </div>
          
          <div class="signin-link">
            Already have an account? <a @click="goToSignin">Sign in</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
    @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);
.signup-container {
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

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.1;
  background: 
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.3) 0%, transparent 40%),
    radial-gradient(circle at 80% 70%, rgba(255,255,255,0.3) 0%, transparent 40%);
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

.hero-title {
  font-family: 'Poppins', sans-serif;
  font-size: 42px;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 20px;
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
.hero-subtitle {
  font-size: 20px;
  line-height: 1.6;
  opacity: 0.9;
  margin-bottom: 40px;
}

.features {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.feature {
  display: flex;
  align-items: center;
  gap: 15px;
}

.feature-icon {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-icon span {
  font-size: 24px;
}

.feature-text {
  font-size: 18px;
  font-weight: 500;
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

.submit-btn:active {
  transform: translateY(0);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
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

.success-message {
  background: #dcfce7;
  color: #166534;
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
  .signup-container {
    flex-direction: column;
  }
  
  .hero-section {
    padding: 40px 30px;
  }
  
  .form-section {
    padding: 40px 30px;
  }
  
  .hero-title {
    font-size: 32px;
  }
  
  .form-title {
    font-size: 28px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 28px;
  }
  
  .form-title {
    font-size: 24px;
  }
  
  .logo {
    margin-bottom: 30px;
  }
  
  .logo-text {
    font-size: 24px;
  }
}
</style>