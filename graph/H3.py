import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 

x = np.array([100, 97, 94, 91, 88, 85, 82, 79, 76, 73, 70])
y1 = np.array([18.4, 18.6, 18.4, 18.6, 18.6, 18.6, 18.6, 18.6, 18.6, 18.6, 0])
x2 = np.array([93, 95, 97, 100])
y3 = np.array([18.6, 18.6, 18.6, 18.4])
y=y1
y2=y3

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
plt.title('Зависимость амплитуды выходного сигнала от М при включенной емкости')
plt.savefig('HH3.pdf',dpi=300)
plt.legend(("прямой", "обратный"))
plt.show()
