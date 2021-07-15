import tkinter as tk
from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    try:
        im = Image.open(f'img/{img_entry.get()}')
        width, height = im.size
        draw = ImageDraw.Draw(im)
        text = wm_entry.get()
        font = ImageFont.truetype('arial.ttf', 24)
        textwidth, textheight = draw.textsize(text, font)
        x = width - textwidth - 10
        y = height - textheight - 10
        draw.text((x,y), text, font=font)
        im.show()
        im.save(f'watermarked_img/{img_entry.get()}')
    except FileNotFoundError:
        print("Sorry, there is no image with that name located in the folder, please add it to the folder or try again.")



# UI

window = tk.Tk()
window.title('Watermark Adder')

#Labels

app_label = tk.Label(text='Type in the name of an image to watermark. \nNOTE: If the image name cannot be found in the img folder, it will not be watermarked.')
app_label.grid(column=1, row=0)

image_label = tk.Label(text='Image name (e.g. sky.jpg):')
image_label.grid(column=0, row=1)

wm_label = tk.Label(text='Watermark text:')
wm_label.grid(column=0, row=2)

# Entries

img_entry = tk.Entry(width=30)
img_entry.grid(column=1, row=1)

wm_entry = tk.Entry(width=30)
wm_entry.grid(column=1, row=2)

#Button

mark_button = tk.Button(text='Add watermark', command=add_watermark, width=30)
mark_button.grid(column=1, row=3)

window.mainloop()