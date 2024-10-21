import random

""" Banania 3000 """

#------------------------------------------------------------------------------#
# Paths
#------------------------------------------------------------------------------#

ressources_p = "images/"
out_svg_p = "monkey.svg"

basic_phenos_p = [
 "Tail.xml",
 "Legs.xml",
 "Arms.xml",
 "BodyUpper.xml",
 "FootLeft.xml",
 "FootRight.xml",
 "Ears.xml",
 "Face.xml",
 "HandRight.xml",
 "HandLeft.xml",
 "Eyes.xml",
 "Nose.xml"
 ]

hats_p = [
    None,
    "CapBackwards.xml",
    "CapBanano.xml",
    "CapBebe.xml",
    "CapCarlos.xml",
    "CapHngPlus.xml",
    "CapHng.xml",
    "CapKappa.xml",
    "CapPepe.xml",
    "CapRick.xml",
    "CapSmugGreen.xml",
    "CapSmug.xml",
    "CapThonk.xml",
    "Cap.xml",
    "Crown.xml",
    "HatCowboy.xml",
    "HatJester.xml",
    "HelmetViking.xml",
    "BeanieBanano.xml",
    "BeanieHippie.xml",
    "BeanieLongBanano.xml",
    "BeanieLong.xml",
    "Beanie.xml"
]

glasses_p = [
    None,
    "SunglassesAviatorCyan.xml",
    "SunglassesAviatorGreen.xml",
    "SunglassesAviatorYellow.xml",
    "SunglassesThug.xml",
    "GlassesNerdCyan.xml",
    "GlassesNerdGreen.xml",
    "GlassesNerdPink.xml"
]

mouths_p = [
    None,
    "SmileBigTeeth.xml",
    "SmileNormal.xml",
    "SmileTongue.xml",
    "Confused.xml",
    "Meh.xml"
]

#------------------------------------------------------------------------------#
# Utils functions
#------------------------------------------------------------------------------#

def import_pheno(ressource_p, pheno):
    pheno_p = ressource_p + pheno
    pheno_s = open(pheno_p, 'r')
    pheno_svg = pheno_s.readline()
    filtered_pheno = pheno_svg[pheno_svg.find('>')+1:pheno_svg.rfind('<')]
    pheno_s.close()
    return filtered_pheno

#------------------------------------------------------------------------------#
# Add basic phenotypes
#------------------------------------------------------------------------------#
rand_color = "#"+"%06x" % random.randint(0, 0xFFFFFF)
out_data = ['<svg fill="none" height="4000" viewBox="0 0 4000 4000" width="4000" xmlns="http://www.w3.org/2000/svg">']

for pheno in basic_phenos_p:
    pheno_val = import_pheno(ressources_p, pheno)
    pheno_val = pheno_val.replace("#7f6145", rand_color)
    pheno_val = pheno_val.replace("#7F6145", rand_color)
    out_data.append(pheno_val)

#------------------------------------------------------------------------------#
# Add random phenotypes
#------------------------------------------------------------------------------#
for pheno_lst in [hats_p, glasses_p, mouths_p]:
    rand_idx = random.randint(0,len(pheno_lst)-1)
    pheno = pheno_lst[rand_idx]
    # if pheno is none, just do nothing
    if pheno: out_data.append(import_pheno(ressources_p, pheno))

#------------------------------------------------------------------------------#
# Save phenotypes
#------------------------------------------------------------------------------#
out_svg_s = open(out_svg_p, 'w')
for line in out_data:
    out_svg_s.write(line)
out_svg_s.write('</svg>')
out_svg_s.close()