Drinkme is a microapp for basic image resizing. 

You POST an image and a size, and it resizes the image 
to that size and returns it. not very complicated.

a sample curl session looks like:

  $ curl -X POST  -F "image=@MyImage.jpg" \
    http://drinkme.example.com/resize > thumb.jpg

The default size is 100 pixels. It will scale the image so its 
longest side is at most 100 pixels, while preserving the aspect
ratio. 

You can specify a different size with a 'size' parameter like so:

  $ curl -X POST  -F size=200 -F "image=@MyImage.jpg" \
    http://drinkme.example.com/resize > thumb200.jpg

Drinkme will also make square thumbnails. Ie, it will crop the 
image so its width and height are equal and then scale it to 
the specified size. This is disabled by default but can be 
enabled by sending a non-zero value for the 'square' parameter:

  $ curl -X POST  -F square=1 -F "image=@MyImage.jpg" \
    http://drinkme.example.com/resize > square.jpg

That's pretty much it. Currently only jpg, gif, and png images are
supported. 

Drinkme was developed by Anders Pearson at the Columbia Center For New
Media Teaching and Learning (http://ccnmtl.columbia.edu/). 
