// Google Clean Theme Switcher for AP Human Geography Studio
function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  try {
    localStorage.setItem('ap_hug_theme', isDark ? 'dark' : 'light');
  } catch (e) {}
  updateThemeToggleButtons(isDark);
}

function updateThemeToggleButtons(isDark) {
  const label = isDark ? '☀️ Google Clean' : '🌙 Dark Mode';
  document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
    btn.innerHTML = `<i class="${isDark ? 'fa-solid fa-sun text-amber-400' : 'fa-solid fa-moon text-indigo-400'}"></i> ${label}`;
  });
}

function initTheme() {
  try {
    const isDark = localStorage.getItem('ap_hug_theme') === 'dark';
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    updateThemeToggleButtons(isDark);
  } catch (e) {}
}

document.addEventListener('DOMContentLoaded', initTheme);
