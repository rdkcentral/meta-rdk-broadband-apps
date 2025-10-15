IMAGE_INSTALL:append = "${@ ' lcm' if d.getVar('RDK_BB_APPS_TOOLKIT_CRUNTIME') == 'LCM' else ' dobby crun readline dsm' }"
