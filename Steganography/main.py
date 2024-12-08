from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from numpy import array, uint8


def open_pic(img):
    file_path = askopenfilename(title = 'Выберите файл', defaultextension='.bmp', filetypes=[(".bmp", ".bmp")])
    if not file_path:
        return img

    img = Image.open(file_path).convert('RGB')

    to_display = ImageTk.PhotoImage(img.resize((250, 250)))
    pic['image'] = to_display
    pic.image = to_display

    return img, ''


def bitmap(img):
    width, height = img.size

    pixels = []
    for h in range(height):
        pixels.append([])
        for w in range(width):
            pixels[-1].append(list(img.getpixel(tuple([w, h]))))
    pixels = array(pixels, dtype = uint8)

    return pixels


def encrypt(img):
    img_mask = 0b11111110
    last_bit = 0b10000000

    if img is None:
        print('open before')
        return img, "open .bmp picture before doing smth."

    width, height = img.size
    pixels = bitmap(img)
    s = text.get()
    if s == '':
        print('Nothing to encrypt.')
        return img, "Nothing to encrypt."
    elif len(s) > height * width // 3 - 1:
        print('Too many symbols.')
        return img, "Too many symbols to encrypt."
    else:
        try:
            s = list(text.get().encode('ascii')) + [0]
        except:
            return img, "Not ascii symbols."

    shape = pixels.shape
    pixels = pixels.ravel()

    i = 0
    while s:
            if (i + 1) % 9 != 0 or i == 0:
                pixels[i] = pixels[i] & img_mask | int((s[0] & last_bit) != 0)
                last_bit >>= 1
            else:
                last_bit = 0b10000000
                s.pop(0)
            i += 1

    pixels.resize(shape)

    encrypted_img = Image.fromarray(pixels)
    return encrypted_img, 'successfully encrypted.'


def decrypt(img):
    if img is None:
        print('open before')

        return img, "open .bmp picture before doing smth."

    last_bit = 0b00000001
    i = 0
    s = 0
    pixels = bitmap(img)

    shape = pixels.shape
    pixels = pixels.ravel()

    i = 0
    enc_text = ''
    symb = ''

    while i < len(pixels) and symb != '\x00':
        if (i + 1) % 9 != 0 or i == 0:
            s += (pixels[i] % 2) << (8 - (i + 1) % 9)
        else:
            enc_text += symb
            symb = chr(s)
            s = 0
        i += 1

    pixels.resize(shape)

    print('text: ', enc_text)
    text.delete(0, END)
    text.insert(0, enc_text)
    return img, enc_text


def save_img(img):
    if img is None:
        print('open before')
        return img, "open .bmp picture before doing smth."

    save_path = asksaveasfilename(title = 'Save file', defaultextension='.bmp', filetypes=[(".bmp", ".bmp")])
    if save_path:
        img.save(save_path)


def message(text):
    if text != '':
        messagebox.showinfo('message', text)


window = Tk()
window.title('Steganography')


class image:
    pass


img = image()
img.img = None
img.img_m = None, ''

Button(window, text="choose picture", command = lambda: setattr(img, 'img_m', open_pic(img.img_m[0]))).pack()

pic = Label(window)
pic.pack()

text = Entry(window, width = 50)
text.pack()

Button(window, text="encrypt", command = lambda: [setattr(img, 'img_m', encrypt(img.img_m[0])), message(img.img_m[1])]).pack(side=LEFT)

Button(window, text="decrypt", command = lambda: [setattr(img, 'img_m', decrypt(img.img_m[0])), message(img.img_m[1])]).pack(side=RIGHT)

Button(window, text="save picture", command = lambda: [save_img(img.img_m[0]), message(img.img_m[1]) ]).pack(side=TOP)

window.mainloop()

