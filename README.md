# NBA pairs
Function that searches through NBA player heights
based on user input.

### About
Takes a single integer input and print a list of all pairs of players
whose height in inches adds up to the integer input to the application. If no
matches are found, the application will print "No matches found"

Sample output is as follows:
```
> NBA-pairs 139

- Nate Robinson      	Mike Wilks
- Nate Robinson      	Brevin Knight
```

The pairs are presented with the small player on the left and the tall player on the right, except when they have the same height. In that case the first player found will be on the left side of the pair.
This avoids duplicated pairs just if the orders could be swapped for a second pairing.

The middle values provides a big numbers of pairs. It is interesting trying to find the tallest and the smallest pairs.

### Built With

NBA_pairs was built using the following technologies:
* [Python](https://www.python.org/) version 3.6
* [Pycharm](https://www.jetbrains.com/pycharm/download) as IDE
* [Binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) in recursive version
* [Linear search](https://en.wikipedia.org/wiki/Linear_search)


The recursive binary search is used to find the first match.
The linear search is used to find matches adjacent to the first match found.
This implementation has a time complexity of O(nlogn).

### Installation and usage

1. Clone the repo
   ```sh
   git clone https://github.com/ZoltanMG/Tempo.git
   ```
2. Go to NBA_pairs directory
   ```sh
   cd NBA_pairs
   ```
3. Add execution permission to file
   ```sh
   chmod u+x nba_pairs.py
   ```
4. Run the file
   ```
   ./nba_pairs.py
   ```
5. Play entering one integer and hit enter
   ```
   NBA-pairs 143
   - Brevin Knight         Mike Conley
   - Brevin Knight         Mario Chalmers
   - Mike Wilks            Jacque Vaughn
   - Mike Wilks            Earl Watson
   ```
6. Quit the game entering q and hit enter
   ```sh
   NBA-pairs q
   ```
------
- Danilo Romero   <a href="https://twitter.com/terpenoide"><img src="https://img.icons8.com/fluent/48/000000/twitter.png" width="20px"></a> &nbsp;  <a href="https://www.linkedin.com/in/danilo-romero-beltran/"><img src="https://img.icons8.com/fluent/20/000000/linkedin.png"></a> &nbsp; <a href="https://github.com/daniloromero"><img src="https://img.icons8.com/fluent/20/000000/github.png"></a>