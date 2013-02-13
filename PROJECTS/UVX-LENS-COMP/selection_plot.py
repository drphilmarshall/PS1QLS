#!/usr/bin/env python
"""
Produces selection plots for a given sample of candidates and knownlenses.

"""
import sys
if len(sys.argv) != 5:
  print "selection_plot.py candidates knownlenses imin imax"
  print "candidates and knownlenses are taken from Eric's ps1_sdss database"
  print "imin and imax are minimum and maximum SDSS i band magnitudes"
  print "set imin imax to 0 and 0 if you just want to look at everything"
  print "example selection_plot.py DR8_UVX_10sig.fits knownlenses.fits 0 0"
  sys.exit(1)

candidates_s=sys.argv[1]
lenses_s=sys.argv[2]
imin=float(sys.argv[3])
imax=float(sys.argv[4])

import os

# Checking input validity

if (imin >= imax) & (imin != 0):
  print "imax must be greater than imin unless they are both 0."
  sys.exit(1)
if not (os.path.isfile(candidates_s)):
  print candidates_s+" not found."
  sys.exit(1)
if not os.path.isfile(lenses_s):
  print knownlenses_s+" not found."
  sys.exit(1)

#import all the larger libraries
import pyfits, sys
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, pylab

# The one subroutine. pdf2d makes a contour plot in 2d space
def pdf2d(ax,ay,imp,xbins,ybins,smooth,color="grey",style='shaded'):

  from scipy import ndimage

  pylab.xlim([xbins[0],xbins[-1]])
  pylab.ylim([ybins[0],ybins[-1]])

  # npts = int((ax.size/4)**0.5)
  H,x,y = pylab.histogram2d(ax,ay,weights=imp,bins=[xbins,ybins])
  
  H = ndimage.gaussian_filter(H,smooth)
  norm = np.sum(H.flatten())
  H = H * (norm > 0.0) / (norm + (norm == 0.0))
  
  sortH = np.sort(H.flatten())
  cumH = sortH.cumsum()
  # Set contours to show number of objects *outside* the contours
  fracs=[0.3, 0.1, 0.03, 0.01, 0.003, 0.001]
  labels=[]
  lvls=[]
  for f in fracs:
    lvls.append( sortH[cumH>cumH.max()*f].min()  )
    labels.append(str(1-f))

  print "2D histogram: min,max = ",H.min(),H.max()
  print "Contour levels: ",lvls

  if style == 'shaded':

    # Plot shaded areas first:
    for num in range(len(lvls)-1):
      pylab.contourf(H.T,[lvls[num],lvls[num+1]],colors=color,alpha=np.sqrt(fracs[num]),\
                   extent=(xbins[0],xbins[-1],ybins[0],ybins[-1]))
  # endif

  # Always plot outlines:
  CS=pylab.contour(H.T,lvls,colors='black',\
                  extent=(xbins[0],xbins[-1],ybins[0],ybins[-1]))
  plt.clabel(CS,fontsize=10,text=labels)
  return

froot=candidates_s.replace('.fits','')
if imin or imax:
  froot=froot+'_'+str(imin)+'_'+str(imax)

candidates=pyfits.open(candidates_s)
lenses=pyfits.open(lenses_s)

csdss=candidates[1].data['sdss']-candidates[1].data['sdss_dr']
if imin or imax:
  crange=(csdss[:,3]<imax) & (csdss[:,3]>imin)
else:
  crange=np.ones(csdss[:,3].size)>0
ctype=candidates[1].data['sdss_type'][crange]
cextent=candidates[1].data['mean'][crange]-candidates[1].data['mean_ap'][crange]
cmextent=np.max(cextent,axis=1)
cnm=candidates[1].data['nmag_ap_ok'][crange]; cnd=np.sum(cnm, axis=1); cndof=cnd[:]-np.sum((cnm>0), axis=1)
cchi=candidates[1].data['c_chi_t_ap'][crange]*cndof
cns=np.sqrt(2.*cchi)-np.sqrt(2.*cndof-1.)

lsdss=lenses[1].data['sdss']-lenses[1].data['sdss_dr']
if imin or imax:
  lrange=(lsdss[:,3]<imax) & (lsdss[:,3]>imin)
else:
  lrange=np.ones(lsdss[:,3].size)>0
ltype=lenses[1].data['sdss_type'][lrange]
lextent=lenses[1].data['mean'][lrange]-lenses[1].data['mean_ap'][lrange]
lmextent=np.max(lextent,axis=1)
lnm=lenses[1].data['nmag_ap_ok'][lrange]; lnd=np.sum(lnm, axis=1); lndof=lnd[:]-np.sum((lnm>0), axis=1)
lchi=lenses[1].data['c_chi_t_ap'][lrange]*lndof
lns=np.sqrt(2.*lchi)-np.sqrt(2.*lndof-1.)

# Tags for uvx quasars and high z quasars. Also SDSS galaxies versus stars
#uvx= ( lsdss[:,0]-lsdss[:,1] < 0.6 ) & ( lsdss[:,0]-lsdss[:,1] > -0.4 )\
#  &  ( lsdss[:,1]-lsdss[:,2] < 0.7 ) & ( lsdss[:,1]-lsdss[:,2] > -0.5 )\
#  &  ( lsdss[:,2]-lsdss[:,3] < 0.4 ) & ( lsdss[:,2]-lsdss[:,3] > -0.4 )
#hzq = ~uvx
#gal=ctype==3; star=ctype==6

xbins=np.linspace(-0.2,1.4,81)
ybins=np.linspace(-1.0,3,81)
smooth=1
imp=np.ones(len(cmextent))
pdf2d(cmextent,np.log10(cns),imp,xbins,ybins,smooth)
plt.xlabel('Maximum Extent'); 
plt.ylabel(r'n $\sigma$'); 
pylab.scatter(lmextent,np.log10(lns))

pylab.savefig(froot+"_nsig_maxextent.png")
plt.clf()

xmin=0;xmax=1; nbins=20
bins=np.arange(.025,1,0.05)
[lmxdist,edges]=np.histogram(lmextent,bins=nbins,range=(xmin,xmax)); 
[cmxdist,edges]=np.histogram(cmextent,bins=nbins,range=(xmin,xmax)); 
plt.subplot(111,yscale="log"); plt.rcParams['font.size'] = 18; plt.xlim((xmin,xmax)); plt.ylim((1,1000000)); 
plt.plot(bins,cmxdist,'k',drawstyle='steps-mid'); 
plt.plot(bins,1+lmxdist,'k--',drawstyle='steps-mid'); 
h_legend=plt.legend(('UVX Objects','Known Lenses'),prop={'size':14})
plt.xlabel('Maximum Extent'); plt.ylabel('Number per bin'); plt.savefig(froot+"_maxextent.png"); plt.clf()

xmin=-1;xmax=4; nbins=25
bins=10**np.arange(-1,4,.2)
[lnsdist,edges]=np.histogram(np.log10(lns),bins=nbins,range=(xmin,xmax)); 
[cnsdist,edges]=np.histogram(np.log10(cns),bins=nbins,range=(xmin,xmax)); 
plt.subplot(111,yscale="log",xscale="log"); plt.rcParams['font.size'] = 18; plt.xlim((10**xmin,10**xmax)); plt.ylim((1,1000000)); 
plt.plot(bins,cnsdist,'k',drawstyle='steps-mid'); 
plt.plot(bins,1+lnsdist,'k--',drawstyle='steps-mid'); 
h_legend=plt.legend(('UVX Objects','Known Lenses'),prop={'size':14})
plt.xlabel(r'n $\sigma$'); plt.ylabel('Number per bin'); plt.savefig(froot+"_nsig.png"); plt.clf()

xmin=15;xmax=22; nbins=35
bins=np.arange(15.1,22,.2)
[udist,edges]=np.histogram(csdss[:,0],bins=nbins,range=(xmin,xmax)); 
[gdist,edges]=np.histogram(csdss[:,1],bins=nbins,range=(xmin,xmax)); 
[rdist,edges]=np.histogram(csdss[:,2],bins=nbins,range=(xmin,xmax)); 
[idist,edges]=np.histogram(csdss[:,3],bins=nbins,range=(xmin,xmax)); 
[zdist,edges]=np.histogram(csdss[:,4],bins=nbins,range=(xmin,xmax)); 
[idist2,edges]=np.histogram(lsdss[:,2],bins=nbins,range=(xmin,xmax)); 
plt.figure(figsize=(8,10)); plt.subplot(111,yscale="log"); plt.rcParams['font.size'] = 18; plt.xlim((xmin,xmax)); plt.ylim((1,200000)); 
plt.plot(bins,udist,'b',drawstyle='steps-mid'); 
plt.plot(bins,gdist,'g',drawstyle='steps-mid'); 
plt.plot(bins,rdist,'r',drawstyle='steps-mid'); 
plt.plot(bins,idist,'k',drawstyle='steps-mid'); 
plt.plot(bins,zdist,color='grey',drawstyle='steps-mid'); 
plt.plot(bins,idist2+1,'k--',drawstyle='steps-mid'); 
h_legend=plt.legend(('u band','g band', 'r band', 'i band', 'z band', 'i lens'),prop={'size':14},loc=2)

plt.xlabel('mag'); plt.ylabel('Number per bin'); plt.savefig(froot+"_ugriz.png"); plt.clf()

print "Produced:\n"+froot+"_nsig_maxextent.png\n"+froot+"_nsig.png\n"+froot+"_maxextent.png\n"+froot+"_ugriz.png\n"
sys.exit()


# Everything below is antiquated

plt.scatter(lsdss[:,1][uvx]-lsdss[:,2][uvx],lsdss[:,0][uvx]-lsdss[:,1][uvx]); plt.scatter(lsdss[:,1][hzq]-lsdss[:,2][hzq],lsdss[:,0][hzq]-lsdss[:,1][hzq],c='r'); plt.fill([-0.5,-0.5,.7,.7], [0.6,-0.4,-0.4,0.6], 'b', alpha=0.2, edgecolor='k'); plt.fill([0.0,0.0,.2,.2], [1.5,0.6,0.6,1.5], 'r', alpha=0.2, edgecolor='k'); plt.xlabel('g-r'); plt.ylabel('u-g'); plt.savefig("knownlenses_ug_gr.png"); plt.clf()

xs=np.arange(-1,1,.01)
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_zx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_rx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,2][uvx],lextent[:,1][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,2][hzq],lextent[:,1][hzq],c='r'); plt.xlabel('i extent'); plt.ylabel('r extent'); plt.savefig("knownlenses_rx_ix.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,3][uvx],lextent[:,2][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,3][hzq],lextent[:,2][hzq],c='r'); plt.xlabel('z extent'); plt.ylabel('i extent'); plt.savefig("knownlenses_ix_zx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,4][uvx],lextent[:,3][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,4][hzq],lextent[:,3][hzq],c='r'); plt.xlabel('y extent'); plt.ylabel('z extent'); plt.savefig("knownlenses_zx_yx.png"); plt.clf()
plt.plot(xs,xs,'k'); plt.scatter(lextent[:,4][uvx],lextent[:,0][uvx]); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.scatter(lextent[:,4][hzq],lextent[:,0][hzq],c='r'); plt.xlabel('y extent'); plt.ylabel('g extent'); plt.savefig("knownlenses_gx_yx.png"); plt.clf()


plt.plot(xs,xs,'k'); plt.scatter(uextent[:,3][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,3][star],uextent[:,0][star],alpha=0.002,c='r'); plt.scatter(lextent[:,1][uvx],lextent[:,0][uvx],c='brown'); plt.scatter(lextent[:,1][hzq],lextent[:,0][hzq],c='g'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('z extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_zx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,1][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,1][star],uextent[:,0][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('r extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_rx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,2][gal],uextent[:,1][gal],alpha=0.002); plt.scatter(uextent[:,2][star],uextent[:,1][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('i extent'); plt.ylabel('r extent'); plt.savefig("uvx_rx_ix.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,3][gal],uextent[:,2][gal],alpha=0.002); plt.scatter(uextent[:,3][star],uextent[:,2][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('z extent'); plt.ylabel('i extent'); plt.savefig("uvx_ix_zx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,4][gal],uextent[:,3][gal],alpha=0.002); plt.scatter(uextent[:,4][star],uextent[:,3][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('y extent'); plt.ylabel('z extent'); plt.savefig("uvx_zx_yx.png"); plt.clf()
#plt.plot(xs,xs,'k'); plt.scatter(uextent[:,4][gal],uextent[:,0][gal],alpha=0.002); plt.scatter(uextent[:,4][star],uextent[:,0][star],alpha=0.002,c='r'); plt.xlim([-0.1,0.9]);plt.ylim([-0.1,0.7]); plt.axhline(c='k'); plt.axvline(c='k');  plt.xlabel('y extent'); plt.ylabel('g extent'); plt.savefig("uvx_gx_yx.png"); plt.clf()

plt.subplot(111,yscale="log"); plt.rcParams['font.size'] = 18; plt.xlim((0,1)); plt.ylim((1,1000)); 
plt.scatter(lmextent,lns); 
plt.xlabel('Maximum Extent'); 
plt.ylabel(r'n $\sigma$'); 
plt.savefig("uvx_lens_nsig_maxextent.png"); 
plt.clf()

