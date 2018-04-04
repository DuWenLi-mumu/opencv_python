# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ���Եĵ��ڶԱȶȺ�����
def contrast_brightness_image(src1, a, g):
    h, w, ch = src1.shape   # ��ȡshape����ֵ��height��width��ͨ��

    # �½�ȫ��ͼƬ����src2,��height��width����������ΪԭͼƬ��ͨ������(ɫ��ȫΪ�㣬���Ϊȫ��ͼƬ)
    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1-a, g) # addWeighted����˵������
    cv.namedWindow("�޸ĺ�", cv.WINDOW_NORMAL)
    cv.imshow("�޸ĺ�", dst)

src = cv.imread("1.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)
contrast_brightness_image(src, 1.2, 0)  # ��һ��1.2Ϊ�Աȶ�  �ڶ���Ϊ����
cv.waitKey(0)
cv.destroyAllWindows()