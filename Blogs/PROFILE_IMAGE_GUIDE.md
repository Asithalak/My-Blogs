# 📸 Profile Picture එකතු කිරීමේ මාර්ගෝපදේශය

## 🎯 Quick Guide

### විධිය 1: Batch File භාවිතා කරමින්

1. `open_images_folder.bat` ගොනුව double-click කරන්න
2. ඔබේ photo එක එම folder එකට drag කරන්න
3. ගොනුව නම් කරන්න: **profile.jpg**

### විධිය 2: Manual Copy

1. ඔබේ photo එක copy කරන්න
2. මෙම folder එක විවෘත කරන්න:
   ```
   D:\My-Blogs\Blogs\app\static\images\
   ```
3. Photo එක paste කරන්න
4. නම් කරන්න: **profile.jpg** (හෝ profile.png, profile.jpeg)

---

## 📐 Image Requirements

| විස්තරය | අගය |
|---------|------|
| **Recommended Size** | 400x400 pixels හෝ වැඩි |
| **Aspect Ratio** | Square (1:1) වඩාත් සුදුසුයි |
| **Format** | JPG, PNG, JPEG, GIF |
| **File Name** | profile.jpg (හෝ profile.png) |

---

## 🎨 පිහිටීම

```
┌─────────────────────────────────────────────────────────┐
│  📅 Thursday, March 20, 2026    👤    🕐 02:30:45 PM   │
│                          Asitha Lakmal                   │
│                          Personal Blog                   │
└─────────────────────────────────────────────────────────┘
```

---

## ✨ විශේෂාංග

- ✅ ස්වයංක්‍රීයව .jpg, .png, .jpeg හොයනවා
- ✅ Photo එක නැත්නම්, "AL" initials පෙන්වනවා
- ✅ Hover කළාම photo විශාල වේ
- ✅ Circular shape සමඟ border එකක්
- ✅ භ්‍රමණය වන වර්ණ gradient background

---

## 🚀 Test කරන්න

```bash
./start_blog.bat
```

http://localhost:5000/ - ඔබේ profile එක පිටුවේ උඩම පෙන්වයි!

---

## 🔧 නම වෙනස් කරන්න

`app/templates/base.html` ගොනුවේ 75-76 lines:

```html
<h4 class="profile-name mb-0">Asitha Lakmal</h4>
<p class="profile-subtitle mb-0">Personal Blog</p>
```

මෙය ඔබට අවශ්‍ය ලෙස වෙනස් කරන්න!
