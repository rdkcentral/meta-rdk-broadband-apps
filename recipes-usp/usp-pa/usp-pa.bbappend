TARGET_CFLAGS  += " -DINCLUDE_LCM_DATAMODEL "

do_install:append() {
    sed -i '/ExecStartPre=.*current_wan_state.*sleep 1.*done/d' ${D}${systemd_system_unitdir}/usp-pa.service
}
