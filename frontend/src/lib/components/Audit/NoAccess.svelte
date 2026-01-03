<script lang="ts">
	import { m } from '$paraglide/messages';
</script>

<div class="no-access-container">
	<div class="no-access-content">
		<div class="no-access-icon">
			<i class="fa-solid fa-lock"></i>
		</div>
		<h2 class="no-access-title">{m.accessDenied()}</h2>
		<p class="no-access-message">
			{m.noAuditPermissions()}
		</p>
		<p class="no-access-help">
			{m.contactAdministrator()}
		</p>
	</div>
</div>

<style>
	.no-access-container {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 60vh;
		padding: 2rem;
	}

	.no-access-content {
		text-align: center;
		max-width: 400px;
	}

	.no-access-icon {
		font-size: 4rem;
		color: #ef4444;
		margin-bottom: 1.5rem;
	}

	.no-access-title {
		font-size: 1.875rem;
		font-weight: 700;
		color: #1f2937;
		margin-bottom: 1rem;
	}

	.no-access-message {
		color: #6b7280;
		font-size: 1.125rem;
		margin-bottom: 0.5rem;
	}

	.no-access-help {
		color: #9ca3af;
		font-size: 0.875rem;
	}
</style>
