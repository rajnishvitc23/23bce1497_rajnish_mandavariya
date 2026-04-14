import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse

fig, ax = plt.subplots(figsize=(10,12))

def activity(x,y,text):
    box = FancyBboxPatch((x,y),3,0.8,
                         boxstyle="round,pad=0.02",
                         edgecolor="black",
                         facecolor="#e6f2ff")
    ax.add_patch(box)
    ax.text(x+1.5,y+0.4,text,ha='center',va='center',fontsize=10)

def start(x,y):
    s = Ellipse((x,y),0.4,0.4,color='black')
    ax.add_patch(s)

def end(x,y):
    e = Ellipse((x,y),0.4,0.4,edgecolor='black',facecolor='white',linewidth=2)
    ax.add_patch(e)

def arrow(x1,y1,x2,y2):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),
                arrowprops=dict(arrowstyle="->"))

# Start
start(3,11)

# Activities
activity(1.5,10,"User Opens Bus Tracking App")
activity(1.5,9,"Load Map Interface")
activity(1.5,8,"Request Bus Location Data")
activity(1.5,7,"Backend API Receives Request")
activity(1.5,6,"Process Request in Location Service")
activity(1.5,5,"Query Bus Data from MongoDB")
activity(1.5,4,"Return Bus Coordinates")
activity(1.5,3,"Update Map with Bus Locations")
activity(1.5,2,"Display Bus Positions to User")

# GPS update cycle
activity(6,6,"Receive GPS Data from Bus Device")
activity(6,5,"Update Bus Location in Database")

# End
end(3,1)

# Flow arrows
arrow(3,10.8,3,10)
arrow(3,9.8,3,9)
arrow(3,8.8,3,8)
arrow(3,7.8,3,7)
arrow(3,6.8,3,6)
arrow(3,5.8,3,5)
arrow(3,4.8,3,4)
arrow(3,3.8,3,3)
arrow(3,2.8,3,2)

# GPS update arrows
arrow(4.5,6.4,6,6.4)
arrow(7.5,6.4,7.5,5.4)
arrow(7.5,5.4,4.5,5.4)

# End arrow
arrow(3,2,3,1.2)

ax.set_xlim(0,10)
ax.set_ylim(0,12)

ax.axis('off')

plt.title("Real-Time Bus Tracking System - Activity Diagram",
          fontsize=14,fontweight='bold')

plt.savefig("activity_diagram.png",
            dpi=300,bbox_inches="tight")

plt.show()