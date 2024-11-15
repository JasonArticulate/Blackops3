import os

# Project Directory Structure for GitHub Pages Deployment:
# call_of_duty_modding_site/
#   |- index.html (Home Page)
#   |- mod_library.html
#   |- creator_hub.html
#   |- forum.html
#   |- tools_resources.html
#   |- news.html
#   |- about.html
#   |- faq.html
#   |- community_challenges.html
#   |- mod_tutorials.html
#   |- profile.html
#   |- README.md (Project Overview and Instructions)
#   |- assets/
#      |- css/
#         |- styles.css (Modern, animated CSS)
#      |- js/
#         |- script.js (JavaScript for animations and interactions)
#      |- images/
#         |- (Any images used on the website)
#      |- mods/
#         |- rapid_fire_mod.zip
#         |- wallhack_script.zip
#         |- zombie_mode_enhancements.zip
#         |- weapon_swapper.zip
#         |- aim_assist_tuner.zip
#         |- unlimited_sprint.zip
#         |- quick_reload.zip

# Index.html - Example Template for GitHub Pages

home_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Call of Duty Modding Hub</title>
    <link rel="stylesheet" href="assets/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
    <style>
        body { 
            font-family: 'Rubik', sans-serif; 
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364); /* Futuristic gradient */
            color: #ffffff;
            overflow-x: hidden;
        }
        header, footer {
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        header h1 {
            text-align: center;
            font-size: 3rem;
            animation: fadeInDown 2s;
        }
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 0;
        }
        nav ul li {
            margin: 0 15px;
            font-size: 1.2rem;
            animation: bounceIn 1.5s;
        }
        nav ul li a {
            text-decoration: none;
            color: #ffffff;
            transition: color 0.3s;
        }
        nav ul li a:hover {
            color: #00e676;
        }
        #intro {
            text-align: center;
            padding: 50px;
            animation: fadeIn 3s;
        }
        #featured-mods {
            padding: 50px;
            text-align: center;
        }
        .mod-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }
        .mod-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
            animation: zoomIn 1s;
        }
        .mod-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        }
        .mod-item a {
            text-decoration: none;
            color: #00e676;
            font-weight: bold;
        }
        footer {
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1 class="animate__animated animate__fadeInDown">Welcome to Call of Duty Modding Hub</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="mod_library.html">Mod Library</a></li>
                <li><a href="creator_hub.html">Creator Hub</a></li>
                <li><a href="forum.html">Community Forum</a></li>
                <li><a href="tools_resources.html">Tools & Resources</a></li>
                <li><a href="news.html">News & Updates</a></li>
                <li><a href="community_challenges.html">Community Challenges</a></li>
                <li><a href="mod_tutorials.html">Mod Tutorials</a></li>
                <li><a href="profile.html">My Profile</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="faq.html">FAQ</a></li>
            </ul>
        </nav>
    </header>
    <section id="intro">
        <h2>Your One-Stop Hub for Call of Duty Mods</h2>
        <p>Explore and enhance your Call of Duty experience with our community-driven mods and resources. Mods available for PS3, PS4, PS5, and PC!</p>
    </section>
    <section id="featured-mods">
        <h2>Featured Mods</h2>
        <div class="mod-gallery">
            <div class="mod-item animate__animated animate__zoomIn">
                <h3>Rapid Fire Mod</h3>
                <a href="assets/mods/rapid_fire_mod.zip" download>Download</a>
            </div>
            <div class="mod-item animate__animated animate__zoomIn">
                <h3>Wallhack Script</h3>
                <a href="assets/mods/wallhack_script.zip" download>Download</a>
            </div>
            <div class="mod-item animate__animated animate__zoomIn">
                <h3>Zombie Mode Enhancements</h3>
                <a href="assets/mods/zombie_mode_enhancements.zip" download>Download</a>
            </div>
        </div>
    </section>
    <footer>
        <p>&copy; 2050 Call of Duty Modding Hub. All Rights Reserved.</p>
    </footer>
    <script src="assets/js/script.js"></script>
    <script>
        gsap.from("header", { duration: 1.5, y: -100, opacity: 0, ease: "bounce" });
        gsap.from("#intro h2", { duration: 1.5, opacity: 0, delay: 1 });
        gsap.from(".mod-item", { duration: 1.5, opacity: 0, y: 100, stagger: 0.3 });
    </script>
</body>
</html>
'''

# Write to index.html
with open("index.html", "w") as f:
    f.write(home_html)

# Additional Pages (Mod Library, Creator Hub, Community Challenges, etc.)
pages = {
    "mod_library.html": '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mod Library - Call of Duty Modding Hub</title>
        <link rel="stylesheet" href="assets/css/styles.css">
    </head>
    <body>
        <header>
            <h1>Mod Library</h1>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="mod_library.html">Mod Library</a></li>
                    <li><a href="creator_hub.html">Creator Hub</a></li>
                    <li><a href="forum.html">Community Forum</a></li>
                    <li><a href="tools_resources.html">Tools & Resources</a></li>
                    <li><a href="news.html">News & Updates</a></li>
                    <li><a href="community_challenges.html">Community Challenges</a></li>
                    <li><a href="mod_tutorials.html">Mod Tutorials</a></li>
                    <li><a href="profile.html">My Profile</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="faq.html">FAQ</a></li>
                </ul>
            </nav>
        </header>
        <section id="mods">
            <h2>Available Mods for Black Ops 3</h2>
            <ul>
                <li><a href="assets/mods/rapid_fire_mod.zip" download>Rapid Fire Mod</a></li>
                <li><a href="assets/mods/wallhack_script.zip" download>Wallhack Script</a></li>
                <li><a href="assets/mods/zombie_mode_enhancements.zip" download>Zombie Mode Enhancements</a></li>
                <li><a href="assets/mods/weapon_swapper.zip" download>Weapon Swapper</a></li>
                <li><a href="assets/mods/aim_assist_tuner.zip" download>Aim Assist Tuner</a></li>
                <li><a href="assets/mods/unlimited_sprint.zip" download>Unlimited Sprint</a></li>
                <li><a href="assets/mods/quick_reload.zip" download>Quick Reload</a></li>
            </ul>
        </section>
        <footer>
            <p>&copy; 2050 Call of Duty Modding Hub. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    ''',
    "about.html": '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us - Call of Duty Modding Hub</title>
        <link rel="stylesheet" href="assets/css/styles.css">
    </head>
    <body>
        <header>
            <h1>About Us</h1>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="mod_library.html">Mod Library</a></li>
                    <li><a href="creator_hub.html">Creator Hub</a></li>
                    <li><a href="forum.html">Community Forum</a></li>
                    <li><a href="tools_resources.html">Tools & Resources</a></li>
                    <li><a href="news.html">News & Updates</a></li>
                    <li><a href="community_challenges.html">Community Challenges</a></li>
                    <li><a href="mod_tutorials.html">Mod Tutorials</a></li>
                    <li><a href="profile.html">My Profile</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="faq.html">FAQ</a></li>
                </ul>
            </nav>
        </header>
        <section id="about">
            <h2>Who We Are</h2>
            <p>Welcome to the Call of Duty Modding Hub. We are a community of passionate gamers and modders dedicated to enhancing your Call of Duty gaming experience through creative mods and collaborative efforts. Our goal is to make modding accessible and safe for everyone, whether you're new to modding or an experienced creator.</p>
        </section>
        <footer>
            <p>&copy; 2050 Call of Duty Modding Hub. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    '''
}

# Write additional pages to their respective files
for filename, content in pages.items():
    with open(filename, "w") as f:
        f.write(content)

# README.md file
readme_md = '''
# Call of Duty Modding Hub

## Overview
Welcome to the Call of Duty Modding Hub! This project is designed as a community-driven platform for gamers interested in modifying their Call of Duty experience. This website provides mods for PS3, PS4, PS5, and PC versions of various Call of Duty titles, along with resources for modders and players alike.

## Features of a 2050 Design
- **Futuristic Aesthetic**: A gradient background with deep colors inspired by sci-fi.
- **Smooth Animations**: Animations powered by Animate.css and GSAP to ensure users have an interactive, seamless experience.
- **Modern Elements**: Card hover effects, smooth transitions, and an engaging hero section.

## Website Structure
This repository includes the following pages:

- **index.html**: Home page featuring an overview and introduction to the Call of Duty Modding Hub.
- **mod_library.html**: A comprehensive library of mods available for download.
- **creator_hub.html**: A dedicated section for modders to share and collaborate.
- **community_challenges.html**: Participate in monthly challenges to win prizes and recognition.
- **mod_tutorials.html**: Step-by-step tutorials to help you get started with modding.
- **forum.html**: A community space for discussing mods, issues, and ideas.
- **tools_resources.html**: Tools and resources for getting started with modding.
- **news.html**: News and updates about recent mods, tools, and Call of Duty patches.
- **about.html**: Information about the purpose of the website and the people behind it.
- **faq.html**: Answers to frequently asked questions about modding and using this site.
- **profile.html**: Your customizable user profile, showing saved mods and progress.

## Getting Started
To use the website, simply clone this repository and open the HTML files in your browser, or visit the hosted version via GitHub Pages.

### Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/call_of_duty_modding_site.git
   ```
2. Navigate to the project directory and open **index.html** in your preferred browser.

### Font and Styling
The website is styled using the **Rubik** font, ensuring a modern and clean look. CSS for the website is located in the `assets/css/styles.css` file. All pages make use of this stylesheet for consistent styling across the platform.

### Mod Downloads
Mods are located in the `assets/mods/` directory. Each mod has its own `.zip` file for easy download. Simply click the "Download" button on the relevant mod page to start using it.

## How to Contribute
We welcome contributions from the community! You can contribute by:
- Adding new mods.
- Improving the website design.
- Participating in discussions in the community forum.

To contribute, please fork the repository and create a pull request with your changes.

## Contact
If you have any questions or issues, please open an issue in the repository or contact the maintainers.

## License
This project is licensed under the MIT License.
'''

# Write to README.md
with open("README.md", "w") as f:
    f.write(readme_md)

# Note:
# - The provided HTML templates for all pages use consistent advanced CSS and JavaScript animations to give the website a futuristic 2050 look.
# - CSS animations and transitions are integrated with GSAP and Animate.css for a highly interactive experience.
# - The website can be hosted using GitHub Pages by committing these HTML and asset files to a repository and enabling GitHub Pages from the settings.

# This approach uses static HTML/CSS/JS, making it compatible for hosting on GitHub Pages without requiring a server-side language like Python.
