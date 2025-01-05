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
            <img src="/src/assets/Fontura-Title.svg" alt="Fontura" shape-rendering="crispEdges"/>
        </div>

        <!-- Minimize button -->
        <div class="titlebar-button" id="titlebar-minimize">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none" shape-rendering="crispEdges">
                <rect x="12.25" y="18.25" width="11.5" height="0.5" fill="#332922" stroke="#332922" stroke-width="0.5"/>
            </svg>
        </div>

        <!-- Maximize button -->
        <div class="titlebar-button" id="titlebar-maximize">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
                <rect x="12.5" y="14.5" width="9" height="9" stroke="#332922"/>
                <rect x="24" y="12" width="1" height="9" transform="rotate(90 24 12)" fill="#332922"/>
                <rect x="15" y="14" width="1" height="2" transform="rotate(-180 15 14)" fill="#332922"/>
                <rect x="22" y="22" width="1" height="2" transform="rotate(-90 22 22)" fill="#332922"/>
                <rect x="24" y="21" width="1" height="9" transform="rotate(-180 24 21)" fill="#332922"/>
            </svg>
        </div>

        <!-- Close button -->
        <div class="titlebar-button" id="titlebar-close">
            <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
                <path d="M12 12L24 24M24 12L12 24" stroke="#332922"/>
            </svg>
        </div>
    </div>

    <!-- System font list -->
    <main class="container">
        <h1>Fonts List</h1>
        <ul>
            <li v-for="(font, index) in fonts" :key="index" :style="{ fontFamily: font }">
                {{ font }}
            </li>
        </ul>
    </main>
</template>

<style scoped>
    /* Titlebar styling */
    .titlebar {
        height: 36px;
        background: #e5e5e5;
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
        left: 2px;
        top: 2px;
    }

    .titlebar-logo img {
        height: 50px;
        width: auto;
    }

    .titlebar-button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 36px;
        height: 36px;
        user-select: none;
        -webkit-user-select: none;
    }

    /* Titlebar icon animation */
    .titlebar-button .icon {
        width: 36px;
        height: 36px;
        display: block;
        transition: transform 0.125s ease-in-out;
    }

    .titlebar-button:hover .icon {
        transform: scale(1.5);
    }

    /* Font list styling */
    .container {
        margin-top: 60px;
        padding: 20px;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        margin: 5px 0;
        font-size: 16px;
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
            color: #111111;
            background-color: #e5e5e5;
        }
    }
</style>