# ======================================================================

import PS1QLS

# ======================================================================

def apply_radec_offset(RA,Dec,dRA,dDec):

    from astropy import coordinates as coord
    from astropy import units as u
    
    x = coord.ICRSCoordinates(ra=RA, dec=Dec, unit=(u.degree, u.degree))
    dx = coord.ICRSCoordinates(ra=dRA/3600.0, dec=dDec/3600.0, unit=(u.degree, u.degree))
    
    x2 = coord.ICRSCoordinates(ra=x.ra+dx.ra, dec=x.dec+dx.dec, unit=(u.degree, u.degree))
    
    return x2.ra.degrees, x2.dec.degrees
    
# ======================================================================

if __name__ == '__main__':

    # simulator()
    
    print "Testing offsets:"
    print "Initial RA, dec = (10.68458,41.26917)"
    print "Offset RA, dec  = (10.68472, 41.26945)"
    
    ra,dec = apply_radec_offset(10.68458,41.26917,0.5,1.0)
    print "But: returned values = ", ra,dec
    ra0,dec0 = apply_radec_offset(ra,dec,-0.5,-1.0)
    print "And: going back again = ", ra0,dec0

# ======================================================================


