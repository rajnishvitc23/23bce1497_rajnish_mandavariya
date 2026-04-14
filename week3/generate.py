import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(14,10))

def draw_class(x,y,w,h,title,attributes="",methods=""):
    
    box = Rectangle((x,y),w,h,edgecolor='black',facecolor='#f8f8f8')
    ax.add_patch(box)
    
    ax.text(x+w/2,y+h-0.3,title,ha='center',fontsize=11,fontweight='bold')
    
    ax.plot([x,x+w],[y+h-0.6,y+h-0.6],color='black')
    ax.text(x+0.1,y+h-1,attributes,fontsize=9,va='top')
    
    ax.plot([x,x+w],[y+h-2,y+h-2],color='black')
    ax.text(x+0.1,y+h-2.2,methods,fontsize=9,va='top')

def arrow(x1,y1,x2,y2):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="->"))

# Core Classes
draw_class(1,8,3,2.5,"User",
"+userId: String\n+name: String\n+email: String",
"+viewBusLocations()\n+trackBus()\n+viewRoutes()")

draw_class(1,5.5,3,2.5,"Admin",
"+adminId: String",
"+manageRoutes()\n+monitorSystem()\n+viewLogs()")

draw_class(5,8,3,2.5,"Bus",
"+busId: String\n+routeId: String\n+currentLocation",
"+updateLocation()\n+sendGPS()")

draw_class(9,8,3,2.5,"Route",
"+routeId: String\n+startPoint\n+endPoint",
"+getStops()\n+calculatePath()")

draw_class(5,5.5,3,2.5,"GPSDevice",
"+deviceId\n+busId\n+coordinates",
"+sendLocation()")

draw_class(9,5.5,3,2.5,"LocationService",
"+processLocation()",
"+updateBusPosition()")

draw_class(5,3,3,2.5,"BackendAPI",
"+receiveLocation()\n+fetchBusData()",
"+handleRequests()")

draw_class(9,3,3,2.5,"Database",
"+storeRoutes\n+storeLocations",
"+saveData()\n+retrieveData()")

draw_class(5,0.8,3,2.2,"MapInterface",
"+mapView",
"+displayBusMarkers()\n+updatePositions()")

# Relationships
arrow(2.5,8,2.5,7)
arrow(3.8,9,5,9)
arrow(7,9,9,9)
arrow(6.5,8,6.5,6.5)
arrow(10.5,8,10.5,6.5)
arrow(6.5,5.5,6.5,4.2)
arrow(10.5,5.5,10.5,4.2)
arrow(6.5,3,6.5,2)
arrow(6.5,2,10.5,2)

ax.set_xlim(0,13)
ax.set_ylim(0,11)
ax.axis('off')

plt.title("Real-Time Bus Tracking System - Class Diagram",fontsize=14,fontweight='bold')

plt.savefig("class_diagram.png",dpi=300,bbox_inches="tight")
plt.show()