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

    <!-- Main content rectangle container -->
    <div class="main-content">
        <!-- Add your content here -->
        <h1>Welcome to the Main Content</h1>
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

    /* Main content rectangle container */
    .main-content {
        position: absolute;
        top: 44px;
        left: 44px;
        right: 0;
        bottom: 0;
        background-color: #f8f8f8;
        padding: 20px;
    }
</style>


<style>
    :root {
        font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
        font-size: 16px;
        line-height: 24px;
        font-weight: 400;

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