with open("preproinsulin-seq-clean.txt", "r") as raw_file:
    cleaned_sequence = raw_file.read()


    with open("lsinsulin-seq-clean.txt", "w") as file:
        current_sequence = cleaned_sequence[0:24]
        file.write(current_sequence)
        print("lsinsulin amino acids length: ", len(current_sequence))

    with open("binsulin-seq-clean.txt", "w") as file:
        current_sequence = cleaned_sequence[24:54]
        file.write(current_sequence)
        print("binsulin amino acids length: ", len(current_sequence))

    with open("cinsulin-seq-clean.txt", "w") as file:
        current_sequence = cleaned_sequence[54:89]
        file.write(current_sequence)
        print("cinsulin amino acids length: ", len(current_sequence))

    with open("ainsulin-seq-clean.txt", "w") as file:
        current_sequence = cleaned_sequence[89:]
        file.write(current_sequence)
        print("ainsulin amino acids length: ", len(current_sequence))