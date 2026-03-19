# 📸 Profile Picture Upload කිරීමේ මාර්ගෝපදේශය

## ✨ Upload කරන්නේ කෙසේද?

### **ක්‍රමය 1: "Change Photo" Button**

1. Blog එක start කරන්න:
   ```bash
   ./start_blog.bat
   ```

2. http://localhost:5000/ වෙත යන්න

3. පිටුවේ උඩ profile section එකේ **"Change Photo"** button එක click කරන්න

4. ඔබේ image එක select කරන්න (PNG, JPG, JPEG, GIF)

5. ස්වයංක්‍රීයව upload වේ! 🎉

---

### **ක්‍රමය 2: Profile Image මත Hover**

1. Profile picture එකට mouse ගෙන යන්න

2. Camera icon 📷 පෙනෙනවා

3. Click කරන්න - file selector එක open වේ

4. Image එක select කරන්න

5. ස්වයංක්‍රීයව upload වේ!

---

## 🎯 විශේෂාංග

### ✅ සහාය දක්වන Formats:
- PNG (.png)
- JPEG/JPG (.jpg, .jpeg)
- GIF (.gif)

### 📏 File සීමාවන්:
- **Maximum Size**: 5MB
- **Recommended Size**: 400x400 pixels හෝ වැඩි
- **Aspect Ratio**: Square (1:1) වඩාත් සුදුසුයි

### 🔄 ස්වයංක්‍රීය Features:
- පැරණි photo එක ස්වයංක්‍රීයව delete වේ
- නව photo එක `profile.{extension}` ලෙස save වේ
- Page reload වීමෙන් පසු profile පෙන්වයි

---

## 🖼️ UI Features

### Profile Section:
```
┌──────────────────────────────────────────┐
│  📅 Date    👤 Asitha Lakmal    🕐 Time  │
│                                           │
│          [Profile Picture]                │
│          📷 (Camera on hover)             │
│       [📤 Change Photo Button]            │
└──────────────────────────────────────────┘
```

### Upload Options:
1. **Hover Effect**: Profile picture මත mouse ගෙන ගියාම camera icon 📷 පෙන්වයි
2. **Direct Button**: "Change Photo" button click කරන්න
3. **Instant Preview**: Upload කිරීමට පෙර preview පෙන්වයි

---

## 🚀 භාවිතය

### පළමු වරට:
```bash
./start_blog.bat
```

### Upload කරන්න:
1. පිටුව විවෘත කරන්න
2. Profile section එකට යන්න
3. "Change Photo" click කරන්න
4. Image select කරන්න
5. Done! ✅

---

## 🛡️ Security Features

✅ File type validation
✅ File size checking (max 5MB)
✅ Secure filename handling
✅ Old files auto-cleanup
✅ Server-side validation

---

## 📂 File එක Save වන තැන

```
D:\My-Blogs\Blogs\app\static\images\profile.{extension}
```

Upload කළ image එක browser cache කිරීම නිසා instant update නොවුනොත්:
- Page එක refresh කරන්න (F5)
- හෝ Hard refresh (Ctrl + F5)

---

## 🎨 Customization

### නම වෙනස් කරන්න:

`app/templates/base.html` line 162:
```html
<h4 class="profile-name mb-0">Asitha Lakmal</h4>
```

### Max file size වෙනස් කරන්න:

`app/templates/base.html` line 185:
```javascript
if (file.size > 5 * 1024 * 1024) { // 5MB
```

### Upload folder වෙනස් කරන්න:

`app/routes.py` line 84:
```python
upload_folder = os.path.join('app', 'static', 'images')
```

---

## ⚠️ Troubleshooting

### Upload වැඩ නොකරන්නේ නම්:

1. **Folder permissions check කරන්න:**
   ```bash
   ls -la app/static/images/
   ```

2. **Console errors බලන්න:**
   - Browser DevTools විවෘත කරන්න (F12)
   - Console tab එකේ errors තිබේද බලන්න

3. **Flask server logs බලන්න:**
   - Terminal එකේ error messages බලන්න

### Image පෙන්වන්නේ නැත්නම්:

1. Hard refresh කරන්න (Ctrl + F5)
2. Browser cache clear කරන්න
3. File නම `profile.jpg` (හෝ .png, .jpeg) ද බලන්න

---

## 🔧 Technical Details

### Backend Route:
```python
@bp.route('/upload-profile', methods=['POST'])
```

### Upload Handler:
- Validates file type and size
- Removes old profile images
- Saves with standardized name
- Returns with flash message

### Frontend:
- Drag & drop support - ❌ (future feature)
- Instant preview - ✅
- Size validation - ✅
- Type validation - ✅

---

හැකි නම් **manual copy** කරනවාට වඩා **upload feature** එක භාවිතා කරන්න! 😊
