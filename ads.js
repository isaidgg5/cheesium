const brokie = "https://recollectsideway.com/u51ydi5ybu?key=3b96cebdf6fcc47e6e2cf07f0034c04c"
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
