# GUI-extension
MVP of basic shopping cart activities through graphical interface.

Package Justification:

I decided to use tkinter for the GUI package this project as it's already with Pythons standard library. This meant I didn't need anything external and still had functionality. For just the cart MVP, it only needed to display items, accept quantities, show cart contents, tkinter works for all the requirements. It uses a simple grid layout and runs on any system with python making it suitable for developing and demonstrating.

Another alternative could have been PyQt5, this package would help with more complex or polished styles, a true finished look. This however would need a seporate installation and apparently has a more difficult learning curve. I defaulted to tkinter which I have previously used. PyQt5 seems like it would be overkill on a basic MVP. Staying with tkinter kept it simple and approachable.

Tkinter fit the MVP philosophy since it allowed for quick transition from method creation to a working interface. The grid makes it simple to place items in rows with their images, labels, quantities and adding buttons without resistance. It seems to be easily maintainable.

A limitation I encountered with tkinter was that images only support PNG and GIF formats. It also doesn't have an inbuilt resizing function. If I used a JPEG or vastly different images sizes the GUI would break. I standardised all my images to PNGs and became aware that Pillow could be used for dynamic resizing.