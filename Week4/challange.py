#  File Processor
print("📁 Simple File Processor")

try:
    # Ask for input filename
    #The file name is myfile.txt in the same directory
    input_file = input("Enter input filename: ")
    
    # Read the file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Count words and convert to uppercase
    word_count = len(content.split())
    uppercase_content = content.upper()
    
    # Write to output file
    output_file = "output.txt"
    with open(output_file, 'w') as file:
        file.write(uppercase_content)
        file.write(f"\n\nWord count: {word_count}")
    
    print(f"✅ Success! Created {output_file}")
    print(f"📊 Word count: {word_count}")

except FileNotFoundError:
    print("❌ Error: File not found!")

except:
    print("❌ Error: Could not process the file!")