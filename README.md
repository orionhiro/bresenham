    :::::::::  :::::::::  ::::::::::  ::::::::  :::::::::: ::::    ::: :::    :::     :::     ::::    ::::  
    :+:    :+: :+:    :+: :+:        :+:    :+: :+:        :+:+:   :+: :+:    :+:   :+: :+:   +:+:+: :+:+:+ 
    +:+    +:+ +:+    +:+ +:+        +:+        +:+        :+:+:+  +:+ +:+    +:+  +:+   +:+  +:+ +:+:+ +:+ 
    +#++:++#+  +#++:++#:  +#++:++#   +#++:++#++ +#++:++#   +#+ +:+ +#+ +#++:++#++ +#++:++#++: +#+  +:+  +#+ 
    +#+    +#+ +#+    +#+ +#+               +#+ +#+        +#+  +#+#+# +#+    +#+ +#+     +#+ +#+       +#+ 
    #+#    #+# #+#    #+# #+#        #+#    #+# #+#        #+#   #+#+# #+#    #+# #+#     #+# #+#       #+# 
    #########  ###    ### ##########  ########  ########## ###    #### ###    ### ###     ### ###       ### 

## About

Simple implementation of Bresenham Algorithm for lines and circles

## Documentation

To create a line, you need to use the `line()` method and pass in the parameters start and end points of line

```python
import bresenham

points = [(0, 5), (6, 9)]

line_points = bresenham.line(*points) # returns list of points of line

print(line_points)

```

To create a circle, you need to use the `circle()` method and pass in the parameters center and radius of circle(to get a thicker line, pass the third parameter `True`)

```python
center = (10, 10)
radius = 10

circle_points = bresenham.circle(center, radius) # returns list of points of circle

print(circle_points)

```

## Developers

- [Marek](https://github.com/orionhiro)

## License

Project orionhiro.bresenham in distributed under the MIT license
