# Space Gym — Mahmoud Nagaty Client App

Space Gym is a private, mobile-first training companion for gym members and coaches. It turns a paper or WhatsApp program into one shared place for the member profile, workout plan, exercise history, progress, recovery reminders, and coach follow-up.

This client edition is separate from the original AXIS tracker. It keeps the existing workout engine and data model while presenting a Space Gym experience for one trainee.

## Client profile

- **Member:** Mahmoud Nagaty
- **Member ID:** 2106
- **Age:** 23
- **Level:** Intermediate
- **Primary target:** Muscle gain
- **Membership:** Active through November 2026
- **Private coaching:** Coach Hady through September 2026

The supplied member photo is stored in `assets/mahmoud-nagaty.jpg`. The member QR code is generated in the browser from the Space Gym member ID and can be saved with the **Save QR pass** button.

## Main experience

### Member Profile

The profile is the landing page. It presents the trainee’s identity, target, membership status, coach relationship, QR member pass, renewal actions, and a clear path into today’s plan.

### Today

Today is deliberately focused on training rather than marketing content. The client has one active program:

**Anterior / Posterior rotation**

1. Anterior A
2. Posterior A
3. Anterior B
4. Posterior B

The next template is selected from the most recently completed rotation session. After Anterior A, the next session becomes Posterior A; after Posterior A, it becomes Anterior B; and so on. The rotation continues when the app is reopened on another day.

### Train

The workout logger supports:

- Exercise-by-exercise set logging
- Weight, reps, RPE, volume, and rest timing
- Session notes
- Upcoming exercise preview
- Exercise swapping while training
- Mobile previous/next navigation
- Editing saved sessions
- Coach-readable exercise history

### Insights and recovery

Progress dashboards include total sessions, volume, PRs, trends, and history. Recovery includes hydration, supplements, and optional workout, creatine, and recovery reminders.

### Membership and renewal

The pricing page contains three client-facing options:

- Space Basic gym access
- Private coaching with Coach Hady
- Longer-term performance phase

Renewal and plan questions open WhatsApp with a pre-filled message referencing Mahmoud’s member ID. Replace the WhatsApp destination in `contactWhatsApp()` with Space Gym’s official number before production if a direct business chat is preferred.

## Importing the supplied Kinetic backup

The app supports the exported `Kinetic_Full_Backup.json` format. From the Member Profile page, choose **Import Kinetic history**, select the JSON backup, and the app will restore:

- Workout sessions and history
- Supplement state
- Custom templates
- Personal records

The restored sessions are stored in browser `localStorage` for the current app origin. Keep the same deployed URL if the member needs to keep seeing the same local data. For cross-device coach access, configure the existing Google Sheets webhook in the Data Vault.

## Running locally

Open `index.html` directly for a static preview, or serve the repository from a local web server:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/space_gym/
```

The app uses CDN-hosted Tailwind, Chart.js, SheetJS, Google Fonts, Material Symbols, and QRCode.js. An internet connection is required for those resources and for WhatsApp links.

## Deployment

When GitHub Pages is enabled for the repository root, the clone is available at:

```text
https://mahmoudnagatyy.github.io/gym-tracker-v1/space_gym/
```

Add that URL to the iPhone Home Screen. Do not use the local `file:///` URL for the phone shortcut.

## Data and privacy

The app stores workout data locally in the browser by default. The member photo and profile details are client-specific assets and should only be published in a private repository or a deployment intended for the client. Use a secure, authenticated backend before deploying multiple members or exposing coach dashboards publicly.

## Brand direction

The visual direction follows the supplied Space Gym mark: a dark gym environment, electric blue/cyan accents, high-contrast typography, bold training language, and clear conversion actions. The page structure also takes inspiration from the referenced coaching-plan model: personalized plans, regular progress follow-up, direct support, and clear plan tiers.
