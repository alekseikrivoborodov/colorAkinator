import aggdraw
from PIL import Image
import random
import imageio

def generationGif(color):
    gif_frames = []

    def generationImg(simple_color):
        image = Image.new("RGB", (320, 320), (255, 255, 255))
        draw = aggdraw.Draw(image)
        draw.ellipse((10, 10, 300, 300), aggdraw.Pen(simple_color, 0.5), aggdraw.Brush(simple_color))
        draw.ellipse((8, 8, 302, 302), aggdraw.Pen("black", 0.5))
        draw.rectangle((10, 298, 300, 356), aggdraw.Pen((92, 42, 9), 0.5), aggdraw.Brush((92, 42, 9)))
        draw.flush()
        return image

    for i in range(4):
        image = generationImg((color[0] + random.randint(0, 30),
                               color[1] - random.randint(0, 30),
                               color[2] - random.randint(0, 30)))

        gif_frames.append(image)

    imageio.mimwrite("result.gif", gif_frames, 'GIF', fps=5)


generationGif((100, 100, 100))
