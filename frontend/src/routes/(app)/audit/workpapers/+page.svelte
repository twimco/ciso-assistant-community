<script lang="ts">
	import { m } from '$paraglide/messages';
</script>

<!-- NOTE: Page-level slot fragments must be direct children of the layout component.
     This page is not a component instance, so using a named slot causes a build error.
     Render the action button inline for now. -->
<div class="flex justify-end mb-4">
	<button class="btn btn-primary">
		<i class="fa-solid fa-plus"></i>
		{m.addWorkpaper()}
	</button>
</div>

<div class="workpapers-page">
	<div class="page-header">
		<h2>{m.workpapers()}</h2>
		<p class="page-description">{m.workpapersDescription()}</p>
	</div>

	<div class="page-content">
		<div class="placeholder-card">
			<div class="placeholder-icon">
				<i class="fa-solid fa-file-lines"></i>
			</div>
			<h3>{m.noWorkpapersYet()}</h3>
			<p>{m.workpapersHelpText()}</p>
		</div>
	</div>
</div>

<style>
	.workpapers-page {
		max-width: 1200px;
		margin: 0 auto;
	}

	.page-header {
		margin-bottom: 2rem;
	}

	.page-header h2 {
		font-size: 1.875rem;
		font-weight: 700;
		color: #1f2937;
		margin-bottom: 0.5rem;
	}

	.page-description {
		color: #6b7280;
		font-size: 1.125rem;
	}

	.page-content {
		background: white;
		border-radius: 0.75rem;
		padding: 3rem;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
		text-align: center;
	}

	.placeholder-card {
		max-width: 400px;
		margin: 0 auto;
	}

	.placeholder-icon {
		font-size: 4rem;
		color: #cbd5e1;
		margin-bottom: 1.5rem;
	}

	.placeholder-card h3 {
		font-size: 1.5rem;
		font-weight: 600;
		color: #374151;
		margin-bottom: 1rem;
	}

	.placeholder-card p {
		color: #6b7280;
		margin-bottom: 2rem;
		line-height: 1.6;
	}
</style>
