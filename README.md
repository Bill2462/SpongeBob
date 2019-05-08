 # Sponge Bob
 Calculate porosity by processing microscopic images using openCV.
 
 ### Instalation
 ```
 python3 setup.py dist_wheel
 cd dist
 pip3 install --upgrade spongeBob-0.1-py3-none-any.whl
 ```
 
 ### Usage
 ```
 spongeBob [-h] --output-file OUTPUT_FILE dataInput
 ```
 As a dataInput program takes:
  - Path to a directory containing images.
  - Path to a image file. 

Program can save results into a CSV file. Option --output-file takes a path to this file.

Example:
```
python3 -m spongeBob /home/patrik/porositySamples --output-file=/home/patrik/porosity.csv
```
 
Example output:
```
6 images detected in '/home/patrik/porosity'
Loading file /home/patrik/porosity/8bars - center.jpg ...
Loading file /home/patrik/porosity/8bars - edge.jpg ...
Loading file /home/pqtrik/porosity/12bars - center.jpg ...
Loading file /home/patrik/porosity/12bars - edge.jpg ...
Loading file /home/patrik/porosity/15bars - center.jpg ...
Loading file /home/patrik/porosity/15bars - edge.jpg ...
Processing image '/home/patrik/porosity/8bars - center.jpg' ...
Porosity: 39.35546875%
Processing image '/home/patrik/porosity/8bars - edge.jpg' ...
Porosity: 48.59822591145833%
Processing image '/home/patrik/porosity/12bars - center.jpg' ...
Porosity: 45.508544921875%
Processing image '/home/patrik/porosity/12bars - edge.jpg' ...
Porosity: 40.063313802083336%
Processing image '/home/patrik/porosity/15bars - center.jpg' ...
Porosity: 38.288167317708336%
Processing image '/home/patrik/porosity/15bars - edge.jpg' ...
Porosity: 25.493896484375%
Exporting results to /home/patrik/output.csv ...
 ```
 
Example csv output file:

| filename	                                | porosity           |
| ---------------------------------------- | ------------------ |
| /home/patrik/porosity/8bars - center.jpg	 | 39.35546875        |
| /home/patrik/porosity/8bars - edge.jpg	   | 48.59822591145833  |
| /home/patrik/porosity/12bars - center.jpg | 45.508544921875    |
| /home/patrik/porosity/12bars - edge.jpg	  | 40.063313802083336 |
| /home/patrik/porosity/15bars - center.jpg	| 38.288167317708336 |
| /home/patrik/porosity/15bars - edge.jpg	  | 25.493896484375    |
