#WPEFramework dependecy is added in dobby.bb, removing that
RDEPENDS_${PN} = ""
#Below flag enables dobby to create run-time containers using json spec
PACKAGECONFIG:append = " legacycomponents"
