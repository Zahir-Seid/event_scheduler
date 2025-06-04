<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { $fetch } from 'ofetch'

const baseUrl = import.meta.env.VITE_API_BASE_URL
const router = useRouter()
const route = useRoute()

const event = ref({
  title: '',
  description: '',
  start_datetime: '',
  end_datetime: '',
  is_recurring: false,
  recurrence_rule: {
    frequency: 'DAILY',
    interval: 1,
    weekdays: [],
    nth: null,
    weekday_for_nth: null,
    day_of_month: null,
    month: null,
    day: null,
    until: null,
    count: null,
    monthly_type: 'day_of_month'
  }
})

const occurrenceDate = ref('')
const endsType = ref('never') // 'never', 'after', 'date'

function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'))
  return match ? decodeURIComponent(match[2]) : null
}

function formatForDatetimeLocal(datetimeStr) {
  const date = new Date(datetimeStr)
  const offset = date.getTimezoneOffset()
  const localDate = new Date(date.getTime() - offset * 60000)
  return localDate.toISOString().slice(0, 16) // "YYYY-MM-DDTHH:MM"
}

onMounted(async () => {
  await fetchEvent()
})

async function fetchEvent() {
  try {
    const accessToken = getCookie('access_token')
    const data = await $fetch(`${baseUrl}/events/${route.params.id}/`, {
      headers: { Authorization: `Bearer ${accessToken}` }
    })

    data.start_datetime = formatForDatetimeLocal(data.start_datetime)
    data.end_datetime = formatForDatetimeLocal(data.end_datetime)

    // Fallback: ensure recurrence_rule exists if missing
    if (data.is_recurring && !data.recurrence_rule) {
      data.recurrence_rule = {
        frequency: 'DAILY',
        interval: 1,
        weekdays: [],
        nth: null,
        weekday_for_nth: null,
        day_of_month: null,
        month: null,
        day: null,
        until: null,
        count: null,
        monthly_type: 'day_of_month'
      }
    }

    // Set endsType for UI
    if (data.recurrence_rule?.count) {
      endsType.value = 'after'
    } else if (data.recurrence_rule?.until) {
      endsType.value = 'date'
    } else {
      endsType.value = 'never'
    }

    event.value = data
  } catch (error) {
    console.error('Failed to fetch event:', error)
  }
}

async function updateEvent() {
  try {
    const accessToken = getCookie('access_token')

    const payload = JSON.parse(JSON.stringify(event.value))

    if (!payload.is_recurring) {
      payload.recurrence_rule = null
    } else {
      if (!payload.recurrence_rule) {
        payload.recurrence_rule = {
          frequency: 'DAILY',
          interval: 1,
          weekdays: [],
          nth: null,
          weekday_for_nth: null,
          day_of_month: null,
          month: null,
          day: null,
          until: null,
          count: null,
          monthly_type: 'day_of_month'
        }
      }

      // Weekly handling
      if (payload.recurrence_rule.frequency !== 'WEEKLY') {
        payload.recurrence_rule.weekdays = []
      }

      // Handle ends type logic
      if (endsType.value === 'after') {
        payload.recurrence_rule.until = null
      } else if (endsType.value === 'date') {
        payload.recurrence_rule.count = null
      } else {
        payload.recurrence_rule.count = null
        payload.recurrence_rule.until = null
      }

      // Monthly logic
      if (payload.recurrence_rule.frequency === 'MONTHLY') {
        if (payload.recurrence_rule.monthly_type === 'day_of_month') {
          payload.recurrence_rule.nth = null
          payload.recurrence_rule.weekday_for_nth = null
        } else {
          payload.recurrence_rule.day_of_month = null
        }
        delete payload.recurrence_rule.monthly_type
      }

      // Yearly logic
      if (payload.recurrence_rule.frequency !== 'YEARLY') {
        payload.recurrence_rule.month = null
        payload.recurrence_rule.day = null
      }
    }

    await $fetch(`${baseUrl}/events/${route.params.id}/`, {
      method: 'PUT',
      body: payload,
      headers: { Authorization: `Bearer ${accessToken}` }
    })

    alert('Event updated successfully!')
  } catch (error) {
    console.error('Update failed:', error)
    alert(`Failed to update event: ${error.data?.detail || error.message}`)
  }
}

async function cancelOccurrence() {
  try {
    const accessToken = getCookie('access_token')
    await $fetch(`${baseUrl}/events/${event.value.id}/cancel-occurrence/`, {
      method: 'POST',
      body: {
        event: event.value.id,
        occurrence_date: occurrenceDate.value,
        is_cancelled: true
      },
      headers: { Authorization: `Bearer ${accessToken}` }
    })
    alert('Occurrence canceled successfully!')
    occurrenceDate.value = ''
  } catch (error) {
    console.error('Cancel occurrence failed:', error)
    alert(`Failed to cancel occurrence: ${error.data?.detail || error.message}`)
  }
}

async function deleteEvent() {
  if (confirm('Are you sure you want to delete this event? This action cannot be undone.')) {
    try {
      const accessToken = getCookie('access_token')
      await $fetch(`${baseUrl}/events/${route.params.id}/`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${accessToken}` }
      })
      router.push('/events/')
    } catch (error) {
      console.error('Delete failed:', error)
      alert(`Failed to delete event: ${error.data?.detail || error.message}`)
    }
  }
}
</script>


<template>
<div id="webcrumbs">
    <div class="mx-auto bg-gradient-to-br from-white to-primary-50 font-['Roboto'] min-h-screen">
    <nav class="bg-white/80 border-b border-[#8ca5e4] backdrop-blur-sm sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
            <div class="flex items-center space-x-8">
            <div
                class="bg-gradient-to-r from-primary-500 to-primary-600 text-white px-4 py-2 rounded-xl font-['Poppins'] font-bold"
            >
                EventSync
            </div>
            </div>
            <div class="flex items-center space-x-4">
            <button 
                @click="router.push('/events/')"
                class="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-lg transition-all duration-200 hover:scale-105"
            >
                Back to Dashboard
            </button>
            </div>
        </div>
        </div>
    </nav>
    
    <main class="max-w-4xl mx-auto px-6 py-8">
        <div class="bg-white rounded-2xl shadow-lg p-8">
        <h1 class="text-3xl font-['Poppins'] font-bold text-gray-900 mb-2">
            Edit Event
        </h1>
        <p class="text-gray-600 mb-8">Update your event details</p>
        
        <form @submit.prevent="updateEvent" class="space-y-6">
            <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Title*</label>
            <input
                v-model="event.title"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
            />
            </div>
            
            <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea
                v-model="event.description"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200 h-32 resize-none"
            ></textarea>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Start Date & Time*</label>
                <input
                v-model="event.start_datetime"
                type="datetime-local"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
                />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">End Date & Time*</label>
                <input
                v-model="event.end_datetime"
                type="datetime-local"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
                />
            </div>
            </div>
            
            <div>
            <label class="flex items-center cursor-pointer">
                <input 
                v-model="event.is_recurring" 
                type="checkbox" 
                class="rounded text-primary-600 focus:ring-primary-500"
                >
                <span class="ml-2 text-sm font-medium text-gray-700">Recurring Event</span>
            </label>
            
            <div v-if="event.is_recurring" class="mt-4 pl-6 border-l-2 border-primary-200 space-y-4">
                <!-- Recurrence UI same as in create form -->
            </div>
            </div>
            
            <div class="flex justify-between pt-6">
            <button
                type="button"
                @click="deleteEvent"
                class="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-xl transition-all duration-200 font-medium"
            >
                Delete Event
            </button>
            <div class="flex space-x-4">
                <button
                type="button"
                @click="router.push('/events/')"
                class="px-6 py-3 text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200"
                >
                Cancel
                </button>
                <button
                type="submit"
                class="bg-primary-600 hover:bg-primary-700 text-white px-8 py-3 rounded-xl transition-all duration-200 hover:scale-105 font-medium"
                >
                Update Event
                </button>
            </div>
            </div>
        </form>
        </div>
        
        <div class="bg-white rounded-2xl shadow-lg p-8 mt-8">
        <h2 class="text-xl font-['Poppins'] font-bold text-gray-900 mb-4">
            Cancel Specific Occurrence
        </h2>
        <p class="text-gray-600 mb-4">
            Use this to cancel a single instance of a recurring event
        </p>
        
        <form @submit.prevent="cancelOccurrence" class="space-y-4">
            <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
                Occurrence Date (YYYY-MM-DD)
            </label>
            <input
                v-model="occurrenceDate"
                type="date"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
            />
            </div>
            
            <button
            type="submit"
            class="bg-orange-600 hover:bg-orange-700 text-white px-6 py-3 rounded-xl transition-all duration-200 font-medium"
            >
            Cancel Occurrence
            </button>
        </form>
        </div>
    </main>
    </div>
</div>
</template>

<style scoped>
    @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);

    /*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
    *,
    :after,
    :before {
        border: 0 solid #e5e7eb;
        box-sizing: border-box;
    }
    :after,
    :before {
        --tw-content: "";
    }
    :host,
    html {
        line-height: 1.5;
        -webkit-text-size-adjust: 100%;
        font-family:
            Open Sans,
            ui-sans-serif,
            system-ui,
            sans-serif,
            Apple Color Emoji,
            Segoe UI Emoji,
            Segoe UI Symbol,
            Noto Color Emoji;
        font-feature-settings: normal;
        font-variation-settings: normal;
        -moz-tab-size: 4;
        tab-size: 4;
        -webkit-tap-highlight-color: transparent;
    }
    body {
        line-height: inherit;
        margin: 0;
    }
    hr {
        border-top-width: 1px;
        color: inherit;
        height: 0;
    }
    abbr:where([title]) {
        text-decoration: underline dotted;
    }
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        font-size: inherit;
        font-weight: inherit;
    }
    a {
        color: inherit;
        text-decoration: inherit;
    }
    b,
    strong {
        font-weight: bolder;
    }
    code,
    kbd,
    pre,
    samp {
        font-family:
            ui-monospace,
            SFMono-Regular,
            Menlo,
            Monaco,
            Consolas,
            Liberation Mono,
            Courier New,
            monospace;
        font-feature-settings: normal;
        font-size: 1em;
        font-variation-settings: normal;
    }
    small {
        font-size: 80%;
    }
    sub,
    sup {
        font-size: 75%;
        line-height: 0;
        position: relative;
        vertical-align: baseline;
    }
    sub {
        bottom: -0.25em;
    }
    sup {
        top: -0.5em;
    }
    table {
        border-collapse: collapse;
        border-color: inherit;
        text-indent: 0;
    }
    button,
    input,
    optgroup,
    select,
    textarea {
        color: inherit;
        font-family: inherit;
        font-feature-settings: inherit;
        font-size: 100%;
        font-variation-settings: inherit;
        font-weight: inherit;
        letter-spacing: inherit;
        line-height: inherit;
        margin: 0;
        padding: 0;
    }
    button,
    select {
        text-transform: none;
    }
    button,
    input:where([type="button"]),
    input:where([type="reset"]),
    input:where([type="submit"]) {
        -webkit-appearance: button;
        background-color: transparent;
        background-image: none;
    }
    :-moz-focusring {
        outline: auto;
    }
    :-moz-ui-invalid {
        box-shadow: none;
    }
    progress {
        vertical-align: baseline;
    }
    ::-webkit-inner-spin-button,
    ::-webkit-outer-spin-button {
        height: auto;
    }
    [type="search"] {
        -webkit-appearance: textfield;
        outline-offset: -2px;
    }
    ::-webkit-search-decoration {
        -webkit-appearance: none;
    }
    ::-webkit-file-upload-button {
        -webkit-appearance: button;
        font: inherit;
    }
    summary {
        display: list-item;
    }
    blockquote,
    dd,
    dl,
    figure,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hr,
    p,
    pre {
        margin: 0;
    }
    fieldset {
        margin: 0;
    }
    fieldset,
    legend {
        padding: 0;
    }
    menu,
    ol,
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }
    dialog {
        padding: 0;
    }
    textarea {
        resize: vertical;
    }
    input::placeholder,
    textarea::placeholder {
        color: #9ca3af;
        opacity: 1;
    }
    [role="button"],
    button {
        cursor: pointer;
    }
    :disabled {
        cursor: default;
    }
    audio,
    canvas,
    embed,
    iframe,
    img,
    object,
    svg,
    video {
        display: block;
        vertical-align: middle;
    }
    img,
    video {
        height: auto;
        max-width: 100%;
    }
    [hidden] {
        display: none;
    }
    *,
    :after,
    :before {
        --tw-border-spacing-x: 0;
        --tw-border-spacing-y: 0;
        --tw-translate-x: 0;
        --tw-translate-y: 0;
        --tw-rotate: 0;
        --tw-skew-x: 0;
        --tw-skew-y: 0;
        --tw-scale-x: 1;
        --tw-scale-y: 1;
        --tw-pan-x: ;
        --tw-pan-y: ;
        --tw-pinch-zoom: ;
        --tw-scroll-snap-strictness: proximity;
        --tw-gradient-from-position: ;
        --tw-gradient-via-position: ;
        --tw-gradient-to-position: ;
        --tw-ordinal: ;
        --tw-slashed-zero: ;
        --tw-numeric-figure: ;
        --tw-numeric-spacing: ;
        --tw-numeric-fraction: ;
        --tw-ring-inset: ;
        --tw-ring-offset-width: 0px;
        --tw-ring-offset-color: #fff;
        --tw-ring-color: rgba(59, 130, 246, 0.5);
        --tw-ring-offset-shadow: 0 0 #0000;
        --tw-ring-shadow: 0 0 #0000;
        --tw-shadow: 0 0 #0000;
        --tw-shadow-colored: 0 0 #0000;
        --tw-blur: ;
        --tw-brightness: ;
        --tw-contrast: ;
        --tw-grayscale: ;
        --tw-hue-rotate: ;
        --tw-invert: ;
        --tw-saturate: ;
        --tw-sepia: ;
        --tw-drop-shadow: ;
        --tw-backdrop-blur: ;
        --tw-backdrop-brightness: ;
        --tw-backdrop-contrast: ;
        --tw-backdrop-grayscale: ;
        --tw-backdrop-hue-rotate: ;
        --tw-backdrop-invert: ;
        --tw-backdrop-opacity: ;
        --tw-backdrop-saturate: ;
        --tw-backdrop-sepia: ;
        --tw-contain-size: ;
        --tw-contain-layout: ;
        --tw-contain-paint: ;
        --tw-contain-style: ;
    }
    ::backdrop {
        --tw-border-spacing-x: 0;
        --tw-border-spacing-y: 0;
        --tw-translate-x: 0;
        --tw-translate-y: 0;
        --tw-rotate: 0;
        --tw-skew-x: 0;
        --tw-skew-y: 0;
        --tw-scale-x: 1;
        --tw-scale-y: 1;
        --tw-pan-x: ;
        --tw-pan-y: ;
        --tw-pinch-zoom: ;
        --tw-scroll-snap-strictness: proximity;
        --tw-gradient-from-position: ;
        --tw-gradient-via-position: ;
        --tw-gradient-to-position: ;
        --tw-ordinal: ;
        --tw-slashed-zero: ;
        --tw-numeric-figure: ;
        --tw-numeric-spacing: ;
        --tw-numeric-fraction: ;
        --tw-ring-inset: ;
        --tw-ring-offset-width: 0px;
        --tw-ring-offset-color: #fff;
        --tw-ring-color: rgba(59, 130, 246, 0.5);
        --tw-ring-offset-shadow: 0 0 #0000;
        --tw-ring-shadow: 0 0 #0000;
        --tw-shadow: 0 0 #0000;
        --tw-shadow-colored: 0 0 #0000;
        --tw-blur: ;
        --tw-brightness: ;
        --tw-contrast: ;
        --tw-grayscale: ;
        --tw-hue-rotate: ;
        --tw-invert: ;
        --tw-saturate: ;
        --tw-sepia: ;
        --tw-drop-shadow: ;
        --tw-backdrop-blur: ;
        --tw-backdrop-brightness: ;
        --tw-backdrop-contrast: ;
        --tw-backdrop-grayscale: ;
        --tw-backdrop-hue-rotate: ;
        --tw-backdrop-invert: ;
        --tw-backdrop-opacity: ;
        --tw-backdrop-saturate: ;
        --tw-backdrop-sepia: ;
        --tw-contain-size: ;
        --tw-contain-layout: ;
        --tw-contain-paint: ;
        --tw-contain-style: ;
    }
    #webcrumbs .absolute {
        position: absolute;
    }
    #webcrumbs .relative {
        position: relative;
    }
    #webcrumbs .sticky {
        position: sticky;
    }
    #webcrumbs .left-0 {
        left: 0;
    }
    #webcrumbs .left-1\/2 {
        left: 50%;
    }
    #webcrumbs .top-0 {
        top: 0;
    }
    #webcrumbs .top-1\/2 {
        top: 50%;
    }
    #webcrumbs .z-40 {
        z-index: 40;
    }
    #webcrumbs .z-50 {
        z-index: 50;
    }
    #webcrumbs .mx-auto {
        margin-left: auto;
        margin-right: auto;
    }
    #webcrumbs .mb-2 {
        margin-bottom: 8px;
    }
    #webcrumbs .mb-4 {
        margin-bottom: 16px;
    }
    #webcrumbs .mb-6 {
        margin-bottom: 24px;
    }
    #webcrumbs .mb-8 {
        margin-bottom: 32px;
    }
    #webcrumbs .mr-2 {
        margin-right: 8px;
    }
    #webcrumbs .mr-3 {
        margin-right: 12px;
    }
    #webcrumbs .mt-1 {
        margin-top: 4px;
    }
    #webcrumbs .block {
        display: block;
    }
    #webcrumbs .flex {
        display: flex;
    }
    #webcrumbs .grid {
        display: grid;
    }
    #webcrumbs .hidden {
        display: none;
    }
    #webcrumbs .aspect-square {
        aspect-ratio: 1/1;
    }
    #webcrumbs .h-12 {
        height: 48px;
    }
    #webcrumbs .h-2 {
        height: 8px;
    }
    #webcrumbs .h-24 {
        height: 96px;
    }
    #webcrumbs .h-3 {
        height: 12px;
    }
    #webcrumbs .h-8 {
        height: 32px;
    }
    #webcrumbs .h-\[400px\] {
        height: 400px;
    }
    #webcrumbs .w-12 {
        width: 48px;
    }
    #webcrumbs .w-2 {
        width: 8px;
    }
    #webcrumbs .w-3 {
        width: 12px;
    }
    #webcrumbs .w-8 {
        width: 32px;
    }
    #webcrumbs .w-\[1440px\] {
        width: 1440px;
    }
    #webcrumbs .w-full {
        width: 100%;
    }
    #webcrumbs .max-w-2xl {
        max-width: 42rem;
    }
    #webcrumbs .max-w-3xl {
        max-width: 48rem;
    }
    #webcrumbs .max-w-6xl {
        max-width: 72rem;
    }
    #webcrumbs .flex-1 {
        flex: 1 1 0%;
    }
    #webcrumbs .-translate-x-1\/2 {
        --tw-translate-x: -50%;
    }
    #webcrumbs .-translate-x-1\/2,
    #webcrumbs .-translate-y-1\/2 {
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .-translate-y-1\/2 {
        --tw-translate-y: -50%;
    }
    #webcrumbs .transform {
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .cursor-pointer {
        cursor: pointer;
    }
    #webcrumbs .resize-none {
        resize: none;
    }
    #webcrumbs .grid-cols-1 {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }
    #webcrumbs .grid-cols-7 {
        grid-template-columns: repeat(7, minmax(0, 1fr));
    }
    #webcrumbs .flex-row {
        flex-direction: row;
    }
    #webcrumbs .flex-col {
        flex-direction: column;
    }
    #webcrumbs .items-center {
        align-items: center;
    }
    #webcrumbs .justify-start {
        justify-content: flex-start;
    }
    #webcrumbs .justify-end {
        justify-content: flex-end;
    }
    #webcrumbs .justify-center {
        justify-content: center;
    }
    #webcrumbs .justify-between {
        justify-content: space-between;
    }
    #webcrumbs .gap-2 {
        gap: 8px;
    }
    #webcrumbs .gap-4 {
        gap: 16px;
    }
    #webcrumbs .gap-8 {
        gap: 32px;
    }
    #webcrumbs :is(.space-x-4 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(16px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(16px * var(--tw-space-x-reverse));
    }
    #webcrumbs :is(.space-x-6 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(24px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(24px * var(--tw-space-x-reverse));
    }
    #webcrumbs :is(.space-x-8 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(32px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(32px * var(--tw-space-x-reverse));
    }
    #webcrumbs :is(.space-y-3 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(12px * var(--tw-space-y-reverse));
        margin-top: calc(12px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs :is(.space-y-6 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(24px * var(--tw-space-y-reverse));
        margin-top: calc(24px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs .overflow-hidden {
        overflow: hidden;
    }
    #webcrumbs .rounded-2xl {
        border-radius: 48px;
    }
    #webcrumbs .rounded-full {
        border-radius: 9999px;
    }
    #webcrumbs .rounded-lg {
        border-radius: 24px;
    }
    #webcrumbs .rounded-xl {
        border-radius: 36px;
    }
    #webcrumbs .border {
        border-width: 1px;
    }
    #webcrumbs .border-b {
        border-bottom-width: 1px;
    }
    #webcrumbs .border-\[\#8ca5e4\] {
        --tw-border-opacity: 1;
        border-color: rgb(140 165 228 / var(--tw-border-opacity));
    }
    #webcrumbs .border-gray-300 {
        --tw-border-opacity: 1;
        border-color: rgb(209 213 219 / var(--tw-border-opacity));
    }
    #webcrumbs .bg-black\/50 {
        background-color: rgba(0, 0, 0, 0.5);
    }
    #webcrumbs .bg-blue-500 {
        --tw-bg-opacity: 1;
        background-color: rgb(59 130 246 / var(--tw-bg-opacity));
    }
    .bg-red-600 {
    --tw-bg-opacity: 1;
    background-color: rgba(220, 38, 38, var(--tw-bg-opacity)); /* rgb(220, 38, 38) = #dc2626 */
    }

    /* Hover background color similar to Tailwind's hover:bg-red-700 */
    .bg-red-700:hover {
    --tw-bg-opacity: 1;
    background-color: rgba(185, 28, 28, var(--tw-bg-opacity)); /* rgb(185, 28, 28) = #b91c1c */
    }
    #webcrumbs .bg-gray-100 {
        --tw-bg-opacity: 1;
        background-color: rgb(243 244 246 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-green-500 {
        --tw-bg-opacity: 1;
        background-color: rgb(34 197 94 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-orange-500 {
        --tw-bg-opacity: 1;
        background-color: rgb(249 115 22 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-orange-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(234 88 12 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-primary-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(0 80 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-white {
        --tw-bg-opacity: 1;
        background-color: rgb(255 255 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-white\/80 {
        background-color: hsla(0, 0%, 100%, 0.8);
    }
    #webcrumbs .bg-gradient-to-br {
        background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));
    }
    #webcrumbs .bg-gradient-to-r {
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
    }
    #webcrumbs .from-blue-50 {
        --tw-gradient-from: #eff6ff var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(239, 246, 255, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-green-50 {
        --tw-gradient-from: #f0fdf4 var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(240, 253, 244, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-orange-50 {
        --tw-gradient-from: #fff7ed var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(255, 247, 237, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-primary-500 {
        --tw-gradient-from: #1465ff var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(20, 101, 255, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-white {
        --tw-gradient-from: #fff var(--tw-gradient-from-position);
        --tw-gradient-to: hsla(0, 0%, 100%, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .to-blue-100 {
        --tw-gradient-to: #dbeafe var(--tw-gradient-to-position);
    }
    #webcrumbs .to-green-100 {
        --tw-gradient-to: #dcfce7 var(--tw-gradient-to-position);
    }
    #webcrumbs .to-orange-100 {
        --tw-gradient-to: #ffedd5 var(--tw-gradient-to-position);
    }
    #webcrumbs .to-primary-50 {
        --tw-gradient-to: #e5f5ff var(--tw-gradient-to-position);
    }
    #webcrumbs .to-primary-600 {
        --tw-gradient-to: #0050ff var(--tw-gradient-to-position);
    }
    #webcrumbs .p-2 {
        padding: 8px;
    }
    #webcrumbs .p-3 {
        padding: 12px;
    }
    #webcrumbs .p-6 {
        padding: 24px;
    }
    #webcrumbs .p-8 {
        padding: 32px;
    }
    #webcrumbs .px-4 {
        padding-left: 16px;
        padding-right: 16px;
    }
    #webcrumbs .px-6 {
        padding-left: 24px;
        padding-right: 24px;
    }
    #webcrumbs .px-8 {
        padding-left: 32px;
        padding-right: 32px;
    }
    #webcrumbs .py-2 {
        padding-bottom: 8px;
        padding-top: 8px;
    }
    #webcrumbs .py-3 {
        padding-bottom: 12px;
        padding-top: 12px;
    }
    #webcrumbs .py-4 {
        padding-bottom: 16px;
        padding-top: 16px;
    }
    #webcrumbs .py-8 {
        padding-bottom: 32px;
        padding-top: 32px;
    }
    #webcrumbs .pt-4 {
        padding-top: 16px;
    }
    #webcrumbs .text-center {
        text-align: center;
    }
    #webcrumbs .text-2xl {
        font-size: 24px;
        line-height: 31.200000000000003px;
    }
    #webcrumbs .text-4xl {
        font-size: 36px;
        line-height: 41.4px;
    }
    #webcrumbs .text-lg {
        font-size: 18px;
        line-height: 27px;
    }
    #webcrumbs .text-sm {
        font-size: 14px;
        line-height: 21px;
    }
    #webcrumbs .text-xl {
        font-size: 20px;
        line-height: 28px;
    }
    #webcrumbs .font-bold {
        font-weight: 700;
    }
    #webcrumbs .font-medium {
        font-weight: 500;
    }
    #webcrumbs .leading-relaxed {
        line-height: 1.625;
    }
    #webcrumbs .text-gray-400 {
        --tw-text-opacity: 1;
        color: rgb(156 163 175 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-500 {
        --tw-text-opacity: 1;
        color: rgb(107 114 128 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-600 {
        --tw-text-opacity: 1;
        color: rgb(75 85 99 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-700 {
        --tw-text-opacity: 1;
        color: rgb(55 65 81 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-900 {
        --tw-text-opacity: 1;
        color: rgb(17 24 39 / var(--tw-text-opacity));
    }
    #webcrumbs .text-primary-600 {
        --tw-text-opacity: 1;
        color: rgb(0 80 255 / var(--tw-text-opacity));
    }
    #webcrumbs .text-white {
        --tw-text-opacity: 1;
        color: rgb(255 255 255 / var(--tw-text-opacity));
    }
    #webcrumbs .shadow-2xl {
        --tw-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        --tw-shadow-colored: 0 25px 50px -12px var(--tw-shadow-color);
    }
    #webcrumbs .shadow-2xl,
    #webcrumbs .shadow-lg {
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .shadow-lg {
        --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
    }
    #webcrumbs .backdrop-blur-sm {
        --tw-backdrop-blur: blur(4px);
        -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast)
            var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert)
            var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
        backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast)
            var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert)
            var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
    }
    #webcrumbs .transition-all {
        transition-duration: 0.15s;
        transition-property: all;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .transition-colors {
        transition-duration: 0.15s;
        transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .transition-shadow {
        transition-duration: 0.15s;
        transition-property: box-shadow;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .duration-200 {
        transition-duration: 0.2s;
    }
    #webcrumbs .duration-300 {
        transition-duration: 0.3s;
    }
    #webcrumbs {
        font-family: Open Sans !important;
        font-size: 16px !important;
    }
    #webcrumbs :is(.bg-primary-600) {
        color: hsla(0, 0%, 100%, 0.9) !important;
    }
    #webcrumbs .hover\:-translate-y-2:hover {
        --tw-translate-y: -8px;
    }
    #webcrumbs .hover\:-translate-y-2:hover,
    #webcrumbs .hover\:scale-105:hover {
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .hover\:scale-105:hover {
        --tw-scale-x: 1.05;
        --tw-scale-y: 1.05;
    }
    #webcrumbs .hover\:bg-gray-200:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(229 231 235 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-orange-700:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(194 65 12 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-primary-50:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(229 245 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-primary-700:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(0 81 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:text-gray-800:hover {
        --tw-text-opacity: 1;
        color: rgb(31 41 55 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:text-primary-600:hover {
        --tw-text-opacity: 1;
        color: rgb(0 80 255 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:shadow-md:hover {
        --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
    }
    #webcrumbs .hover\:shadow-md:hover,
    #webcrumbs .hover\:shadow-xl:hover {
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .hover\:shadow-xl:hover {
        --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
    }
    #webcrumbs .focus\:border-transparent:focus {
        border-color: transparent;
    }
    #webcrumbs .focus\:ring-2:focus {
        --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
        --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
        box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
    }
    #webcrumbs .focus\:ring-primary-500:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(20 101 255 / var(--tw-ring-opacity));
    }
    @media (min-width: 768px) {
        #webcrumbs .md\:flex {
            display: flex;
        }
        #webcrumbs .md\:grid-cols-2 {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }
    @media (min-width: 1024px) {
        #webcrumbs .lg\:col-span-2 {
            grid-column: span 2 / span 2;
        }
        #webcrumbs .lg\:grid-cols-3 {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
    }
</style>