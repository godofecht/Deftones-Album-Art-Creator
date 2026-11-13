# Deftones Album Art Creator

A Processing sketch that generates point-array album art in the style of Deftones' *Ohms*.

## What this is

The sketch turns an image into a dot-matrix drawing: a grid of white dots on black, with a dot wherever the picture has an edge. The look is similar to the point-array artwork on the Deftones album *Ohms*.

It is written in Processing, a free tool for writing programs that make pictures. It finds the edges with OpenCV, a widely used library for computer vision (programs that analyse images).

## What you can learn from it

- How edge detection finds outlines in a photo by looking for sudden changes in brightness (Computer Science).
- How an image is a grid of pixels, and how sampling every tenth pixel shrinks it (Computer Science).
- How a picture can be rebuilt from simple shapes, the idea behind halftone printing and pixel art (Art and Design).
- How nested loops visit every cell in a grid (Computer Science).

## Run it

### On your own computer

**You will need:**

- [Processing](https://processing.org/download). The old README says Processing 3 or later.
- [OpenCV for Processing](https://github.com/atduskgreg/opencv-processing), a library you add inside Processing.

This has not been tested on a specific Processing version or operating system.

1. On the repository page, choose **Code**, then **Download ZIP**, and unzip it.
2. Rename the unzipped folder to `deftones`. Processing needs the folder name to match the `.pde` file name.
3. Open Processing. Choose **Sketch**, then **Import Library**, then **Manage Libraries**. Search for "OpenCV for Processing" and install it.
4. Choose **File**, then **Open**, and pick **deftones.pde**.
5. Press the **Run** button (the triangle at the top left).

A 1000 by 1000 pixel black window opens and fills with white dots in the shape of the input image's edges. The default input is `cicada.jpg`, a picture of insect wings.

To use your own picture, put a JPEG in the same folder and change the `filename` variable near the top of `deftones.pde`. Leave off the `.jpg` ending: the code adds it.

The sketch has no keyboard or mouse controls.

## How it works

1. The sketch loads an image (`cicada.jpg` by default).
2. It runs a Canny edge detector through OpenCV. Canny is a standard method. It labels a pixel as an edge when brightness changes sharply around it. The two numbers in `findCannyEdges(20,75)` are the low and high thresholds.
3. It stretches the edge map to 1000 by 1000 pixels and keeps every tenth pixel, which reduces it to a 100 by 100 grid.
4. It draws a circle wherever the reduced pixel is bright enough.

| File | What is in it |
|---|---|
| `deftones.pde` | The whole sketch |
| `cicada.jpg` | The default input image |
| `doge.jpg` | A second input image, not used by default |

## Ideas to try

1. In `deftones.pde`, change `ellipseSize` for bigger or smaller dots, or `intervalCount` for a denser or sparser grid.
2. Try the second image. In `deftones.pde`, change `filename` from `"cicada"` to `"doge"`.
3. Change the edge thresholds. In `deftones.pde`, try other values in `findCannyEdges(20,75)`. Lower numbers find more edges.
4. Colour the dots. Before the `ellipse` call in `draw`, add a `fill` call that takes its colour from the original image `img` at the same position.
5. Save the result. Add a `keyPressed` function to `deftones.pde` that calls `saveFrame()` when you press `s`.

## Technical details

Parameters at the top of `deftones.pde`:

```java
int intervalCount = 100;   // grid density
int ellipseSize   = 7;     // dot size
int marginSize    = 60;    // margin around the grid
```

`draw` loops from `marginSize` to `width - marginSize` in steps of `width / intervalCount`. With the default values that is 88 steps in each direction, so the sketch uses the top-left 88 by 88 cells of the 100 by 100 grid. The margin crops the right and bottom of the picture instead of shrinking it.

The image is resized to a square before sampling, so a picture that is not square gets stretched.

## Project status

This is a small experiment with no tests. Known problems:

- `cicada.jpg` is a stock photo preview that still carries the stock site's watermark. It is unlikely to be covered by this repository's MIT licence. Use your own image if you share your results.
- The margin crops the image (see "Technical details").
- The sketch redraws the same dots every frame. It could draw once in `setup` instead.

## Licence

You can use, copy and change the code for any purpose, as long as you keep the copyright notice. See [LICENSE](LICENSE) (MIT). The licence covers the code. The example images may belong to other people.

## Credits

Written by Abhishek Shivakumar. Built with [Processing](https://processing.org/) and [OpenCV for Processing](https://github.com/atduskgreg/opencv-processing) by Greg Borenstein. The style is inspired by the artwork for the Deftones album *Ohms*. To cite this work, see [CITATION.cff](CITATION.cff).
