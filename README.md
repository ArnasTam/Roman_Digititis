# Roman_Digititis 
## [Link to the problem](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=5&page=show_problem&problem=280)

Many persons are familiar with the Roman numerals for relatively small numbers. The symbols “i”,
“v”, “x”, “l”, and “c” represent the decimal values 1, 5, 10, 50, and 100 respectively. To represent
other values, these symbols, and multiples where necessary, are concatenated, with the smaller-valued
symbols written further to the right. For example, the number 3 is represented as “iii”, and the value
73 is represented as “lxxiii”. The exceptions to this rule occur for numbers having units values of 4
or 9, and for tens values of 40 or 90. For these cases, the Roman numeral representations are “iv” (4),
“ix” (9), “xl” (40), and “xc” (90). So the Roman numeral representations for 24, 39, 44, 49, and 94
are “xxiv”, “xxxix”, “xliv”, “xlix”, and “xciv”, respectively.
The preface of many books has pages numbered with Roman numerals, starting with “i” for the
first page of the preface, and continuing in sequence. Assume books with pages having 100 or fewer
pages of preface. How many “i”, “v”, “x”, “l”, and “c” characters are required to number the pages in
the preface? For example, in a five page preface we’ll use the Roman numerals “i”, “ii”, “iii”, “iv”,
and “v”, meaning we need 7 “i” characters and 2 “v” characters.

## Input
The input will consist of a sequence of integers in the range 1 to 100, terminated by a zero. For each
such integer, except the final zero, determine the number of different types of characters needed to
number the prefix pages with Roman numerals.

## Output
For each integer in the input, write one line containing the input integer and the number of characters
of each type required. The examples shown below illustrate an acceptable format.

## Sample Input
```
1
2
20
99
0
```

## Sample Output
```
1: 1 i, 0 v, 0 x, 0 l, 0 c
2: 3 i, 0 v, 0 x, 0 l, 0 c
20: 28 i, 10 v, 14 x, 0 l, 0 c
99: 140 i, 50 v, 150 x, 50 l, 10 c
```
