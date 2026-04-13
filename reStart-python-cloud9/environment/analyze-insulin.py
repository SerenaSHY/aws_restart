with open("preproinsulin-seq-clean.txt", "r") as raw_file: 
    cleaned_sequence = raw_file.read() 
    cleaned_sequence_len = len(cleaned_sequence) 
    print(f"The file has {cleaned_sequence_len}" characters)