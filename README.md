# Deftones Album Art Creator

A Processing sketch that turns an image into a dot-matrix drawing, similar to the point-array artwork on the Deftones album *Ohms*.

## How it works

1. Loads an image (`cicada.jpg` by default).
2. Runs a Canny edge detector through OpenCV.
3. Reduces the edge map to a 100 x 100 grid.
4. Draws a circle wherever the reduced pixel is bright enough.

## Requirements

- [Processing 3+](https://processing.org/download)
- [OpenCV for Processing](https://github.com/atduskgreg/opencv-processing)

## Run

1. Open `deftones.pde` in Processing.
2. Put a JPEG named `cicada.jpg` in the sketch folder, or change the `filename` variable.
3. Run the sketch.

## Example output

`cicada.jpg` is included as an example input. The script generates a stippled, dot-matrix version of the source image.

## Parameters

```java
int intervalCount = 100;   // grid density
int ellipseSize   = 7;     // dot size
int marginSize    = 60;    // margin around the grid
```

## License

MIT
