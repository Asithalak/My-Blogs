# 🚀 Quick Start - Work Tracking System

## සරලව Setup කරන්න (3 පියවර)

### පියවර 1️⃣: Database Setup
```bash
cd d:/My-Blogs/Blogs
setup_daily_updates.bat
```

### පියවර 2️⃣: Start Blog
```bash
start_blog.bat
```

### පියවර 3️⃣: කළ වැඩ Log කරන්න
1. http://localhost:5000/ විවෘත කරන්න
2. Navbar → "📢 Daily Update" click
3. Work type, description, time fill කරන්න
4. "Log Work" click

---

## ✨ විශේෂාංග Overview

### 🎯 Work Tracking
- **10 Work Types:** Coding, Design, Meeting, etc.
- **Time Duration:** Hours spent on each task
- **Time Ago:** "2 hours ago" display
- **Daily Stats:** Total hours, task count, breakdown

### 📱 Notifications (Optional)
- SMS alerts when work logged
- Configure at: `/notification-settings`
- Twilio integration supported

### 📊 Statistics
- Real-time today's summary
- Work type breakdown
- Progress bars
- Task count

---

## 📖 Usage Examples

### Example 1: Log Coding Task
```
Work Type: Coding
Description: Implemented JWT authentication
Time: 3.5 hours
```

### Example 2: Log Meeting
```
Work Type: Meeting
Description: Sprint planning with team
Time: 1.5 hours
```

---

## 🎨 UI Features

### Ticker Banner (Auto-scroll အောက်)
```
📢 [Coding] Bug fixes (2.5h) • [Design] New UI (1h) • ...
```

### Modal Features
- ✍️ Add work form (left)
- 📋 Recent work log (right)
- 📊 Today's stats (bottom left)
- 🗑️ Delete old entries

---

## 🔔 Enable SMS (Optional)

### Setup Twilio:
1. Sign up: https://www.twilio.com
2. Get: Account SID, Auth Token, Phone Number
3. Install: `pip install twilio`
4. Uncomment code in `app/routes.py` lines 145-151

---

## 💡 Tips

✅ Log work regularly (2x per day)
✅ Be specific in descriptions
✅ Round time to 0.5h intervals
✅ Use correct work types
✅ Review daily stats

---

## 📚 Documentation

- **Full Guide:** `WORK_TRACKING_GUIDE.md`
- **Notifications:** `DAILY_UPDATES_GUIDE.md`
- **Setup:** `README.md`

---

Happy tracking! 💼✨
