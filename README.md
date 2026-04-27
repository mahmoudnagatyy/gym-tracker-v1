<div align="center">
  <img src="https://raw.githubusercontent.com/mahmoudnagatyy/gym-tracker-v1/main/assets/icon.png" alt="Kinetic Logo" width="120" />
</div>

<h1 align="center">KINETIC GYM TRACKER</h1>

<p align="center">
  <strong>A premium, offline-first mobile web application for tracking progressive overload, volume, and recovery.</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation-pwa">Installation (PWA)</a> •
  <a href="#serverless-sync-google-sheets">Cloud Sync</a> •
  <a href="#data--privacy">Privacy</a>
</p>

---

## ⚡ Overview

Kinetic is designed specifically for powerbuilders and athletes who need a fast, distraction-free logging experience during intense training sessions. Built as a single-page HTML application with Tailwind CSS, Kinetic runs entirely in the browser's `localStorage` meaning it loads instantly and works flawlessly without internet access in the gym.

Through an innovative "Serverless Architecture", Kinetic securely mirrors its local database to Google Sheets, providing indestructible cloud backups without requiring traditional databases or backend servers.

---

## 🚀 Features

- **Offline-First Engine**: Complete reliance on local storage guarantees zero latency when logging sets.
- **Auto-Rest Timers & Live Duration**: Track your time under tension and perfectly time your rest periods with integrated audio cues.
- **Data Analytics Engine**: Visualizes your weekly volume, body weight trends, and exercise-specific strength progression using Chart.js.
- **Live Google Sheets Sync**: PUSH and PULL your entire database to/from the cloud using a custom webhook.
- **Supplement & Hydration Logging**: Built-in tracking for Creatine, Multivitamins, Omega-3, and daily water intake.
- **Glassmorphism UI**: Beautiful, dark-themed interface built natively with Tailwind CSS and CSS variables.

---

## 📱 Installation (PWA)

Kinetic is a Progressive Web App. You do not need to download it from the App Store.

1. Open Safari on your iPhone and navigate to the live URL:
   `https://mahmoudnagatyy.github.io/gym-tracker-v1/`
2. Tap the **Share** icon at the bottom of the screen.
3. Scroll down and select **Add to Home Screen**.
4. The app will now launch in fullscreen native mode directly from your home screen!

---

## ☁️ Serverless Sync (Google Sheets)

Because the app is local-first, it uses Google Sheets as a bridge to back up data and sync between your phone and your Mac.

### 1. Setup the Webhook
1. Create a new Google Sheet.
2. Go to **Extensions > Apps Script**.
3. Paste the following sync code:

```javascript
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var input = JSON.parse(e.postData.contents);
  var appData = input.data;
  var timestamp = new Date();
  var backupString = JSON.stringify(appData);
  sheet.appendRow([timestamp, "Kinetic Backup Snapshot", backupString]);
  return ContentService.createTextOutput(JSON.stringify({"status": "success"}))
         .setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  if (lastRow < 1) {
    return ContentService.createTextOutput(JSON.stringify({"error": "No data"}))
           .setMimeType(ContentService.MimeType.JSON);
  }
  var jsonString = sheet.getRange(lastRow, 3).getValue();
  return ContentService.createTextOutput(jsonString)
         .setMimeType(ContentService.MimeType.JSON);
}
```

### 2. Deploy and Connect
1. Click **Deploy > New Deployment > Web app**.
2. Set "Execute as: Me" and "Who has access: Anyone".
3. Copy the generated Web App URL.
4. Open **Kinetic**, navigate to the **Data Center** tab, and paste the URL.

### 3. The Workflow
- **In the Gym:** Tap **PUSH** (or just hit "Finish Workout") to send your data to the cloud.
- **At Home:** Tap **PULL** on your Mac to download the newest backup from your phone!

---

## 🛡 Data & Privacy

You own your data. Kinetic Tracker does not communicate with any third-party servers. Your raw data is stored either physically on your device or in your personal, private Google Drive. You can factory reset or export your data to CSV/JSON at any time.

---
<p align="center"><i>Designed & Developed by Mahmoud Nagaty.</i></p>
