from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

pylab.rcParams['figure.figsize'] = (8.0, 10.0)

annFile = './annotations/person_keypoints_train2017.json'
# 初始化标注数据的 COCO api
coco = COCO(annFile)

imgIds = coco.getImgIds(imgIds=[897])
img = coco.loadImgs(imgIds[0])[0]

catIds = coco.getCatIds(catIds=["person"])

I = io.imread('./train2017/%s' % (img['file_name']))
plt.figure()
plt.imshow(I)
plt.axis('off')

ax = plt.gca()
annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
anns = coco.loadAnns(annIds)
coco.showAnns(anns)
plt.show()
