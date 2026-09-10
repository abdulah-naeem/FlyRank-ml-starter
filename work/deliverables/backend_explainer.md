# Plain-Words Explainer: How the Contact Form Backend Works

**Feature:** A dynamic contact form built with Netlify Forms.

## 1. What is a "Backend"?
If a website is a restaurant, the **frontend** (the HTML and CSS) is the dining room where customers sit, look at the menu, and eat. The **backend** is the kitchen. It's the hidden machinery (servers, databases, and application logic) that takes a customer's order, cooks the food, stores the ingredients securely, and makes sure everything runs smoothly behind the scenes. 

The frontend is what the user *sees*; the backend is where the data is actually *processed and stored*.

## 2. What this feature does
This feature adds a working contact form to the bottom of the portfolio. Instead of just displaying a static email address, it allows a visitor to type their name, email, and a message directly into the browser and hit "Send". The feature securely captures that information, stores it in a database, and sends an email notification to the site owner, all without the visitor ever needing to open their own email app.

## 3. How the data flows (End to End)
Here is the exact journey of a message from the user's brain to my inbox:

1. **The Input (Frontend):** The user visits the portfolio, types their message into the HTML `<form>`, and clicks the "Send Message" button.
2. **The Request (The Wire):** The browser bundles up the name, email, and message into an HTTP POST request and securely sends it over the internet (via HTTPS) to Netlify's servers. 
3. **The Intercept (Netlify Magic):** Because the HTML tag includes a special `data-netlify="true"` attribute, Netlify's servers recognize this incoming request as a form submission.
4. **The Storage (Backend):** Netlify acts as the backend. Its servers receive the data payload, parse it, and save the message securely in a database connected to the Netlify dashboard.
5. **The Notification (The Output):** Once saved, Netlify's backend triggers an automated email containing the user's message and sends it directly to my personal inbox, completing the loop.
