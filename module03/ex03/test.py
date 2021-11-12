from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
from copy import deepcopy

imp = ImageProcessor()
cf = ColorFilter()

arr = imp.load("./musk.png")

bckp = deepcopy(arr)


inv = cf.invert(deepcopy(arr))
imp.display(inv)

bl = cf.to_blue(deepcopy(arr))
imp.display(bl)

gr = cf.to_green(deepcopy(arr))
imp.display(gr)


re = cf.to_red(deepcopy(arr))
imp.display(re)

# ce = cf.to_celluloid(deepcopy(arr))
# imp.display(ce)

gr = cf.to_grayscale(deepcopy(arr),)
print(gr)
imp.display(gr)

gr = cf.to_grayscale(deepcopy(arr),'m')
print(gr)
imp.display(gr)