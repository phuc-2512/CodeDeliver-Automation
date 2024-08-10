document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('paymentForm');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const progressPercentage = document.getElementById('progressPercentage');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Hiển thị overlay loading
        loadingOverlay.style.display = 'flex';

        // Bắt đầu quá trình xử lý (gọi main.py)
        try {
            const formData = new FormData(form);
            const jsonData = {};
            for (let [key, value] of formData.entries()) {
                jsonData[key] = value;
            }

            const response = await fetch('/start-process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(jsonData),
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
            }

            const data = await response.json();
            console.log("Phản hồi từ server:", data);
        } catch (error) {
            console.error('Lỗi:', error);
            alert('Lỗi khi gửi dữ liệu: ' + error.message);
            loadingOverlay.style.display = 'none';
            return;
        }
        // Cập nhật tiến trình
        const progressInterval = setInterval(async () => {
            try {
                const response = await fetch('/progress');
                if (response.ok) {
                    const data = await response.json();
                    if (data.error) {
                        throw new Error(data.error);
                    }
                    progressPercentage.textContent = `${data.progress}%`;

                    if (data.progress === 100) {
                        clearInterval(progressInterval);
                        loadingOverlay.style.display = 'none';
                        alert('Quá trình xử lý hoàn tất thành công!');
                    } else if (data.progress === -1) {
                        clearInterval(progressInterval);
                        loadingOverlay.style.display = 'none';
                        alert('Có lỗi xảy ra trong quá trình xử lý. Vui lòng kiểm tra logs để biết thêm chi tiết.');
                    }
                }
            } catch (error) {
                console.error('Lỗi khi cập nhật tiến trình:', error);
                clearInterval(progressInterval);
                loadingOverlay.style.display = 'none';
                alert('Có lỗi xảy ra trong quá trình xử lý. Vui lòng thử lại.');
            }
        }, 1000);
    });
});