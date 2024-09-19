def detectNumber(word):
   correct_words=["one","two","three","four","five","six","seven","eight","nine","ten"]
   
   for i, correct_word in enumerate(correct_words):
       if len(word) !=len(correct_word):
           continue
       diff_count=0
       for j in range (len(word)):
           if word[j] !=correct_word[j]:
               diff_count+=1
               
       if diff_count <= 1:
            return i + 1
   return None
    
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    for word in data[1:]:
        result=detectNumber(word)
        print(result)

if __name__ == "__main__":
    main()