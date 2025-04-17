import os
import hashlib
import json

# Get the hash of a file
def get_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()
    except:
        print("Error reading:", file_path)
        return None

# Scan folder and return dictionary with file:hash
def scan_folder(folder_path, hash_file_name):
    result = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == hash_file_name:
                continue  # skip the hash file itself
            full_path = os.path.join(root, file)
            hash_value = get_file_hash(full_path)
            if hash_value:
                relative_path = os.path.relpath(full_path, folder_path)
                result[relative_path] = hash_value
    return result

# Load hashes from file
def load_hashes(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

# Save new hashes
def save_hashes(hashes, file_path):
    with open(file_path, "w") as f:
        json.dump(hashes, f, indent=4)

# Compare hashes and find changes
def compare(old, new):
    modified = []
    deleted = []
    added = []

    for file in old:
        if file not in new:
            deleted.append(file)
        elif old[file] != new[file]:
            modified.append(file)

    for file in new:
        if file not in old:
            added.append(file)

    return modified, deleted, added

# Main function
def main():
    folder = input("Enter the path to the folder you want to monitor: ").strip()
    if not os.path.isdir(folder):
        print("That folder doesn't exist.")
        return

    hash_file_name = input("Enter a name for the hash file (example: hashes.json): ").strip()
    if not hash_file_name:
        hash_file_name = "hashes.json"

    hash_file_path = os.path.join(folder, hash_file_name)

    print("\nScanning:", folder)
    print("Hash file will be saved at:", hash_file_path)

    old_hashes = load_hashes(hash_file_path)
    new_hashes = scan_folder(folder, hash_file_name)

    modified, deleted, added = compare(old_hashes, new_hashes)

    if modified or deleted or added:
        print("\nChanges detected:")
        if modified:
            print("Modified files:", modified)
        if deleted:
            print("Deleted files:", deleted)
        if added:
            print("New files:", added)
    else:
        print("\nNo changes found.")

    save_hashes(new_hashes, hash_file_path)
    print("\nHashes saved inside the folder.")

if __name__ == "__main__":
    main()
