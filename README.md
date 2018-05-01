# Ray Tracing in One Weekend
This repository is an implementation of Peter Shirley's book *Ray Tracing in One Weekend* as implemented in Python 3.

# Note on implementation
After getting half way through chapter 5, I realized that performance was going to be an issue with my naive implementation.
As a result, I decided to change things. The implementation half way through chapter 5 would take ~21 seconds for a 400 x 200 image.
I found a [nice blog post](http://excamera.com/sphinx/article-ray.html) which explained and linked to [this code](https://github.com/jamesbowman/raytrace/blob/master/rt3.py), which suggested that an implementation more friendly to numpy arrays would have significant performance benefits. After implementing those changes, the same functionality ran in about 875 ms for a 2000x1000 image. This represents around a 600x speedup, plus it means the implementation should be amenable to CUDA-based numpy acceleration if such a thing exists.