import pyfits
import numpy as np, matplotlib,os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
lenses=pyfits.open("knownlenses.fits")
uvx=pyfits.open("DR8_UVX_10sig.fits")

lsdss=lenses[1].data['sdss']
ltype=lenses[1].data['sdss_type']
lextent=lenses[1].data['mean']-lenses[1].data['mean_ap']

usdss=uvx[1].data['sdss']
utype=uvx[1].data['sdss_type']
uextent=uvx[1].data['mean']-uvx[1].data['mean_ap']

uvx= ( lsdss[:,0]-lsdss[:,1] < 0.6 ) & ( lsdss[:,0]-lsdss[:,1] > -0.4 )\
  &  ( lsdss[:,1]-lsdss[:,2] < 0.7 ) & ( lsdss[:,1]-lsdss[:,2] > -0.5 )\
  &  ( lsdss[:,2]-lsdss[:,3] < 0.4 ) & ( lsdss[:,2]-lsdss[:,3] > -0.4 )
hzq = ~gal
plt.scatter(lsdss[:,1][uvx]-lsdss[:,2][uvx],lsdss[:,0][uvx]-lsdss[:,1][uvx]); plt.scatter(lsdss[:,1][hzq]-lsdss[:,2][hzq],lsdss[:,0][hzq]-lsdss[:,1][hzq],c='r'); plt.fill([-0.5,-0.5,.7,.7], [0.6,-0.4,-0.4,0.6], 'b', alpha=0.2, edgecolor='k'); plt.fill([0.0,0.0,.2,.2], [1.5,0.6,0.6,1.5], 'r', alpha=0.2, edgecolor='k'); plt.xlabel('g-r'); plt.ylabel('u-g'); plt.savefig("knownlenses_ug_gr.png"); plt.clf()

xs=np.arange(-1,1,.01)
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_zx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_rx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,2][uvx],lextent[:,1][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,2][hzq],lextent[:,1][hzq],c='r'); plt.xlabel('i extent'); plt.ylabel('r extent'); plt.savefig("knownlenses_rx_ix.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,3][uvx],lextent[:,2][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,3][hzq],lextent[:,2][hzq],c='r'); plt.xlabel('z extent'); plt.ylabel('i extent'); plt.savefig("knownlenses_ix_zx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,4][uvx],lextent[:,3][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,4][hzq],lextent[:,3][hzq],c='r'); plt.xlabel('y extent'); plt.ylabel('z extent'); plt.savefig("knownlenses_zx_yx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,4][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,4][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('y extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_yx.png"); plt.clf()


gal=utype==3; star=utype==6
plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx],c='n'); plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='g'); plt.plot(xs,xs,'k'); plt.scatter(uextent[:,3][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,3][star],uextent[:,0][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('z extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_zx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,1][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,1][star],uextent[:,0][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_rx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,2][gal],uextent[:,1][gal],alpha=0.002); plt.scatter(uextent[:,2][star],uextent[:,1][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('i extent'); plt.ylabel('r extent'); plt.savefig("uvx_rx_ix.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,3][gal],uextent[:,2][gal],alpha=0.002); plt.scatter(uextent[:,3][star],uextent[:,2][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('z extent'); plt.ylabel('i extent'); plt.savefig("uvx_ix_zx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,4][gal],uextent[:,3][gal],alpha=0.002); plt.scatter(uextent[:,4][star],uextent[:,3][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('y extent'); plt.ylabel('z extent'); plt.savefig("uvx_zx_yx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,4][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,4][star],uextent[:,0][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('y extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_yx.png"); plt.clf()

xmin=16;xmax=22; nbins=60
np.arange(16.05,22,.1)
[hist,edges]=np.histogram(zs,bins=nbins,range=(xmin,xmax))
plt.subplot(111,yscale="log")
plt.rcParams['font.size'] = 18
plt.xlim((xmin,xmax))
plt.ylim((100,100000))
plt.plot(bins,10.0*hist,'k-')
plt.axvline(color='k',x=20.7,ls='dashed')
plt.xlabel('mag z')
plt.ylabel('N(mag)')
plt.savefig(outname)
plt.clf()

