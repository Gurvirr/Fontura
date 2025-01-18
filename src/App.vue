<script setup lang="ts">
    import { onMounted } from "vue";
    import { ref } from "vue";
    import { getCurrentWindow } from "@tauri-apps/api/window";

    // Font list state //
    const fonts = ref<string[]>([]);
    
    // Search box input //
    const searchQuery = ref<string>("");

    onMounted(() => {
    // Titlebar functionality
    const appWindow = getCurrentWindow();

    document.getElementById("titlebar-minimize")?.addEventListener("click", () => appWindow.minimize());
    document.getElementById("titlebar-maximize")?.addEventListener("click", () => appWindow.toggleMaximize());
    document.getElementById("titlebar-close")?.addEventListener("click", () => appWindow.close());

    // Fetch the fonts.json file
    fetch("/fonts.json")
        .then(response => response.json())
        .then(data => {
            fonts.value = data.fonts;
        })
        .catch(error => {
            console.error('Error reading fonts.json:', error);
        });

    // Slider functionality
    const sliderEl = document.querySelector("#range") as HTMLInputElement | null;
    const sliderValue = document.querySelector(".value");

    if (sliderEl && sliderValue) {
        sliderEl.addEventListener("input", (event) => {
            const tempSliderValue = (event.target as HTMLInputElement).value;

            const numericValue = Number(tempSliderValue);
            sliderValue.textContent = `${numericValue}px`;

            const progress = (Number(tempSliderValue) / Number(sliderEl.max)) * 100;

            sliderEl.style.background = `linear-gradient(to right, #181818 ${progress}%, #d8d8d8 ${progress}%)`;
        });
    }
});

    // Function to clear the search box
    const clearSearch = () => {
        searchQuery.value = "";
    };

</script>

<template>
    <!-- Titlebar structure -->
    <div data-tauri-drag-region class="titlebar">
        <div class="titlebar-logo">
            <img src="/src/assets/Fontura-F.svg" alt="Fontura" shape-rendering="crispEdges"/>
        </div>

        <!-- Minimize button -->
        <div class="titlebar-button" id="titlebar-minimize">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none" shape-rendering="crispEdges">
                <rect x="12.25" y="18.25" width="11.5" height="0.5" fill="#f8f8f8" stroke="#f8f8f8" stroke-width="0.5"/>
            </svg>
        </div>

        <!-- Maximize button -->
        <div class="titlebar-button" id="titlebar-maximize">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
                <rect x="12.5" y="14.5" width="9" height="9" stroke="#f8f8f8"/>
                <rect x="24" y="12" width="1" height="9" transform="rotate(90 24 12)" fill="#f8f8f8"/>
                <rect x="15" y="14" width="1" height="2" transform="rotate(-180 15 14)" fill="#f8f8f8"/>
                <rect x="22" y="22" width="1" height="2" transform="rotate(-90 22 22)" fill="#f8f8f8"/>
                <rect x="24" y="21" width="1" height="9" transform="rotate(-180 24 21)" fill="#f8f8f8"/>
            </svg>
        </div>

        <!-- Close button -->
        <div class="titlebar-button" id="titlebar-close">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
                <path d="M12 12L24 24M24 12L12 24" stroke="#f8f8f8"/>
            </svg>
        </div>
    </div>

    <!-- Utility bar -->
    <div class="utility-bar">
        <!-- Font case control -->
        <div class="case-control">Aa</div>
        
        <!-- Font justification style control -->
        <div class="justify-control"> 
            <!-- Justify left icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M0 0H20V2.85714H0V0Z" fill="#181818"/>
                <path d="M0 5.71429H11.4286V8.57143H0V5.71429Z" fill="#181818"/>
                <path d="M0 11.4286H20V14.2857H0V11.4286Z" fill="#181818"/>
                <path d="M0 17.1429H11.4286V20H0V17.1429Z" fill="#181818"/>
                </svg>

            <!-- Justify center icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M0 0H20V2.85714H0V0Z" fill="#181818"/>
                <path d="M4.28571 5.71429H15.7143V8.57143H4.28571V5.71429Z" fill="#181818"/>
                <path d="M0 11.4286H20V14.2857H0V11.4286Z" fill="#181818"/>
                <path d="M4.28571 17.1429H15.7143V20H4.28571V17.1429Z" fill="#181818"/>
            </svg>

            <!-- Justify right icon -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M20 0H0V2.85714H20V0Z" fill="#181818"/>
                <path d="M20 5.71429H8.57143V8.57143H20V5.71429Z" fill="#181818"/>
                <path d="M20 11.4286H0V14.2857H20V11.4286Z" fill="#181818"/>
                <path d="M20 17.1429H8.57143V20H20V17.1429Z" fill="#181818"/>
            </svg>
        </div>

        <!-- Font size control -->
        <div class="slider">
            <input type="range" min="0" max="100" value="0" id="range" />
            <div class="value">0</div>
        </div>
    </div>

    <!-- Search box container with SVG icons -->
    <div class="search-box-container">
        <!-- Search box -->
        <input type="text" id="search-box" v-model="searchQuery" placeholder="Search fonts..." class="search-box" autocomplete="off"/>
        
        <!-- Search icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 10 10" fill="none" class="search-icon">
            <circle cx="3.82653" cy="3.82653" r="3.32653" stroke="currentColor"/>
            <path d="M6.42859 6.42859L10 10" stroke="currentColor"/>
        </svg>

        <!-- Clear icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 10 10" fill="none" class="clear-icon" @click="clearSearch">
            <path d="M7.5 2.5L2.5 7.5" stroke="currentColor" stroke-linecap="square" stroke-linejoin="round"/>
            <path d="M2.5 2.5L7.5 7.5" stroke="currentColor" stroke-linecap="square" stroke-linejoin="round"/>
        </svg>

        <!-- Sort icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 10 10" fill="none" class="sort-icon">
            <path d="M0 0H10V1H0V0Z" fill="#currentColor"/>
            <path d="M0 3H8V4H0V3Z" fill="#currentColor"/>
            <path d="M0 6H6V7H0V6Z" fill="#currentColor"/>
            <path d="M0 9H4V10H0V9Z" fill="#currentColor"/>
        </svg>
    </div>

    <!-- Main content rectangle container -->
    <div class="main-content">
        <h1>Font list</h1>
        <ul>
            <li v-for="font in fonts" :key="font" :style="{ fontFamily: font }">
                {{ font }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&display=swap');

    /* Titlebar styling */
    .titlebar {
        height: 44px;
        background: #181818;
        user-select: none;
        display: flex;
        justify-content: flex-end;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        align-items: center;
    }

    .titlebar-logo {
        position: absolute;
        left: 10px;
        top: 10px;
    }

    .titlebar-logo img {
        height: 50px;
        width: auto;
    }

    .titlebar-button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 44px;
        height: 44px;
        user-select: none;
        -webkit-user-select: none;
    }

    /* Titlebar icon animation */
    .titlebar-button .icon {
        width: 44px;
        height: 44px;
        display: block;
        transition: transform 0.125s ease-in-out;
    }

    .titlebar-button:hover .icon {
        transform: scale(1.5);
    }

    /* Utility bar styling */
    .utility-bar {
        display: flex;
        height: 70px;
        background-color: #f1f1f1;
        border-top-left-radius: 50px;
        position: absolute;
        padding: 0 30px;
        top: 44px;
        left: 150px;
        right: 0;
        justify-content: space-between;
        align-items: center;
        z-index: 1;
        gap: 30px;
    }
    
    .case-control {
        font-family: "Space Grotesk", sans-serif;
        font-size: 35px;
        font-weight: 700;
        color: #181818;
    }

    .justify-control {
        display: flex;
        gap: 0.4rem;
        flex-shrink: 0;
    }

    input[type="range"] {
        /* removing default appearance */
        -webkit-appearance: none;
        appearance: none;
        /* creating a custom design */
        width: 100%;
        cursor: pointer;
        outline: none;
        height: 2px;
        background: #d8d8d8;
    }

    /* Thumb: webkit */
    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        height: 10px;
        width: 10px;
        background-color: #181818;
        border: none;
    }

    /* Thumb: Firefox */
    input[type="range"]::-moz-range-thumb {
        height: 10px;
        width: 10px;
        background-color: #181818;
        border: none;
    }

    .slider {
        display: flex;
        align-items: center;
        flex-grow: 1;
        height: 4rem;
        width: 100%;
    }

    .value {
        font-size: 16px;
        color: #181818;
        text-align: center;
        width: 30px;
        margin-left: 10px;
    }

    /* Container for the search box and icons */
    .search-box-container {
        position: relative;
        width: 45vw;
        height: 30px;
        margin: -1px auto;
        display: flex;
        justify-content: center;
        transition: width 0.3s ease;
    }

    /* Styling for the search box */
    .search-box {
        width: 100%;
        height: 100%;
        background-color: #1f1f1f;
        color: #d8d8d8;
        padding-left: 30px;
        padding-right: 30px;
        border: none;
        border-radius: 5px;
        font-family: "Space Grotesk", sans-serif;
        font-size: 14px;
        text-align: center;
        outline: none;
        box-sizing: border-box;
        transition: background-color 0.3s, color 0.3s;
    }

    /* Hover effect for the search box container */
    .search-box-container:hover .search-box {
        background-color: #282828;
        color: #d8d8d8;
    }

    /* Styling for the left search icon */
    .search-icon {
        position: absolute;
        top: 50%;
        left: 7px;
        transform: translateY(-50%);
        color: #888888;
        transition: color 0.3s;
    }

    /* Styling for the right search icon (clear icon) */
    .clear-icon {
        position: absolute;
        top: 50%;
        right: 7px;
        transform: translateY(-50%);
        color: #888888;
        transition: color 0.3s;
        cursor: pointer;
    }

    /* Hover effect for the search icons */
    .search-box-container:hover .search-icon,
    .search-box-container:hover .clear-icon {
        color: #d8d8d8;
    }

    /* Hover effect for the placeholder text */
    .search-box-container:hover .search-box::placeholder {
        color: #d8d8d8;
    }

    /* Styling for the placeholder text */
    .search-box::placeholder {
        color: #888888;
        text-align: center;
        font-family: "Space Grotesk", sans-serif;
        font-size: 14px;
        transition: color 0.3s;
    }
    /* Styling for the sort icon */
    .sort-icon {
        position: absolute;
        top: 50%;
        right: -20px;
        transform: translateY(-50%);
        fill: #888888;
        transition: fill 0.3s;
    }

    .sort-icon:hover {
        fill: #d8d8d8;
    }

    /* Main content rectangle container */
    .main-content {
        position: absolute;
        top: 114px;
        left: 150px;
        right: 0;
        color: #181818;
        background-color: #f8f8f8;
        padding: 20px;
        z-index: -1;
        height: calc(100vh - 114px);
        overflow-y: auto;
        box-sizing: border-box;
    }

    .main-content h1 {
        margin-top: 10px;
        margin-left: 6px;
        font-size: 40px;
        font-weight: 700;
        -webkit-text-stroke: 1px #181818;
    }
</style>


<style>
    :root {
        font-family: "Space Grotesk", sans-serif;
        font-size: 16px;
        line-height: 24px;

        color: #0f0f0f;
        background-color: #f6f6f6;

        font-synthesis: none;
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        -webkit-text-size-adjust: 100%;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            color: #181818;
            background-color: #181818;
        }
    }
</style>