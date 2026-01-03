import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciso_assistant.settings')
django.setup()

from django.contrib.auth import get_user_model
from iam.models import Role, RoleAssignment, Folder

User = get_user_model()

def add_audit_permissions():
    # Get the user (assuming it's the first/last user, or you can specify by email)
    try:
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            user = User.objects.first()
        
        print(f"Adding audit permissions to user: {user.email}")
        
        # Get or create audit permissions
        audit_permissions = [
            'view_engagement',
            'view_workpaper', 
            'view_evidence',
            'view_finding',
            'view_report',
            'add_engagement',
            'add_workpaper',
            'add_evidence', 
            'add_finding',
            'add_report',
            'change_engagement',
            'change_workpaper',
            'change_evidence',
            'change_finding',
            'change_report',
            'delete_engagement',
            'delete_workpaper',
            'delete_evidence',
            'delete_finding',
            'delete_report'
        ]
        
        # Add permissions to user
        for perm_name in audit_permissions:
            if not user.permissions.get(perm_name, False):
                user.permissions[perm_name] = True
                print(f"Added permission: {perm_name}")
        
        user.save()
        print(f"✅ Successfully added audit permissions to {user.email}")
        print(f"User permissions: {list(user.permissions.keys())}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    add_audit_permissions()
