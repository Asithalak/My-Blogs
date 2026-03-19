# Personal Blog Interface - Step-by-Step Guide
# සිංහල භාෂාවෙන් සම්පූර්ණ මාර්ගෝපදේශය

## 📋 අන්තර්ගතය (Table of Contents)

1. [Server එක Start කරන්නේ කොහොමද?](#step-1-server-start)
2. [Homepage බලන්නේ කොහොමද?](#step-2-homepage)
3. [Post එකක් බලන්නේ කොහොමද?](#step-3-view-post)
4. [නව Post එකක් හදන්නේ කොහොමද?](#step-4-create-post)
5. [Post එකක් Edit කරන්නේ කොහොමද?](#step-5-edit-post)
6. [Post එකක් Delete කරන්නේ කොහොමද?](#step-6-delete-post)
7. [Admin Panel භාවිතා කරන්නේ කොහොමද?](#step-7-admin-panel)
8. [Server එක Stop කරන්නේ කොහොමද?](#step-8-stop-server)

---

## STEP 1: Server එක Start කරන්නේ කොහොමද? 🚀 {#step-1-server-start}

### Step 1.1: Terminal/Command Prompt Open කරන්න

**Windows:**
- `Windows Key + R` press කරන්න
- `cmd` type කරලා Enter press කරන්න
- හෝ Git Bash open කරන්න

**ඔබට පෙන්වෙන්නේ:**
```
C:\Users\YourName>
```

---

### Step 1.2: Blog Folder එකට යන්න

**Type කරන්න:**
```bash
cd d:/My-Blogs/Blogs
```

**Press:** `Enter`

**ඔබට පෙන්වෙන්නේ:**
```
d:\My-Blogs\Blogs>
```

---

### Step 1.3: Virtual Environment Activate කරන්න

**Type කරන්න:**
```bash
source venv/Scripts/activate
```

**Press:** `Enter`

**ඔබට පෙන්වෙන්නේ:**
```
(venv) d:\My-Blogs\Blogs>
```

**✅ Note:** `(venv)` කියන එක ඉස්සරහ පෙන්වෙනවා නම් virtual environment එක activate වුණා කියන එක!

---

### Step 1.4: Server Start කරන්න

**Type කරන්න:**
```bash
python run.py
```

**Press:** `Enter`

**ඔබට පෙන්වෙන්නේ:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.75.243.49:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 768-480-406
```

**✅ සාර්ථකයි!** Server එක දැන් run වෙනවා!

**⚠️ Important:** Terminal window එක close කරන්න එපා! Server එක run වෙන්න ඕනේ.

---

## STEP 2: Homepage බලන්නේ කොහොමද? 🏠 {#step-2-homepage}

### Step 2.1: Browser Open කරන්න

ඕනෑම browser එකක්:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- හෝ වෙනත් browser එකක්

---

### Step 2.2: URL එක Type කරන්න

**Browser එකේ address bar එකේ type කරන්න:**
```
http://localhost:5000
```

**හෝ:**
```
http://127.0.0.1:5000
```

**Press:** `Enter`

---

### Step 2.3: Homepage Load වෙනවා

**ඔබට පෙන්වෙන දේ:**

```
┌────────────────────────────────────────────────────────┐
│  My Blog              [Home] [Create Post] [Admin]     │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Welcome to My Blog                                     │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │                                                   │ │
│  │  Welcome to My Personal Blog!                    │ │
│  │                                                   │ │
│  │  By Blog Admin on March 17, 2026                 │ │
│  │                                                   │ │
│  │  Thank you for visiting my personal blog.        │ │
│  │  This is my first blog post!                     │ │
│  │                                                   │ │
│  │  Features                                         │ │
│  │                                                   │ │
│  │  This blog has several great features:           │ │
│  │  - Markdown Support - Write posts using...       │ │
│  │                                                   │ │
│  │  [Read More]                                     │ │
│  │                                                   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │                                                   │ │
│  │  Python Flask: A Powerful Web Framework          │ │
│  │                                                   │ │
│  │  By Tech Enthusiast on March 17, 2026            │ │
│  │                                                   │ │
│  │  Flask is a lightweight and powerful web         │ │
│  │  framework for Python...                         │ │
│  │                                                   │ │
│  │  [Read More]                                     │ │
│  │                                                   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│              [Previous]  [1]  [Next]                   │
│                                                         │
└────────────────────────────────────────────────────────┘
```

**ඔබට පෙන්වෙන්නේ:**
- ✅ Navigation bar top එකේ (My Blog, Home, Create Post, Admin)
- ✅ "Welcome to My Blog" heading එක
- ✅ Sample blog posts 2ක්
- ✅ සෑම post එකක් සඳහා "Read More" button එකක්
- ✅ Pagination buttons (Previous, 1, Next)

---

## STEP 3: Post එකක් බලන්නේ කොහොමද? 📄 {#step-3-view-post}

### Step 3.1: Post එකක් Click කරන්න

Homepage එකේ ඕනෑම post එකක **"Read More"** button එක click කරන්න.

**හෝ Post Title එක Click කරන්න:**
- "Welcome to My Personal Blog!" click කරන්න

---

### Step 3.2: Post Page Load වෙනවා

**URL එක වෙනස් වෙනවා:**
```
http://localhost:5000/post/welcome-to-my-personal-blog
```

---

### Step 3.3: Full Post එක පෙන්වනවා

**ඔබට පෙන්වෙන දේ:**

```
┌────────────────────────────────────────────────────────┐
│  My Blog              [Home] [Create Post] [Admin]     │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Welcome to My Personal Blog!                           │
│                                                         │
│  By Blog Admin on March 17, 2026                        │
│  ───────────────────────────────────────────────────   │
│                                                         │
│  Welcome!                                               │
│  ═════════                                              │
│                                                         │
│  Thank you for visiting my personal blog. This is my   │
│  first blog post!                                       │
│                                                         │
│  Features                                               │
│  ─────────                                              │
│                                                         │
│  This blog has several great features:                  │
│                                                         │
│  • Markdown Support - Write posts using Markdown       │
│  • Rich Formatting - Use headers, lists, bold, italic  │
│  • Easy Management - Create, edit, and delete posts    │
│  • Responsive Design - Works great on mobile           │
│  • Admin Panel - Manage all posts from admin interface │
│                                                         │
│  Getting Started                                        │
│  ────────────────                                       │
│                                                         │
│  To create a new post, simply:                          │
│                                                         │
│  1. Click on "Create Post" in the navigation menu       │
│  2. Fill in the title and content (using Markdown)      │
│  3. Add your author name (optional)                     │
│  4. Choose whether to publish immediately               │
│  5. Submit!                                             │
│                                                         │
│  Code Example                                           │
│  ─────────────                                          │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │  def hello_world():                               │ │
│  │      print("Hello from my blog!")                 │ │
│  │      return "Welcome"                             │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│  Conclusion                                             │
│  ──────────                                             │
│                                                         │
│  I hope you enjoy reading my blog posts. Stay tuned    │
│  for more updates!                                      │
│                                                         │
│  Happy reading!                                         │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │  [Edit Post]  [Delete Post]                      │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
└────────────────────────────────────────────────────────┘
```

**ඔබට පෙන්වෙන්නේ:**
- ✅ Full post title විශාල අකුරෙන්
- ✅ Author name සහ date
- ✅ Markdown formatted content (headings, lists, bold, code blocks)
- ✅ Edit Post button
- ✅ Delete Post button

---

## STEP 4: නව Post එකක් හදන්නේ කොහොමද? ✍️ {#step-4-create-post}

### Step 4.1: Create Post Page එකට යන්න

**2 ක්‍රම තියෙනවා:**

**ක්‍රමය 1:** Navigation bar එකේ **"Create Post"** click කරන්න

**ක්‍රමය 2:** Browser address bar එකේ type කරන්න:
```
http://localhost:5000/create
```

---

### Step 4.2: Create Post Form පෙන්වනවා

**ඔබට පෙන්වෙන දේ:**

```
┌────────────────────────────────────────────────────────┐
│  My Blog              [Home] [Create Post] [Admin]     │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Create New Post                                        │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │                                                   │ │
│  │  Title *                                          │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ [Enter post title here...]                  │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  Content * (Supports Markdown formatting)        │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ [Write your post content here...]           │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  │                                              │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  Author                                           │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ [Your name (optional)]                      │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  ☑ Published                                     │ │
│  │                                                   │ │
│  │  [Submit]                                        │ │
│  │                                                   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
└────────────────────────────────────────────────────────┘
```

---

### Step 4.3: Form එක Fill කරන්න

**Title Field එකේ type කරන්න:**
```
My First Blog Post About Python
```

**Content Field එකේ type කරන්න (Markdown භාවිතා කරන්න):**
```markdown
# Python ඉගෙනීම

මම Python programming ඉගෙනගන්න පටන්ගත්තේ මාස 3කට පෙර.

## මම ඉගෙනගත් දේවල්

- **Variables** - Data store කරන්න
- **Functions** - Code reuse කරන්න
- **Loops** - Repeat tasks
- **Flask** - Web apps හදන්න

## Code උදාහරණයක්

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

## මගේ අත්දැකීම

Python ඉගෙනගන්න **ඉතාම පහසුයි** සහ **ප්‍රබලයි**!

*Happy Coding!* 🚀
```

**Author Field එකේ type කරන්න:**
```
Your Name
```

**Published Checkbox:**
- ☑ Tick කරලා තියෙනවද බලන්න (දැනටමත් tick කරලා තියෙන්න පුළුවන්)
- Tick කරලා නැත්නම් click කරලා tick කරන්න

---

### Step 4.4: Submit කරන්න

**"Submit" button එක click කරන්න**

---

### Step 4.5: Post එක Created වෙනවා

**Success!** ඔබ redirect වෙනවා නව post එකේ page එකට.

**URL වෙනස් වෙනවා:**
```
http://localhost:5000/post/my-first-blog-post-about-python
```

**ඔබට ඔබේ නව post එක පෙන්වනවා:**
- ✅ Title: "My First Blog Post About Python"
- ✅ Author: "Your Name"
- ✅ Markdown formatted content
- ✅ Code block පෙන්වනවා

---

## STEP 5: Post එකක් Edit කරන්නේ කොහොමද? ✏️ {#step-5-edit-post}

### Step 5.1: Post එක Open කරන්න

කලින් කළ විදිහට post එකක් open කරන්න (Step 3 බලන්න).

---

### Step 5.2: Edit Button Click කරන්න

Post page එකේ bottom එකේ **"Edit Post"** button එක click කරන්න.

---

### Step 5.3: Edit Form Load වෙනවා

**URL වෙනස් වෙනවා:**
```
http://localhost:5000/edit/1
```

**ඔබට පෙන්වෙන දේ:**

```
┌────────────────────────────────────────────────────────┐
│  My Blog              [Home] [Create Post] [Admin]     │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Edit Post                                              │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │                                                   │ │
│  │  Title *                                          │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ Welcome to My Personal Blog!                │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  Content * (Supports Markdown formatting)        │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ # Welcome!                                   │ │ │
│  │  │                                              │ │ │
│  │  │ Thank you for visiting my personal blog...  │ │ │
│  │  │                                              │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  Author                                           │ │
│  │  ┌─────────────────────────────────────────────┐ │ │
│  │  │ Blog Admin                                   │ │ │
│  │  └─────────────────────────────────────────────┘ │ │
│  │                                                   │ │
│  │  ☑ Published                                     │ │
│  │                                                   │ │
│  │  [Update Post]  [Cancel]                         │ │
│  │                                                   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
└────────────────────────────────────────────────────────┘
```

**✅ Note:** සියලු fields දැනටමත් post එකේ data එක fill කරලා තියෙනවා!

---

### Step 5.4: Changes කරන්න

**ඕනෑම field එකක් වෙනස් කරන්න:**

උදාහරණයක්:
- Title එකට යමක් add කරන්න
- Content එකේ යමක් වෙනස් කරන්න
- Author name update කරන්න

---

### Step 5.5: Update කරන්න

**"Update Post" button එක click කරන්න**

---

### Step 5.6: Post එක Update වෙනවා

**Success!** ඔබ redirect වෙනවා updated post එකේ page එකට.

**ඔබේ changes පෙන්වනවා:**
- ✅ Updated title
- ✅ Updated content
- ✅ Updated author name

---

## STEP 6: Post එකක් Delete කරන්නේ කොහොමද? 🗑️ {#step-6-delete-post}

### ⚠️ Warning

Post එකක් delete කරපු ගමන් එය database එකෙන් permanently remove වෙනවා!

---

### Step 6.1: Post එක Open කරන්න

Delete කරන්න ඕනේ post එක open කරන්න.

---

### Step 6.2: Delete Button Click කරන්න

Post page එකේ bottom එකේ **"Delete Post"** button එක click කරන්න.

---

### Step 6.3: Post එක Delete වෙනවා

**Post එක database එකෙන් remove වෙනවා.**

**ඔබ redirect වෙනවා homepage එකට.**

**Success message එකක් පෙන්වනවා:**
```
✓ Post deleted successfully!
```

**Post එක homepage list එකෙන් අතුරුදහන් වෙනවා.**

---

## STEP 7: Admin Panel භාවිතා කරන්නේ කොහොමද? ⚙️ {#step-7-admin-panel}

### Step 7.1: Admin Panel එකට යන්න

**2 ක්‍රම:**

**ක්‍රමය 1:** Navigation bar එකේ **"Admin"** click කරන්න

**ක්‍රමය 2:** Browser එකේ type කරන්න:
```
http://localhost:5000/admin
```

---

### Step 7.2: Admin Dashboard Load වෙනවා

**ඔබට පෙන්වෙන දේ:**

```
┌────────────────────────────────────────────────────────┐
│  Blog Admin                                             │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Home                                                   │
│                                                         │
│  Menu:                                                  │
│  ┌──────────────┐                                      │
│  │ 📝 Posts     │                                      │
│  └──────────────┘                                      │
│                                                         │
└────────────────────────────────────────────────────────┘
```

---

### Step 7.3: Posts Menu Click කරන්න

**"Posts" මත click කරන්න**

---

### Step 7.4: Posts Table පෙන්වනවා

**ඔබට පෙන්වෙන දේ:**

```
┌─────────────────────────────────────────────────────────────────┐
│  Blog Admin                          [Home] [Logout]            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Post                                                            │
│                                                                  │
│  [Search...]  [Create]                                          │
│                                                                  │
│  ┌───┬────────────────────────┬──────────────┬───────┬────────┐│
│  │ID │ Title                  │ Author       │ Pub.  │Created ││
│  ├───┼────────────────────────┼──────────────┼───────┼────────┤│
│  │ 1 │ Welcome to My Blog!    │ Blog Admin   │  ✓    │Mar 17  ││
│  │   │                        │              │       │        ││
│  │   │ [Edit] [Delete] [View]                                 ││
│  ├───┼────────────────────────┼──────────────┼───────┼────────┤│
│  │ 2 │ Python Flask...        │ Tech Enthus. │  ✓    │Mar 17  ││
│  │   │                        │              │       │        ││
│  │   │ [Edit] [Delete] [View]                                 ││
│  ├───┼────────────────────────┼──────────────┼───────┼────────┤│
│  │ 3 │ My First Blog Post...  │ Your Name    │  ✓    │Mar 18  ││
│  │   │                        │              │       │        ││
│  │   │ [Edit] [Delete] [View]                                 ││
│  └───┴────────────────────────┴──────────────┴───────┴────────┘│
│                                                                  │
│  Showing 1 to 3 of 3 records                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

### Step 7.5: Admin Panel Features

**මෙතනින් ඔබට:**

✅ **සියලු posts table එකෙන් බලන්න පුළුවන්**
- ID, Title, Author, Published status, Created date

✅ **Search කරන්න පුළුවන්**
- Search box එකේ keywords type කරන්න

✅ **Create කරන්න పුළුවන්**
- "Create" button click කරන්න

✅ **Edit කරන්න පුළුවන්**
- ඕනෑම post එකක "Edit" link click කරන්න

✅ **Delete කරන්න පුළුවන්**
- "Delete" link click කරන්න

✅ **View කරන්න පුළුවන්**
- "View" link click කරලා post එක බලන්න

---

### Step 7.6: Posts Search කරන්නේ කොහොමද?

**Search box එකේ keywords type කරන්න:**
```
Python
```

**Enter press කරන්න**

**"Python" තියෙන posts විතරක් filter වෙලා පෙන්වනවා!**

---

### Step 7.7: Admin Panel එකෙන් Post Creation

**"Create" button click කරන්න**

**Create form එකක් open වෙනවා - ඒකත් කලින් වගේම!**

---

## STEP 8: Server එක Stop කරන්නේ කොහොමද? 🛑 {#step-8-stop-server}

### Step 8.1: Terminal එක Active කරන්න

Server එක run වෙන terminal window එක click කරන්න.

---

### Step 8.2: CTRL + C Press කරන්න

**Keyboard එකේ:**
- `CTRL` key එක hold කරන්න
- `C` key එක press කරන්න
- එකවරම release කරන්න

---

### Step 8.3: Server එක Stop වෙනවා

**Terminal එකේ පෙන්වනවා:**
```
KeyboardInterrupt
(venv) d:\My-Blogs\Blogs>
```

**✅ Server එක stop වුණා!**

---

### Step 8.4: Virtual Environment Deactivate කරන්න (Optional)

**Type කරන්න:**
```bash
deactivate
```

**Press:** `Enter`

**Terminal එකේ `(venv)` කියන එක අතුරුදහන් වෙනවා:**
```
d:\My-Blogs\Blogs>
```

---

## 🎯 Summary - Quick Reference

### Server Start කරන්න:
```bash
cd d:/My-Blogs/Blogs
source venv/Scripts/activate
python run.py
```

### Pages Access කරන්න:
| Page | URL |
|------|-----|
| Homepage | http://localhost:5000/ |
| Create Post | http://localhost:5000/create |
| View Post | http://localhost:5000/post/slug-here |
| Edit Post | http://localhost:5000/edit/1 |
| Admin Panel | http://localhost:5000/admin |

### Server Stop කරන්න:
```
CTRL + C
```

---

## 🎨 Interface Features Summary

✅ **Clean Navigation** - සියලු pages වල top එකේ
✅ **Responsive Design** - Mobile & Desktop යන දෙකෙන්ම
✅ **Markdown Support** - Rich formatting
✅ **CRUD Operations** - Create, Read, Update, Delete
✅ **Admin Panel** - Table view with search
✅ **Pagination** - Homepage එකේ
✅ **Beautiful Design** - Bootstrap 5

---

## 📞 Troubleshooting

### Page Load වෙන්නේ නැත්නම්?
- Server එක run වෙනවද terminal එකෙන් බලන්න
- URL එක හරිද කියලා check කරන්න
- Browser cache clear කරන්න (Ctrl+F5)

### "Connection Refused" error එකක් වුණොත්?
- Server එක start කරලා නැද්ද බලන්න
- Terminal එකේ errors තියෙනවද බලන්න

### Forms submit වෙන්නේ නැත්නම්?
- Required fields (* mark කරලා තියෙන) fill කරලා තියෙනවද බලන්න
- Server එක run වෙනවද බලන්න

---

**සියලු steps සාර්ථකව සම්පූර්ණ කළ හැකියි! 🎉**

**Happy Blogging! 🚀**
