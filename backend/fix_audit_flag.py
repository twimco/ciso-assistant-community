#!/usr/bin/env python
"""
Standalone script to fix the audit feature flag in the database.
Run this instead of the management command if Django imports are failing.
"""

import os
import sys
import django
from pathlib import Path

# Add the backend directory to Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciso_assistant.settings')

try:
    django.setup()

    from global_settings.models import GlobalSettings

    def fix_audit_flag():
        print("🔧 Fixing audit feature flag...")

        # Get or create the feature-flags record
        ff, created = GlobalSettings.objects.get_or_create(name="feature-flags")

        if ff.value is None:
            ff.value = {}
            print("📝 Initialized empty value dict")

        # Check if audit field exists
        if 'audit' not in ff.value:
            ff.value['audit'] = True
            ff.save(update_fields=['value'])
            print("✅ Added audit=True to feature-flags record")
        else:
            print(f"ℹ️  Audit flag already exists: {ff.value.get('audit')}")

        print(f"📊 Current feature flags: {ff.value}")
        return True

    if __name__ == '__main__':
        try:
            fix_audit_flag()
            print("🎉 Audit flag fix completed successfully!")
        except Exception as e:
            print(f"❌ Error fixing audit flag: {e}")
            sys.exit(1)

except ImportError as e:
    print(f"❌ Django import failed: {e}")
    print("💡 Try installing missing system dependencies:")
    print("   macOS: brew install cairo pango gdk-pixbuf libffi")
    print("   Ubuntu: apt-get install libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libffi-dev")
    sys.exit(1)
