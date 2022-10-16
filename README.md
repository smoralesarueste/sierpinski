# Order out of Chaos

Creating one of the most famous fractals by using randomness.
So, you have probably heard about the Sierpinski Triangle. And if you haven't heard about it, you probably have encountered it at some point. 

![The Making of the Sierpinski Triangle](https://user-images.githubusercontent.com/48697836/196031902-75f09497-02bb-46fd-9fcc-a245b56c6090.png)

It feels so in order, full of patterns. But what if we could create such a figure out of pure randomness? 
This is called *The Chaos Game* (you read about it [here](https://en.wikipedia.org/wiki/Chaos_game). The procedure goes as follows: 

1. Choose a point within the starting triangle and mark it. 
2. Randomly choose one of the three corners. 
3. Walk halfway to that corner, and mark the new spot. 
4. Repeat until you get bored. 


That's it. Wait a bit and it will draw itself. No kidding. 
Here you can check a (very) simple code to create a GIF showing how it just magically apperead, and the resulting animation. 

<img src="sierpinski.gif" width="640" height = "640"/>


For me, one of these results that only makes sense once you know the answer. So, why does it happen?
Think about it this way: Can you really draw a point in the big triangle in the middle? Well, yeah, obvioslu, after all, the first point is *randomly* chosen, what if we just pick that area here? Yeah, then you are going to have a point inside this area. But what about afterwards? It is actually **impossible** to get back in there. And guess what happens when you iterate by going repeteadly halfway to the corners. That area in the middle starts to make it impossible to reach its clones as well, growing the *impossible to draw* area right in the same way as the Sierpinski Triangle is defined. 

And just to finish this miniature repo, think about this: The only area which is possible to keep drawing should be the borders of the triangles (the lines *around* the triangles). But this are actually of null area. So how is it possible that that's the only thing we should be seeing? 
