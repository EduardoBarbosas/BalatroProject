import hashlib
import os

def generate_balatro_seed(image_path):
    # Balatro character pools & probabilities
    numbers = "123456789"  
    letters_an = "ABCDEFGHIJKLMN" 
    letters_pz = "PQRSTUVWXYZ" 

    with open(image_path, "rb") as f:
        data = f.read()
    
    hash_hex = hashlib.sha256(data).hexdigest()
    seed = ""

    for i in range(8):
        chunk = int(hash_hex[i*4 : (i+1)*4], 16)
        prob_roll = chunk % 100
        
        if prob_roll < 30: # 30% Number
            char = numbers[chunk % len(numbers)]
        else: # 70% Letter
            sub_roll = (chunk // 100) % 100
            if sub_roll < 55:
                char = letters_an[chunk % len(letters_an)]
            else:
                char = letters_pz[chunk % len(letters_pz)]
        seed += char
    return seed

def process_folder(folder_name="image"):
    # Check if folder exists
    if not os.path.exists(folder_name):
        print(f"Error: Folder '{folder_name}' not found!")
        return

    print(f"{'IMAGE NAME':<25} | {'GENERATED SEED'}")
    print("-" * 45)

    # Loop through all files in the folder
    for filename in os.listdir(folder_name):
        # Only process common image formats
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            path = os.path.join(folder_name, filename)
            seed = generate_balatro_seed(path)
            print(f"{filename:<25} | {seed}")

if __name__ == "__main__":
    process_folder()
    input("\nFinished! Press Enter to exit...")