<script lang="ts">
	import { page } from '$app/stores';
	import { safeTranslate } from '$lib/utils/i18n';
	import { m } from '$paraglide/messages';

	import Breadcrumbs from '$lib/components/Breadcrumbs/Breadcrumbs.svelte';
	import AuditEngagementSelector from '$lib/components/Audit/AuditEngagementSelector.svelte';
	import NoAccess from '$lib/components/Audit/NoAccess.svelte';
	import { clientSideToast } from '$lib/utils/stores';

	// Check if user has audit permissions
	const user = $page.data?.user;
	const hasAuditPermissions =
		user?.permissions &&
		(Object.hasOwn(user.permissions, 'view_engagement') ||
			Object.hasOwn(user.permissions, 'view_workpaper') ||
			Object.hasOwn(user.permissions, 'view_evidence') ||
			Object.hasOwn(user.permissions, 'view_finding') ||
			Object.hasOwn(user.permissions, 'view_report'));

	interface Props {
		children?: import('svelte').Snippet;
		actions?: import('svelte').Snippet;
	}

	let { children, actions }: Props = $props();

	// Page title for the audit section
	const auditTitle = $derived(safeTranslate(m.audit));
</script>

{#if !hasAuditPermissions}
	<NoAccess />
{:else}
	<div class="audit-layout">
		<!-- Header Section -->
		<div class="audit-header">
			<div class="audit-title-section">
				<h1 class="audit-title">{auditTitle}</h1>
				<AuditEngagementSelector />
			</div>

			<!-- Page Actions Slot -->
			{#if actions}
				<div class="audit-actions">
					{@render actions?.()}
				</div>
			{/if}
		</div>

		<!-- Breadcrumbs -->
		<div class="audit-breadcrumbs">
			<Breadcrumbs />
		</div>

		<!-- Main Content -->
		<main class="audit-content">
			{@render children?.()}
		</main>

		<!-- Toast Area -->
		{#if $clientSideToast}
			<div class="audit-toast">
				<!-- Toast component would go here -->
				{$clientSideToast.message}
			</div>
		{/if}
	</div>
{/if}

<style>
	.audit-layout {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
	}

	.audit-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1.5rem 2rem;
		background: white;
		border-bottom: 1px solid #e2e8f0;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
	}

	.audit-title-section {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.audit-title {
		font-size: 2rem;
		font-weight: 700;
		color: #1e293b;
		margin: 0;
		background: linear-gradient(135deg, #3b82f6, #8b5cf6);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.audit-actions {
		display: flex;
		gap: 0.75rem;
		align-items: center;
	}

	.audit-breadcrumbs {
		padding: 0.75rem 2rem;
		background: white;
		border-bottom: 1px solid #e2e8f0;
	}

	.audit-content {
		flex: 1;
		padding: 2rem;
	}

	.audit-toast {
		position: fixed;
		bottom: 2rem;
		right: 2rem;
		max-width: 400px;
		background: #1f2937;
		color: white;
		padding: 1rem 1.5rem;
		border-radius: 0.5rem;
		box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
		z-index: 50;
	}
</style>
