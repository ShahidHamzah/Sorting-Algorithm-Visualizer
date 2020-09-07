README:

Sorting Algorithm Visualizer
Creator: Hamzah Shahid

Sorting Algorithm Visualizer is a Python program built in
PyGame to show how different sorting algorithms work. 

link to executable build (found in build folder under sorter.exe):
https://drive.google.com/drive/folders/12917k-jQjuyKFKhNyOaVebPEOEw6WCB_?usp=sharing

INTERFACE:
- When starting the program, a set of buttons, a slider, and a 
row of 10 differently sized bars will appear on the main screen.
- The buttons and slider can be interacted with to produce different 
effects.
- When the data is unsorted, the bars will appear white
- When the data is being processed, some bars will appear red
- When the data is in its correct position, the sorted data will become green

HOW TO USE:
- The 'Bubble Sort', 'Insert Sort', and 'Selection Sort' buttons
will sort the given data. While the program is sorting the data,
no other actions can be performed until the sorting is completed,
but you are able to exit the program normally.

- Note: when the data is sorted, 'Bubble Sort', 'Insert Sort', 
and 'Selection Sort' buttons will not do anything.

- The 'New Data' button will create a new randomized set of bars
that can be sorted. Pressing this button will allow the user to
use the 'Bubble Sort', 'Insert Sort', and 'Selection Sort' buttons
if the data was previously sorted.
- The "Set Size" slider will increase the amount of bars on the screen
when the slider is moved. By default, the slider is set at 10 bars. The 
maximum amount of bars that can be set on the screen is 100.

- Note: moving the 'Set Size' slider will refresh the data, providing a 
new data set for the user to sort.

- Note: increasing the data size will reduce the delay between steps of the 
sorting algorithm to better improve the visualization. A smaller data size
will have a longer delay between steps.
