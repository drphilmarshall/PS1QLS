# ======================================================================

import numpy,pyfits,sys,os

import om10, PS1QLS

# ======================================================================

def simulator():
    """
    NAME
        simulator

    PURPOSE
        Read in the OM10 mock lens catalog, CFHTLS LRG catalog, and 
        Stripe 82 variability catalog, and make a simulated lens catalog
        for PS1QLS. 

    COMMENTS

    INPUTS
        $OM10_DIR/data/qso_mock.fits 
        $PS1QLS_DIR/PROJECTS/SIMS/lenses/CFHTLS_LRGs_2013-07-29.txt
        $PS1QLS_DIR/PROJECTS/SIMS/sources/SDSS+PS1_Quasars_2013-08-19.txt 
    
    BUGS
      This is half baked code - most of the subroutines that are called do 
      not yet exist!
    
    DEPENDENCIES
      
      OM10 - https://github.com/drphilmarshall/OM10
    
    AUTHORS
      This file is part of the PS1QLS project.

    HISTORY
      2013-09-27  Started Marshall (KIPAC)
    """
    # ------------------------------------------------------------------

    # Read in OM10 lens catalog:
    
    om10catalog = os.path.expandvars("$OM10_DIR/data/qso_mock.fits")
        
    lensdb = om10.DB(catalog=om10catalog)
    
    # Select a mock sample lenses detectable with P1 in the 3pi survey:

    lenses = lensdb.select_random(maglim=21.4,area=30000.0,IQ=1.0)
    if lenses is not None: 
        print "Selected ",len(lenses.LENSID)," OM10 lenses"
        
    # ------------------------------------------------------------------

    # Input LRG list:
    LRGcatalog = os.path.expandvars("$PS1QLS_DIR/PROJECTS/SIMS/lenses/CFHTLS_LRGs_2013-07-29.txt")
    # Output LRG list:
    LRGsimcatalog = os.path.expandvars("$PS1QLS_DIR/PROJECTS/SIMS/lenses/CFHTLS_LRGs_2013-07-29_selected-for-sims.txt")
    # Output sim catalog:
    simcatalog = os.path.expandvars("$PS1QLS_DIR/PROJECTS/SIMS/sims.txt")

    # Start output catalogs:
    PS1QLS.write_LRG_header(LRGsimcatalog)
    PS1QLS.write_sim_header(simcatalog)

    # Read in LRGs as a multi-dimensional array:
    LRGdb = PS1QLS.read_LRGs(LRGcatalog)

    # Loop over lenses, finding an LRG for each one:

    for id in lenses.LENSID:

       lens = lensdb.get_lens(id)

       LRG = PS1QLS.match_LRG(LRGdb,lens)

       print "OM10 lens ",lens.LENSID," has zd,i = ",lens.ZLENS,lens.APMAG_I
       print "Found matching CFHTLS LRG with zd,i = ",LRG.z,LRG.mag_i

       PS1QLS.write_LRG(LRGsimcatalog,LRG)

       print "LRG is at RA,dec = ",LRG.ra, LRG.dec

       for i in range(lens.NIMG):

           dra = -lens.XIMG[i]
           ddec = lens.YIMG[i]
           print "Image ",i," is ",lens.XIMG[i],lens.YIMG[i]," from LRG"
           IMGra,IMGdec = PS1QLS.apply_radec_offset(LRG.ra,LRG.dec,dra,ddec)
           print "  so is at RA,dec = ",IMGra,IMGdec

           PS1QLS.write_sim_line(IMGra,IMGdec,lens,LRG)

    # ------------------------------------------------------------------

    # Make plots!
    
    # 1) Sim lens LRG properties, relative to parent sample.
    
    # 2) Lens system properties: image separations, lens and image mags,
    #     colours etc.

    # ------------------------------------------------------------------

    print "All done."
    
    return
        
# ======================================================================

if __name__ == '__main__':

    simulator()
    
# ======================================================================
