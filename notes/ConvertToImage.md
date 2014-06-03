# How to convert the HTML ASCII file to a JPEG image?

For Mac OSX, check out the below program:
https://github.com/paulhammond/webkit2png

For Linux, check out the below program:
https://github.com/adamn/python-webkit2png


Both of the above solutions use webkit engine to render HTML and save as image file. The OSX program needs "pyobjc" library, while the linux program already has a good installation guide.

You could try to put all the html under a folder, and use the ```convert.sh``` script as below:

```bash

#!/bin/bash

for file in $1
do
    filename=$(basename "$file")
    filename=${filename%.*}
    webkit2png $file -o convert/$filename.jpg
done

```

```find <gallery>/ -name "*.html" -exec convert.sh {} \; -print```

