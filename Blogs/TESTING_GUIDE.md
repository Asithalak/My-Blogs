# 🧪 Testing Guide - Daily Planner System

## ✅ Complete Test Checklist

### 🚀 Setup & Start

```bash
# 1. Database Setup
cd d:/My-Blogs/Blogs
python update_database.py

# Expected Output:
# ✅ Database tables created/updated successfully!
# ✅ Daily Schedule Planner ready!

# 2. Start Blog
start_blog.bat

# Expected Output:
# * Running on http://127.0.0.1:5000

# 3. Open Browser
# Navigate to: http://localhost:5000/
```

---

## 🎯 Test 1: HomePage Display

### **Without Schedule:**
1. Open http://localhost:5000/
2. Should see: "Plan Your Day!" alert box
3. Click "Create Today's Schedule" button
4. Planner modal should open

### **With Schedule:**
- After saving a schedule, home page should show:
  - Today's date
  - Schedule timeline (left)
  - Priorities (right)
  - Goals section
  - Appointments
  - Notes
  - "Edit" button

**✅ Pass if:** Schedule displays correctly on home page

---

## 🎯 Test 2: Category Hover Menu

### **Test Steps:**

1. Click "Daily Update" in navbar
2. Modal opens
3. **Look for Category Menu Bar** (top of modal):
   ```
   📁 Projects | 🐙 GitHub | 🔍 Google | 📚 Learning | 🔧 Tools | 👤 Personal
   ```

### **Hover Test:**

**Projects Category:**
1. Hover over "📁 Projects"
2. Dropdown should appear with:
   - Personal Blog
   - E-commerce Site
   - Mobile App
   - Client Project
3. Menu should animate smoothly
4. Click "Personal Blog"
5. Should add `[PROJECT] Personal Blog` to Notes section
6. Notification should appear: "Added: [PROJECT] Personal Blog"

**GitHub Category:**
1. Hover over "🐙 GitHub"
2. Dropdown should show:
   - Pull Requests (badge: 3)
   - Issues (badge: 5)
   - Code Review
   - Commits
3. Badges should display correctly
4. Click "Pull Requests"
5. Should add to Notes

**Google Category:**
1. Hover over "🔍 Google"
2. Should show:
   - Gmail (badge: 12)
   - Drive
   - Calendar
   - Docs
3. Click "Gmail"
4. Check Notes section

**All Other Categories:**
- Test Learning (📚)
- Test Tools (🔧)
- Test Personal (👤)

**✅ Pass if:**
- All dropdowns appear on hover
- Smooth animations
- Items clickable
- Adds to Notes correctly
- Notifications appear

---

## 🎯 Test 3: Menu Bar Functions

### **Navigation Buttons:**

**Previous Day:**
1. Click "◀ Previous"
2. Date should change to yesterday
3. Schedule should load (if exists)

**Today:**
1. Click "📅 Today"
2. Date should reset to today
3. Today's schedule loads

**Next Day:**
1. Click "Next ▶"
2. Date should change to tomorrow
3. Empty schedule (if not created yet)

**✅ Pass if:** Dates change correctly, schedules load

---

### **Action Buttons:**

**Clear:**
1. Fill some data
2. Click "❌ Clear"
3. Confirmation dialog appears
4. Click OK
5. All fields should be empty

**✅ Pass if:** All data clears after confirmation

**Copy Yesterday:**
1. Create schedule for today
2. Save it
3. Click "Next ▶" (go to tomorrow)
4. Click "📋 Copy Yesterday"
5. Confirmation dialog
6. Click OK
7. Today's schedule should copy to tomorrow
8. Checkboxes should be unchecked
9. Goals/Notes should NOT copy

**✅ Pass if:** Schedule copies correctly, new day starts fresh

**Print:**
1. Click "🖨 Print"
2. Browser print dialog opens
3. Preview looks good

**✅ Pass if:** Print dialog opens

**Save:**
1. Fill schedule data
2. Click "💾 Save"
3. Success alert: "✅ Daily plan saved successfully!"
4. Page reloads (if today's date)
5. Home page shows schedule

**✅ Pass if:** Saves and displays on home page

---

## 🎯 Test 4: Date Picker

1. Click on date input field
2. Calendar picker should open
3. Select a different date
4. Schedule should load for that date
5. Fill some data
6. Save
7. Go back to previous date
8. Data should persist

**✅ Pass if:** Can select any date, data persists per date

---

## 🎯 Test 5: Time Slots

### **Test All Time Slots:**

```
06:00-07:00 AM → Fill: "Morning exercise"
07:00-08:00 AM → Fill: "Breakfast"
08:00-09:00 AM → Fill: "Start coding"
...
08:00-09:00 PM → Fill: "Evening review"
```

### **Work Type Selection:**

1. For each time slot, select different work types:
   - 💻 Coding
   - 🎨 Design
   - 👥 Meeting
   - 📚 Research
   - 🧪 Testing
   - 📝 Documentation
   - ☕ Break
   - 🏃 Exercise
   - 🎓 Learning

2. Save
3. Check home page display
4. Work types should show as colored badges

**✅ Pass if:** All time slots work, types saved correctly

---

## 🎯 Test 6: Priorities

1. Fill 3 priorities:
   ```
   ☐ Complete authentication module
   ☐ Fix critical bug
   ☐ Review pull requests
   ```
2. Check first priority checkbox
3. Save
4. Reload modal
5. First checkbox should be checked
6. Home page should show checked item with strikethrough

**✅ Pass if:** Priorities save, checkboxes persist

---

## 🎯 Test 7: Goals

1. Enter goal:
   ```
   Ship new authentication feature to production
   by end of day. Focus on quality over speed.
   ```
2. Save
3. Check home page
4. Goal should display in formatted box

**✅ Pass if:** Goal saves and displays

---

## 🎯 Test 8: Appointments

1. Add 3 appointments:
   ```
   ☐ Sprint planning | 10:30
   ☐ Client call | 14:00
   ☐ 1-on-1 meeting | 16:30
   ```
2. Check second appointment
3. Save
4. Home page should list appointments with times

**✅ Pass if:** Appointments save with times

---

## 🎯 Test 9: Notes

### **Manual Entry:**
1. Type in Notes:
   ```
   Remember to update documentation
   Backup database before deployment
   Prepare demo for Friday
   ```
2. Save
3. Check home page display

### **Category Addition:**
1. Hover "Projects" → Click "Personal Blog"
2. Check Notes section
3. Should see: `📌 [PROJECT] Personal Blog`
4. Hover "GitHub" → Click "Issues"
5. Should see: `📌 [GITHUB] Issues`
6. Multiple categories can be added

**✅ Pass if:** Both manual and category entries work

---

## 🎯 Test 10: Multi-Day Workflow

### **Monday:**
1. Create full schedule
2. Save

### **Tuesday:**
1. Click "Next ▶"
2. Click "Copy Yesterday"
3. Adjust as needed
4. Save

### **Wednesday:**
1. Navigate to Wednesday
2. Create from scratch
3. Save

### **Review:**
1. Click "◀ Previous" multiple times
2. Check Monday's schedule
3. Click "Next ▶"
4. Check Tuesday's schedule
5. All data should persist per day

**✅ Pass if:** Each day maintains separate data

---

## 🎯 Test 11: Home Page Integration

### **Test Scenarios:**

**Scenario 1: No Schedule**
```
Display: "Plan Your Day!" alert
Button: "Create Today's Schedule"
```

**Scenario 2: Full Schedule**
```
Display:
- Header with date
- Edit button
- Schedule timeline
- Priorities list
- Goals box
- Appointments
- Notes section
```

**Scenario 3: Partial Schedule**
```
Display: Only filled sections
Empty sections: Hidden
```

**✅ Pass if:** Display adjusts based on data

---

## 🎯 Test 12: UI/UX Tests

### **Hover Effects:**
1. Hover over category items → Color change + shadow
2. Hover over menu buttons → Lift effect
3. Hover over time slots → Background highlight

### **Animations:**
1. Category dropdown → Smooth slide down
2. Notification toast → Slide in from right
3. Auto-dismiss after 2 seconds

### **Responsive:**
1. Resize browser window
2. Modal should adapt
3. Categories should remain accessible

### **Visual Consistency:**
1. All buttons same style family
2. Colors: Purple gradient (primary), Green (success)
3. Icons: Bootstrap Icons
4. Fonts: Consistent sizes

**✅ Pass if:** UI looks polished and professional

---

## 🎯 Test 13: Error Handling

### **Empty Save:**
1. Open modal
2. Don't fill anything
3. Click "Save"
4. Should save empty (allowed)
5. Home page shows "No schedule" message

### **Invalid Date:**
1. Manually change date in URL (future testing)
2. Should handle gracefully

### **Network Error:**
1. Disconnect internet
2. Try to save
3. Should show error alert

**✅ Pass if:** Errors handled gracefully

---

## 🎯 Test 14: Performance

### **Load Time:**
1. Open modal
2. Should open < 1 second

### **Save Time:**
1. Full schedule with all fields
2. Click Save
3. Should save < 2 seconds

### **Page Load:**
1. Refresh home page
2. Schedule should load < 1 second

**✅ Pass if:** No lag, smooth experience

---

## 🎯 Test 15: Data Persistence

### **Test Flow:**
1. Create schedule for today
2. Save
3. Close browser completely
4. Reopen http://localhost:5000/
5. Home page still shows schedule
6. Click "Daily Update"
7. Modal loads saved data
8. Edit something
9. Save
10. Changes persist

**✅ Pass if:** Data survives browser restart

---

## 📋 Quick Test Checklist

```
☐ Database setup successful
☐ Blog starts without errors
☐ Home page loads
☐ Navbar "Daily Update" button works
☐ Category menu bar visible
☐ All 6 categories present
☐ Hover shows dropdown menus
☐ Dropdowns animate smoothly
☐ Clicking category adds to Notes
☐ Notification toast appears
☐ Menu bar buttons work (Previous/Today/Next)
☐ Clear button clears all data
☐ Copy Yesterday works
☐ Print dialog opens
☐ Save button saves data
☐ Date picker works
☐ Time slots fill and save
☐ Work types selectable
☐ Priorities checkboxes work
☐ Goals save and display
☐ Appointments with times work
☐ Notes section works
☐ Multi-day navigation works
☐ Home page displays schedule
☐ Edit button opens modal with data
☐ Each day has separate data
☐ Data persists after browser restart
☐ UI looks professional
☐ No console errors (F12)
```

---

## 🐛 Common Issues & Fixes

### **Issue: Modal doesn't open**
```bash
# Check Flask is running
# Check console errors (F12)
# Restart browser
```

### **Issue: Categories don't show dropdown**
```bash
# Clear browser cache (Ctrl + Shift + R)
# Check CSS loaded correctly
```

### **Issue: Data doesn't save**
```bash
# Check Flask terminal for errors
# Verify database setup ran
# Check network tab (F12)
```

### **Issue: Home page shows old data**
```bash
# Hard refresh: Ctrl + F5
# Clear browser cache
```

### **Issue: Database errors**
```bash
# Re-run: python update_database.py
# Check app/models.py has all new models
```

---

## ✅ Expected Results

### **All Tests Pass:**
```
✅ 15/15 Tests Passed
✅ Category hover menu works perfectly
✅ All menu buttons functional
✅ Data saves per day
✅ Home page integration works
✅ UI is polished and professional
```

### **Success Criteria:**
- [ ] Can create daily schedule
- [ ] Categories add items to Notes
- [ ] Menu navigation works
- [ ] Data persists per day
- [ ] Home page displays schedule
- [ ] No console errors
- [ ] Smooth user experience

---

## 📸 Screenshots to Verify

**Before Setup:**
- Home page: "Plan Your Day!" alert

**After Setup:**
- Category menu bar with 6 categories
- Dropdown menus on hover
- Time slots (15 slots visible)
- Priorities (3 checkboxes)
- Goals textarea
- Appointments with time pickers
- Notes section
- Save button at bottom

**Home Page:**
- Schedule card with:
  - Date header
  - Schedule timeline (left)
  - Priorities/Goals (right)
  - Edit button
  - Notes section

---

## 🚀 Performance Benchmarks

| Action | Target | Pass Criteria |
|--------|--------|---------------|
| Modal Open | < 1s | ✅ Instant |
| Category Hover | < 0.3s | ✅ Smooth animation |
| Dropdown Appear | < 0.3s | ✅ Smooth slide |
| Click Category | < 0.5s | ✅ Adds to Notes + notification |
| Save Data | < 2s | ✅ Success message |
| Page Load | < 1s | ✅ Shows schedule |
| Navigate Days | < 1s | ✅ Loads schedule |

---

## 🎓 Testing Tips

1. **Test in Order:** Follow tests 1-15 sequentially
2. **Use F12:** Check console for errors
3. **Clear Cache:** Between major changes
4. **Test Each Category:** Don't skip any
5. **Multi-Day Test:** Essential for persistence
6. **Screenshot Issues:** For debugging
7. **Note Errors:** In terminal/console

---

## 🎉 Success!

සියල්ලම වැඩ කරනවා නම්:

```
🎊 Congratulations!
✅ Professional Daily Planner
✅ Category Hover Menu System
✅ Multi-Day Scheduling
✅ Home Page Integration
✅ Data Persistence
✅ Beautiful UI/UX
```

---

**Ready to Test?**

```bash
cd d:/My-Blogs/Blogs
python update_database.py
start_blog.bat

# Then follow this guide! 🚀
```

Happy Testing! 😊
