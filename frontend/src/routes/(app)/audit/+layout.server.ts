import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	const user = locals.user;

	// Gate the whole audit module behind the feature flag
	// Feature flags are loaded globally in the root layout and exposed via `locals.featureflags`.
	const auditEnabled = locals.featureflags?.audit ?? true;
	if (!auditEnabled) {
		throw redirect(404, '/');
	}

	// Check if user has any audit permissions
	const hasAuditPermissions =
		user?.permissions &&
		(Object.hasOwn(user.permissions, 'view_engagement') ||
			Object.hasOwn(user.permissions, 'view_workpaper') ||
			Object.hasOwn(user.permissions, 'view_evidence') ||
			Object.hasOwn(user.permissions, 'view_finding') ||
			Object.hasOwn(user.permissions, 'view_report'));

	if (!hasAuditPermissions) {
		throw redirect(403, '/');
	}

	return {
		user,
		hasAuditPermissions,
		auditEnabled
	};
};
