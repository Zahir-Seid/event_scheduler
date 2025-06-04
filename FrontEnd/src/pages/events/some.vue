<template
    ><div id="webcrumbs">
        <div class="w-[1440px] bg-gradient-to-br from-white to-primary-50 font-[&#x27;Roboto&#x27;]">
            <nav class="bg-white/80 border-b border-[#8ca5e4] backdrop-blur-sm sticky top-0 z-50">
                <div class="max-w-6xl mx-auto px-6 py-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-8">
                            <div
                                class="bg-gradient-to-r from-primary-500 to-primary-600 text-white px-4 py-2 rounded-xl font-[&#x27;Poppins&#x27;] font-bold"
                            >
                                CalendarApp
                            </div>
                            <div class="hidden md:flex space-x-6">
                                <a href="#" class="text-gray-600 hover:text-primary-600 transition-colors duration-200"
                                    >Dashboard</a
                                >
                                <a href="#" class="text-gray-600 hover:text-primary-600 transition-colors duration-200"
                                    >Events</a
                                >
                                <a href="#" class="text-gray-600 hover:text-primary-600 transition-colors duration-200"
                                    >Calendar</a
                                >
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <button class="text-gray-600 hover:text-primary-600 transition-colors duration-200">
                                <span class="material-symbols-outlined">notifications</span>
                            </button>
                            <button
                                class="text-gray-600 hover:text-primary-600 transition-colors duration-200"
                            ></button>
                            <button
                                class="bg-orange-600 hover:bg-orange-700 text-white px-4 py-2 rounded-lg transition-all duration-200 hover:scale-105"
                            >
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            </nav>
            <main class="max-w-6xl mx-auto px-6 py-8">
                <div class="mb-8">
                    <h1
                        class="text-4xl font-[&#x27;Poppins&#x27;] font-bold bg-gradient-to-r from-primary-600 to-primary-800 bg-clip-text text-transparent mb-4"
                    >
                        Welcome back, Alex
                    </h1>
                    <p class="text-xl text-gray-600 leading-relaxed max-w-3xl">
                        Manage your schedule efficiently with our powerful calendar system
                    </p>
                </div>
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div class="lg:col-span-2">
                        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
                            <div class="bg-gradient-to-r from-primary-500 to-primary-600 px-6 py-4">
                                <h2 class="text-xl font-[&#x27;Poppins&#x27;] font-bold text-white flex items-center">
                                    <span class="material-symbols-outlined mr-2">calendar_month</span> Calendar View -
                                    December 2024
                                </h2>
                            </div>
                            <div class="p-6">
                                <div class="grid grid-cols-7 gap-2 mb-4">
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Sun</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Mon</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Tue</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Wed</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Thu</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Fri</div>
                                    <div class="text-center text-sm font-medium text-gray-500 py-2">Sat</div>
                                </div>
                                <div class="grid grid-cols-7 gap-2">
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">24</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">25</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">26</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">27</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">28</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">29</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 text-gray-400"
                                    >
                                        <span class="text-sm">30</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">1</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">2</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">3</span>
                                        <div class="w-2 h-2 bg-blue-500 rounded-full mt-1"></div>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">4</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">5</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">6</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">7</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">8</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">9</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">10</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">11</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">12</span>
                                        <div class="w-2 h-2 bg-orange-500 rounded-full mt-1"></div>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">13</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">14</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 bg-primary-600 text-white rounded-lg"
                                    >
                                        <span class="text-sm font-bold">15</span>
                                        <div class="w-2 h-2 bg-white rounded-full mt-1"></div>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">16</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">17</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">18</span>
                                        <div class="w-2 h-2 bg-green-500 rounded-full mt-1"></div>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">19</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">20</span>
                                    </div>
                                    <div
                                        class="aspect-square flex flex-col items-center justify-start p-2 hover:bg-primary-50 rounded-lg cursor-pointer transition-colors duration-200"
                                    >
                                        <span class="text-sm font-medium">21</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-6">
                        <div
                            class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-2xl hover:shadow-xl hover:-translate-y-2 transition-all duration-300"
                        >
                            <div class="flex items-center justify-between mb-4">
                                <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
                                    <span class="material-symbols-outlined text-white">add_circle</span>
                                </div>
                                <button
                                    class="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-lg transition-all duration-200 hover:scale-105"
                                >
                                    Quick Add
                                </button>
                            </div>
                            <h3 class="text-lg font-[&#x27;Poppins&#x27;] font-bold text-gray-900 mb-2">
                                Create Event
                            </h3>
                            <p class="text-gray-600 text-sm">Add new events to your calendar quickly and easily</p>
                        </div>
                        <div class="bg-white rounded-2xl shadow-lg p-6">
                            <h3
                                class="text-lg font-[&#x27;Poppins&#x27;] font-bold text-gray-900 mb-4 flex items-center"
                            >
                                <span class="material-symbols-outlined mr-2 text-primary-600">event</span> Today&#x27;s
                                Events
                            </h3>
                            <div class="space-y-3">
                                <div
                                    class="flex items-center p-3 bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl hover:shadow-md transition-shadow duration-200"
                                >
                                    <div class="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
                                    <div class="flex-1">
                                        <p class="font-medium text-gray-900">Team Meeting</p>
                                        <p class="text-sm text-gray-600">9:00 AM - 10:30 AM</p>
                                    </div>
                                </div>
                                <div
                                    class="flex items-center p-3 bg-gradient-to-r from-orange-50 to-orange-100 rounded-xl hover:shadow-md transition-shadow duration-200"
                                >
                                    <div class="w-3 h-3 bg-orange-500 rounded-full mr-3"></div>
                                    <div class="flex-1">
                                        <p class="font-medium text-gray-900">Client Presentation</p>
                                        <p class="text-sm text-gray-600">2:00 PM - 3:00 PM</p>
                                    </div>
                                </div>
                                <div
                                    class="flex items-center p-3 bg-gradient-to-r from-green-50 to-green-100 rounded-xl hover:shadow-md transition-shadow duration-200"
                                >
                                    <div class="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
                                    <div class="flex-1">
                                        <p class="font-medium text-gray-900">Project Review</p>
                                        <p class="text-sm text-gray-600">4:30 PM - 5:30 PM</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div
                    class="absolute top-0 left-0 w-full h-[400px] bg-black/50 z-40"
                    style="display: none"
                    data-modal="event-creation"
                >
                    <div
                        class="relative top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-2xl p-8 w-full max-w-2xl shadow-2xl"
                    >
                        <div class="flex items-center justify-between mb-6">
                            <h2
                                class="text-2xl font-[&#x27;Poppins&#x27;] font-bold bg-gradient-to-r from-primary-600 to-primary-800 bg-clip-text text-transparent"
                            >
                                Create New Event
                            </h2>
                            <button
                                class="w-8 h-8 bg-gray-100 hover:bg-gray-200 rounded-full flex items-center justify-center transition-colors duration-200"
                            >
                                <span class="material-symbols-outlined text-gray-600">close</span>
                            </button>
                        </div>
                        <form class="space-y-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Event Title</label>
                                <input
                                    type="text"
                                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
                                    placeholder="Enter event title"
                                />
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
                                <textarea
                                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200 h-24 resize-none"
                                    placeholder="Event description (optional)"
                                ></textarea>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2"
                                        >Start Date &amp; Time</label
                                    >
                                    <input
                                        type="datetime-local"
                                        class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
                                    />
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2"
                                        >End Date &amp; Time</label
                                    >
                                    <input
                                        type="datetime-local"
                                        class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200"
                                    />
                                </div>
                            </div>
                            <div class="flex justify-end space-x-4 pt-4">
                                <button
                                    type="button"
                                    class="px-6 py-3 text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200"
                                >
                                    Cancel
                                </button>
                                <button
                                    type="submit"
                                    class="bg-primary-600 hover:bg-primary-700 text-white px-8 py-3 rounded-xl transition-all duration-200 hover:scale-105 font-medium"
                                >
                                    Create Event
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    </div></template
>

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
