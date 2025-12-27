# 📦 GITHUB SETUP GUIDE - Step by Step

## 🎯 COMPLETE CHECKLIST

Follow these steps to publish Bitcoin Calc on GitHub!

---

## STEP 1: CREATE GITHUB ACCOUNT (if needed)

1. Go to: https://github.com
2. Click "Sign up"
3. Email: [your email]
4. Username: Choose wisely! (e.g., "michaelsteiner" or "nodewatch21")
5. Verify email
6. ✅ Done!

**Tip:** Use a professional username - it's your developer brand!

---

## STEP 2: CREATE NEW REPOSITORY

1. Go to: https://github.com/new

2. Fill in:
   - **Repository name:** `bitcoin-rechner`
   - **Description:** `Professional Bitcoin calculator with live price & glow effects`
   - **Public** ✅ (not Private!)
   - **Add README:** ❌ (we have our own!)
   - **Add .gitignore:** ❌ (we have our own!)
   - **Choose license:** ❌ (we have MIT!)

3. Click **"Create repository"**

4. ✅ Repo created!

---

## STEP 3: PREPARE YOUR FILES

**In `C:\BitcoinRechner\` create a new folder `github-upload\`**

Copy these files from `source\` to `github-upload\`:

```
github-upload\
├── bitcoin_rechner.py ✅
├── create_icon.py ✅
├── requirements.txt ✅
├── version_info.txt ✅
├── README.md ✅ (new, from download)
├── LICENSE ✅ (new, from download)
└── .gitignore ✅ (new, from download)
```

**DO NOT upload:**
- ❌ BUILD_EXE.bat (keep private)
- ❌ dist/ folder
- ❌ build/ folder
- ❌ .exe files (will be in Releases)
- ❌ bitcoin_icon.ico (generated)

---

## STEP 4: TAKE SCREENSHOT

1. **Open BitcoinRechner.exe**

2. **Make it look good:**
   - Fill in some values (e.g., 100 EUR)
   - Wait for results to show
   - Make sure price is loaded

3. **Take screenshot:**
   - Windows + Shift + S
   - Select app window
   - Screenshot saved to clipboard

4. **Save as:**
   - Paste in Paint/Snipping Tool
   - Save as: `screenshot.png`
   - Copy to `github-upload\` folder

5. ✅ Screenshot ready!

---

## STEP 5: UPLOAD TO GITHUB

### OPTION A: Web Upload (Easiest!)

1. Go to your repo: `https://github.com/YOUR_USERNAME/bitcoin-rechner`

2. Click **"uploading an existing file"** link

3. **Drag & drop** all files from `github-upload\` folder:
   - bitcoin_rechner.py
   - create_icon.py
   - requirements.txt
   - version_info.txt
   - README.md
   - LICENSE
   - .gitignore
   - screenshot.png

4. **Commit message:** `Initial commit - Bitcoin Calc v1.0.0`

5. Click **"Commit changes"**

6. ✅ Code uploaded!

---

### OPTION B: Git Command Line (Advanced)

```bash
# Navigate to github-upload folder
cd C:\BitcoinRechner\github-upload

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Bitcoin Calc v1.0.0"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/bitcoin-rechner.git

# Push
git push -u origin main
```

---

## STEP 6: CREATE RELEASE (with .exe download!)

1. Go to repo → Click **"Releases"** (right sidebar)

2. Click **"Create a new release"**

3. Fill in:
   - **Tag version:** `v1.0.0`
   - **Release title:** `Bitcoin Calc v1.0.0 - Initial Release`
   - **Description:**
     ```
     # 🎉 First Release!
     
     ## Features
     - Live Bitcoin EUR price tracking
     - Instant EUR/BTC/SATS conversions
     - Beautiful Bitcoin-orange glow design
     - Portable Windows executable
     
     ## Download
     Download `BitcoinRechner.exe` below and double-click to run!
     
     No installation needed. ~45 MB file size.
     
     ## What's New
     - Initial release
     - Core conversion features
     - Live price updates every 30 seconds
     
     ---
     
     **Made with ₿ by Michael | NodeWatch21**
     ```

4. **Attach files:**
   - Click "Attach binaries"
   - Upload `BitcoinRechner.exe` from `C:\BitcoinRechner\app\`
   - Wait for upload (~45 MB)

5. **Set as latest release:** ✅

6. Click **"Publish release"**

7. ✅ Release live! People can download!

---

## STEP 7: UPDATE README LINKS

1. Go to `README.md` in your repo

2. Click **"Edit"** (pencil icon)

3. **Replace placeholders:**
   - `YOUR_USERNAME` → your GitHub username
   - `[YOUR_LIGHTNING_ADDRESS]` → your Lightning address (or remove line)

4. **Update download link:**
   ```markdown
   [BitcoinRechner.exe](https://github.com/YOUR_USERNAME/bitcoin-rechner/releases/download/v1.0.0/BitcoinRechner.exe)
   ```

5. Click **"Commit changes"**

6. ✅ Links working!

---

## STEP 8: POLISH REPO

### Add Topics (Tags):

1. Repo → Click ⚙️ next to "About"
2. Add topics:
   - `bitcoin`
   - `calculator`
   - `python`
   - `cryptocurrency`
   - `customtkinter`
   - `gui`
   - `windows`

3. ✅ Searchable!

### Add Website:

1. Same "About" section
2. Website: `https://nodewatch21.io`
3. ✅ Linked!

---

## STEP 9: SHARE ON TWITTER! 🐦

1. **Prepare tweet** (see TWITTER_POSTS.md)

2. **Attach screenshot**

3. **Copy GitHub link:**
   `https://github.com/YOUR_USERNAME/bitcoin-rechner`

4. **POST!** 🚀

**Example:**
```
Built my first Bitcoin tool! 🧡

₿ Bitcoin Calc
• Live EUR price tracking
• Instant EUR/BTC/SATS conversions  
• Beautiful glow design
• 100% free & open source

Building in Public for @NodeWatch21 

⬇️ https://github.com/YOUR_USERNAME/bitcoin-rechner

#Bitcoin #BuildInPublic #FOSS
```

5. **Pin tweet** to profile!

6. ✅ Launched!

---

## STEP 10: ENGAGE!

Watch for:
- ⭐ Stars (people like it!)
- 🍴 Forks (people want to modify!)
- 💬 Issues (bug reports)
- 📬 Pull Requests (contributions!)

**Reply to:**
- Every comment ✅
- Every star (say thanks!) ✅
- Every issue (help users!) ✅

---

## 🎉 CONGRATULATIONS!

**You've launched your first open source project!**

```
✅ GitHub repo live
✅ Code public
✅ .exe downloadable
✅ Twitter announced
✅ Building in Public

= DEVELOPER STATUS! 💎
```

---

## 📊 TRACK SUCCESS

Watch these metrics:

**GitHub:**
- Stars ⭐
- Forks 🍴
- Downloads (Release analytics)
- Traffic (Insights → Traffic)

**Twitter:**
- Likes ❤️
- Retweets 🔄
- Replies 💬
- Profile visits 👀

---

## 🔄 FUTURE UPDATES

When you update the app:

1. Make changes to code
2. Test thoroughly
3. Update version number
4. Build new .exe
5. Create new Release (v1.1.0, etc.)
6. Tweet about new features!

---

## 💡 TIPS

**DO:**
- ✅ Reply to all comments
- ✅ Fix reported bugs quickly
- ✅ Thank people for stars
- ✅ Share progress updates
- ✅ Ask for feedback

**DON'T:**
- ❌ Spam people
- ❌ Ignore issues
- ❌ Over-promise features
- ❌ Forget to engage

---

**YOU'RE READY! LET'S LAUNCH! 🚀**

Questions? Issues? Just ask! 💪
