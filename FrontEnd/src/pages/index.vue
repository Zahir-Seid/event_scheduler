<script setup>
import { computed } from 'vue'

// Helper to get cookie by name
function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'))
  return match ? decodeURIComponent(match[2]) : null
}

// Computed property to check access token
const hasAccessToken = computed(() => !!getCookie('access_token'))
</script>

<template>
  <div id="webcrumbs">
        <div class="container mx-auto bg-gradient-to-b from-white to-primary-50">
            <nav
                class="flex items-center justify-between px-8 py-6 bg-white/80 backdrop-blur-sm border-b border-primary-100"
            >
                <div class="flex items-center space-x-3">
                    <div
                        class="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center"
                    >
                        <span class="material-symbols-outlined text-white text-xl">calendar_month</span>
                    </div>
                    <h1 class="text-2xl font-bold text-gray-900">EventSync</h1>
                </div>
                <div class="flex items-center space-x-6">
                    <a href="#features" class="text-gray-600 hover:text-primary-600 transition-colors duration-200">
                        Features
                    </a>
                    <a :href="hasAccessToken ? '/events/' : '/signup'">
                        <button
                        class="bg-primary-600 hover:bg-primary-700 text-white px-6 py-2 rounded-lg transition-all duration-200 transform hover:scale-105"
                        >
                        Get Started
                        </button>
                    </a>
                </div>
            </nav>
            <section class="px-8 py-20 text-center">
                <div class="max-w-4xl mx-auto">
                    <h1 class="text-6xl font-bold text-gray-900 mb-6 leading-tight">
                        Event Scheduler with
                        <span
                            class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-primary-800 block mt-2"
                        >
                            Complex Recurrence
                        </span>
                    </h1>
                    <p class="text-xl text-gray-600 mb-12 max-w-3xl mx-auto leading-relaxed">
                        A sophisticated web application that handles both one-off and recurring calendar events,
                        including intricate patterns like &quot;the last weekday of every year.&quot; Built with clean
                        architecture and modern development practices.
                    </p>
                    <div class="flex items-center justify-center space-x-4 mb-16"></div>
                </div>
            </section>
            <section id="features" class="px-8 py-20 bg-white">
                <div class="max-w-6xl mx-auto">
                    <div class="text-center mb-16">
                        <h2 class="text-4xl font-bold text-gray-900 mb-4">Core Features</h2>
                        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
                            Sophisticated event management with support for complex recurring patterns
                        </p>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <div
                            class="bg-gradient-to-br from-primary-50 to-primary-100 p-8 rounded-2xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
                        >
                            <div class="w-12 h-12 bg-primary-600 rounded-xl flex items-center justify-center mb-6">
                                <span class="material-symbols-outlined text-white">event</span>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">Single &amp; Recurring Events</h3>
                            <p class="text-gray-600">
                                Create one-time events or complex recurring patterns with full flexibility.
                            </p>
                        </div>
                        <div
                            class="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-2xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
                        >
                            <div class="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center mb-6">
                                <span class="material-symbols-outlined text-white">calendar_view_month</span>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">Calendar &amp; List Views</h3>
                            <p class="text-gray-600">
                                Visualize your schedule in calendar format or browse upcoming events in a list.
                            </p>
                        </div>
                        <div
                            class="bg-gradient-to-br from-orange-50 to-orange-100 p-8 rounded-2xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2"
                        >
                            <div class="w-12 h-12 bg-orange-600 rounded-xl flex items-center justify-center mb-6">
                                <span class="material-symbols-outlined text-white">security</span>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">User Authentication</h3>
                            <p class="text-gray-600">
                                Secure user authentication with personal event management.
                            </p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<style scoped>
    @import url(https://fonts.googleapis.com/css2?family=Poppins&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Roboto&display=swap);
    @import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);
    @import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css);

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
            Poppins,
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
    #webcrumbs .mx-auto {
        margin-left: auto;
        margin-right: auto;
    }
    #webcrumbs .mb-12 {
        margin-bottom: 48px;
    }
    #webcrumbs .mb-16 {
        margin-bottom: 64px;
    }
    #webcrumbs .mb-2 {
        margin-bottom: 8px;
    }
    #webcrumbs .mb-3 {
        margin-bottom: 12px;
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
    #webcrumbs .mr-4 {
        margin-right: 16px;
    }
    #webcrumbs .mt-2 {
        margin-top: 8px;
    }
    #webcrumbs .mt-3 {
        margin-top: 12px;
    }
    #webcrumbs .mt-8 {
        margin-top: 32px;
    }
    #webcrumbs .block {
        display: block;
    }
    #webcrumbs .flex {
        display: flex;
    }
    #webcrumbs .inline-flex {
        display: inline-flex;
    }
    #webcrumbs .grid {
        display: grid;
    }
    #webcrumbs .h-10 {
        height: 40px;
    }
    #webcrumbs .h-12 {
        height: 48px;
    }
    #webcrumbs .h-16 {
        height: 64px;
    }
    #webcrumbs .h-8 {
        height: 32px;
    }
    #webcrumbs .w-10 {
        width: 40px;
    }
    #webcrumbs .w-12 {
        width: 48px;
    }
    #webcrumbs .w-16 {
        width: 64px;
    }
    #webcrumbs .w-8 {
        width: 32px;
    }
    #webcrumbs .w-\[1440px\] {
        width: 1440px;
    }
    #webcrumbs .max-w-2xl {
        max-width: 42rem;
    }
    #webcrumbs .max-w-3xl {
        max-width: 48rem;
    }
    #webcrumbs .max-w-4xl {
        max-width: 56rem;
    }
    #webcrumbs .max-w-5xl {
        max-width: 64rem;
    }
    #webcrumbs .max-w-6xl {
        max-width: 72rem;
    }
    #webcrumbs .transform {
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    #webcrumbs .cursor-pointer {
        cursor: pointer;
    }
    #webcrumbs .grid-cols-1 {
        grid-template-columns: repeat(1, minmax(0, 1fr));
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
    #webcrumbs .justify-center {
        justify-content: center;
    }
    #webcrumbs .justify-between {
        justify-content: space-between;
    }
    #webcrumbs .gap-12 {
        gap: 48px;
    }
    #webcrumbs .gap-4 {
        gap: 16px;
    }
    #webcrumbs .gap-8 {
        gap: 32px;
    }
    #webcrumbs :is(.space-x-3 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-x-reverse: 0;
        margin-left: calc(12px * (1 - var(--tw-space-x-reverse)));
        margin-right: calc(12px * var(--tw-space-x-reverse));
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
    #webcrumbs :is(.space-y-2 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(8px * var(--tw-space-y-reverse));
        margin-top: calc(8px * (1 - var(--tw-space-y-reverse)));
    }
    #webcrumbs :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
        --tw-space-y-reverse: 0;
        margin-bottom: calc(16px * var(--tw-space-y-reverse));
        margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
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
    #webcrumbs .border-2 {
        border-width: 2px;
    }
    #webcrumbs .border-b {
        border-bottom-width: 1px;
    }
    #webcrumbs .border-t {
        border-top-width: 1px;
    }
    #webcrumbs .border-dashed {
        border-style: dashed;
    }
    #webcrumbs .border-blue-300 {
        --tw-border-opacity: 1;
        border-color: rgb(147 197 253 / var(--tw-border-opacity));
    }
    #webcrumbs .border-gray-800 {
        --tw-border-opacity: 1;
        border-color: rgb(31 41 55 / var(--tw-border-opacity));
    }
    #webcrumbs .border-primary-100 {
        --tw-border-opacity: 1;
        border-color: rgb(140 165 228 / var(--tw-border-opacity));
    }
    #webcrumbs .border-primary-600 {
        --tw-border-opacity: 1;
        border-color: rgb(0 49 175 / var(--tw-border-opacity));
    }
    #webcrumbs .bg-blue-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(37 99 235 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-gray-50 {
        --tw-bg-opacity: 1;
        background-color: rgb(249 250 251 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-gray-900 {
        --tw-bg-opacity: 1;
        background-color: rgb(17 24 39 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-green-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(22 163 74 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-orange-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(234 88 12 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-primary-100 {
        --tw-bg-opacity: 1;
        background-color: rgb(140 165 228 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-primary-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(0 49 175 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-purple-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(147 51 234 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-red-600 {
        --tw-bg-opacity: 1;
        background-color: rgb(220 38 38 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-white {
        --tw-bg-opacity: 1;
        background-color: rgb(255 255 255 / var(--tw-bg-opacity));
    }
    #webcrumbs .bg-white\/10 {
        background-color: hsla(0, 0%, 100%, 0.1);
    }
    #webcrumbs .bg-white\/20 {
        background-color: hsla(0, 0%, 100%, 0.2);
    }
    #webcrumbs .bg-white\/70 {
        background-color: hsla(0, 0%, 100%, 0.7);
    }
    #webcrumbs .bg-white\/80 {
        background-color: hsla(0, 0%, 100%, 0.8);
    }
    #webcrumbs .bg-gradient-to-b {
        background-image: linear-gradient(to bottom, var(--tw-gradient-stops));
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
    #webcrumbs .from-primary-50 {
        --tw-gradient-from: #a6b9ea var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(166, 185, 234, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-primary-500 {
        --tw-gradient-from: #0036c2 var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(0, 54, 194, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-primary-600 {
        --tw-gradient-from: #0031af var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(0, 49, 175, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-purple-50 {
        --tw-gradient-from: #faf5ff var(--tw-gradient-from-position);
        --tw-gradient-to: rgba(250, 245, 255, 0) var(--tw-gradient-to-position);
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
    }
    #webcrumbs .from-red-50 {
        --tw-gradient-from: #fef2f2 var(--tw-gradient-from-position);
        --tw-gradient-to: hsla(0, 86%, 97%, 0) var(--tw-gradient-to-position);
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
    #webcrumbs .to-primary-100 {
        --tw-gradient-to: #8ca5e4 var(--tw-gradient-to-position);
    }
    #webcrumbs .to-primary-50 {
        --tw-gradient-to: #a6b9ea var(--tw-gradient-to-position);
    }
    #webcrumbs .to-primary-600 {
        --tw-gradient-to: #0031af var(--tw-gradient-to-position);
    }
    #webcrumbs .to-primary-800 {
        --tw-gradient-to: #002074 var(--tw-gradient-to-position);
    }
    #webcrumbs .to-purple-100 {
        --tw-gradient-to: #f3e8ff var(--tw-gradient-to-position);
    }
    #webcrumbs .to-red-100 {
        --tw-gradient-to: #fee2e2 var(--tw-gradient-to-position);
    }
    #webcrumbs .bg-clip-text {
        background-clip: text;
    }
    #webcrumbs .p-2 {
        padding: 8px;
    }
    #webcrumbs .p-4 {
        padding: 16px;
    }
    #webcrumbs .p-6 {
        padding: 24px;
    }
    #webcrumbs .p-8 {
        padding: 32px;
    }
    #webcrumbs .px-6 {
        padding-left: 24px;
        padding-right: 24px;
    }
    #webcrumbs .px-8 {
        padding-left: 32px;
        padding-right: 32px;
    }
    #webcrumbs .py-12 {
        padding-bottom: 48px;
        padding-top: 48px;
    }
    #webcrumbs .py-2 {
        padding-bottom: 8px;
        padding-top: 8px;
    }
    #webcrumbs .py-20 {
        padding-bottom: 80px;
        padding-top: 80px;
    }
    #webcrumbs .py-4 {
        padding-bottom: 16px;
        padding-top: 16px;
    }
    #webcrumbs .py-6 {
        padding-bottom: 24px;
        padding-top: 24px;
    }
    #webcrumbs .pt-8 {
        padding-top: 32px;
    }
    #webcrumbs .text-center {
        text-align: center;
    }
    #webcrumbs .text-2xl {
        font-size: 24px;
        line-height: 31.200000000000003px;
    }
    #webcrumbs .text-3xl {
        font-size: 30px;
        line-height: 36px;
    }
    #webcrumbs .text-4xl {
        font-size: 36px;
        line-height: 41.4px;
    }
    #webcrumbs .text-6xl {
        font-size: 60px;
        line-height: 66px;
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
    #webcrumbs .font-semibold {
        font-weight: 600;
    }
    #webcrumbs .leading-relaxed {
        line-height: 1.625;
    }
    #webcrumbs .leading-tight {
        line-height: 1.25;
    }
    #webcrumbs .text-gray-400 {
        --tw-text-opacity: 1;
        color: rgb(156 163 175 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-600 {
        --tw-text-opacity: 1;
        color: rgb(75 85 99 / var(--tw-text-opacity));
    }
    #webcrumbs .text-gray-900 {
        --tw-text-opacity: 1;
        color: rgb(17 24 39 / var(--tw-text-opacity));
    }
    #webcrumbs .text-green-500 {
        --tw-text-opacity: 1;
        color: rgb(34 197 94 / var(--tw-text-opacity));
    }
    #webcrumbs .text-primary-100 {
        --tw-text-opacity: 1;
        color: rgb(140 165 228 / var(--tw-text-opacity));
    }
    #webcrumbs .text-primary-600 {
        --tw-text-opacity: 1;
        color: rgb(0 49 175 / var(--tw-text-opacity));
    }
    #webcrumbs .text-primary-700 {
        --tw-text-opacity: 1;
        color: rgb(0 41 146 / var(--tw-text-opacity));
    }
    #webcrumbs .text-transparent {
        color: transparent;
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
    #webcrumbs .shadow-xl {
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs .shadow-xl {
        --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
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
    #webcrumbs .transition-transform {
        transition-duration: 0.15s;
        transition-property: transform;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    #webcrumbs .duration-200 {
        transition-duration: 0.2s;
    }
    #webcrumbs .duration-300 {
        transition-duration: 0.3s;
    }
    #webcrumbs {
        font-family: Roboto !important;
        font-size: 16px !important;
    }
    #webcrumbs :is(.bg-primary-100) {
        color: rgba(0, 0, 0, 0.9) !important;
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
    #webcrumbs .hover\:bg-gray-100:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(243 244 246 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-gray-50:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(249 250 251 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-primary-50:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(166 185 234 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-primary-700:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(0 41 146 / var(--tw-bg-opacity));
    }
    #webcrumbs .hover\:bg-white\/20:hover {
        background-color: hsla(0, 0%, 100%, 0.2);
    }
    #webcrumbs .hover\:text-primary-600:hover {
        --tw-text-opacity: 1;
        color: rgb(0 49 175 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:text-white:hover {
        --tw-text-opacity: 1;
        color: rgb(255 255 255 / var(--tw-text-opacity));
    }
    #webcrumbs .hover\:shadow-xl:hover {
        --tw-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    }
    #webcrumbs :is(.group[open] .group-open\:rotate-180) {
        --tw-rotate: 180deg;
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate))
            skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
    }
    @media (min-width: 768px) {
        #webcrumbs .md\:mb-0 {
            margin-bottom: 0;
        }
        #webcrumbs .md\:grid-cols-2 {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        #webcrumbs .md\:grid-cols-3 {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
        #webcrumbs .md\:flex-row {
            flex-direction: row;
        }
    }
    @media (min-width: 1024px) {
        #webcrumbs .lg\:grid-cols-2 {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        #webcrumbs .lg\:grid-cols-3 {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
    }
</style>
