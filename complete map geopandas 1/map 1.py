import geopandas as gpd
import matplotlib.pyplot as plt 
from matplotlib_scalebar.scalebar import ScaleBar
import matplotlib.patches as mpatches 

#load shapefile
shapefile_path="counties/counties.shp"
gdf= gpd.read_file(shapefile_path)

#create figure and axes
fig, ax =plt.subplots(figsize=(10,8))

# plot shapefile on ax
gdf.plot(ax=ax, edgecolor="black", facecolor="lightblue")

#title
plt.title("kenya boundaries", fontsize=14, fontweight="bold")

#labels
plt.xlabel("longitude")
plt.ylabel("latitude")

#grindlines
ax.grid(True,linestyle="--", alpha=0.5)

#scalebar
scalebar = ScaleBar(1,location="lower right")#1 means data units in degreeAx.add_artist(scalebar)

#north arrow
x,y, arrow_length=0.9,0.98,0.06
ax.annotate("N",xy=(x,y), xytext=(x,y-arrow_length),
   arrowprops=dict(facecolor="black",width=5, headwidth=15),
   ha="center",va="center",fontsize=12,
   xycoords=ax.transAxes)

#legend
counties_patch= mpatches.Patch(color="lightblue", label="kenya county boundaries")
ax.legend(handles=[counties_patch],loc="lower left")
plt.show()




