<script lang="ts">
	import { m } from '$paraglide/messages';

	// Placeholder component for engagement selector
	// TODO: Implement engagement selection logic in future versions

	interface Props {
		selectedEngagement?: string;
	}

	let { selectedEngagement }: Props = $props();
</script>

<!-- Engagement Selector - Placeholder for v1 -->
<div class="engagement-selector">
	<div class="engagement-placeholder">
		<i class="fa-solid fa-handshake"></i>
		<span>{m.selectEngagement()}</span>
	</div>
</div>

<style>
	.engagement-selector {
		display: flex;
		align-items: center;
	}

	.engagement-placeholder {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0.5rem 1rem;
		background: #f1f5f9;
		border-radius: 0.375rem;
		color: #64748b;
		font-size: 0.875rem;
		font-weight: 500;
	}

	.engagement-placeholder i {
		color: #94a3b8;
	}
</style>
