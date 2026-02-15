This tool converts any image (like your favorite Shrek memes) into a unique, playable **Balatro Seed**. 

Unlike a random generator, this script uses **Cryptographic Hashing (SHA-256)** to turn the binary data of an image into an 8-character string. It even follows the specific **generation probabilities** of the game to ensure the seeds feel authentic.

## 📊 How it Works
The script analyzes the pixels and data of an image and maps them to Balatro's valid character set:
* **No Zeros (0)** or **Letters (O)**.
* **Numbers (1-9):** ~30% appearance rate.
* **Letters (A-Z):** ~70% appearance rate.
