function m() {
    let wm = document.getElementById('watermerk');
    if (!wm) {
        wm = document.createElement('div');
        wm.id = 'watermerk';
        wm.textContent = 'port by aj';
        wm.style.cssText = 'position:fixed;bottom:12px;right:12px;color:rgba(255,255,255,0.4);font-family:sans-serif;font-size:13px;pointer-events:none;z-index:9999;user-select:none;';
        document.body.appendChild(wm);
    }
}

const observer = new MutationObserver(m);
document.addEventListener('DOMContentLoaded', function() {
    m();
    observer.observe(document.body, { childList: true, subtree: true, characterData: true });
});