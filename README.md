# Spellcheck 

Spellcheck is a basic spell checker which uses the "edit distance" concept. The edit distance is the number of changes you need to make to a string so that it will become a different string. A “change” can be either an insertion (adding a letter), a deletion (removing a letter), or a substitution (replacing a letter with a different one.) For instance, the edit distance between "cat" and "cake" is two: you replace the letter "t" with the letter "k" before adding the letter "e". 

If the input string is not a real word, which means it cannot be found in the dictionary, spellcheck will suggest alternatives that have a "suitable" edit distance. For example, if the input string is "cax", the output are strings like "cab", "car", "cat", or "tax", all of which have an edit distance of only one. This implementation requires string manipulation and reading from a file. 
