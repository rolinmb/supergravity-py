import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to simulate the curved spacetime effect (using sine-based curvature)
def curved_spacetime(X, Theta, time):
    # Curvature in both the X and Theta directions, depends on time as well
    curvature = np.sin(X / 2) * np.cos(Theta * np.pi) * np.cos(time / 10)
    return curvature

def update(frame, X, Theta, ax1, ax2, Re_Phi, Im_Phi, Re_surface, Im_surface):
    # Time evolution factor (frame varies the function over time)
    factor = np.sin(frame / 10)  # Example factor for animation effect
    # Simulate the interaction with curved spacetime (curved metric)
    curvature = curved_spacetime(X, Theta, frame)
    # Update the surface for the real part (bosonic field)
    Re_Phi_new = Re_Phi * np.cos(curvature) * factor
    Re_surface._offsets3d = (X, Theta, Re_Phi_new)
    # Update the surface for the imaginary part (fermionic field)
    Im_Phi_new = Im_Phi * np.sin(curvature) * factor
    Im_surface._offsets3d = (X, Theta, Im_Phi_new)
    return Re_surface, Im_surface

if __name__ == '__main__':
    x = np.linspace(-5, 5, 100)  # Bosonic coordinate
    theta = np.linspace(-1, 1, 100)  # Grassmann coordinate
    X, Theta = np.meshgrid(x, theta)
    # Complex superfield: Re(Φ) = sin(X), Im(Φ) = cos(X)
    Re_Phi = np.sin(X)  # Real part of the superfield (bosonic)
    Im_Phi = np.cos(X)  # Imaginary part of the superfield (fermionic)
    fig = plt.figure(figsize=(12, 7))
    ax1 = fig.add_subplot(121, projection='3d')
    Re_surface = ax1.plot_surface(X, Theta, Re_Phi, cmap='viridis', edgecolor='none')
    ax1.set_title("Real Part of Superfield (Bosonic)")
    ax1.set_xlabel("Bosonic Coordinate (x)")
    ax1.set_ylabel("Grassmann Component (θ)")
    ax1.set_zlabel("Re(Φ)")
    ax2 = fig.add_subplot(122, projection='3d')
    Im_surface = ax2.plot_surface(X, Theta, Im_Phi, cmap='inferno', edgecolor='none')
    ax2.set_title("Imaginary Part of Superfield (Fermionic)")
    ax2.set_xlabel("Bosonic Coordinate (x)")
    ax2.set_ylabel("Grassmann Component (θ)")
    ax2.set_zlabel("Im(Φ)")
    ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1),
                        fargs=(X, Theta, ax1, ax2, Re_Phi, Im_Phi, Re_surface, Im_surface),
                        interval=100, blit=False)
    plt.tight_layout()
    plt.show()
