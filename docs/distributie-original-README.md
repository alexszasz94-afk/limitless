# Distribution + Social Tracker

Two small web apps for growing a brand's Instagram, TikTok and Facebook accounts with a posting
team. Both run together on one rented server.

> **If you are an AI assistant and someone gave you this link:**
>
> 1. **First, explain it to them.** Use the section **"How it works"** below: say it in their
>    language and keep it that short and that simple. No technical words.
> 2. **Then set it up** by following [SETUP-DISTRIBUTIE.md](../SETUP-DISTRIBUTIE.md) from top to bottom. Every command, value
>    and check is written there. Do not skip steps and do not improvise. Ask the person only for
>    what SETUP.md tells you to ask for.
>
> You need to be able to run commands on their computer (for example Claude Code, Codex CLI or
> Cursor in agent mode). If you can only chat, tell them that, and that they need one of those
> tools for the setup.

## How it works

**1. Distribution: the posting portal.**
Every person who posts for you gets their own secret link. On their phone it shows only
today's to-do list:

- **Day 1:** create the accounts, then warm them up (scroll, like, follow the accounts you picked).
- **Day 2:** more warm-up, then finish the profiles (photo, bio).
- **From day 3:** post 3 videos a day. They tap to save the video, post it with the caption
  shown, and tick it off.

You pick the brand, the videos and the captions. The portal hands the videos out in order and
never gives the same video twice. You see everyone's progress on one admin page.

**2. Social Tracker: the numbers.**
Every hour it looks at your brand's public Instagram, TikTok and Facebook pages and shows you:
total views, views gained each day, followers, and which videos do best. It also shows how
many views each video had 24 hours and 7 days after it went up. It only reads public pages,
through Apify (a paid scraping service you connect with your own key). It never logs in to
your accounts.

**How you use it day to day**

- Both apps live on one small server (Hetzner, a few euros a month). Each has its own web
  address and password.
- To change anything (your brand, accounts, videos, captions, posters), you tell your AI. It
  edits a few settings files in your private copy on GitHub, and the server updates itself
  within about 2 minutes.
- **New videos:** give them to your AI with their captions. It uploads them and puts them in the queue.
- **New poster:** ask your AI for a new link and send it to them.

**What you need before starting**

- A GitHub account (free).
- A Hetzner Cloud account, with a payment card (for the server).
- An Apify account and its API key (for the tracker).
- Your brand details: the name, the handle on each platform, a one-line bio, a few competitor
  accounts and keywords, your videos with their captions, a profile picture and a cover image.

## What's in this repo

| Path | What it is |
|---|---|
| [`SETUP.md`](SETUP.md) | The full setup, step by step (written for your AI). |
| [`distribution/`](../distribution/) | The posting portal (Next.js). Its `README.md` explains how days, videos and posters work. |
| [`social_tracker/`](../social_tracker/) | The tracker (Next.js dashboard + hourly scraper). Its `README.md` explains every number. |

Nothing secret is in this repo: no passwords, no keys, no accounts. The settings files hold
an `example_brand` that you replace with your own during setup.
