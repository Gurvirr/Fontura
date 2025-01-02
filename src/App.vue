<script setup lang="ts">
    import { ref } from "vue";
    import { onMounted } from "vue";
    import { invoke } from "@tauri-apps/api/core";
    import { getCurrentWindow } from "@tauri-apps/api/window";

    const greetMsg = ref("");
    const name = ref("");

    async function greet() {
        greetMsg.value = await invoke("greet", { name: name.value });
    }

    // Titlebar functionality //
    onMounted(() => {
        const appWindow = getCurrentWindow();

        // Event listeners for minimize button //
        document.getElementById("titlebar-minimize")?.addEventListener("click", () => appWindow.minimize());

        // Event listeners for maximize button //
        document.getElementById("titlebar-maximize")?.addEventListener("click", () => appWindow.toggleMaximize());

        // Event listeners for close button //
        document.getElementById("titlebar-close")?.addEventListener("click", () => appWindow.close());
    });
</script>

<template>
    <!-- Titlebar structure -->
    <div data-tauri-drag-region class="titlebar">
        <div class="titlebar-logo">
            <img src="./assets/Fontura-Title.svg" alt="Fontura" shape-rendering="crispEdges"/>
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

    <main class="container">
        <h1>Welcome to Tauri + Vue</h1>

        <div class="row">
            <a href="https://vitejs.dev" target="_blank">
                <img src="/Fontura.png" class="logo vite" alt="Vite logo" />
            </a>
            <a href="https://tauri.app" target="_blank">
                <img src="/Fontura.png" class="logo tauri" alt="Tauri logo" />
            </a>
            <a href="https://vuejs.org/" target="_blank">
                <img src="/Fontura.png" class="logo vue" alt="Vue logo" />
            </a>
        </div>
        <p>Click on the Tauri, Vite, and Vue logos to learn more.</p>

        <form class="row" @submit.prevent="greet">
            <input id="greet-input" v-model="name" placeholder="Enter a name..." />
            <button type="submit">Greet</button>
        </form>
        <p>{{ greetMsg }}</p>
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
        left: 2px; /* Adjust the distance from the left edge */
        top: 2px; /* Center vertically */
    }

    .titlebar-logo img {
        height: 50px; /* Adjust the logo size */
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

    /* .titlebar-button:hover {
        background: #5bbec3;
    } */

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
    
    .logo.vite:hover {
        filter: drop-shadow(0 0 2em #747bff);
    }

    .logo.vue:hover {
        filter: drop-shadow(0 0 2em #249b73);
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

    .container {
        margin: 0;
        padding-top: 10vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }

    .logo {
        height: 6em;
        padding: 1.5em;
        will-change: filter;
        transition: 0.75s;
    }

    .logo.tauri:hover {
        filter: drop-shadow(0 0 2em #24c8db);
    }

    .row {
        display: flex;
        justify-content: center;
    }

    a {
        font-weight: 500;
        color: #646cff;
        text-decoration: inherit;
    }

    a:hover {
        color: #535bf2;
    }

    h1 {
        text-align: center;
    }

    input,
    button {
        border-radius: 8px;
        border: 1px solid transparent;
        padding: 0.6em 1.2em;
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
        color: #0f0f0f;
        background-color: #ffffff;
        transition: border-color 0.25s;
        box-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
    }

    button {
        cursor: pointer;
    }

    button:hover {
        border-color: #396cd8;
    }
    button:active {
        border-color: #396cd8;
        background-color: #e8e8e8;
    }

    input,
    button {
        outline: none;
    }

    #greet-input {
        margin-right: 5px;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            color: #111111;
            background-color: #e5e5e5;
        }

        a:hover {
            color: #24c8db;
        }

        input,
        button {
            color: #ffffff;
            background-color: #0f0f0f98;
        }
        button:active {
            background-color: #0f0f0f69;
        }
    }
</style>