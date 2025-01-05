<script setup lang="ts">
    import { onMounted } from "vue";
    import { ref } from "vue";
    import { getCurrentWindow } from "@tauri-apps/api/window";

    // Font list state //
    const fonts = ref<string[]>([]);
    
    onMounted(() => {
        // Titlebar functionality //
        const appWindow = getCurrentWindow();

        // Event listeners for minimize button //
        document.getElementById("titlebar-minimize")?.addEventListener("click", () => appWindow.minimize());

        // Event listeners for maximize button //
        document.getElementById("titlebar-maximize")?.addEventListener("click", () => appWindow.toggleMaximize());

        // Event listeners for close button //
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
    });
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

    <!-- Search box container with SVG icons -->
    <div class="search-box-container">
        <!-- Search box -->
        <input type="text" id="search-box" placeholder="Search fonts..." class="search-box"/>
        
        <!-- Search icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 10 10" fill="none" class="search-icon">
            <circle cx="3.82653" cy="3.82653" r="3.32653" stroke="currentColor"/>
            <path d="M6.42859 6.42859L10 10" stroke="currentColor"/>
        </svg>


        <!-- Clear icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 10 10" fill="none" class="clear-icon">
            <path d="M7.5 2.5L2.5 7.5" stroke="currentColor" stroke-linecap="square" stroke-linejoin="round"/>
            <path d="M2.5 2.5L7.5 7.5" stroke="currentColor" stroke-linecap="square" stroke-linejoin="round"/>
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

    /* Container for the search box and icon */
    .search-box-container {
        position: relative;
        width: 315px;
        height: 24px;
        margin: 10px auto; /* Center the container horizontally */
        display: flex;
        justify-content: center;
    }

    /* Styling for the search box */
    .search-box {
        width: 100%;
        height: 100%;
        background-color: #1f1f1f;
        color: #d8d8d8;
        padding-left: 30px; /* Space for the icon */
        padding-right: 30px; /* Space for the icon */
        border: none;
        border-radius: 5px;
        font-family: 'Brockmann', sans-serif;
        font-size: 14px;
        text-align: center; /* Center the input text */
        outline: none; /* Remove the default outline */
        box-sizing: border-box; /* Include padding in the total height */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition */
    }

    /* Hover effect for the search box container */
    .search-box-container:hover .search-box {
        background-color: #282828; /* Change background color */
        color: #d8d8d8; /* Keep text color the same */
    }

    /* Styling for the left search icon */
    .search-icon {
        position: absolute;
        top: 50%;
        left: 7px;
        transform: translateY(-50%);
        color: #888888; /* Default color for the icon */
        transition: color 0.3s; /* Smooth transition */
    }

    /* Styling for the right search icon (close icon) */
    .clear-icon {
        position: absolute;
        top: 50%;
        right: 7px;
        transform: translateY(-50%);
        color: #888888; /* Default color for the icon */
        transition: color 0.3s; /* Smooth transition */
    }

    /* Hover effect for the search icons */
    .search-box-container:hover .search-icon,
    .search-box-container:hover .clear-icon {
        color: #d8d8d8; /* Change icon color to red */
    }

    /* Hover effect for the placeholder text */
    .search-box-container:hover .search-box::placeholder {
        color: #d8d8d8; /* Change placeholder text color */
    }

    /* Styling for the placeholder text */
    .search-box::placeholder {
        color: #888888; /* Initial placeholder text color */
        text-align: center; /* Center the placeholder text */
        font-family: 'Brockmann', sans-serif; /* Apply the Brockmann font to placeholder */
        font-size: 14px; /* Ensure the font size matches the input text */
        transition: color 0.3s; /* Smooth transition */
    }

    /* Main content rectangle container */
    .main-content {
        position: absolute;
        top: 44px;
        left: 44px;
        right: 0;
        color: #181818;
        background-color: #f8f8f8;
        padding: 20px;
        z-index: -1;
        height: calc(100vh - 44px);
        overflow-y: auto;
        border-top-left-radius: 50px;
        box-sizing: border-box;
    }

    .main-content h1 {
        margin-top: 10px;
        margin-left: 6px;
        font-size: 35px;
        text-shadow: 
            0.5px 0.5px 0 #181818, 
            -0.5px -0.5px 0 #181818,  
            0.5px -0.5px 0 #181818, 
            -0.5px 0.5px 0 #181818;
    }
</style>

<style>
    :root {
        font-family: "Brockmann", sans-serif;
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
            color: #f8f8f8;
            background-color: #181818;
        }
    }
</style>