# Helix United FC — Official Website

Welcome to the official repository for the **Helix United FC** website, the digital home of the Yellow Army based in Dhaka, Bangladesh. Built on the philosophy that "Football is nothing more than friendship," this project serves as the central hub for club news, match fixtures, player statistics, and youth academy registrations.

## Features

* **Dynamic Front-End:** A fully responsive, single-page application built with vanilla HTML, CSS, and JavaScript.
* **Player Database:** Interactive player cards featuring stats, jersey numbers, and positions.
* **Match Tracking:** Live and upcoming fixture tracking alongside historical club results.
* **Registration System:** Multi-step registration form for the Youth Academy.
* **Admin Dashboard:** A secure, built-in administrative panel to manage news, roster updates, matches, and event scheduling.

## Repository Structure

* `Helix United website.html`: The core application file containing the markup, styling, and client-side logic.
* `helix united team logo.png` & `helix_cover_photo.jpg`: Core visual assets for the site branding.
* **Encoding Utilities:** A suite of Python and Node.js scripts (`fix.js`, `fix.py`, `fix_emojis.py`, `fix_safe.py`, `test_decode.py`, `test_decode2.py`) utilized to clean up and restore corrupted UTF-8 characters and mojibake (specifically emojis and formatting marks) that occurred during file transfers or editing. 

## Development & Utility Scripts

If you encounter corrupted characters (mojibake) in the HTML file, the included utility scripts can restore them. The scripts target specific mangled Windows-1252 to UTF-8 decoding errors.

To run the Python restoration script:
\`\`\`bash
python test_decode.py
\`\`\`
*Note: Ensure you update the file paths within the scripts to match your local directory structure before executing.*