import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciso_assistant.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def add_missing_permissions():
    # Get the user
    user = User.objects.filter(email='feliks@twimco.com').first()
    if not user:
        user = User.objects.filter(is_superuser=True).first()
    if not user:
        user = User.objects.first()
    
    if not user:
        print("❌ No user found!")
        return
    
    print(f"Adding missing audit permissions to: {user.email}")
    
    # Missing permissions
    missing_perms = [
        'view_engagement',    # for Engagements nav item
        'view_workpaper',     # for Workpapers nav item  
        'view_report'         # for Audit Reports nav item
    ]
    
    added = []
    for perm in missing_perms:
        if not user.permissions.get(perm, False):
            user.permissions[perm] = True
            added.append(perm)
            print(f"✅ Added: {perm}")
        else:
            print(f"ℹ️  Already has: {perm}")
    
    if added:
        user.save()
        print(f"✅ Saved {len(added)} new permissions")
    else:
        print("ℹ️  All permissions already present")
    
    # Show current audit permissions
    audit_perms = [p for p in user.permissions.keys() if 'engagement' in p or 'workpaper' in p or 'evidence' in p or 'finding' in p or 'report' in p]
    print(f"Current audit permissions: {audit_perms}")

if __name__ == '__main__':
    add_missing_permissions()
