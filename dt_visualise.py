import matplotlib.pyplot as plt
import numpy as np

def show(model, X, y, ax):
    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, clim=(y.min(), y.max()), zorder=3)
    ax.axis('tight')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    model.fit(X, y)
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200),
                         np.linspace(*ylim, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    n_classes = len(np.unique(y))
    contours = ax.contourf(xx, yy, Z, alpha=0.3, levels=np.arange(n_classes + 1) - 0.5, zorder=1)
    ax.set(xlim=xlim, ylim=ylim)
    return ax