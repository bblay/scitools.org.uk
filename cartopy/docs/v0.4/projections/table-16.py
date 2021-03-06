import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(5.91496652704, 3))
delta = 0.125
ax = plt.axes([0+delta, 0+delta, 1-delta, 1-delta], projection=ccrs.Robinson())
#ax.set_global()
ax.coastlines()
ax.gridlines()