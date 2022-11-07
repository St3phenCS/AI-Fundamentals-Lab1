# About visualize.py

## Important

Change directory (cd) into folder which includes your `visualize.py`.

Don't forget to install required packages first:

```sh
pip install -r requirements.txt
```

or install then run when installation complete:

```sh
bash run.sh
```

## Usage

```sh
python visualize <level> <input_file> <algorithm>
```

Where:

| `<level>`         | `<input_file>`    | `<algorithm>`                                                   |
| ----------------- | ----------------- | --------------------------------------------------------------- |
| `1` `2` `advance` | `1` `2` `3` `...` | `bfs` `dfs` `ucs` `gbfs1` `gbfs2` `astar1` `astar2` `adv` `...` |

Eg. if we wanna run a visualization with `astar algorithm` - `heuristic-function-1` on `input1.txt` of `level_1` we use:

```sh
python -m visualize 1 1 astar1
```

![picture 1](images/Screenshot%202022-11-02%20213554.png)

~~Enjoin~~ :)

### One more thing

When the visualization done, there is an output visualize-image file in folder `./visualize_img/` . The image is the last frame captured of the visualize-process. Something like this:

![picture 2](images/5b75e99bf9aa5e5fb18666e4c06b634b0ee8c4e806ce7c4d9b2af0da10ab2c55.png)
