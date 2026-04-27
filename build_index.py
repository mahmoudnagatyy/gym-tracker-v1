import json

html_content = """<!DOCTYPE html>
<html class="dark" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>KINETIC - Elite Performance</title>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Lexend:wght@400;600;700;900&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet"/>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Chart.js and SheetJS -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>

<!-- Tailwind Config -->
<script id="tailwind-config">
tailwind.config = {
    darkMode: "class",
    theme: {
    extend: {
        "colors": {
            "surface": "#131313",
            "outline-variant": "#564334",
            "error": "#ffb4ab",
            "on-primary-container": "#623200",
            "surface-container-low": "#1c1b1b",
            "on-tertiary-container": "#004922",
            "outline": "#a48c7a",
            "surface-tint": "#ffb77d",
            "on-primary-fixed": "#2f1500",
            "on-tertiary-fixed": "#00210c",
            "inverse-surface": "#e5e2e1",
            "tertiary-fixed": "#6bfe9c",
            "on-secondary-fixed-variant": "#004f58",
            "inverse-on-surface": "#313030",
            "on-secondary": "#00363d",
            "primary": "#ffb77d",
            "on-primary": "#4d2600",
            "on-error-container": "#ffdad6",
            "on-primary-fixed-variant": "#6e3900",
            "primary-fixed-dim": "#ffb77d",
            "on-background": "#e5e2e1",
            "tertiary": "#4ae183",
            "on-surface": "#e5e2e1",
            "tertiary-container": "#1bc268",
            "secondary-fixed-dim": "#00daf3",
            "surface-variant": "#353534",
            "secondary": "#bdf4ff",
            "on-secondary-container": "#00616d",
            "on-tertiary": "#003919",
            "on-error": "#690005",
            "primary-container": "#ff8c00",
            "surface-container-lowest": "#0e0e0e",
            "on-tertiary-fixed-variant": "#005228",
            "on-secondary-fixed": "#001f24",
            "surface-container-high": "#2a2a2a",
            "inverse-primary": "#904d00",
            "background": "#131313",
            "surface-container-highest": "#353534",
            "surface-dim": "#131313",
            "surface-bright": "#393939",
            "error-container": "#93000a",
            "tertiary-fixed-dim": "#4ae183",
            "primary-fixed": "#ffdcc3",
            "secondary-container": "#00e3fd",
            "surface-container": "#201f1f",
            "on-surface-variant": "#ddc1ae",
            "secondary-fixed": "#9cf0ff"
        },
        "fontFamily": {
            "label-caps": ["Space Grotesk"],
            "h2": ["Lexend"],
            "body-lg": ["Inter"],
            "h1": ["Lexend"],
            "data-display": ["Space Grotesk"],
            "body-md": ["Inter"]
        }
    }
    }
}
</script>
<style>
    .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
    .material-symbols-outlined.fill { font-variation-settings: 'FILL' 1; }
    .glass-panel { background: rgba(30, 30, 30, 0.6); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.2); }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255, 140, 0, 0.5); }
    
    .view-section { display: none; }
    .view-section.active { display: block; animation: fadeIn 0.3s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

    /* Timer overlay */
    #timer-overlay {
        position: fixed; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(5px);
        display: none; justify-content: center; align-items: center; z-index: 1000; flex-direction: column;
    }
    .circular-chart { display: block; margin: 0 auto; max-width: 80%; max-height: 250px; }
    .circle-bg { fill: none; stroke: #333; stroke-width: 3.8; }
    .circle { fill: none; stroke-width: 3.8; stroke-linecap: round; transition: stroke-dasharray 1s linear; }
    .percentage { fill: #fff; font-family: 'Space Grotesk'; font-size: 0.5em; text-anchor: middle; font-weight: bold; }
</style>
</head>
<body class="bg-background text-on-surface min-h-screen flex overflow-hidden">

<!-- SideNavBar (WEB) -->
<nav class="hidden md:flex h-screen w-64 fixed left-0 top-0 z-40 bg-zinc-950 border-r border-white/10 flex-col py-6 px-4 gap-2">
    <div class="mb-8 px-2">
        <h1 class="font-['Lexend'] text-xl font-black text-orange-500 tracking-tighter">KINETIC</h1>
        <p class="font-['Space_Grotesk'] text-[10px] font-bold tracking-widest text-zinc-500 mt-1">ELITE PERFORMANCE</p>
    </div>
    <div class="flex flex-col gap-2 w-full" id="nav-web">
        <button data-target="home" class="nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100">
            <span class="material-symbols-outlined">home_storage</span><span>Home</span>
        </button>
        <button data-target="workout" class="nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100">
            <span class="material-symbols-outlined">fitness_center</span><span>Workout Logger</span>
        </button>
        <button data-target="progress" class="nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100">
            <span class="material-symbols-outlined">monitoring</span><span>Progress</span>
        </button>
        <button data-target="supps" class="nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100">
            <span class="material-symbols-outlined">pill</span><span>Supplements</span>
        </button>
        <button data-target="export" class="nav-btn mt-auto flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100">
            <span class="material-symbols-outlined">ios_share</span><span>Export</span>
        </button>
    </div>
</nav>

<!-- TopAppBar (MOBILE) -->
<header class="md:hidden fixed top-0 w-full z-50 border-b border-white/10 bg-zinc-950/80 backdrop-blur-xl flex justify-between items-center px-5 h-16">
    <div class="font-['Lexend'] tracking-tight text-2xl font-black text-orange-500 tracking-tighter">KINETIC</div>
</header>

<!-- Main Canvas -->
<main class="flex-1 md:ml-64 h-screen overflow-y-auto pt-16 md:pt-0 pb-24 md:pb-0 relative">
    <div class="p-4 md:p-8 max-w-7xl mx-auto space-y-8">
        
        <!-- HOME SECTION -->
        <section id="view-home" class="view-section active">
            <header class="mb-8">
                <h2 class="font-h1 text-4xl text-on-surface font-bold">Dashboard</h2>
                <p class="font-body-lg text-zinc-400">Overview of your training metrics.</p>
            </header>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="glass-panel p-6 rounded-xl flex flex-col justify-between h-40">
                    <div class="flex justify-between items-start">
                        <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest">Total Sessions</h3>
                        <span class="material-symbols-outlined text-orange-500">calendar_month</span>
                    </div>
                    <div class="font-data-display text-4xl text-on-surface mt-auto" id="home-total-sessions">0</div>
                </div>
                <div class="glass-panel p-6 rounded-xl flex flex-col justify-between h-40 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-orange-500/10 to-transparent pointer-events-none"></div>
                    <div class="flex justify-between items-start relative z-10">
                        <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest">Total Volume</h3>
                        <span class="material-symbols-outlined text-cyan-400">fitness_center</span>
                    </div>
                    <div class="font-data-display text-4xl text-on-surface mt-auto relative z-10 flex items-baseline gap-2">
                        <span id="home-total-volume">0</span> <span class="font-label-caps text-sm text-zinc-500">kg</span>
                    </div>
                </div>
                <div class="glass-panel p-6 rounded-xl flex flex-col justify-between h-40 border-l-4 border-l-orange-500">
                    <div class="flex justify-between items-start">
                        <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest">Last Session</h3>
                        <span class="material-symbols-outlined text-zinc-500">history</span>
                    </div>
                    <div class="mt-auto">
                        <p class="font-h2 text-xl text-on-surface" id="home-last-type">-</p>
                        <p class="font-body-md text-sm text-zinc-400" id="home-last-date">-</p>
                    </div>
                </div>
            </div>
            
            <div class="mt-8">
                <h3 class="font-h2 text-2xl text-on-surface mb-6">Recent Sessions</h3>
                <div class="glass-panel rounded-xl overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-white/5 bg-white/[0.02]">
                                    <th class="py-4 px-6 font-label-caps text-xs text-zinc-500 uppercase">Date</th>
                                    <th class="py-4 px-6 font-label-caps text-xs text-zinc-500 uppercase">Type</th>
                                    <th class="py-4 px-6 font-label-caps text-xs text-zinc-500 uppercase">Volume</th>
                                </tr>
                            </thead>
                            <tbody id="home-recent-table" class="font-body-md text-zinc-300">
                                <!-- Populated by JS -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- WORKOUT LOGGER SECTION -->
        <section id="view-workout" class="view-section">
            <header class="mb-8">
                <h2 class="font-h1 text-4xl text-on-surface font-bold">Workout Logger</h2>
            </header>
            
            <div id="workout-setup" class="glass-panel p-6 rounded-xl max-w-lg">
                <div class="mb-4">
                    <label class="block text-xs text-zinc-400 uppercase tracking-widest mb-2 font-label-caps">Session Type</label>
                    <select id="wo-type" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-3 text-white focus:border-orange-500 focus:ring-1 focus:ring-orange-500 outline-none">
                        <option value="ANT-A">ANT-A (Anterior A)</option>
                        <option value="POST-A">POST-A (Posterior A)</option>
                        <option value="ANT-B">ANT-B (Anterior B)</option>
                        <option value="POST-B">POST-B (Posterior B)</option>
                    </select>
                </div>
                <div class="grid grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-xs text-zinc-400 uppercase tracking-widest mb-2 font-label-caps">Date</label>
                        <input type="date" id="wo-date" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-3 text-white">
                    </div>
                    <div>
                        <label class="block text-xs text-zinc-400 uppercase tracking-widest mb-2 font-label-caps">Time</label>
                        <input type="time" id="wo-time" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-3 text-white">
                    </div>
                </div>
                <div class="mb-6">
                    <label class="block text-xs text-zinc-400 uppercase tracking-widest mb-2 font-label-caps">Bodyweight (kg) - Optional</label>
                    <input type="number" id="wo-bw" step="0.1" placeholder="e.g. 75.5" class="w-full bg-zinc-900 border border-white/10 rounded-lg p-3 text-white focus:border-orange-500 focus:ring-1 focus:ring-orange-500 outline-none">
                </div>
                <button onclick="startWorkout()" class="w-full bg-orange-500 text-black font-bold py-3 rounded-lg hover:bg-orange-400 transition-colors">START WORKOUT</button>
            </div>
            
            <div id="workout-active" class="hidden flex-col md:flex-row gap-6">
                <!-- Sidebar / Exercises -->
                <div class="md:w-1/3 space-y-4" id="wo-exercise-list">
                    <!-- Populated by JS -->
                </div>
                
                <!-- Main Area / Sets -->
                <div class="md:w-2/3 glass-panel p-6 rounded-xl flex-1 flex flex-col">
                    <div class="flex justify-between items-center mb-6">
                        <h3 id="wo-current-ex-name" class="font-h2 text-2xl text-on-surface">Select Exercise</h3>
                        <div class="text-right">
                            <div class="text-xs text-zinc-400 font-label-caps uppercase tracking-widest">Total Volume</div>
                            <div id="wo-total-volume" class="text-xl font-bold text-cyan-400">0 kg</div>
                        </div>
                    </div>
                    <div id="wo-sets-area" class="flex-1 space-y-3 mb-6">
                        <!-- Populated by JS -->
                    </div>
                    <button onclick="addSet()" class="w-full border border-orange-500 text-orange-500 font-bold py-3 rounded-lg hover:bg-orange-500/10 transition-colors mb-4">+ ADD SET</button>
                    <button onclick="finishWorkout()" class="w-full bg-cyan-500 text-black font-bold py-3 rounded-lg hover:bg-cyan-400 transition-colors mt-auto">FINISH SESSION</button>
                </div>
            </div>
        </section>
        
        <!-- PROGRESS SECTION -->
        <section id="view-progress" class="view-section">
            <header class="mb-8">
                <h2 class="font-h1 text-4xl text-on-surface font-bold">Progress Analytics</h2>
            </header>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div class="glass-panel p-4 rounded-xl">
                    <canvas id="chart-volume" height="250"></canvas>
                </div>
                <div class="glass-panel p-4 rounded-xl">
                    <canvas id="chart-bw" height="250"></canvas>
                </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="glass-panel p-4 rounded-xl md:col-span-1 flex items-center justify-center">
                    <canvas id="chart-doughnut" height="250"></canvas>
                </div>
                <div class="glass-panel p-4 rounded-xl md:col-span-2 overflow-x-auto">
                    <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest mb-4">Best Volume per Exercise</h3>
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="border-b border-white/5 text-zinc-500 font-label-caps">
                                <th class="pb-2">Exercise</th>
                                <th class="pb-2 text-right">Best Vol (kg)</th>
                                <th class="pb-2 text-right">Date</th>
                            </tr>
                        </thead>
                        <tbody id="progress-best-table" class="text-zinc-300">
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- SUPPLEMENTS SECTION -->
        <section id="view-supps" class="view-section">
            <header class="mb-8">
                <h2 class="font-h1 text-4xl text-on-surface font-bold">Supplements & Wellness</h2>
            </header>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Supps Checklist -->
                <div class="glass-panel p-6 rounded-xl">
                    <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest mb-6">Daily Stack</h3>
                    <div class="space-y-4">
                        <label class="flex justify-between items-center p-4 bg-white/5 rounded-lg border border-white/5 cursor-pointer hover:bg-white/10 transition-colors">
                            <span class="font-bold text-lg text-white">Creatine <span class="text-zinc-500 text-sm font-normal">5g</span></span>
                            <input type="checkbox" id="supp-creatine" onchange="saveSupps()" class="w-6 h-6 rounded text-orange-500 focus:ring-0 bg-zinc-900 border-zinc-600">
                        </label>
                        <label class="flex justify-between items-center p-4 bg-white/5 rounded-lg border border-white/5 cursor-pointer hover:bg-white/10 transition-colors">
                            <span class="font-bold text-lg text-white">Multivitamin</span>
                            <input type="checkbox" id="supp-multi" onchange="saveSupps()" class="w-6 h-6 rounded text-orange-500 focus:ring-0 bg-zinc-900 border-zinc-600">
                        </label>
                        <label class="flex justify-between items-center p-4 bg-white/5 rounded-lg border border-white/5 cursor-pointer hover:bg-white/10 transition-colors">
                            <span class="font-bold text-lg text-white">Omega-3</span>
                            <input type="checkbox" id="supp-omega" onchange="saveSupps()" class="w-6 h-6 rounded text-orange-500 focus:ring-0 bg-zinc-900 border-zinc-600">
                        </label>
                    </div>
                </div>
                
                <!-- Water Tracker -->
                <div class="glass-panel p-6 rounded-xl">
                    <div class="flex justify-between items-center mb-6">
                        <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest">Hydration Tracker</h3>
                        <span class="text-cyan-400 font-bold" id="water-count-text">0 / 8</span>
                    </div>
                    <div class="grid grid-cols-4 gap-4 mb-6" id="water-grid">
                        <!-- Glasses JS -->
                    </div>
                    <div class="mt-4 pt-4 border-t border-white/10">
                        <canvas id="chart-water" height="150"></canvas>
                    </div>
                </div>
            </div>
            
            <!-- Streak -->
            <div class="glass-panel p-6 rounded-xl mt-6">
                <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest mb-4">7-Day Consistency</h3>
                <div class="flex gap-2 justify-between" id="streak-grid">
                    <!-- JS filled -->
                </div>
                <p id="motivational-msg" class="mt-4 text-center text-orange-400 italic font-medium">Keep pushing!</p>
            </div>
        </section>

        <!-- EXPORT SECTION -->
        <section id="view-export" class="view-section">
            <header class="mb-8">
                <h2 class="font-h1 text-4xl text-on-surface font-bold">Data Center</h2>
            </header>
            <div class="glass-panel p-6 rounded-xl max-w-lg mb-6">
                <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest mb-6">Export Data</h3>
                <div class="space-y-4">
                    <button onclick="exportCSV()" class="w-full border border-white/20 text-white font-medium py-3 rounded-lg hover:bg-white/5 transition-colors flex justify-center items-center gap-2">
                        <span class="material-symbols-outlined">description</span> CSV (All Sets)
                    </button>
                    <button onclick="exportXLSX()" class="w-full bg-cyan-500/20 border border-cyan-500 text-cyan-400 font-bold py-3 rounded-lg hover:bg-cyan-500/30 transition-colors flex justify-center items-center gap-2">
                        <span class="material-symbols-outlined">table_view</span> XLSX Excel Backup
                    </button>
                    <button onclick="exportJSON()" class="w-full border border-white/20 text-white font-medium py-3 rounded-lg hover:bg-white/5 transition-colors flex justify-center items-center gap-2">
                        <span class="material-symbols-outlined">code</span> JSON Backup
                    </button>
                </div>
            </div>
            
            <div class="glass-panel p-6 rounded-xl max-w-lg">
                <h3 class="font-label-caps text-xs text-zinc-400 uppercase tracking-widest mb-6">Danger Zone</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs text-zinc-400 uppercase mb-2">Import JSON</label>
                        <input type="file" id="import-file" accept=".json" class="w-full bg-zinc-900 text-sm text-zinc-400 border border-white/10 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-l-lg file:border-0 file:bg-white/10 file:text-white hover:file:bg-white/20">
                        <button onclick="importJSON()" class="mt-2 w-full border border-orange-500 text-orange-500 font-medium py-2 rounded-lg hover:bg-orange-500/10">Import</button>
                    </div>
                    <button onclick="clearAllData()" class="w-full bg-red-500/20 border border-red-500 text-red-400 font-bold py-3 rounded-lg hover:bg-red-500/30 transition-colors flex justify-center items-center gap-2 mt-4">
                        <span class="material-symbols-outlined">delete_forever</span> CLEAR ALL DATA
                    </button>
                </div>
            </div>
        </section>
        
    </div>
</main>

<!-- BottomNavBar (MOBILE) -->
<nav class="md:hidden fixed bottom-0 w-full z-40 bg-zinc-950/90 backdrop-blur-xl border-t border-white/10 flex justify-around items-center h-20 pb-safe" id="nav-mobile">
    <button data-target="home" class="nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1">
        <span class="material-symbols-outlined text-[24px]">home_storage</span><span class="font-['Lexend'] text-[10px] font-bold">Home</span>
    </button>
    <button data-target="workout" class="nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1">
        <span class="material-symbols-outlined text-[24px]">fitness_center</span><span class="font-['Lexend'] text-[10px] font-bold">Log</span>
    </button>
    <button data-target="progress" class="nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1">
        <span class="material-symbols-outlined text-[24px]">monitoring</span><span class="font-['Lexend'] text-[10px] font-bold">Stats</span>
    </button>
    <button data-target="supps" class="nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1">
        <span class="material-symbols-outlined text-[24px]">pill</span><span class="font-['Lexend'] text-[10px] font-bold">Supps</span>
    </button>
    <button data-target="export" class="nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1">
        <span class="material-symbols-outlined text-[24px]">ios_share</span><span class="font-['Lexend'] text-[10px] font-bold">More</span>
    </button>
</nav>

<!-- Timer Overlay -->
<div id="timer-overlay">
    <svg viewBox="0 0 36 36" class="circular-chart text-orange-500">
        <path class="circle-bg" stroke="rgba(255,140,0,0.2)" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
        <path class="circle" id="timer-circle" stroke="currentColor" stroke-dasharray="100, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
        <text x="18" y="20.35" class="percentage" id="timer-text">90</text>
    </svg>
    <div class="flex gap-4 mt-8">
        <button onclick="addTimerTime()" class="border border-white/20 px-6 py-2 rounded-full text-white">+15s</button>
        <button onclick="closeTimer()" class="bg-orange-500 text-black px-6 py-2 rounded-full font-bold">SKIP</button>
    </div>
</div>

<script>
// --- STATE & DATA ---
const PRESETS = {
    'ANT-A': ['Incline DB Press', 'Pec Deck', 'Leg Press', 'Leg Ext', 'Lateral Raises', 'Tricep Pushdowns'],
    'POST-A': ['Lat Pulldown', 'Seated Row', 'Hamstring Curls', 'Calf Raises', 'Face Pulls', 'Bicep Curls'],
    'ANT-B': ['Bench Press', 'Overhead Press', 'Hack Squat', 'Split Squats', 'Cable Laterals', 'Overhead Tricep'],
    'POST-B': ['Barbell Row', 'Pullups', 'RDL', 'Calf Raises', 'Reverse Pec Deck', 'Hammer Curls']
};

let sessions = JSON.parse(localStorage.getItem('kinetic_sessions') || '[]');
let supps = JSON.parse(localStorage.getItem('kinetic_supps') || '{}');
let woState = null;
let timerInt = null;

// --- AUDIO ---
const beepCtx = new (window.AudioContext || window.webkitAudioContext)();
function playBeep() {
    if(beepCtx.state === 'suspended') beepCtx.resume();
    const osc = beepCtx.createOscillator();
    const gain = beepCtx.createGain();
    osc.connect(gain); gain.connect(beepCtx.destination);
    osc.type = 'sine'; osc.frequency.setValueAtTime(800, beepCtx.currentTime);
    gain.gain.setValueAtTime(1, beepCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, beepCtx.currentTime + 0.5);
    osc.start(beepCtx.currentTime); osc.stop(beepCtx.currentTime + 0.5);
}

// --- NAVIGATION ---
function switchNav(target) {
    document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
    document.getElementById('view-' + target).classList.add('active');
    
    // update web nav
    document.querySelectorAll('#nav-web .nav-btn').forEach(b => {
        b.className = "nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 text-zinc-500 hover:bg-white/5 hover:text-zinc-100";
        if(b.dataset.target === target) {
            b.className = "nav-btn flex items-center gap-3 px-4 py-3 rounded-lg w-full text-left font-['Lexend'] text-sm font-medium transition-all duration-200 bg-orange-500/10 text-orange-500 border-r-2 border-orange-500 backdrop-blur-md";
            b.querySelector('span').classList.add('fill');
        } else {
            b.querySelector('span').classList.remove('fill');
        }
    });
    
    // update mobile nav
    document.querySelectorAll('#nav-mobile .nav-btn-mob').forEach(b => {
        b.className = "nav-btn-mob flex flex-col items-center justify-center w-full h-full text-zinc-500 gap-1";
        if(b.dataset.target === target) b.classList.replace('text-zinc-500', 'text-orange-500');
    });

    if(target === 'home') renderHome();
    if(target === 'progress') renderProgress();
    if(target === 'supps') renderSupps();
}

document.querySelectorAll('.nav-btn, .nav-btn-mob').forEach(b => {
    b.addEventListener('click', () => switchNav(b.dataset.target));
});

// --- HOME ---
function renderHome() {
    document.getElementById('home-total-sessions').textContent = sessions.length;
    let totV = sessions.reduce((s, x) => s + x.totalVolume, 0);
    document.getElementById('home-total-volume').textContent = totV.toLocaleString();
    
    if(sessions.length > 0) {
        const last = sessions[sessions.length - 1];
        document.getElementById('home-last-type').textContent = last.type;
        document.getElementById('home-last-date').textContent = last.date;
    }
    
    const tbody = document.getElementById('home-recent-table');
    tbody.innerHTML = '';
    [...sessions].reverse().slice(0, 5).forEach(s => {
        tbody.innerHTML += `
            <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                <td class="py-4 px-6">${s.date}</td>
                <td class="py-4 px-6"><span class="bg-orange-500/20 text-orange-400 px-2 py-1 rounded font-label-caps">${s.type}</span></td>
                <td class="py-4 px-6 text-cyan-400 font-bold">${s.totalVolume.toLocaleString()} kg</td>
            </tr>
        `;
    });
}

// --- WORKOUT LOGGER ---
function initLogger() {
    const d = new Date();
    document.getElementById('wo-date').value = d.toISOString().split('T')[0];
    document.getElementById('wo-time').value = d.toTimeString().slice(0,5);
}

function startWorkout() {
    const type = document.getElementById('wo-type').value;
    const date = document.getElementById('wo-date').value;
    const time = document.getElementById('wo-time').value;
    const bw = document.getElementById('wo-bw').value;
    
    woState = {
        type, date, time, bw,
        startMs: Date.now(),
        exercises: PRESETS[type].map(e => ({ name: e, sets: [] })),
        currExIdx: 0,
        totalVolume: 0, totalSets: 0
    };
    
    document.getElementById('workout-setup').classList.add('hidden');
    document.getElementById('workout-active').classList.remove('hidden');
    document.getElementById('workout-active').classList.add('flex');
    renderWOExercises();
    renderWOSets();
}

function renderWOExercises() {
    const list = document.getElementById('wo-exercise-list');
    list.innerHTML = '';
    woState.exercises.forEach((ex, idx) => {
        const active = idx === woState.currExIdx;
        const cls = active ? "bg-orange-500/10 border-l-2 border-orange-500 text-white" : "glass-panel text-zinc-400 hover:bg-white/5 cursor-pointer";
        const vol = ex.sets.reduce((s,x)=>s+(x.w*x.r),0);
        list.innerHTML += `
            <div onclick="woState.currExIdx=${idx}; renderWOSets(); renderWOExercises();" class="${cls} p-4 rounded-r-xl transition-all">
                <div class="font-bold">${ex.name}</div>
                <div class="text-xs mt-1 text-cyan-400">${ex.sets.length} sets • ${vol} kg</div>
            </div>
        `;
    });
    
    // total volume
    let tVol = 0, tSets = 0;
    woState.exercises.forEach(ex => {
        ex.sets.forEach(s => { tVol += s.w * s.r; tSets++; });
    });
    woState.totalVolume = tVol; woState.totalSets = tSets;
    document.getElementById('wo-total-volume').textContent = tVol.toLocaleString() + ' kg';
}

function renderWOSets() {
    const ex = woState.exercises[woState.currExIdx];
    document.getElementById('wo-current-ex-name').textContent = ex.name;
    const area = document.getElementById('wo-sets-area');
    area.innerHTML = '';
    ex.sets.forEach((set, sIdx) => {
        area.innerHTML += `
            <div class="flex items-center gap-2 bg-black/30 p-3 rounded-lg border border-white/5">
                <div class="text-zinc-500 font-label-caps w-6">${sIdx+1}</div>
                <input type="number" placeholder="kg" value="${set.w || ''}" onchange="updateSet(${sIdx}, 'w', this.value)" class="w-20 bg-transparent border-b border-white/20 text-white text-center focus:border-orange-500 outline-none">
                <span class="text-zinc-500">×</span>
                <input type="number" placeholder="reps" value="${set.r || ''}" onchange="updateSet(${sIdx}, 'r', this.value)" class="w-16 bg-transparent border-b border-white/20 text-white text-center focus:border-cyan-500 outline-none">
                <div class="flex-1 text-right text-cyan-400 font-bold">${(set.w*set.r)||0}</div>
                <button onclick="delSet(${sIdx})" class="text-red-500 material-symbols-outlined ml-2">close</button>
            </div>
        `;
    });
}

function addSet() {
    const ex = woState.exercises[woState.currExIdx];
    let defW = '', defR = '';
    if(ex.sets.length > 0) { defW = ex.sets[ex.sets.length-1].w; defR = ex.sets[ex.sets.length-1].r; }
    ex.sets.push({w: defW, r: defR});
    renderWOSets(); renderWOExercises();
}

function updateSet(sIdx, field, val) {
    const ex = woState.exercises[woState.currExIdx];
    ex.sets[sIdx][field] = parseFloat(val) || 0;
    renderWOSets(); renderWOExercises();
    if(field === 'r' && val > 0) startTimer(90);
}

function delSet(sIdx) {
    woState.exercises[woState.currExIdx].sets.splice(sIdx, 1);
    renderWOSets(); renderWOExercises();
}

function finishWorkout() {
    if(!confirm('Finish session?')) return;
    woState.duration = Math.round((Date.now() - woState.startMs)/60000);
    sessions.push(woState);
    localStorage.setItem('kinetic_sessions', JSON.stringify(sessions));
    
    // Reset UI
    document.getElementById('workout-active').classList.add('hidden');
    document.getElementById('workout-active').classList.remove('flex');
    document.getElementById('workout-setup').classList.remove('hidden');
    alert(`Session Saved!\nVolume: ${woState.totalVolume} kg\nSets: ${woState.totalSets}\nTime: ${woState.duration} min`);
    woState = null;
    initLogger();
    switchNav('home');
}

// --- TIMER ---
let timeLeft = 0, totalTime = 0;
function startTimer(seconds) {
    totalTime = seconds; timeLeft = seconds;
    document.getElementById('timer-overlay').style.display = 'flex';
    updateTimerUI();
    if(timerInt) clearInterval(timerInt);
    timerInt = setInterval(() => {
        timeLeft--;
        updateTimerUI();
        if(timeLeft <= 0) { closeTimer(); playBeep(); }
    }, 1000);
}
function updateTimerUI() {
    document.getElementById('timer-text').textContent = timeLeft;
    const dash = (timeLeft/totalTime)*100;
    document.getElementById('timer-circle').setAttribute('stroke-dasharray', `${dash}, 100`);
}
function addTimerTime() { timeLeft += 15; totalTime += 15; updateTimerUI(); }
function closeTimer() { clearInterval(timerInt); document.getElementById('timer-overlay').style.display = 'none'; }

// --- PROGRESS ---
let charts = {};
function renderProgress() {
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'Inter', sans-serif";
    
    const dates = sessions.map(s => s.date.slice(5));
    const vols = sessions.map(s => s.totalVolume);
    const bws = sessions.map(s => s.bw).filter(b => b);
    
    // Vol Chart
    if(charts.vol) charts.vol.destroy();
    charts.vol = new Chart(document.getElementById('chart-volume'), {
        type: 'bar',
        data: { labels: dates, datasets: [{ label: 'Volume (kg)', data: vols, backgroundColor: '#00e3fd', borderRadius: 4 }] },
        options: { responsive: true, maintainAspectRatio: false }
    });
    
    // BW Chart
    if(charts.bw) charts.bw.destroy();
    charts.bw = new Chart(document.getElementById('chart-bw'), {
        type: 'line',
        data: { labels: dates.slice(dates.length - bws.length), datasets: [{ label: 'Bodyweight (kg)', data: bws, borderColor: '#ffb77d', tension: 0.4 }] },
        options: { responsive: true, maintainAspectRatio: false }
    });
    
    // Type Doughnut
    const types = {}; sessions.forEach(s => { types[s.type] = (types[s.type]||0) + s.totalVolume; });
    if(charts.type) charts.type.destroy();
    charts.type = new Chart(document.getElementById('chart-doughnut'), {
        type: 'doughnut',
        data: { labels: Object.keys(types), datasets: [{ data: Object.values(types), backgroundColor: ['#ff8c00', '#00e3fd', '#4ae183', '#ffb4ab'], borderWidth: 0 }] },
        options: { responsive: true, maintainAspectRatio: false, cutout: '70%' }
    });
    
    // Best Table
    const bests = {};
    sessions.forEach(s => {
        s.exercises.forEach(ex => {
            const v = ex.sets.reduce((sum,x)=>sum+(x.w*x.r),0);
            if(v>0 && (!bests[ex.name] || v > bests[ex.name].v)) bests[ex.name] = {v:v, d:s.date};
        });
    });
    const tb = document.getElementById('progress-best-table');
    tb.innerHTML = '';
    Object.entries(bests).sort((a,b)=>b[1].v - a[1].v).slice(0,10).forEach(([name, data]) => {
        tb.innerHTML += `<tr class="border-b border-white/5 hover:bg-white/5"><td class="py-3">${name}</td><td class="text-right text-cyan-400 font-bold">${data.v}</td><td class="text-right">${data.d}</td></tr>`;
    });
}

// --- SUPPS ---
function renderSupps() {
    const today = new Date().toISOString().split('T')[0];
    if(!supps[today]) supps[today] = { c:false, m:false, o:false, water:0 };
    const t = supps[today];
    
    document.getElementById('supp-creatine').checked = t.c;
    document.getElementById('supp-multi').checked = t.m;
    document.getElementById('supp-omega').checked = t.o;
    
    // Water grid
    document.getElementById('water-count-text').textContent = `${t.water} / 8`;
    const wg = document.getElementById('water-grid');
    wg.innerHTML = '';
    for(let i=1; i<=8; i++) {
        const fill = i <= t.water ? 'bg-cyan-500 shadow-[0_0_15px_rgba(0,227,253,0.5)]' : 'bg-zinc-900 border border-white/10';
        wg.innerHTML += `<div onclick="setWater(${i})" class="aspect-square rounded-full ${fill} cursor-pointer transition-all hover:scale-105"></div>`;
    }
    
    // Streak
    const sg = document.getElementById('streak-grid');
    sg.innerHTML = '';
    const d = new Date();
    let streakCount = 0;
    for(let i=6; i>=0; i--) {
        const dt = new Date(d); dt.setDate(d.getDate()-i);
        const dateStr = dt.toISOString().split('T')[0];
        const hasWork = sessions.some(s=>s.date===dateStr);
        const hasSupp = supps[dateStr] && supps[dateStr].c; // arbitrary proxy for streak
        const done = hasWork || hasSupp;
        if(done) streakCount++;
        const bg = done ? 'bg-orange-500 shadow-[0_0_10px_rgba(255,140,0,0.5)]' : 'bg-zinc-900 border border-white/10';
        sg.innerHTML += `<div class="w-full aspect-square rounded-md ${bg} flex items-center justify-center text-[10px] text-black font-bold">${done?'✓':''}</div>`;
    }
    
    const msgs = ["Embrace the grind.", "You're building the machine.", "Consistency is the only currency.", "No days off for the mind."];
    document.getElementById('motivational-msg').textContent = msgs[streakCount % msgs.length];
    
    // Water chart
    const wData = [];
    for(let i=6; i>=0; i--) {
        const dt = new Date(d); dt.setDate(d.getDate()-i);
        const ds = dt.toISOString().split('T')[0];
        wData.push((supps[ds]&&supps[ds].water)||0);
    }
    if(charts.water) charts.water.destroy();
    charts.water = new Chart(document.getElementById('chart-water'), {
        type: 'bar',
        data: { labels: ['-6','-5','-4','-3','-2','-1','Today'], datasets: [{ label: 'Water', data: wData, backgroundColor: '#00e3fd' }] },
        options: { responsive: true, maintainAspectRatio: false, scales:{y:{max:8}} }
    });
}
function saveSupps() {
    const today = new Date().toISOString().split('T')[0];
    if(!supps[today]) supps[today] = { water:0 };
    supps[today].c = document.getElementById('supp-creatine').checked;
    supps[today].m = document.getElementById('supp-multi').checked;
    supps[today].o = document.getElementById('supp-omega').checked;
    localStorage.setItem('kinetic_supps', JSON.stringify(supps));
    renderSupps();
}
function setWater(n) {
    const today = new Date().toISOString().split('T')[0];
    if(!supps[today]) supps[today] = { c:false,m:false,o:false,water:0 };
    supps[today].water = (supps[today].water === n) ? n-1 : n;
    localStorage.setItem('kinetic_supps', JSON.stringify(supps));
    renderSupps();
}

// --- EXPORT ---
function exportCSV() {
    let csv = "Date,Type,Duration,Bodyweight,Exercise,Set,Weight,Reps,Volume\n";
    sessions.forEach(s => {
        s.exercises.forEach(ex => {
            ex.sets.forEach((set, idx) => {
                csv += `${s.date},${s.type},${s.duration},${s.bw||''},"${ex.name}",${idx+1},${set.w},${set.r},${set.w*set.r}\n`;
            });
        });
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'kinetic_data.csv'; a.click();
}

function exportXLSX() {
    if(typeof XLSX === 'undefined') { alert("SheetJS not loaded yet. Try again in a second."); return; }
    const wb = XLSX.utils.book_new();
    
    // Summary
    const sumData = sessions.map(s => ({ Date: s.date, Type: s.type, BW: s.bw, Vol: s.totalVolume, Sets: s.totalSets, Mins: s.duration }));
    XLSX.utils.book_append_sheet(wb, XLSX.utils.json_to_sheet(sumData), "Summary");
    
    // All sets
    const allSets = [];
    sessions.forEach(s => s.exercises.forEach(ex => ex.sets.forEach((set, i) => allSets.push({
        Date: s.date, Type: s.type, Exercise: ex.name, Set: i+1, Weight: set.w, Reps: set.r, Vol: set.w*set.r
    }))));
    XLSX.utils.book_append_sheet(wb, XLSX.utils.json_to_sheet(allSets), "All_Sets");
    
    XLSX.writeFile(wb, 'Kinetic_Backup.xlsx');
}

function exportJSON() {
    const data = JSON.stringify({sessions, supps}, null, 2);
    const blob = new Blob([data], { type: 'application/json' });
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'kinetic_backup.json'; a.click();
}

function importJSON() {
    const file = document.getElementById('import-file').files[0];
    if(!file) return alert("Select a file first.");
    const reader = new FileReader();
    reader.onload = e => {
        try {
            const data = JSON.parse(e.target.result);
            if(data.sessions) {
                sessions = data.sessions; supps = data.supps || {};
                localStorage.setItem('kinetic_sessions', JSON.stringify(sessions));
                localStorage.setItem('kinetic_supps', JSON.stringify(supps));
                alert("Import successful!");
                location.reload();
            }
        } catch(err) { alert("Invalid JSON file."); }
    };
    reader.readAsText(file);
}

function clearAllData() {
    if(confirm("DANGER! This will wipe all data permanently. Are you sure?")) {
        localStorage.clear();
        alert("Data cleared.");
        location.reload();
    }
}

// --- BOOTSTRAP ---
initLogger();
switchNav('home');
</script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
