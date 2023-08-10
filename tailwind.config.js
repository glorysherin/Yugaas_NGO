/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors :{
        'primary':"#f59e0b",
        'background':"#FEFDFC",
        'third': "#FEEAAB"
      },
    },
  },
  plugins: [], 
}
