IMAGE_INSTALL:append = "${@ ' ' if d.getVar('RDK_BB_APPS_TOOLKIT_CRUNTIME') == 'LCM' else ' dobby crun readline dsm' }"
