# Personal Blog - සම්පූර්ණ විස්තර

## ✓ ඔබේ Blog Website එක සාර්ථකව සකස් වුණා!

Python Flask භාවිතා කරලා `d:/My-Blogs/Blogs/` folder එකේ personal blog website එකක් හදලා තියෙනවා.

---

## 🚀 Blog එක Run කරන්නේ කොහොමද?

### 1. Folder එකට යන්න
```bash
cd d:/My-Blogs/Blogs
```

### 2. Virtual environment එක activate කරන්න
```bash
source venv/Scripts/activate
```

### 3. Server එක start කරන්න
```bash
python run.py
```

### 4. ඔබේ browser එකෙන් විවෘත කරන්න
- **මුල් පිටුව**: http://localhost:5000/
- **Post එකක් හදන්න**: http://localhost:5000/create
- **Admin Panel**: http://localhost:5000/admin

---

## 📝 Blog Post එකක් හදන්නේ කොහොමද?

### විධානය 1: Create Post පිටුවට යන්න
Browser එකෙන් http://localhost:5000/create වෙත යන්න හෝ navigation bar එකේ "Create Post" click කරන්න.

### විධානය 2: Form එක fill කරන්න
- **Title**: ඔබේ blog post එකේ heading එක
- **Content**: Post එකේ content එක (Markdown support තියෙනවා)
- **Author**: ඔබේ නම (අත් හැරියොත් "Anonymous" වෙනවා)
- **Published**: Tick කරොත් එකවරම publish වෙනවා

### විධානය 3: Submit කරන්න
"Submit" button එක click කරන්න. ඔබේ post එක එකවරම blog එකේ පෙන්වයි!

---

## 🎨 Markdown භාවිතා කරන්නේ කොහොමද?

Blog posts ලියන විට Markdown syntax භාවිතා කරලා rich formatting කරගන්න පුළුවන්:

```markdown
# විශාල Heading
## මධ්‍යම Heading
### කුඩා Heading

**Bold text** - තද අකුරු
*Italic text* - ඇල අකුරු

- Bullet point 1
- Bullet point 2

1. අංකිත list
2. දෙවැනි item

[Link text](https://example.com)

`code inline` - තනි code

```code block``` - code block එකක්
```

---

## 🎯 Features

✓ **Blog Posts** - Posts create, edit, delete කරන්න පුළුවන්
✓ **Markdown Support** - Rich text formatting
✓ **Admin Panel** - සියලු posts manage කරන්න පහසුයි
✓ **Responsive Design** - Mobile හා desktop යන දෙකෙන්ම හොඳින් වැඩකරනවා
✓ **Beautiful Design** - Bootstrap 5 නිසා ලස්සන look එකක්
✓ **SEO Friendly** - URL slugs auto-generate වෙනවා
✓ **Secure** - CSRF protection තියෙනවා

---

## 🛠 දැනට තියෙන Posts

ඔබේ blog එකේ දැනටමත් sample posts 2ක් තියෙනවා:

1. **Welcome to My Personal Blog!** - Blog එකේ introduction එක
2. **Python Flask: A Powerful Web Framework** - Flask ගැන technical post එකක්

මේවා test කරන්න හා වගේම blog එක කොහොමද වැඩකරන්නේ කියලා තේරුම්ගන්න පුළුවන්.

---

## 📁 Project Structure

```
Blogs/
├── app/                      # Main application folder
│   ├── templates/           # HTML files
│   ├── static/css/         # CSS files
│   ├── models.py           # Database models
│   ├── routes.py           # URL routes
│   └── forms.py            # Forms
├── instance/
│   └── blog.db             # Database file
├── venv/                    # Virtual environment
├── run.py                   # මෙතනින් server start වෙනවා
├── config.py                # Settings
└── README.md                # Documentation
```

---

## 🎨 Customize කරන්නේ කොහොමද?

### Blog title එක වෙනස් කරන්න
`app/templates/base.html` file එක open කරලා "My Blog" කියන එක වෙනස් කරන්න.

### Colors හා styles වෙනස් කරන්න
`app/static/css/style.css` file එක edit කරන්න.

### Logo එකක් add කරන්න
`app/static/` folder එකේ image එකක් දාලා `base.html` එකේ navbar එකට add කරන්න.

---

## 💡 Admin Panel භාවිතා කරන්නේ කොහොමද?

### Admin Panel එකට යන්න
Browser එකෙන් http://localhost:5000/admin වෙත යන්න.

### Posts manage කරන්න
1. "Posts" මත click කරන්න
2. සියලු posts table එකක පෙන්වයි
3. මෙතනින් posts:
   - Create කරන්න පුළුවන්
   - Edit කරන්න පුළුවන්
   - Delete කරන්න පුළුවන්
   - Search කරන්න පුළුවන්

---

## 🔄 Database Commands

### Database එක reset කරන්න
```bash
cd d:/My-Blogs/Blogs
source venv/Scripts/activate
rm instance/blog.db
flask db upgrade
```

### සියලු posts බලන්න
Admin panel එකෙන් හෝ homepage එකෙන් බලන්න පුළුවන්.

---

## ⚠️ Problems වුණොත්?

### Server start වෙන්නේ නැත්නම්
1. Virtual environment activate කරලා තියෙනවද බලන්න:
   ```bash
   source venv/Scripts/activate
   ```
2. Port 5000 use වෙලා නැද්ද බලන්න
3. Terminal එකේ error messages බලන්න

### "Module not found" error එකක් වුණොත්
```bash
source venv/Scripts/activate
pip install -r requirements.txt
```

### Database errors වුණොත්
```bash
rm instance/blog.db
flask db upgrade
```

---

## 📚 වැඩිදුර ඉගෙනගන්න

සම්පූර්ණ documentation එක `README.md` file එකේ තියෙනවා (English):
```bash
cd d:/My-Blogs/Blogs
cat README.md
```

---

## 🎉 සාර්ථකව සම්පූර්ණයි!

✓ සියලු files හදලා තියෙනවා
✓ Database setup කරලා තියෙනවා
✓ Sample posts 2ක් add කරලා තියෙනවා
✓ Server test කරලා තියෙනවා - හොඳින් වැඩකරනවා!

---

## 🚀 දැන් මොනවද කරන්න ඕනේ?

1. **Server start කරන්න**: `python run.py`
2. **Browser එකෙන් විවෘත කරන්න**: http://localhost:5000
3. **ඔබේ පළමු post එක හදන්න**: Create Post මත click කරන්න
4. **Customize කරන්න**: CSS, colors, blog title වෙනස් කරන්න

---

**ඔබේ Personal Blog Website එක භාවිතා කරන්න සූදානම්! 🎉**

Created: 2026-03-18
Technology: Python Flask
Database: SQLite
Design: Bootstrap 5
