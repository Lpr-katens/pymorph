"""Configure file for PyMorph. Authors: Vinu Vikram, Yogesh Wadadekar and Ajit Kembhavi (IUCAA) 2008, Alan Meert (UPenn)"""
###----Specify the input images and Catalogues----###
imagefile = 'tot.fits'
whtfile = 'tot_rms.fits'
#whtfile = 'j8f643-1-1_drz_rms.fits'   #The weight image. If it contains the 
                                      #string 'rms', this will treated as 
				      #RMS_MAP and if it contains weight, then 
                                      #that will be treated as WEIGHT_MAP. 
				      #If nothing found, then by default it 
				      #is treated as MAP_RMS 
sex_cata = 'test.cat'           #The sextractor catalogue which has 
                                      #the format given in the file
clus_cata = 'input.cat'         #catalogue of galaxies from
                                      #online catalogu service
                                      #(name ra1 ra2 ra2 dec1 dec2 dec3)

datadir = '~/git_projects/pymorph/examples/full_image/data/'
				       #the directory containing input images
                                       #if commented out, then program uses
                                       # current directory

###----Specify the output names of images and catalogues----###
out_cata = 'out.cat'      #catalogue of galaxies in the field
rootname = 'test'

outdir = '~/git_projects/pymorph/examples/full_image/results/'
					#the directory containing output data
                                        #if commented out, then program uses
                                        # current directory

###----Psf list----###
psfselect = 0                         #0 => No psfselection
                                      #1 => Only Select psf 
                                      #2 => Select psf and run pipeline
                                      #Recommended: Run with '1' and then run
                                      #pipeline
starsize = 20                         #psf image size will be startsize times 
                                      #the SMA given by SExtractor
#psflist = ['psf_1216382-1200443.fits', 'psf_1216408-1200251.fits', 'psf_1216424-1202057.fits','psf_1216487-1201246.fits','psf_1216504-1202104.fits']   
psflist = ['psf_1447282+0829523.fits']
#psflist = '@psflist.list'
                                      #List of psf containg their 
                                      #position information in the 
                                      #header (RA_TARG, DEC_TARG). 
                                      #Make psf with the names as here 
                                      #and use psf_header_update.py. 
                                      #It will update the header information.
mag_zero = 22.5                     #magnitude zero point

###----Conditions for Masking----###
manual_mask = 0
mask_reg = 2.0
thresh_area = 0.2
threshold = 3.0                       #Masking will be done for neighbours 
                                      #whose semimajor*threshold overlaps with 
                                      #threshold * semi-major axis of 
                                      #the object and area of the neighbour 
                                      #less than thresh_area * object area in
                                      #sq.pixel. 
                                      #The masking will be for a circular 
                                      #region of radius mask_reg*semi-major 
                                      #axis of the nighbour with respect to 
                                      #the center of the neightbour.

###---Size of the cut out and search conditions---###
###---size = [resize?, varsize?, fracrad, square?, fixsize]---###
size = [1, 1, 9, 1, 240]              #size of the stamp image
searchrad = '0.3arc'                    #The search radius  

###----Parameters for calculating the physical parameters of galaxy----###
pixelscale = 0.396                    #Pixel scale (arcsec/pixel)
H0 = 71                               #Hubble parameter
WM = 0.27                             #Omega matter
WV = 0.73                             #Omega Lambda

###----Parameters to be set for calculating the CASGM----###
back_extraction_radius = 15.0
back_ini_xcntr = 32.0 
back_ini_ycntr = 22.0
angle = 180.0

###----Fitting modes----###
repeat = False				#Repeat the pipeline manually
galcut = False #True if we provide cutouts
decompose = True
detail = False #Detailed fitting
galfit = True #Always keep this True as it is not functional yet!
cas = True
findandfit = 0
maglim = [22, 14] #if findandfit= 1, then maglim = [faint_mag, bright_mag]
stargal = 0.6 #Star-galaxy classification 
crashhandler = 0

###---Galfit Controls---###
components = ['bulge', 'disk']        #The components to be fitted to the object
devauc = False # set to False to fit sersic bulge, set to true to fit devacouler's bulge (n = 4)

###---fixing = [bulge_center, disk_center, sky]
fitting = [1, 1, 0]                    # = 0, Fix params at SExtractor value

###----Set the SExtractor and GALFIT path here----###
GALFIT_PATH = '~/SOFTWARE/galfit/galfit'
SEX_PATH = '/usr/bin/sextractor'
PYMORPH_PATH = '~/git_projects/pymorph/pymorph/'
#galfitv = '3.0.4'
galfitv = '2.0'

###----The following conditions are used to classify fit goo/bad----###
chi2sq = 1.9                          #< chi2sq
Goodness = 0.60                       #> Goodness
center_deviation = 3.0                #< abs(center - fitted center)
center_constrain = 2.0                #Keep center within +/- center_constrain

###----Database Informations----###
host = 'localhost'
database = 'Junk'
table = 'junk'
usr = 'vinu'
pword = 'cluster'
dbparams = ['Cluster:cl1216-1201', 'ObsID:1:int']
