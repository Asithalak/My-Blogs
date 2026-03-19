"""
Database update script to add DailyUpdate, NotificationSettings, and DailyPlanner tables
Run this script to update your database with new features
"""

from app import create_app, db
from app.models import DailyUpdate, NotificationSettings, DailyPlanner, TimeSlot, Priority, Appointment

def update_database():
    app = create_app()

    with app.app_context():
        print("="*60)
        print("  Updating Database - Daily Planner System")
        print("="*60)
        print()

        print("Creating/updating tables...")
        db.create_all()
        print("✅ Database tables created/updated successfully!")
        print()

        # Check if sample data exists
        existing_updates = DailyUpdate.query.count()
        if existing_updates == 0:
            print("Adding sample work update...")
            sample = DailyUpdate(
                message="Welcome to the Work Tracker! Log your daily tasks here.",
                work_type="General",
                duration_hours=0.5
            )
            db.session.add(sample)
            db.session.commit()
            print("✅ Sample work update added!")
        else:
            print(f"📊 Found {existing_updates} existing work updates")

        print()
        print("="*60)
        print("  Setup Complete!")
        print("="*60)
        print()
        print("✨ New Features Available:")
        print("  1. Daily Schedule Planner with time slots")
        print("  2. Top Priorities tracking")
        print("  3. Daily goals and notes")
        print("  4. Appointments management")
        print("  5. Day-specific schedule saving")
        print("  6. Home page schedule display")
        print()
        print("🚀 Next Steps:")
        print("  1. Run: ./start_blog.bat")
        print("  2. Click 'Daily Update' in navbar")
        print("  3. Plan your day with time slots")
        print("  4. Save and view on home page")
        print()
        print("="*60)

if __name__ == '__main__':
    update_database()
