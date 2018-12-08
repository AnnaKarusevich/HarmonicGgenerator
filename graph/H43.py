import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 

x = np.array([20, 25, 30, 40, 42, 44, 45, 46, 47, 48, 50, 54, 56, 58, 60, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 80, 110, 115, 120, 125, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 145, 150, 160, 170, 180])
y1 = np.array([0.2, 0.24, 0.24, 0.44, 0.5, 0.7, 1.08, 1.44, 0.92, 0.68, 0.52, 0.6, 0.68, 0.84, 1.24, 1.6, 2.16, 3.04, 4.16, 3.64, 2.32, 1.84, 1.4, 1.24, 1.08, 0.9, 0.76, 0.7, 0.84, 0.96, 1.24, 1.6, 2.6, 3.08, 3.4])

y=y1/2

# x2 = np.array([])
# y2= np.array([])
# z2 = np.polyfit(x2, y2, 1)
# p2 = np.poly1d(z2)
# xp2 = np.linspace(12,60,2)
# p12 = np.poly1d(np.polyfit(x2, y2, 1))
# plt.errorbar(x, y, xerr=0., yerr=0, c='navy', marker='.', mfc='white', ms=5, fmt='o')
plt.plot(x, y, '.',color='orange')
#plt.plot(xp, p(xp), '-.', color='blue')
plt.plot(x2, y2, '.',color='steelblue')
#plt.plot(xp2, p2(xp2), '-.', color='yellow')
# plt.plot(x2, y2, '.',color='green')
# plt.plot(xp2, p2(xp2), '-.', color='yellow')
# plt.ylim(1800)
# plt.xlim(200)
plt.grid(True)
plt.xlabel('М')
plt.ylabel('Uбэ, B')
plt.title('Зависимость Uк от частоты')
plt.savefig('HH43.pdf',dpi=300)
plt.legend(("прямой", "обратный"))
plt.show()
