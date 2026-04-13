# Improved Script (using Regex)
import re

with open("preproinsulin-seq.txt", "r") as raw_file:
    raw_data = raw_file.read()
    
    clean_data = re.sub(r"ORIGIN|//|\d+|\s", "", raw_data)
    
    clean_data_length = len(clean_data)
    
    # Verify
    print("Length:", clean_data_length)
    print(clean_data)
    
    if clean_data_length!= 110:
        print(f"[WARNING]: Expected length is 110, cleaned data length is {clean_data_length}")
    else:
        # Save cleaned data
        with open("preproinsulin-seq-clean.txt", "w") as file:
            file.write(clean_data)
            print("Cleaned data saved to file!")