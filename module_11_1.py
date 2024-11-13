import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageFilter


with Image.open('photo_osen.jpg', 'r') as img:
    img.load()
    print(type(img))
    print(img.format, img.size, img.mode, img.width, img.height )
    img.show()
    img_low = img.resize((img.width//4, img.height//4))
    print('new_size =', img_low.size)
    img_low.save('mini_osen.png')
    img_low.show()

with Image.open('photo_DS.jpg', 'r') as img:
    img.load()
    print(img.format, img.size, img.mode)
    cropped_img = img.crop((255,315,825,770))
    print(cropped_img.size)
    cropped_img.show()
    cropped_img.save('logotype.jpg')
    low_img = cropped_img.reduce(2)
    emboss = low_img.filter(ImageFilter.EMBOSS)
    emboss.save('grey_logo.jpg')
    emboss.show()
    rotate_img = low_img.rotate(45, expand=True)
    rotate_img.show()

# with Image.open('photo_bokal.jpg', 'r') as img:
#     img.load()
#     print('количество слоев: ', img.getbands())
#     red, green, blue = img.split()
#     zeroed_band = red.point(lambda _:0)
#     red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
#     red_merge.show()
#     green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
#     green_merge.show()
#     blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
#     blue_merge.show()


x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y, 'g--',linewidth=2)
plt.plot(x,y2, 'r-.')
plt.plot(x,y3, color='#87a3cc', linestyle='--')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1, 0, 1, 2, 3],
           [r'$-1$', r'$0$',r'$+1$',r'$+2$',r'$+3$'])

plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}= 1$', xy=[0,1],xycoords='data',
             xytext=[30,30],fontsize=16, textcoords='offset points', arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()

data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([0,4,0,7])
plt.plot(x,df)
plt.legend(data, loc=2)
plt.show()

xx = np.array([range(0, 20)])
xx.resize(4,5)
print(xx)
print('Сумма элементов =', xx.sum(), 'минимальный элемент =', xx.min(), 'максимальный элемент =', xx.max())