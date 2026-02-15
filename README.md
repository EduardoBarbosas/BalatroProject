This tool converts any image (like your favorite Shrek memes) into a unique, playable **Balatro Seed**. 

Unlike a random generator, this script uses **Cryptographic Hashing (SHA-256)** to turn the binary data of an image into an 8-character string. It even follows the specific **generation probabilities** of the game to ensure the seeds feel authentic.

## 📊 How it Works
The script analyzes the pixels and data of an image and maps them to Balatro's valid character set:
* **No Zeros (0)** or **Letters (O)**.
* **Numbers (1-9):** ~30% appearance rate.
* **Letters (A-Z):** ~70% appearance rate.

🖼 Example Walkthrough
To help you get started, here is a breakdown of how the script processes an image into a Balatro Seed.

1. Choose Your Image
Let's say you have a file named swamp_shrek.jpg in your /images folder.

2. Run the Script
When you run python seed_gen.py, the script reads the binary data of the image. Even though it looks like a green ogre to you, the computer sees it as a unique string of hex code.

4. Get Your Seed
The script crunches that hash using Balatro's probability logic and spits out:

image used:

![7821cdaf7cc6bb3572e41fcc2e832ac1](https://github.com/user-attachments/assets/5d2e02f3-4dda-4485-a448-38b83c48981c)


Plaintext
IMAGE NAME                | GENERATED SEED
---------------------------------------------
821cdaf7cc6bb3572e41fcc2e832ac1.jpg | 5TC9Z65R
4. Input into Balatro
Launch Balatro.

Start a New Run.

Click the Customize button (bottom left).

Enter 5TC9Z65R into the seed box.
