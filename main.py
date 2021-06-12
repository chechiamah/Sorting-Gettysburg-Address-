# returns a dictionary
def read_file(file_name="gettysburg.txt"):
  letter_dict = {}
  file_in = open(file_name, "r")
  # loop thru rows
  for line in file_in:
    line = line.strip()
    # loop thru line
    for letter in line:
      letter = letter.lower()
      if letter.isalpha():
        if letter not in letter_dict.keys():
          letter_dict[letter] = 1
        else:
          letter_dict[letter] += 1
  file_in.close()
  return letter_dict
    
# Returns a list of the dictionaries keys sorted alphabetically
def sort_keys(dictionary):
  dictionary_keys = list(dictionary.keys())
  dictionary_keys.sort()
  return dictionary_keys

def main():
  alpha_dict = read_file()
  key_list = sort_keys(alpha_dict)
  
  print("The letter frequency of the Gettysburg Address is")
  for key in key_list:
    print(key, alpha_dict[key])

main()
