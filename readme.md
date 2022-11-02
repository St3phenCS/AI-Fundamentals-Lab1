# About visualize.py

## To visualize step by step

### Step 1

Change directory into folder which includes your visualize.py.

### Step 2

In your terminal:

```sh
python visualize <level> <input_file> <algorithm>
```

With these arguments values following optionally the table below:

| `<level>`         | `<input_file>`    | `<algorithm>`                                                   |
| ----------------- | ----------------- | --------------------------------------------------------------- |
| `1` `2` `advance` | `1` `2` `3` `...` | `bfs` `dfs` `ucs` `gbfs1` `gbfs2` `astar1` `astar2` `adv` `...` |

Eg. if we want run a visualization of `astar algorithm` with `heuristic-function-1` on `input1.txt` of `level_1` we use this command line:

```sh
python -m visualize 1 1 astar1
```

![picture 1](images/Screenshot%202022-11-02%20213554.png)

~~Enjoin~~ :)

### One more thing

When the visualization done, you will see an output visualize image file in folder `./visualize_img/` . The image is the last fame captured of the visualize process. Something like this:

![picture 2](images/5b75e99bf9aa5e5fb18666e4c06b634b0ee8c4e806ce7c4d9b2af0da10ab2c55.png)
