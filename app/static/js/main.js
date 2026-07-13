document.addEventListener('DOMContentLoaded', function() {

    // Dark Mode Toggle
    const darkToggle = document.getElementById('darkModeToggle');
    if (darkToggle) {
        darkToggle.addEventListener('click', function() {
            fetch('/toggle-dark-mode')
                .then(r => r.json())
                .then(data => {
                    location.reload();
                });
        });
    }

    // Copy to Clipboard
    window.copyToClipboard = function(text) {
        navigator.clipboard.writeText(text).then(() => {
            showToast('Copied to clipboard!');
        }).catch(() => {
            const ta = document.createElement('textarea');
            ta.value = text;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showToast('Copied to clipboard!');
        });
    };

    // Toast notification
    function showToast(message) {
        const existing = document.querySelector('.custom-toast');
        if (existing) existing.remove();
        const toast = document.createElement('div');
        toast.className = 'custom-toast';
        toast.style.cssText = `
            position: fixed; bottom: 20px; right: 20px; z-index: 9999;
            background: var(--islamic-green); color: white; padding: 12px 24px;
            border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            animation: fadeInUp 0.3s ease;
            font-weight: 500;
        `;
        toast.textContent = message;
        document.body.appendChild(toast);
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 2000);
    }

    // Digital Tasbeeh
    const countDisplay = document.getElementById('countDisplay');
    const countBtn = document.getElementById('countBtn');
    const resetBtn = document.getElementById('resetBtn');
    const saveBtn = document.getElementById('saveBtn');
    const dhikrSelect = document.getElementById('dhikrSelect');
    const targetInput = document.getElementById('targetCount');
    const progressBar = document.getElementById('progressBar');

    if (countDisplay) {
        let count = parseInt(localStorage.getItem('tasbeeh_count') || '0');
        let target = parseInt(targetInput?.value || '33');
        countDisplay.textContent = count;
        updateProgress();

        if (countBtn) {
            countBtn.addEventListener('click', function() {
                count++;
                countDisplay.textContent = count;
                localStorage.setItem('tasbeeh_count', count);
                updateProgress();

                if (count >= target) {
                    count = 0;
                    countDisplay.textContent = count;
                    localStorage.setItem('tasbeeh_count', count);
                    updateProgress();
                    if (navigator.vibrate) navigator.vibrate(100);
                    showToast('Target reached! ' + (dhikrSelect ? dhikrSelect.value : ''));
                }
            });
        }

        if (resetBtn) {
            resetBtn.addEventListener('click', function() {
                count = 0;
                countDisplay.textContent = count;
                localStorage.setItem('tasbeeh_count', count);
                updateProgress();
            });
        }

        if (saveBtn) {
            saveBtn.addEventListener('click', function() {
                const name = dhikrSelect ? dhikrSelect.value : 'Tasbeeh';
                const target = parseInt(targetInput?.value || '33');
                fetch('/tasbeeh/save', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({name, target, count})
                }).then(r => r.json()).then(data => {
                    showToast('Progress saved!');
                });
            });
        }

        if (dhikrSelect) {
            dhikrSelect.addEventListener('change', function() {
                const targets = {
                    'Subhanallah': 33, 'Alhamdulillah': 33,
                    'Allahu Akbar': 34, 'La ilaha illallah': 100,
                    'Astaghfirullah': 100, 'custom': 33
                };
                if (targetInput) {
                    targetInput.value = targets[this.value] || 33;
                    target = parseInt(targetInput.value);
                }
                count = 0;
                countDisplay.textContent = '0';
                localStorage.setItem('tasbeeh_count', '0');
                updateProgress();
            });
        }

        if (targetInput) {
            targetInput.addEventListener('change', function() {
                target = parseInt(this.value) || 33;
                updateProgress();
            });
        }

        function updateProgress() {
            if (progressBar) {
                const pct = target > 0 ? Math.min(100, (count / target) * 100) : 0;
                progressBar.style.width = pct + '%';
            }
        }
    }

    // Bookmark button
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    if (bookmarkBtn) {
        bookmarkBtn.addEventListener('click', function() {
            const type = this.dataset.type;
            const id = this.dataset.id;
            fetch('/bookmark/toggle', {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCSRFToken()},
                body: JSON.stringify({content_type: type, content_id: id})
            }).then(r => r.json()).then(data => {
                showToast(data.bookmarked ? 'Bookmarked!' : 'Bookmark removed');
            });
        });
    }

    function getCSRFToken() {
        const meta = document.querySelector('meta[name="csrf-token"]');
        if (meta) return meta.getAttribute('content');
        const input = document.querySelector('input[name="csrf_token"]');
        return input ? input.value : '';
    }

    // Auto-dismiss alerts
    document.querySelectorAll('.alert-dismissible').forEach(function(alert) {
        setTimeout(function() {
            alert.classList.remove('show');
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });

    // Active nav highlighting
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
