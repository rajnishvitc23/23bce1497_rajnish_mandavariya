import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(16,10))

def draw_layer(x, y, w, h, title, color):
    layer = Rectangle((x,y), w, h, linewidth=2, edgecolor='black', facecolor=color, alpha=0.15)
    ax.add_patch(layer)
    ax.text(x+w/2, y+h-0.3, title, ha='center', va='top', fontsize=12, fontweight='bold')

def draw_box(x, y, w, h, text):
    box = Rectangle((x,y), w, h, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(box)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=10, wrap=True)

def arrow(x1,y1,x2,y2):
    ax.annotate("", xy=(x2,y2), xytext=(x1,y1), arrowprops=dict(arrowstyle="->", linewidth=1.5))

# ---------------- LAYERS ----------------

draw_layer(0.5,7,15,2,"Client Layer","#4A90E2")
draw_layer(0.5,5,15,1.5,"Application Layer","#2ECC71")
draw_layer(0.5,3.5,15,1.3,"Real-Time Update Layer","#F5A623")
draw_layer(0.5,1.2,15,1.8,"Data Layer","#9B59B6")

# ---------------- CLIENT COMPONENTS ----------------

draw_box(1,7.6,2,0.7,"User")
draw_box(3.5,7.6,4,0.7,"Web App\n(Frontend Interface)")
draw_box(8.5,7.6,4,0.7,"Map Visualization\n(Google Maps / Map UI)")
draw_box(13,7.6,2,0.7,"Admin Dashboard")

# ---------------- APPLICATION COMPONENTS ----------------

draw_box(6,5.4,4,0.8,"Backend API Server\n(Node.js / Express)")
draw_box(11,5.4,3,0.8,"Authentication\n& Access Control")

# ---------------- REAL TIME LAYER ----------------

draw_box(5.5,3.7,5,0.8,"Real-Time Location Update Handler\n(Location Processing Service)")

# ---------------- DATA LAYER ----------------

draw_box(1,1.7,3.5,0.8,"MongoDB\n(Bus Data, Routes,\nGPS Coordinates)")
draw_box(5.5,1.7,3.5,0.8,"GPS Devices / Bus\nLocation Simulator")
draw_box(10,1.7,3.5,0.8,"System Logs\nMonitoring")

# ---------------- ARROWS ----------------

arrow(3,7.95,3.5,7.95)
arrow(7.5,7.95,8.5,7.95)
arrow(12.5,7.95,13,7.95)

arrow(6,7.6,6,6.2)
arrow(8,7.6,8,6.2)

arrow(8,5.4,8,4.5)
arrow(8,4.5,8,3.7)

arrow(8,3.7,3,2.5)
arrow(8,3.7,7.3,2.5)
arrow(8,3.7,11.5,2.5)

# ---------------- SETTINGS ----------------

ax.set_xlim(0,16)
ax.set_ylim(1,9.5)
ax.axis('off')

plt.title("Real-Time Bus Tracking System Architecture", fontsize=16, fontweight='bold')

plt.savefig("bus_tracking_architecture.png", dpi=300, bbox_inches="tight")
plt.show()