# One-time GitHub profile setup

After you push the README updates, do these on GitHub (takes ~5 minutes).

## 1. Log in with GitHub CLI (optional but handy)

```powershell
gh auth login
```

Pick GitHub.com → HTTPS → login in browser.

## 2. Fix profile fields

Go to [github.com/settings/profile](https://github.com/settings/profile)

| Field | Value |
|-------|--------|
| **Name** | Venkata Anirudh Devireddy (fix typo if it still says Aniurdh) |
| **Bio** | Full-stack + AI · Bellevue · endokelp.com |
| **Website** | https://endokelp.com |

## 3. Pin these 6 public repos

[github.com/Endokelp?tab=repositories](https://github.com/Endokelp) → Customize pins:

1. **Endoweb** — portfolio
2. **Endokelp_Projects** — experiments + quant + robotics
3. **Forcelogic** — client commercial site
4. **Caraige** — LaCrosse Wagon client
5. **flashforward** or **AquaticsEDU** — nonprofit work
6. **Actual-IndianHypermarket** or **Endokelp** (this profile repo)

Skip **HostingWeather** and empty stubs.

## 4. Push script

From PowerShell, after `gh auth login` or if git credentials work:

```powershell
# Profile README (shows on github.com/Endokelp)
cd C:\Users\venni\Endokelp-profile
git add README.md GITHUB_SETUP.md
git commit -m "Refresh profile README for internships and freelance"
git push origin main

# Portfolio repo
cd C:\Users\venni\EndokelpWeb\EndoWeb
git add README.md
git commit -m "Add proper README for endokelp.com portfolio"
git push origin main

# ForceLogic
cd C:\Users\venni\subbuWeb\SubbuWebProj
git add README.md
git commit -m "Add client case study README"
git push origin main

# Caraige
cd C:\Users\venni\orchids-projects\orchids-lacrosse-website
git add README.md
git commit -m "Replace boilerplate with client case study README"
git push origin main

# Indian hypermarket
cd "C:\Users\venni\indian hypermarket"
git add README.md
git commit -m "Add project README"
git push origin main
```

## 5. Bio via CLI (after gh auth)

```powershell
gh api user -X PATCH -f name="Venkata Anirudh Devireddy" -f bio="Full-stack + AI · Bellevue · endokelp.com" -f blog="https://endokelp.com"
```
