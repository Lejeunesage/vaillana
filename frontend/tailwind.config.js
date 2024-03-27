/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./src/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        JakartaSans: ['JakartaSans', 'sans-serif'],
        Ballsye: ['Ballsye', 'sans-serif'],
        Komikula: ['Komikula', 'sans-serif'],
        Acumin: ['Acumin', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

