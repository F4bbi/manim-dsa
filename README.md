<p align="center">
    <a><img src="https://github.com/user-attachments/assets/7d18b40d-e455-4d2d-8a86-39b16401bbf0" width="525" height="300"></a>
    <br />
    <br />
    <a href="https://pypi.org/project/manim-dsa/"><img src="" alt="PyPI Latest Release"></a>
    <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-red.svg?style=flat" alt="MIT License"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
    <a href="https://pepy.tech/project/manim-dsa"><img src="https://pepy.tech/badge/manim-dsa" alt="Downloads"> </a>
    <br />
    <br />
    <i>A Manim plugin designed to animate common data structures and algorithms</i>
</p>
<hr />

**Manim DSA**, short for *Manim Data Structures & Algorithms*, is a [Manim](https://www.manim.community/) plugin designed to animate common data structures and algorithms. Whether you are an educator looking to enhance your lectures, a student seeking to better understand these concepts, or a content creator making educational videos, Manim DSA provides a robust toolkit to bring abstract concepts to life.

## Table of Contents:

-  [Installation](#installation)
-  [Importing](#importing)
-  [Usage](#usage)
-  [Documentation](#documentation)
-  [Help with Manim DSA](#help-with-manim-dsa)
-  [Contributing](#contributing)
-  [License](#license)

## Installation

To install Manim DSA, you can use `pip`:

```bash
pip install manim-dsa
```

If you don't have Manim installed, please refer to the [official Manim documentation](https://docs.manim.community/en/stable/installation.html) for installation instructions.

## Importing

Simply use the following line of code to import the package:

```py
from manim_dsa import *
```

## Usage

The following is an example `Scene` where an array, a stack and a graph are created.

```python
from manim import *
from manim_dsa import *

class Example(Scene):
    def construct(self):
        graph = {
            'A': [('C', 11), ('D', 7)],
            'B': [('A', 5),  ('C', 3)],
            'C': [('A', 11), ('B', 3)],
            'D': [('A', 7),  ('C', 4)],
        }
        nodes_and_positions = {
            'A': LEFT * 1.5,
            'B': UP * 2,
            'C': RIGHT * 1.5,
            'D': DOWN * 2,
        }

        mArray = (
            MArray([1, 2, 3], style=ArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array", font="Cascadia Code"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=StackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack", font="Cascadia Code"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, GraphStyle.PURPLE)
            .add_label(Text("Graph", font="Cascadia Code"))
            .to_edge(RIGHT, 1)
        )

        self.play(Create(mArray))
        self.play(Create(mStack))
        self.play(Create(mGraph))
        self.wait()
```

The result is as follows:

https://github.com/user-attachments/assets/05307dc9-65d9-4262-ae32-3fb53068c8e4

## Documentation

Work in progess.

## Help with Manim DSA

If you need help installing or using Manim DSA, or you need to submit a bug report or feature request, please open an issue.

## Contributing

Contributions are welcome! Whether it’s reporting a bug, suggesting new features, or submitting pull requests, any help is greatly appreciated.

## How to Cite Manim DSA

To demonstrate the value of Manim DSA, we ask that you cite Manim DSA in your work. Currently, the best way to cite Manim DSA is to go to the [repository page](https://github.com/F4bbi/manim-dsa) (if you aren't already) and click the "cite this repository" button on the right sidebar. This will generate a citation in your preferred format, and will also integrate well with citation managers.
For guidance on how to properly cite Manim, please refer to the [Manim GitHub page](https://github.com/ManimCommunity/manim/blob/main/README.md#how-to-cite-manim).

## License

Manim DSA is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original license.

## Acknowledgements

- **[Manim Community](https://www.manim.community/)**: For creating and maintaining the amazing Manim library.
- **[drageelr](https://github.com/drageelr/manim-data-structures)**: For the inspiration behind the array implementation.
- **[Verdiana Pasqualini](https://verdianapasqualini.github.io/ManimGraphLibrary)**: For the inspiration behind the graph implementation.
