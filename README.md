# LabReport01
git hub link: https://github.com/Israt28jahan/LabReport01.git
DFS Grid Path Finder

Description

This Python script generates a random N×N grid (where N is between 4 and 7), places a random source and goal position (both on non-obstacle cells), and uses Depth-First Search (DFS) to find a path from the source to the goal. It also records the topological order of traversal during DFS.

Features

Randomly generates an N×N grid with obstacles (1) and open paths (0)

Selects a random source and goal that are not obstacles

Uses DFS to search for a path from the source to the goal

Displays the grid with:

S for the source

G for the goal

* for the DFS path

# for obstacles

Prints the topological order of DFS traversal

Installation & Usage

1. Clone the Repository

git clone https://github.com/yourusername/dfs-grid-path.git
cd dfs-grid-path

2. Run the Script

Ensure you have Python installed, then execute:

python dfs_grid_path.py

Example Output

Generated Grid:
. . # . S
# . # . .
. . . # .
. # G . #
. . . . #

Source: (0, 4)
Goal: (3, 2)
DFS Path: [(0,4), (1,4), (2,4), (2,3), (3,3), (3,2)]
Topological Order of DFS Traversal: [(0,4), (1,4), (2,4), (2,3), (3,3), (3,2)]

Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request to enhance the project.

License

This project is licensed under the MIT License.

GitHub Repository

🔗 GitHub Link: https:https://github.com/Israt28jahan/LabReport01.git

