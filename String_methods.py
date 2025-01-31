print(dir("Hello"))

print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize)
print("hello".center(50,"-"))
print("gmail.com".find("."))
print("gmail.com".find("john"))
s = "i see a cat who like to cat whike i cat on a cat"
# find all occurences

poz = 0
poz = s.find("cat", poz)
if poz == -1:
    breakpoint(print("found cat on osition", poz))
    poz += 1
# we will come back to join later

#lower
s = "I SEE A LOT OF THINGS"
print(s.lower())
if s.lower() == "yes":

# replace
sample_string = "hello-world-example"
processed_string = replace_characters(sample_string, "-", " ")
print(processed_string)

# title
sample_string = "hello world example"
titled_string = convert_to_title_case(sample_string)
print(titled_string)

# split
sample_string = "hello world example"
split_words = split_string(sample_string)
print(split_words)

# join
words_list = ['hello', 'world', 'example']
joined_string = join_words(words_list)
print(joined_string)