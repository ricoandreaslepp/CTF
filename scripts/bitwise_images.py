import cv2
import sys

i1 = cv2.imread(sys.argv[1],0)
i2 = cv2.imread(sys.argv[2],0)

bwa = cv2.bitwise_and(i1,i2)
bwo = cv2.bitwise_or(i1,i2)
bwx = cv2.bitwise_xor(i1,i2)

cv2.imshow("Bitwise AND", bwa)
cv2.imshow("Bitwise OR", bwo)
cv2.imshow("Bitwise XOR", bwx)
cv2.waitKey(0)
cv2.destroyAllWindows()
