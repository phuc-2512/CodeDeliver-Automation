document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('paymentForm');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const progressPercentage = document.getElementById('progressPercentage');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Show loading overlay
        loadingOverlay.style.display = 'flex';

        // Start the main.py process
        try {
            const response = await fetch('/start-process', { method: 'POST' });
            if (!response.ok) {
                throw new Error('Failed to start the process');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to start the process. Please try again.');
            loadingOverlay.style.display = 'none';
            return;
        }

        // Poll for progress updates
        const progressInterval = setInterval(async () => {
            try {
                const response = await fetch('/progress');
                if (response.ok) {
                    const data = await response.json();
                    progressPercentage.textContent = `${data.progress}%`;

                    if (data.progress >= 100) {
                        clearInterval(progressInterval);
                        loadingOverlay.style.display = 'none';
                        alert('Process completed successfully!');
                    }
                }
            } catch (error) {
                console.error('Error fetching progress:', error);
            }
        }, 1000);
    });
});