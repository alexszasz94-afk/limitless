# SETUP: for the AI assistant doing the setup

Follow this file from top to bottom, one step at a time. After every step, run its **Check**.
Go on only when the check passes. If a check fails, use **Troubleshooting** at the end. If
that doesn't solve it, stop and tell the person exactly what failed (the command and its
output). Never guess a value: every value is either written here or something you ask the
person for in Step 4.

What you will build: one Ubuntu server running two apps, both deployed from the person's own
**private** copy of this repo.

- **Distribution** (posting portal) at `https://portal.<IPDASH>.nip.io`
- **Social Tracker** at `https://tracker.<IPDASH>.nip.io`

Every push to the private copy's `main` branch updates the server by itself within about 2 minutes.

## Values used in this file

Write these down as you learn them. Every `<NAME>` in a command means "put the value here".

| Placeholder | What it is | Where it comes from |
|---|---|---|
| `<OWNER>` | the person's GitHub username | Step 2 |
| `<REPO>` | their private copy, always `social-stack` (or `social-stack-2`, `-3`... if that name is taken) | Step 3 |
| `<TZ>` | their timezone, e.g. `Europe/London` (IANA name) | Step 4 |
| `<ID>` | the brand id: lowercase letters, digits and `_`, e.g. `glow_lamp` | Step 4 |
| `<IP>` | the server's IPv4 address, e.g. `203.0.113.7` | Step 6 |
| `<IPDASH>` | the same IP with dashes, e.g. `203-0-113-7` | Step 6 |

Rules for the whole setup:

- **Never put a password, an API key, a video or a picture into the repo.** Passwords and keys
  go only into `.env` files on the server. Videos and pictures go only into the server's content folder.
- **The person's copy must stay private.** It will hold their accounts and captions.
- **On Windows, run every command in Git Bash** (it comes with Git for Windows), not in
  PowerShell or cmd. On macOS and Linux, use the normal terminal.
- Always connect to the server with `ssh root@<IP> '<command>'` (one command at a time) and
  copy files with `scp`.
- Long steps (Steps 7 and 8) take up to 15 minutes. If your command tool has a shorter time
  limit, use the background form given in those steps.

---

## Step 1: Tools on the computer

Check what's already installed:

```bash
git --version
gh --version
ssh -V
```

Install whatever is missing:

| System | git | gh (GitHub CLI) |
|---|---|---|
| Windows | `winget install --id Git.Git -e --source winget` | `winget install --id GitHub.cli -e --source winget` |
| macOS | `xcode-select --install` | `brew install gh` (no Homebrew? ask the person to install it from https://brew.sh) |
| Ubuntu/Debian | `sudo apt install -y git` | follow https://github.com/cli/cli/blob/trunk/docs/install_linux.md |

`ssh` and `scp` come with Windows 10/11, macOS and Linux. On Windows, after installing, close
the terminal and open a new **Git Bash** window.

**Check:** all three commands print a version.

## Step 2: GitHub login

1. If the person has no GitHub account, ask them to create one at https://github.com/signup.
2. Run `gh auth status`. If it says you are not logged in, have them run this (or run it
   yourself if your tool can handle the prompts). It opens the browser, where they approve:

   ```bash
   gh auth login --hostname github.com --git-protocol https --web
   ```

3. Let git use that login, then read the username:

   ```bash
   gh auth setup-git
   gh api user --jq .login
   ```

   The printed name is `<OWNER>`.

**Check:** `gh auth status` says "Logged in to github.com account `<OWNER>`".

## Step 3: The person's private copy

Run these in the person's home folder:

```bash
cd ~
git clone https://github.com/DanlexVentures/distribution-and-tracker.git social-stack
cd social-stack
git remote rename origin upstream
gh repo create social-stack --private --source . --remote origin --push
```

If `gh repo create` says the name already exists, use `social-stack-2` in that command (and
from now on `<REPO>` = `social-stack-2`).

If git has no name and email yet (`git config user.email` prints nothing), set them for this
repo only:

```bash
git config user.name "<OWNER>"
git config user.email "$(gh api user --jq .id)+<OWNER>@users.noreply.github.com"
```

**Check:** `gh repo view <OWNER>/<REPO> --json visibility --jq .visibility` prints `PRIVATE`.

From now on, every file path in this guide is relative to `~/social-stack`.

## Step 4: Ask the person for their details

Ask these questions in one simple message. Explain any that aren't clear to them.

1. **Which city or country are your posters in?** Turn the answer into an IANA timezone name
   (`Europe/London`, `America/New_York`, `Europe/Berlin`...). That is `<TZ>`. It decides
   when a new "day" starts in the portal and how days are counted in the tracker.
2. **The brand name**, e.g. "Glow Lamp". Make `<ID>` from it: lowercase, spaces become `_`,
   only `a-z 0-9 _` (e.g. `glow_lamp`).
3. **The account names (handles) on Instagram, TikTok and Facebook**, the ones the posters will
   create on day 1, without `@`. Ask whether these accounts already exist and are public.
4. **A one-line bio** for the profiles.
5. **3 to 10 competitor accounts** (platform + handle) the posters should follow and watch
   during the warm-up.
6. **3 to 6 search keywords** for the niche (e.g. "desk lamp", "home office setup").
7. **A pinned comment** for the videos (optional, can be empty).
8. **The posters' names** (one secret link per poster).
9. **The Apify API key.** If they have no account: sign up at https://apify.com. The key is at
   https://console.apify.com/settings/integrations ("Personal API token", starts with
   `apify_api_`). Also ask **how many US dollars a month the tracker may spend** at most:
   suggest their Apify plan's monthly credit, shown under Billing in the Apify console.
10. **The videos**, in the order they should be posted, **with one caption each** (or one
    caption per platform). Also **a profile picture** and **a cover image**. Ask for the folder
    on this computer where these files are.

Keep the Apify key out of every file in the repo and out of every commit. You'll use it only in Step 8.

**Check:** you have all ten answers. The handles and the videos are required. If the accounts
don't exist yet, that's fine: the tracker waits (Step 5d).

## Step 5: Fill in the settings files

Edit these files in `~/social-stack`. Keep the JSON valid: double quotes, no trailing commas.

**a) `distribution/config/personas.json`:** replace the whole `example_brand` object with
the person's brand:

```json
{
  "id": "<ID>",
  "name": "<brand name>",
  "handles": { "instagram": "<ig handle>", "tiktok": "<tiktok handle>", "facebook": "<facebook handle>" },
  "bio": "<one-line bio>",
  "competitors": [ { "platform": "instagram", "handle": "<competitor>" } ],
  "keywords": [ "<keyword 1>", "<keyword 2>" ],
  "voice_notes": "",
  "pinned_comment": "<pinned comment or empty>"
}
```

`competitors[].platform` is `instagram`, `tiktok` or `facebook`. Keep the `_note` line at the top.

**b) The content list.** Rename the example file to match the brand:

```bash
git mv distribution/content-manifests/example_brand.json distribution/content-manifests/<ID>.json
```

Then edit `distribution/content-manifests/<ID>.json`:

- `"persona": "<ID>"`
- `"profile_image": "images/profile.<jpg or png>"` and `"cover_image": "images/cover.<jpg or png>"`,
  using the real file types.
- `"items"`: one entry per video, in posting order, numbered `video_1`, `video_2`, ...:

  ```json
  { "id": "video_1", "kind": "reel", "master": "reels/video_1.mp4", "proxy": "reels/video_1_proxy.mp4", "caption": "<caption>" }
  ```

  - `master` keeps the real file type (`reels/video_3.mov` for a .mov file).
  - `proxy` is always `reels/video_N_proxy.mp4`.
  - Per-platform captions: `"caption": { "instagram": "...", "tiktok": "...", "facebook": "..." }`.
  - Remove `duration_seconds` (optional), or set it to the length in seconds.

  Write down which local file became `video_1`, `video_2`, ... You'll need that list in Step 9.

**c) `distribution/config/schedule.json`:** leave it as it is. By default: day 1 creates the
accounts and warms them up, day 2 warms up and sets up the profiles, days 3 and 4 warm up and
post 3 reels, and every day from day 5 posts 3 reels. A poster may start the next day right
after finishing one. Change it only if the person asks; the file's `_note` explains each setting.

**d) `social_tracker/config/products.json`:** replace the example product:

- `"id": "<ID>"` and `"name": "<brand name>"`
- One account per platform: `"handle"` (no `@`) and `"url"`:
  - `https://www.instagram.com/<handle>/`
  - `https://www.tiktok.com/@<handle>`
  - `https://www.facebook.com/<handle>`
- Product `"active": true` if the accounts already exist and are public. Otherwise set it to
  `false` and tell the person to ask you to switch it on once the accounts exist (edit,
  commit, push).
- Leave out `"avatar"`.

**e) `social_tracker/config/cadence.json`:** set `"timezone": "<TZ>"`.

**f) `social_tracker/config/budget.json`:** set `"monthlyBudgetUsd"` to the amount from
question 9 (a number, e.g. `29`). At that limit the tracker stops scraping until the next
month. It never spends more.

Validate every edited JSON file. Use whichever of these works on the computer:

```bash
node -e "JSON.parse(require('fs').readFileSync(process.argv[1],'utf8'))" <file>
python3 -m json.tool <file> > /dev/null
```

Then save and push:

```bash
git add -A
git status          # only the files above may be listed: no videos, pictures or .env
git commit -m "Brand settings"
git push origin main
```

**Check:** `git status` says "nothing to commit, working tree clean", and
`gh api repos/<OWNER>/<REPO>/contents/distribution/content-manifests/<ID>.json --jq .name`
prints `<ID>.json`.

## Step 6: The server (the person clicks, you guide)

1. On this computer, make an SSH key if there isn't one yet, and show the public half:

   ```bash
   [ -f ~/.ssh/id_ed25519.pub ] || ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
   cat ~/.ssh/id_ed25519.pub
   ```

2. Walk the person through this in their browser:
   - Create an account at https://www.hetzner.com/cloud and add a payment method.
   - In the Cloud Console (https://console.hetzner.cloud): open the default project (or make
     a new one) and click **Add Server**.
   - **Location:** the one closest to the posters.
   - **Image:** Ubuntu **24.04**.
   - **Type:** shared vCPU, x86, **CX23** (2 vCPU, 4 GB RAM). If it's missing, pick the
     cheapest x86 type with at least 2 vCPU and 4 GB RAM.
   - **Networking:** keep **Public IPv4** switched on. It's required: GitHub can't be reached
     over IPv6 only.
   - **SSH keys:** "Add SSH key", paste the line you showed them (it starts with
     `ssh-ed25519`), save it, and make sure it's ticked.
   - **Backups:** recommended (a small extra cost).
   - **Name:** anything, e.g. `social-stack`. Click **Create & Buy now**.
   - Copy the server's **IPv4 address** from the server list and give it to you.
3. `<IP>` = that address. `<IPDASH>` = the same with `-` instead of `.`.

**Check:** this prints `VERSION_ID="24.04"` (a fresh server can take a minute to accept logins):

```bash
ssh -o StrictHostKeyChecking=accept-new root@<IP> 'grep VERSION_ID /etc/os-release'
```

## Step 7: Install Distribution (the posting portal)

1. Copy the setup script to the server and run it:

   ```bash
   scp distribution/deploy/server-setup.sh root@<IP>:/root/distribution-setup.sh
   ssh root@<IP> 'bash /root/distribution-setup.sh git@github.com:<OWNER>/<REPO>.git portal.<IPDASH>.nip.io <TZ>'
   ```

   Background form (for command tools with a short time limit). Start it, then repeat the
   second command every 30 to 60 seconds until the log ends with `Done:` or shows an error:

   ```bash
   ssh root@<IP> 'nohup bash /root/distribution-setup.sh git@github.com:<OWNER>/<REPO>.git portal.<IPDASH>.nip.io <TZ> > /root/distribution-setup.log 2>&1 &'
   ssh root@<IP> 'tail -n 15 /root/distribution-setup.log'
   ```

2. **The first run is supposed to stop** after a few minutes with
   `ADD THIS READ-ONLY DEPLOY KEY TO GitHub` (exit code 2). Add that key to the private repo
   (read-only, which is gh's default):

   ```bash
   ssh root@<IP> 'cat /root/.ssh/repo_pull.pub' > ~/server_deploy_key.pub
   gh repo deploy-key add ~/server_deploy_key.pub --repo <OWNER>/<REPO> --title "server (read-only)"
   ```

3. **Run the same setup command again** (the normal or the background form). This run builds
   the app and takes 5 to 10 minutes. It ends with `Done: https://portal.<IPDASH>.nip.io`.
   Earlier in its output there's a line `Admin passphrase (also in /srv/distribution/app/.env): ...`.
   Write the passphrase down for the person. To read it again later:

   ```bash
   ssh root@<IP> 'grep ADMIN_PASSPHRASE /srv/distribution/app/.env'
   ```

**Check:**

```bash
ssh root@<IP> 'cd /srv/distribution/app && docker compose ps'
```

Both `app` and `caddy` must be listed as running ("Up"). Then open
`https://portal.<IPDASH>.nip.io/admin`. The first visit can take up to a minute while the
HTTPS certificate is issued. The admin login page must appear, and the passphrase must open it.

## Step 8: Install the Social Tracker

1. Run its setup (the background form works the same way, with `/root/tracker-setup.log`):

   ```bash
   scp social_tracker/deploy/server-setup.sh root@<IP>:/root/tracker-setup.sh
   ssh root@<IP> 'bash /root/tracker-setup.sh git@github.com:<OWNER>/<REPO>.git tracker.<IPDASH>.nip.io'
   ```

   It takes 5 to 10 minutes and ends with `Done: https://tracker.<IPDASH>.nip.io`. Write down
   the line `Dashboard passphrase (also in /srv/social_tracker/app/.env): ...`.

2. Put the Apify key on the server, and only there. Replace `<APIFY_KEY>` with the key from
   question 9:

   ```bash
   ssh root@<IP> "sed -i 's|^APIFY_TOKENS=.*|APIFY_TOKENS=<APIFY_KEY>|' /srv/social_tracker/app/.env && cd /srv/social_tracker/app && docker compose up -d"
   ```

   (To use several keys later: separate them with commas, no spaces.)

**Check:**

```bash
ssh root@<IP> 'cd /srv/social_tracker/app && docker compose ps'
```

`web` and `scraper` must both be running. After about 2 minutes, `scraper` must show
`(healthy)`. Then open `https://tracker.<IPDASH>.nip.io` and log in with the dashboard
passphrase. On the **Keys** page, click **Check now**: it must show 1 key with status `ok`.
If the product is active, the first numbers appear within the hour. **Run now** on the
**Runs** page starts a full pass straight away.

## Step 9: Put the videos into the portal

Use the list from Step 5b (which local file is `video_1`, `video_2`, ...).

1. Make the folders and upload the files under their manifest names. Never re-encode or edit
   the originals: posters download exactly the file you upload.

   ```bash
   ssh root@<IP> 'mkdir -p /srv/distribution/content/<ID>/reels /srv/distribution/content/<ID>/images'
   scp "<local path of the first video>" root@<IP>:/srv/distribution/content/<ID>/reels/video_1.mp4
   scp "<local path of the second video>" root@<IP>:/srv/distribution/content/<ID>/reels/video_2.mp4
   scp "<local profile picture>" root@<IP>:/srv/distribution/content/<ID>/images/profile.jpg
   scp "<local cover image>" root@<IP>:/srv/distribution/content/<ID>/images/cover.jpg
   ```

   Use the real file types, exactly as written in the manifest (`video_3.mov`, `profile.png`...).
   Repeat the `scp` line for every video.

2. Make the small preview copies (the proxies the in-page player uses) on the server, and give
   the files to the app's user:

   ```bash
   ssh root@<IP> 'cd /srv/distribution/content/<ID>/reels && for f in *.mp4 *.mov; do [ -e "$f" ] || continue; case "$f" in *_proxy.mp4) continue;; esac; p="${f%.*}_proxy.mp4"; [ -s "$p" ] || ffmpeg -v error -y -i "$f" -vf "scale=540:-2,format=yuv420p" -c:v libx264 -crf 28 -maxrate 1500k -bufsize 3000k -c:a aac -b:a 64k -movflags +faststart "$p"; done; chown -R 1000:1000 /srv/distribution/content/<ID>; ls -la'
   ```

3. Make sure the server already runs the commit that has `<ID>.json` (it deploys within
   about 2 minutes of the push in Step 5; this command deploys right away if it hasn't yet):

   ```bash
   ssh root@<IP> '/srv/distribution/app/deploy/pull-deploy.sh; cd /srv/distribution/app && docker compose exec -T app ls content-manifests'
   ```

   Repeat it after a minute until `<ID>.json` is in the list.

4. Load the brand and its videos:

   ```bash
   ssh root@<IP> 'cd /srv/distribution/app && docker compose exec -T app npm run manage -- import <ID>'
   ```

   It must print `✓ <brand name>: persona saved, N new item(s) queued`. If it prints
   `Nothing imported. Fix these first`, the file names on the server don't match the manifest.
   Fix the names (or the manifest, then commit, push and redo step 3) and run it again.
   Running it again is always safe.

5. Make one link per poster:

   ```bash
   ssh root@<IP> 'cd /srv/distribution/app && docker compose exec -T app npm run manage -- add-poster <ID> "<poster name>"'
   ```

   It prints `/d/<token>`. The poster's link is `https://portal.<IPDASH>.nip.io/d/<token>`.

**Check:** open one poster link. Day 1 must show the account creation and warm-up tasks for
the brand. On the admin page, the poster must be listed.

## Step 10: Hand everything over

Give the person this summary and tell them to keep it in a password manager:

- Posting portal admin: `https://portal.<IPDASH>.nip.io/admin`, passphrase `<from Step 7>`
- Poster links: one `https://portal.<IPDASH>.nip.io/d/<token>` per poster. Each poster opens
  their link on their phone and adds it to the home screen.
- Social Tracker: `https://tracker.<IPDASH>.nip.io`, passphrase `<from Step 8>`
- Server: Hetzner, IP `<IP>`, logged in with the SSH key of this computer
- Private code copy: `https://github.com/<OWNER>/<REPO>`

Then explain in three sentences how they'll use it: they send posters their links, they watch
progress on the admin page and numbers on the tracker, and for anything new they ask you
(recipes below).

Finally, delete `~/server_deploy_key.pub` (it's only a public key, but it's not needed any more).

---

## Day-to-day recipes (for the AI)

All commands run from `~/social-stack`. Server commands for the portal run in
`/srv/distribution/app`; for the tracker in `/srv/social_tracker/app`.

**Add more videos.** Upload the new files as the next numbers (`video_N`), run the proxy
command from Step 9.2, append the new items to `distribution/content-manifests/<ID>.json` (the
order in the file is the posting order), commit and push, then do Step 9.3 and 9.4. Import never
deletes anything and never changes a poster's progress.

**Add a poster:** Step 9.5. **List posters, their links and the queue:**
`docker compose exec -T app npm run manage -- list`.
**Restart a poster from day 1 (same link):** `docker compose exec -T app npm run manage -- reset-poster <token>`.

**Change captions or the order of unposted videos:** edit the manifest, push, then Steps 9.3 and 9.4.

**Track another account or brand:** edit `social_tracker/config/products.json`, commit, push.
The tracker picks it up within minutes, with no restart needed.

**A second brand in the portal:** add a second persona to `distribution/config/personas.json`,
create `distribution/content-manifests/<new id>.json`, push, then do Step 9 with the new id.

**Change the daily plan:** edit `distribution/config/schedule.json` and push. Days a poster has
already opened keep their tasks; the change applies to days nobody has opened yet.

**Change the Apify key or budget:** key: the `sed` command from Step 8.2. Budget:
`social_tracker/config/budget.json`, then push.

**Use a real domain instead of nip.io.** Point two DNS `A` records at `<IP>`, e.g.
`portal.example.com` and `tracker.example.com`. Then:

- Portal: `ssh root@<IP> "sed -i 's|^SITE_ADDRESS=.*|SITE_ADDRESS=portal.example.com|' /srv/distribution/app/.env && cd /srv/distribution/app && docker compose up -d caddy"`
- Tracker: `ssh root@<IP> "echo tracker.example.com > /etc/social_tracker/site_address && /srv/social_tracker/app/deploy/pull-deploy.sh --force"`

Poster links keep their token; only the address before `/d/` changes.

**Get updates from the original public repo:**
`git fetch upstream && git merge upstream/main`. If a settings file conflicts, keep the
person's version, then commit and push.

**Look at what's happening:**

- Deploys: `journalctl -u distribution-deploy -n 50` and `journalctl -u social-tracker-deploy -n 50`
- Apps: `docker compose logs --tail 100 app` (portal), `docker compose logs --tail 100 scraper` (tracker)

**Backups:** each app copies its database every night (14 copies kept in `/srv/*/db/backups`).
Hetzner backups (if switched on) copy the whole server daily.

**Never run `npm run seed` on the server.** It wipes the portal's database. (It refuses once
real data exists, but don't try.)

## Troubleshooting

| What you see | What to do |
|---|---|
| Setup stops with `ADD THIS READ-ONLY DEPLOY KEY` again after you added it | The repo address in the command is wrong, or the key went to another repo. Compare it with `gh repo view <OWNER>/<REPO> --json sshUrl --jq .sshUrl`, and check `gh repo deploy-key list --repo <OWNER>/<REPO>`. |
| `Permission denied (publickey)` when connecting to the server | The server was created without this computer's SSH key. Before Step 7 nothing is on it, so the simplest fix is to delete the server in Hetzner and create it again with the key ticked (Step 6). |
| The web address doesn't open | Wait a minute (certificate). Then check `docker compose logs --tail 50 caddy` in `/srv/distribution/app`. If it opens on mobile data but not on the person's Wi-Fi, their network blocks nip.io: use a real domain (recipe above). |
| The tracker address shows nothing but the portal works | Run `/srv/social_tracker/app/deploy/pull-deploy.sh --force` on the server. It rewrites the tracker's site file and reloads Caddy. |
| `scraper` isn't `healthy` | `docker compose logs --tail 100 scraper` in `/srv/social_tracker/app`. An empty `APIFY_TOKENS` means Step 8.2 was skipped. |
| Keys page says `invalid` | Wrong Apify key. Copy it again from the Apify console and redo Step 8.2. |
| Runs page shows `budget stop` | This month's limit in `budget.json` is reached, or the Apify credit is used up. |
| Poster page says "No video is ready yet" | The queue is empty: add videos (recipe above). |
| A build fails during deploy | `journalctl -u distribution-deploy -n 100` (or `social-tracker-deploy`). The previous version keeps running. A failed deploy is not retried by itself: fix the cause, push again, or run `/srv/distribution/app/deploy/pull-deploy.sh --force` (or `/srv/social_tracker/app/deploy/pull-deploy.sh --force`). |
