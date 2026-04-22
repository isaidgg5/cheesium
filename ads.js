const brokie = "https://recollectsideway.com/i7dd7ruzr?key=e370275100340ce26eafdcb83fe93826"
const key = "hasOpenedTab";
document.addEventListener("DOMContentLoaded", () => {
  if (sessionStorage.getItem(key)) return;
  function firstclick() {
    window.open(brokie, "_blank", "noopener,noreferrer");
    sessionStorage.setItem(key, "1");
    document.removeEventListener("click", firstclick);
  }
  document.addEventListener("click", firstclick);
});
