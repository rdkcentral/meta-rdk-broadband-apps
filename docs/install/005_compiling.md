# Compiling & Verifying The Image

!!! danger
    (verify using hello-rdk-app native build, which will be included as part of the toolkit)

This page provides acceptance testing procedures and reference values for validating the RDK Broadband Apps Toolkit on reference hardware.

## Banana Pi R4 with RDK-B 2025q2

=== "DAC"

    ```bash
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ grep -nir "CONFIG_CGROUP_CPUACCT=y" .
    ./.config:144:CONFIG_CGROUP_CPUACCT=y
    ./.config.old:144:CONFIG_CGROUP_CPUACCT=y
    ^C
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ grep -nir "CONFIG_CGROUP_CPUACCT=y" .config
    144:CONFIG_CGROUP_CPUACCT=y
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ grep -nir "CONFIG_IP_NF_RAW" .config
    1128:CONFIG_IP_NF_RAW=m
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ grep -nir "CONFIG_CGROUP_DEBUG" .config
    147:CONFIG_CGROUP_DEBUG=y
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ grep -nir "CONFIG_CGROUP_SCHED" .config
    135:CONFIG_CGROUP_SCHED=y
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build$ cd ..
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0$ cd ..
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek$ cd ..
    build-bananapi4-rdk-broadband/tmp/work/bananapi4_rdk_broadband-rdk-linux$ cd ..
    build-bananapi4-rdk-broadband/tmp/work$ cd ..
    build-bananapi4-rdk-broadband/tmp$ cd work-shared/
    bananapi4-rdk-broadband/ gcc-11.3.0-r0/           
    build-bananapi4-rdk-broadband/tmp$ cd work-shared/bananapi4-rdk-broadband/kernel-source/
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ grep -nir "CGROUP_CPUACCT" .
    ./arch/s390/configs/defconfig:26:CONFIG_CGROUP_CPUACCT=y
    ./arch/s390/configs/debug_defconfig:27:CONFIG_CGROUP_CPUACCT=y
    ./arch/um/configs/x86_64_defconfig:17:CONFIG_CGROUP_CPUACCT=y
    ./arch/um/configs/i386_defconfig:19:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/generic_kc705_defconfig:12:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/nommu_kc705_defconfig:12:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/virt_defconfig:11:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/cadence_csp_defconfig:11:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/smp_lx200_defconfig:12:CONFIG_CGROUP_CPUACCT=y
    ./arch/xtensa/configs/audio_kc705_defconfig:12:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/generic_defconfig:14:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/ci20_defconfig:16:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/sb1250_swarm_defconfig:7:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/vocore2_defconfig:15:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/db1xxx_defconfig:19:CONFIG_CGROUP_CPUACCT=y
    ./arch/mips/configs/omega2p_defconfig:15:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm64/configs/defconfig:24:CONFIG_CGROUP_CPUACCT=y
    ./arch/powerpc/configs/ppc64_defconfig:18:CONFIG_CGROUP_CPUACCT=y
    ./arch/powerpc/configs/pseries_defconfig:24:CONFIG_CGROUP_CPUACCT=y
    ./arch/powerpc/configs/fsl-emb-nonhw.config:14:CONFIG_CGROUP_CPUACCT=y
    ./arch/powerpc/configs/ppc6xx_defconfig:17:CONFIG_CGROUP_CPUACCT=y
    ./arch/powerpc/configs/powernv_defconfig:25:CONFIG_CGROUP_CPUACCT=y
    ./arch/sh/configs/shx3_defconfig:13:CONFIG_CGROUP_CPUACCT=y
    ./arch/sh/configs/sdk7786_defconfig:18:CONFIG_CGROUP_CPUACCT=y
    ./arch/sh/configs/urquell_defconfig:15:CONFIG_CGROUP_CPUACCT=y
    ./arch/sh/configs/apsh4ad0a_defconfig:11:CONFIG_CGROUP_CPUACCT=y
    ./arch/sh/configs/se7206_defconfig:11:CONFIG_CGROUP_CPUACCT=y
    ./arch/x86/configs/x86_64_defconfig:17:CONFIG_CGROUP_CPUACCT=y
    ./arch/x86/configs/i386_defconfig:18:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm/configs/bcm2835_defconfig:13:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm/configs/omap2plus_defconfig:21:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm/configs/tegra_defconfig:11:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm/configs/keystone_defconfig:10:CONFIG_CGROUP_CPUACCT=y
    ./arch/arm/configs/zx_defconfig:8:CONFIG_CGROUP_CPUACCT=y
    ./.kernel-meta/configs/dobby.cfg:25:CONFIG_CGROUP_CPUACCT=y
    ./kernel/sched/Makefile:27:obj-$(CONFIG_CGROUP_CPUACCT) += cpuacct.o
    ./kernel/configs/android-base.config:21:CONFIG_CGROUP_CPUACCT=y
    ./init/Kconfig:1010:config CGROUP_CPUACCT
    ./include/linux/cgroup.h:762:#ifdef CONFIG_CGROUP_CPUACCT
    ./include/linux/cgroup_subsys.h:20:#if IS_ENABLED(CONFIG_CGROUP_CPUACCT)
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ grep -nir "CGROUP_SCHED" .
    ./arch/um/configs/x86_64_defconfig:18:CONFIG_CGROUP_SCHED=y
    ./arch/um/configs/i386_defconfig:20:CONFIG_CGROUP_SCHED=y
    ./arch/mips/configs/ci20_defconfig:13:CONFIG_CGROUP_SCHED=y
    ./arch/mips/configs/pistachio_defconfig:11:CONFIG_CGROUP_SCHED=y
    ./arch/mips/configs/vocore2_defconfig:12:CONFIG_CGROUP_SCHED=y
    ./arch/mips/configs/db1xxx_defconfig:14:CONFIG_CGROUP_SCHED=y
    ./arch/mips/configs/omega2p_defconfig:12:CONFIG_CGROUP_SCHED=y
    ./arch/powerpc/configs/ppc64_defconfig:14:CONFIG_CGROUP_SCHED=y
    ./arch/powerpc/configs/pseries_defconfig:20:CONFIG_CGROUP_SCHED=y
    ./arch/powerpc/configs/fsl-emb-nonhw.config:15:CONFIG_CGROUP_SCHED=y
    ./arch/powerpc/configs/ppc6xx_defconfig:14:CONFIG_CGROUP_SCHED=y
    ./arch/powerpc/configs/powernv_defconfig:21:CONFIG_CGROUP_SCHED=y
    ./arch/riscv/configs/rv32_defconfig:8:CONFIG_CGROUP_SCHED=y
    ./arch/riscv/configs/defconfig:8:CONFIG_CGROUP_SCHED=y
    ./arch/sh/configs/sdk7786_defconfig:21:CONFIG_CGROUP_SCHED=y
    ./arch/sh/configs/urquell_defconfig:18:CONFIG_CGROUP_SCHED=y
    ./arch/x86/configs/x86_64_defconfig:18:CONFIG_CGROUP_SCHED=y
    ./arch/x86/configs/i386_defconfig:19:CONFIG_CGROUP_SCHED=y
    ./arch/arm/configs/omap2plus_defconfig:15:CONFIG_CGROUP_SCHED=y
    ./arch/arm/configs/tegra_defconfig:8:CONFIG_CGROUP_SCHED=y
    ./arch/arm/configs/keystone_defconfig:11:CONFIG_CGROUP_SCHED=y
    ./arch/arm/configs/zx_defconfig:9:CONFIG_CGROUP_SCHED=y
    ./Documentation/scheduler/sched-design-CFS.rst:214:CONFIG_CGROUP_SCHED strives to achieve exactly that.  It lets tasks to be
    ./.kernel-meta/configs/dobby.cfg:26:CONFIG_CGROUP_SCHED=y
    ./kernel/sched/debug.c:417:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/debug.c:474:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/sched.h:323:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/sched.h:485:#else /* CONFIG_CGROUP_SCHED */
    ./kernel/sched/sched.h:489:#endif	/* CONFIG_CGROUP_SCHED */
    ./kernel/sched/sched.h:1480:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/sched.h:1519:#else /* CONFIG_CGROUP_SCHED */
    ./kernel/sched/sched.h:1527:#endif /* CONFIG_CGROUP_SCHED */
    ./kernel/sched/core.c:6648:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/core.c:6717:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/core.c:6724:#endif /* CONFIG_CGROUP_SCHED */
    ./kernel/sched/core.c:7017:#ifdef CONFIG_CGROUP_SCHED
    ./kernel/sched/core.c:8036:#endif	/* CONFIG_CGROUP_SCHED */
    ./kernel/events/core.c:848:static inline void perf_cgroup_sched_out(struct task_struct *task,
    ./kernel/events/core.c:874:static inline void perf_cgroup_sched_in(struct task_struct *prev,
    ./kernel/events/core.c:1017:static inline void perf_cgroup_sched_out(struct task_struct *task,
    ./kernel/events/core.c:1022:static inline void perf_cgroup_sched_in(struct task_struct *prev,
    ./kernel/events/core.c:3376:		perf_cgroup_sched_out(task, next);
    ./kernel/events/core.c:3615:		perf_cgroup_sched_in(prev, task);
    ./kernel/configs/android-base.config:24:CONFIG_CGROUP_SCHED=y
    ./kernel/cgroup/cgroup.c:3703:#ifdef CONFIG_CGROUP_SCHED
    ./init/init_task.c:93:#ifdef CONFIG_CGROUP_SCHED
    ./init/Kconfig:875:menuconfig CGROUP_SCHED
    ./init/Kconfig:883:if CGROUP_SCHED
    ./init/Kconfig:886:	depends on CGROUP_SCHED
    ./init/Kconfig:887:	default CGROUP_SCHED
    ./init/Kconfig:902:	depends on CGROUP_SCHED
    ./init/Kconfig:911:endif #CGROUP_SCHED
    ./init/Kconfig:915:	depends on CGROUP_SCHED
    ./init/Kconfig:1131:	select CGROUP_SCHED
    ./include/linux/sched/autogroup.h:28:#ifdef CONFIG_CGROUP_SCHED
    ./include/linux/sched/autogroup.h:30:#endif /* CONFIG_CGROUP_SCHED */
    ./include/linux/sched.h:682:#ifdef CONFIG_CGROUP_SCHED
    ./include/linux/cgroup_subsys.h:16:#if IS_ENABLED(CONFIG_CGROUP_SCHED)
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ 
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ grep -nir "NETFILTER_XT_TARGET_CT" .
    ./arch/s390/configs/defconfig:180:CONFIG_NETFILTER_XT_TARGET_CT=m
    ./arch/s390/configs/debug_defconfig:185:CONFIG_NETFILTER_XT_TARGET_CT=m
    ./arch/mips/configs/xway_defconfig:55:CONFIG_NETFILTER_XT_TARGET_CT=m
    ./arch/mips/configs/rt305x_defconfig:53:CONFIG_NETFILTER_XT_TARGET_CT=m
    ./net/netfilter/Kconfig:833:config NETFILTER_XT_TARGET_CT
    ./net/netfilter/Kconfig:992:	select NETFILTER_XT_TARGET_CT
    ./net/netfilter/Makefile:143:obj-$(CONFIG_NETFILTER_XT_TARGET_CT) += xt_CT.o
    ./.kernel-meta/cfg/merge_config_build.log:27:Value of CONFIG_NETFILTER_XT_TARGET_CT is redefined by fragment .kernel-meta/configs//./dobby.cfg:
    ./.kernel-meta/cfg/merge_config_build.log:28:Previous value: # CONFIG_NETFILTER_XT_TARGET_CT is not set
    ./.kernel-meta/cfg/merge_config_build.log:29:New value: CONFIG_NETFILTER_XT_TARGET_CT=y
    ./.kernel-meta/cfg/merge_config_build.log:14274:Value requested for CONFIG_NETFILTER_XT_TARGET_CT not in final .config
    ./.kernel-meta/cfg/merge_config_build.log:14275:Requested value:  CONFIG_NETFILTER_XT_TARGET_CT=y
    ./.kernel-meta/cfg/merge_config_build.log:14276:Actual value:     CONFIG_NETFILTER_XT_TARGET_CT=m
    ./.kernel-meta/cfg/redefinition.txt:671:    - option CONFIG_NETFILTER_XT_TARGET_CT is defined more than once
    ./.kernel-meta/configs/iptables_nf.cfg:2:CONFIG_NETFILTER_XT_TARGET_CT=y
    ./.kernel-meta/configs/defconfig:3412:# CONFIG_NETFILTER_XT_TARGET_CT is not set
    ./.kernel-meta/configs/dobby.cfg:18:CONFIG_NETFILTER_XT_TARGET_CT=y
    ./.kernel-meta/patches/999-1718-v5.15-net-netfilter-add-nf-hw-offload.patch:1242: 	select NETFILTER_XT_TARGET_CT
    ./.kernel-meta/patches/999-1718-v5.15-net-netfilter-add-nf-hw-offload.patch:1272: obj-$(CONFIG_NETFILTER_XT_TARGET_CT) += xt_CT.o
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ ls ../../../
    abi_version          cache/               hosttools/           pkgdata/             saved_tmpdir         stamps/              sysroots-components/ work/                
    buildstats/          deploy/              log/                 qa.log               sstate-control/      sysroots/            sysroots-uninative/  work-shared/         
    build-bananapi4-rdk-broadband/tmp/work-shared/bananapi4-rdk-broadband/kernel-source$ ls ../../../work/bananapi4_rdk_broadband-rdk-linux/linux-mediatek/1_5.4.281+gitAUTOINC+feeb59687b_84d75fd864-r0/linux-bananapi4_rdk_broadband-standard-build/net/netfilter/
    built-in.a                    nf_conntrack_h323.mod.c        nf_conntrack_proto_sctp.o  nf_flow_table_core.o     nf_nat_sip.mod.o     nft_dynset.o      xt_HL.ko             xt_NFLOG.ko
    core.o                        nf_conntrack_h323.mod.o        nf_conntrack_proto_tcp.o   nf_flow_table_ip.o       nf_nat_sip.o         nft_exthdr.o      xt_HL.mod            xt_NFLOG.mod
    ipset                         nf_conntrack_h323.o            nf_conntrack_proto_udp.o   nf_flow_table_netlink.o  nf_nat_tftp.ko       nft_immediate.o   xt_HL.mod.c          xt_NFLOG.mod.c
    ipvs                          nf_conntrack_helper.o          nf_conntrack_sane.ko       nf_flow_table_offload.o  nf_nat_tftp.mod      nft_lookup.o      xt_HL.mod.o          xt_NFLOG.mod.o
    modules.builtin               nf_conntrack_irc.ko            nf_conntrack_sane.mod      nf_log_common.o          nf_nat_tftp.mod.c    nft_meta.o        xt_hl.o              xt_NFLOG.o
    modules.order                 nf_conntrack_irc.mod           nf_conntrack_sane.mod.c    nf_log.o                 nf_nat_tftp.mod.o    nft_payload.o     xt_HL.o              xt_physdev.o
    nf_conntrack_acct.o           nf_conntrack_irc.mod.c         nf_conntrack_sane.mod.o    nf_nat_amanda.ko         nf_nat_tftp.o        nft_range.o       xt_iprange.o         xt_pkttype.o
    nf_conntrack_amanda.ko        nf_conntrack_irc.mod.o         nf_conntrack_sane.o        nf_nat_amanda.mod        nfnetlink_log.ko     nft_rt.o          xt_limit.o           xt_policy.o
    nf_conntrack_amanda.mod       nf_conntrack_irc.o             nf_conntrack_seqadj.o      nf_nat_amanda.mod.c      nfnetlink_log.mod    utils.o           xt_LOG.ko            xt_recent.o
    nf_conntrack_amanda.mod.c     nf_conntrack_netbios_ns.ko     nf_conntrack_sip.ko        nf_nat_amanda.mod.o      nfnetlink_log.mod.c  x_tables.o        xt_LOG.mod           xt_REDIRECT.ko
    nf_conntrack_amanda.mod.o     nf_conntrack_netbios_ns.mod    nf_conntrack_sip.mod       nf_nat_amanda.o          nfnetlink_log.mod.o  xt_addrtype.o     xt_LOG.mod.c         xt_REDIRECT.mod
    nf_conntrack_amanda.o         nf_conntrack_netbios_ns.mod.c  nf_conntrack_sip.mod.c     nf_nat_core.o            nfnetlink_log.o      xt_comment.o      xt_LOG.mod.o         xt_REDIRECT.mod.c
    nf_conntrack_broadcast.ko     nf_conntrack_netbios_ns.mod.o  nf_conntrack_sip.mod.o     nf_nat_ftp.o             nfnetlink.o          xt_conntrack.o    xt_LOG.o             xt_REDIRECT.mod.o
    nf_conntrack_broadcast.mod    nf_conntrack_netbios_ns.o      nf_conntrack_sip.o         nf_nat_helper.o          nfnetlink_queue.o    xt_CT.ko          xt_MASQUERADE.ko     xt_REDIRECT.o
    nf_conntrack_broadcast.mod.c  nf_conntrack_netlink.ko        nf_conntrack_snmp.ko       nf_nat_irc.ko            nf_queue.o           xt_CT.mod         xt_MASQUERADE.mod    xt_state.o
    nf_conntrack_broadcast.mod.o  nf_conntrack_netlink.mod       nf_conntrack_snmp.mod      nf_nat_irc.mod           nf_sockopt.o         xt_CT.mod.c       xt_MASQUERADE.mod.c  xt_TCPMSS.ko
    nf_conntrack_broadcast.o      nf_conntrack_netlink.mod.c     nf_conntrack_snmp.mod.c    nf_nat_irc.mod.c         nf_tables_api.o      xt_CT.mod.o       xt_MASQUERADE.mod.o  xt_TCPMSS.mod
    nf_conntrack_core.o           nf_conntrack_netlink.mod.o     nf_conntrack_snmp.mod.o    nf_nat_irc.mod.o         nf_tables_core.o     xt_CT.o           xt_MASQUERADE.o      xt_TCPMSS.mod.c
    nf_conntrack_expect.o         nf_conntrack_netlink.o         nf_conntrack_snmp.o        nf_nat_irc.o             nf_tables_offload.o  xt_ecn.ko         xt_multiport.o       xt_TCPMSS.mod.o
    nf_conntrack_extend.o         nf_conntrack_pptp.o            nf_conntrack_standalone.o  nf_nat_masquerade.o      nf_tables_trace.o    xt_ecn.mod        xt_nat.o             xt_TCPMSS.o
    nf_conntrack_ftp.o            nf_conntrack_proto_generic.o   nf_conntrack_tftp.ko       nf_nat_proto.o           nft_bitwise.o        xt_ecn.mod.c      xt_NETMAP.ko         xt_tcpudp.o
    nf_conntrack_h323_asn1.o      nf_conntrack_proto_gre.o       nf_conntrack_tftp.mod      nf_nat_redirect.o        nft_byteorder.o      xt_ecn.mod.o      xt_NETMAP.mod
    nf_conntrack_h323.ko          nf_conntrack_proto_icmp.o      nf_conntrack_tftp.mod.c    nf_nat_sip.ko            nft_chain_filter.o   xt_ecn.o          xt_NETMAP.mod.c
    nf_conntrack_h323_main.o      nf_conntrack_proto_icmpv6.o    nf_conntrack_tftp.mod.o    nf_nat_sip.mod           nft_chain_route.o    xt_FLOWOFFLOAD.o  xt_NETMAP.mod.o
    nf_conntrack_h323.mod         nf_conntrack_proto.o           nf_conntrack_tftp.o        nf_nat_sip.mod.c         nft_cmp.o            xt_helper.o       xt_NETMAP.o

    Summary: There was 1 WARNING message.
    === Matched appended recipes ===
    dobby.bb:
    meta-rdk-broadband-apps/recipes-containers/dobby/dobby.bbappend
    build-bananapi4-rdk-broadband$ 


    http://192.168.0.10/busybox.tar.gz

    rbuscli method_values "Device.SoftwareModules.InstallDU()" URL string http://192.168.0.10/busybox.tar.gz ExecutionEnvRef string default
    rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" RequestedState string Active


    ic-GW:~# dmcli eRT getv Device.SoftwareModules.
    CR component name is: eRT.com.cisco.spvtg.ccsp.CR
    subsystem_prefix eRT.
    Execution succeed.
    Parameter    1 name: Device.SoftwareModules.ExecEnv.1.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    2 name: Device.SoftwareModules.ExecEnv.1.Enable
                type:       bool,    value: true 
    Parameter    3 name: Device.SoftwareModules.ExecEnv.1.InitialRunLevel
                type:        int,    value: 5 
    Parameter    4 name: Device.SoftwareModules.ExecEnv.1.Name
                type:     string,    value: default 
    Parameter    5 name: Device.SoftwareModules.ExecEnv.1.Status
                type:     string,    value: Up 
    Parameter    6 name: Device.SoftwareModules.ExecEnv.2.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    7 name: Device.SoftwareModules.ExecEnv.2.Enable
                type:       bool,    value: true 
    Parameter    8 name: Device.SoftwareModules.ExecEnv.2.InitialRunLevel
                type:        int,    value: 5 
    Parameter    9 name: Device.SoftwareModules.ExecEnv.2.Name
                type:     string,    value: test 
    Parameter   10 name: Device.SoftwareModules.ExecEnv.2.Status
                type:     string,    value: Up 
    Parameter   11 name: Device.SoftwareModules.ExecEnv.3.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   12 name: Device.SoftwareModules.ExecEnv.3.Enable
                type:       bool,    value: true 
    Parameter   13 name: Device.SoftwareModules.ExecEnv.3.InitialRunLevel
                type:        int,    value: 5 
    Parameter   14 name: Device.SoftwareModules.ExecEnv.3.Name
                type:     string,    value: user 
    Parameter   15 name: Device.SoftwareModules.ExecEnv.3.Status
                type:     string,    value: Up 

    root@Filogic-GW:~# 
    root@Filogic-GW:~# dmcli eRT getv Device.SoftwareModules.
    CR component name is: eRT.com.cisco.spvtg.ccsp.CR
    subsystem_prefix eRT.
    Execution succeed.
    Parameter    1 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef
                type:     string,    value: Device.SoftwareModules.ExecEnv.1 
    Parameter    2 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList
                type:     string,    value: Device.SoftwareModules.ExecutionUnit.1 
    Parameter    3 name: Device.SoftwareModules.DeploymentUnit.1.Status
                type:     string,    value: Installed 
    Parameter    4 name: Device.SoftwareModules.DeploymentUnit.1.URL
                type:     string,    value: http://192.168.0.10/busybox.tar.gz 
    Parameter    5 name: Device.SoftwareModules.ExecEnv.1.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    6 name: Device.SoftwareModules.ExecEnv.1.Enable
                type:       bool,    value: true 
    Parameter    7 name: Device.SoftwareModules.ExecEnv.1.InitialRunLevel
                type:        int,    value: 5 
    Parameter    8 name: Device.SoftwareModules.ExecEnv.1.Name
                type:     string,    value: default 
    Parameter    9 name: Device.SoftwareModules.ExecEnv.1.Status
                type:     string,    value: Up 
    Parameter   10 name: Device.SoftwareModules.ExecEnv.2.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   11 name: Device.SoftwareModules.ExecEnv.2.Enable
                type:       bool,    value: true 
    Parameter   12 name: Device.SoftwareModules.ExecEnv.2.InitialRunLevel
                type:        int,    value: 5 
    Parameter   13 name: Device.SoftwareModules.ExecEnv.2.Name
                type:     string,    value: test 
    Parameter   14 name: Device.SoftwareModules.ExecEnv.2.Status
                type:     string,    value: Up 
    Parameter   15 name: Device.SoftwareModules.ExecEnv.3.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   16 name: Device.SoftwareModules.ExecEnv.3.Enable
                type:       bool,    value: true 
    Parameter   17 name: Device.SoftwareModules.ExecEnv.3.InitialRunLevel
                type:        int,    value: 5 
    Parameter   18 name: Device.SoftwareModules.ExecEnv.3.Name
                type:     string,    value: user 
    Parameter   19 name: Device.SoftwareModules.ExecEnv.3.Status
                type:     string,    value: Up 
    Parameter   20 name: Device.SoftwareModules.ExecutionUnit.1.Name
                type:     string,    value: Kn 
    Parameter   21 name: Device.SoftwareModules.ExecutionUnit.1.Status
                type:     string,    value: Idle 

    root@Filogic-GW:~# dmcli eRT getv Device.SoftwareModules.
    CR component name is: eRT.com.cisco.spvtg.ccsp.CR
    subsystem_prefix eRT.
    Execution succeed.
    Parameter    1 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef
                type:     string,    value: Device.SoftwareModules.ExecEnv.1 
    Parameter    2 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList
                type:     string,    value: Device.SoftwareModules.ExecutionUnit.1 
    Parameter    3 name: Device.SoftwareModules.DeploymentUnit.1.Status
                type:     string,    value: Installed 
    Parameter    4 name: Device.SoftwareModules.DeploymentUnit.1.URL
                type:     string,    value: http://192.168.0.10/busybox.tar.gz 
    Parameter    5 name: Device.SoftwareModules.ExecEnv.1.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    6 name: Device.SoftwareModules.ExecEnv.1.Enable
                type:       bool,    value: true 
    Parameter    7 name: Device.SoftwareModules.ExecEnv.1.InitialRunLevel
                type:        int,    value: 5 
    Parameter    8 name: Device.SoftwareModules.ExecEnv.1.Name
                type:     string,    value: default 
    Parameter    9 name: Device.SoftwareModules.ExecEnv.1.Status
                type:     string,    value: Up 
    Parameter   10 name: Device.SoftwareModules.ExecEnv.2.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   11 name: Device.SoftwareModules.ExecEnv.2.Enable
                type:       bool,    value: true 
    Parameter   12 name: Device.SoftwareModules.ExecEnv.2.InitialRunLevel
                type:        int,    value: 5 
    Parameter   13 name: Device.SoftwareModules.ExecEnv.2.Name
                type:     string,    value: test 
    Parameter   14 name: Device.SoftwareModules.ExecEnv.2.Status
                type:     string,    value: Up 
    Parameter   15 name: Device.SoftwareModules.ExecEnv.3.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   16 name: Device.SoftwareModules.ExecEnv.3.Enable
                type:       bool,    value: true 
    Parameter   17 name: Device.SoftwareModules.ExecEnv.3.InitialRunLevel
                type:        int,    value: 5 
    Parameter   18 name: Device.SoftwareModules.ExecEnv.3.Name
                type:     string,    value: user 
    Parameter   19 name: Device.SoftwareModules.ExecEnv.3.Status
                type:     string,    value: Up 
    Parameter   20 name: Device.SoftwareModules.ExecutionUnit.1.Name
                type:     string,    value: Kn 
    Parameter   21 name: Device.SoftwareModules.ExecutionUnit.1.Status
                type:     string,    value: Active 

    root@Filogic-GW:~# DobbyTool list
    descriptor | id                               | state
    ------------|----------------------------------|-------------
            734 | Kn                               | running
    root@Filogic-GW:~# DobbyTool list
    no containers
    root@Filogic-GW:~# dmcli eRT getv Device.SoftwareModules.
    CR component name is: eRT.com.cisco.spvtg.ccsp.CR
    subsystem_prefix eRT.
    Execution succeed.
    Parameter    1 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef
                type:     string,    value: Device.SoftwareModules.ExecEnv.1 
    Parameter    2 name: Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList
                type:     string,    value: Device.SoftwareModules.ExecutionUnit.1 
    Parameter    3 name: Device.SoftwareModules.DeploymentUnit.1.Status
                type:     string,    value: Installed 
    Parameter    4 name: Device.SoftwareModules.DeploymentUnit.1.URL
                type:     string,    value: http://192.168.0.10/busybox.tar.gz 
    Parameter    5 name: Device.SoftwareModules.ExecEnv.1.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    6 name: Device.SoftwareModules.ExecEnv.1.Enable
                type:       bool,    value: true 
    Parameter    7 name: Device.SoftwareModules.ExecEnv.1.InitialRunLevel
                type:        int,    value: 5 
    Parameter    8 name: Device.SoftwareModules.ExecEnv.1.Name
                type:     string,    value: default 
    Parameter    9 name: Device.SoftwareModules.ExecEnv.1.Status
                type:     string,    value: Up 
    Parameter   10 name: Device.SoftwareModules.ExecEnv.2.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   11 name: Device.SoftwareModules.ExecEnv.2.Enable
                type:       bool,    value: true 
    Parameter   12 name: Device.SoftwareModules.ExecEnv.2.InitialRunLevel
                type:        int,    value: 5 
    Parameter   13 name: Device.SoftwareModules.ExecEnv.2.Name
                type:     string,    value: test 
    Parameter   14 name: Device.SoftwareModules.ExecEnv.2.Status
                type:     string,    value: Up 
    Parameter   15 name: Device.SoftwareModules.ExecEnv.3.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   16 name: Device.SoftwareModules.ExecEnv.3.Enable
                type:       bool,    value: true 
    Parameter   17 name: Device.SoftwareModules.ExecEnv.3.InitialRunLevel
                type:        int,    value: 5 
    Parameter   18 name: Device.SoftwareModules.ExecEnv.3.Name
                type:     string,    value: user 
    Parameter   19 name: Device.SoftwareModules.ExecEnv.3.Status
                type:     string,    value: Up 
    Parameter   20 name: Device.SoftwareModules.ExecutionUnit.1.Name
                type:     string,    value: Kn 
    Parameter   21 name: Device.SoftwareModules.ExecutionUnit.1.Status
                type:     string,    value: Idle 

    root@Filogic-GW:~# 


    :/tmp# rbuscli method_values "Device.SoftwareModules.InstallDU()" URL string http://192.168.0.10/busybox.tar.gz ExecutionEnvRef string default
    Parameter  1:
                Name  : Status
                Type  : string
                Value : {"response":"Installation Started"}
    root@Filogic-GW:/tmp# 
    root@Filogic-GW:/tmp# 
    root@Filogic-GW:/tmp# rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" RequestedState string Active
    Parameter  1:
                Name  : Ret
                Type  : string
                Value : "Starting EU"
    root@Filogic-GW:/tmp# rbuscli method_values "Device.SoftwareModules.ExecutionUnit.1.SetRequestedState()" RequestedState string Idle  
    Parameter  1:
                Name  : Ret
                Type  : string
                Value : "Stopping EU"
    root@Filogic-GW:/tmp# 

    root@Filogic-GW:~# dmcli eRT getv Device.SoftwareModules.
    CR component name is: eRT.com.cisco.spvtg.ccsp.CR
    subsystem_prefix eRT.
    Execution succeed.
    Parameter    1 name: Device.SoftwareModules.ExecEnv.1.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    2 name: Device.SoftwareModules.ExecEnv.1.Enable
                type:       bool,    value: true 
    Parameter    3 name: Device.SoftwareModules.ExecEnv.1.InitialRunLevel
                type:        int,    value: 5 
    Parameter    4 name: Device.SoftwareModules.ExecEnv.1.Name
                type:     string,    value: default 
    Parameter    5 name: Device.SoftwareModules.ExecEnv.1.Status
                type:     string,    value: Up 
    Parameter    6 name: Device.SoftwareModules.ExecEnv.2.CurrentRunLevel
                type:        int,    value: 5 
    Parameter    7 name: Device.SoftwareModules.ExecEnv.2.Enable
                type:       bool,    value: true 
    Parameter    8 name: Device.SoftwareModules.ExecEnv.2.InitialRunLevel
                type:        int,    value: 5 
    Parameter    9 name: Device.SoftwareModules.ExecEnv.2.Name
                type:     string,    value: test 
    Parameter   10 name: Device.SoftwareModules.ExecEnv.2.Status
                type:     string,    value: Up 
    Parameter   11 name: Device.SoftwareModules.ExecEnv.3.CurrentRunLevel
                type:        int,    value: 5 
    Parameter   12 name: Device.SoftwareModules.ExecEnv.3.Enable
                type:       bool,    value: true 
    Parameter   13 name: Device.SoftwareModules.ExecEnv.3.InitialRunLevel
                type:        int,    value: 5 
    Parameter   14 name: Device.SoftwareModules.ExecEnv.3.Name
                type:     string,    value: user 
    Parameter   15 name: Device.SoftwareModules.ExecEnv.3.Status
                type:     string,    value: Up 

    root@Filogic-GW:~# 

    /tmp# rbuscli method_values "Device.SoftwareModules.DeploymentUnit.1.Uninstall()"
    Invalid arguments. Please see the help
    root@Filogic-GW:/tmp# 
    root@Filogic-GW:/tmp# 
    root@Filogic-GW:/tmp# rbuscli method_noargs "Device.SoftwareModules.DeploymentUnit.1.Uninstall()"
    Parameter  1:
                Name  : Ret
                Type  : string
                Value : "Uninstallation started"
    root@Filogic-GW:/tmp# 

    W:~# zcat /proc/config.gz | grep -E "CONFIG_NF_LOG_IPV6|CONFIG_NETFILTER_XT_TARGET_CT|CONFIG_CGROUP_DEBUG|CONFIG_CPUSETS|CONFIG_PROC_PID_CPUSET|CONFIG_CGROUP_SCHED|CONFIG_CGROUP_CPUACCT"
    CONFIG_CGROUP_SCHED=y
    CONFIG_CPUSETS=y
    CONFIG_PROC_PID_CPUSET=y
    CONFIG_CGROUP_CPUACCT=y
    CONFIG_CGROUP_DEBUG=y
    CONFIG_NETFILTER_XT_TARGET_CT=m
    CONFIG_NF_LOG_IPV6=y
    root@Filogic-GW:~# 
    root@Filogic-GW:~# 
    root@Filogic-GW:~# cat /version.txt 
    imagename:rdkb-generic-broadband-image_rdkb-2025q2-kirkstone_20251106010940
    BRANCH=rdkb-2025q2-kirkstone
    YOCTO_VERSION=kirkstone
    VERSION=rdkb-2025q2-kirkstone.11.06.25
    SPIN=0
    BUILD_TIME="2025-11-06 01:09:40"
    JENKINS_JOB=Default
    JENKINS_BUILD_NUMBER=0
    Generated on Thu Nov 06  01:09:40 UTC 2025
    root@Filogic-GW:~# 
    ```

=== "LCM"

    ```bash
    ~$ ssh root@192.168.0.10
    Warning: Permanently added '192.168.0.10' (ED25519) to the list of known hosts.
    root@Filogic-GW:~# 
    root@Filogic-GW:~# 
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.InstallDU(URL = "docker://index.docker.io/piotrnakraszewicz/alpine64", UUID = "1713d242-80ba-55b4-a115-07bbb1d318ab", ExecutionEnvRef = "generic", AutoStart = "false", Privileged = true, NetworkConfig={ShareParentNetwork=1})'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.InstallDU(URL = "docker://index.docker.io/piotrnakraszewicz/alpine64", UUID = "1713d242-80ba-55b4-a115-07bbb1d318ab", ExecutionEnvRef = "generic", AutoStart = "false", Privileged = true, NetworkConfig={ShareParentNetwork=1})

    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4 IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 STOPPED 0         -      -    -    false        
    root@Filogic-GW:~# 
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.?'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.?
    Device.SoftwareModules.
    Device.SoftwareModules.DeploymentUnitNumberOfEntries=1
    Device.SoftwareModules.ExecEnvNumberOfEntries=1
    Device.SoftwareModules.ExecutionUnitNumberOfEntries=1
    Device.SoftwareModules.DeploymentUnit.1.
    Device.SoftwareModules.DeploymentUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.DUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.Description="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef="Device.SoftwareModules.ExecEnv.1."
    Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList="Device.SoftwareModules.ExecutionUnit.1."
    Device.SoftwareModules.DeploymentUnit.1.Installed=2025-11-21T11:34:47Z
    Device.SoftwareModules.DeploymentUnit.1.LastUpdate=1970-01-01T00:00:00Z
    Device.SoftwareModules.DeploymentUnit.1.ModuleVersion=""
    Device.SoftwareModules.DeploymentUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.DeploymentUnit.1.Resolved=true
    Device.SoftwareModules.DeploymentUnit.1.Status="Installed"
    Device.SoftwareModules.DeploymentUnit.1.URL="docker://index.docker.io/piotrnakraszewicz/alpine64:latest"
    Device.SoftwareModules.DeploymentUnit.1.UUID="1713d242-80ba-55b4-a115-07bbb1d318ab"
    Device.SoftwareModules.DeploymentUnit.1.Vendor="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.VendorConfigList=""
    Device.SoftwareModules.DeploymentUnit.1.VendorLogList=""
    Device.SoftwareModules.DeploymentUnit.1.Version="latest"
    Device.SoftwareModules.ExecEnv.1.
    Device.SoftwareModules.ExecEnv.1.ActiveExecutionUnits=""
    Device.SoftwareModules.ExecEnv.1.Alias="cpe-generic"
    Device.SoftwareModules.ExecEnv.1.AllocatedCPUPercent=100
    Device.SoftwareModules.ExecEnv.1.AllocatedDiskSpace=5120
    Device.SoftwareModules.ExecEnv.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableDiskSpace=4762
    Device.SoftwareModules.ExecEnv.1.AvailableMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableRoles=""
    Device.SoftwareModules.ExecEnv.1.CreatedAt=2022-04-28T17:42:57Z
    Device.SoftwareModules.ExecEnv.1.CurrentRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.Description=""
    Device.SoftwareModules.ExecEnv.1.Enable=true
    Device.SoftwareModules.ExecEnv.1.InitialExecutionUnitRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.InitialRunLevel=0
    Device.SoftwareModules.ExecEnv.1.Name="generic"
    Device.SoftwareModules.ExecEnv.1.ParentExecEnv=""
    Device.SoftwareModules.ExecEnv.1.ProcessorRefList=""
    Device.SoftwareModules.ExecEnv.1.RestartReason=""
    Device.SoftwareModules.ExecEnv.1.Status="Up"
    Device.SoftwareModules.ExecEnv.1.Type="lxc:4.0.12"
    Device.SoftwareModules.ExecEnv.1.Vendor="Cthulhu"
    Device.SoftwareModules.ExecEnv.1.Version="3.9.0"
    Device.SoftwareModules.ExecutionUnit.1.
    Device.SoftwareModules.ExecutionUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.AllocatedCPUPercent=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedDiskSpace=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.AssociatedProcessList=""
    Device.SoftwareModules.ExecutionUnit.1.AutoStart=false
    Device.SoftwareModules.ExecutionUnit.1.AvailableDiskSpace=-1
    Device.SoftwareModules.ExecutionUnit.1.AvailableMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.Description=""
    Device.SoftwareModules.ExecutionUnit.1.DiskSpaceInUse=-1
    Device.SoftwareModules.ExecutionUnit.1.EUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecEnvLabel="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionEnvRef="generic"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode="NoFault"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage=""
    Device.SoftwareModules.ExecutionUnit.1.MemoryInUse=-1
    Device.SoftwareModules.ExecutionUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.ExecutionUnit.1.References=""
    Device.SoftwareModules.ExecutionUnit.1.RunLevel=0
    Device.SoftwareModules.ExecutionUnit.1.Status="Idle"
    Device.SoftwareModules.ExecutionUnit.1.Vendor=""
    Device.SoftwareModules.ExecutionUnit.1.VendorConfigList=""
    Device.SoftwareModules.ExecutionUnit.1.VendorLogList=""
    Device.SoftwareModules.ExecutionUnit.1.Version="latest"
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.X_PRPL-COM_DNSSDRefList=""
    Device.SoftwareModules.NetworkConfig.
    Device.SoftwareModules.NetworkConfig.DefaultBridge=""
    Device.SoftwareModules.NetworkConfig.DefaultFirewallChain=""

    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( RequestedState = "Active")'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( RequestedState = "Active")

    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.?'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.?
    Device.SoftwareModules.
    Device.SoftwareModules.DeploymentUnitNumberOfEntries=1
    Device.SoftwareModules.ExecEnvNumberOfEntries=1
    Device.SoftwareModules.ExecutionUnitNumberOfEntries=1
    Device.SoftwareModules.DeploymentUnit.1.
    Device.SoftwareModules.DeploymentUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.DUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.Description="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef="Device.SoftwareModules.ExecEnv.1."
    Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList="Device.SoftwareModules.ExecutionUnit.1."
    Device.SoftwareModules.DeploymentUnit.1.Installed=2025-11-21T11:34:47Z
    Device.SoftwareModules.DeploymentUnit.1.LastUpdate=1970-01-01T00:00:00Z
    Device.SoftwareModules.DeploymentUnit.1.ModuleVersion=""
    Device.SoftwareModules.DeploymentUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.DeploymentUnit.1.Resolved=true
    Device.SoftwareModules.DeploymentUnit.1.Status="Installed"
    Device.SoftwareModules.DeploymentUnit.1.URL="docker://index.docker.io/piotrnakraszewicz/alpine64:latest"
    Device.SoftwareModules.DeploymentUnit.1.UUID="1713d242-80ba-55b4-a115-07bbb1d318ab"
    Device.SoftwareModules.DeploymentUnit.1.Vendor="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.VendorConfigList=""
    Device.SoftwareModules.DeploymentUnit.1.VendorLogList=""
    Device.SoftwareModules.DeploymentUnit.1.Version="latest"
    Device.SoftwareModules.ExecEnv.1.
    Device.SoftwareModules.ExecEnv.1.ActiveExecutionUnits=""
    Device.SoftwareModules.ExecEnv.1.Alias="cpe-generic"
    Device.SoftwareModules.ExecEnv.1.AllocatedCPUPercent=100
    Device.SoftwareModules.ExecEnv.1.AllocatedDiskSpace=5120
    Device.SoftwareModules.ExecEnv.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableDiskSpace=4756
    Device.SoftwareModules.ExecEnv.1.AvailableMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableRoles=""
    Device.SoftwareModules.ExecEnv.1.CreatedAt=2022-04-28T17:42:57Z
    Device.SoftwareModules.ExecEnv.1.CurrentRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.Description=""
    Device.SoftwareModules.ExecEnv.1.Enable=true
    Device.SoftwareModules.ExecEnv.1.InitialExecutionUnitRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.InitialRunLevel=0
    Device.SoftwareModules.ExecEnv.1.Name="generic"
    Device.SoftwareModules.ExecEnv.1.ParentExecEnv=""
    Device.SoftwareModules.ExecEnv.1.ProcessorRefList=""
    Device.SoftwareModules.ExecEnv.1.RestartReason=""
    Device.SoftwareModules.ExecEnv.1.Status="Up"
    Device.SoftwareModules.ExecEnv.1.Type="lxc:4.0.12"
    Device.SoftwareModules.ExecEnv.1.Vendor="Cthulhu"
    Device.SoftwareModules.ExecEnv.1.Version="3.9.0"
    Device.SoftwareModules.ExecutionUnit.1.
    Device.SoftwareModules.ExecutionUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.AllocatedCPUPercent=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedDiskSpace=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.AssociatedProcessList=""
    Device.SoftwareModules.ExecutionUnit.1.AutoStart=false
    Device.SoftwareModules.ExecutionUnit.1.AvailableDiskSpace=4756
    Device.SoftwareModules.ExecutionUnit.1.AvailableMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.Description=""
    Device.SoftwareModules.ExecutionUnit.1.DiskSpaceInUse=20
    Device.SoftwareModules.ExecutionUnit.1.EUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecEnvLabel="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionEnvRef="generic"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode="NoFault"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage=""
    Device.SoftwareModules.ExecutionUnit.1.MemoryInUse=1260
    Device.SoftwareModules.ExecutionUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.ExecutionUnit.1.References=""
    Device.SoftwareModules.ExecutionUnit.1.RunLevel=0
    Device.SoftwareModules.ExecutionUnit.1.Status="Active"
    Device.SoftwareModules.ExecutionUnit.1.Vendor=""
    Device.SoftwareModules.ExecutionUnit.1.VendorConfigList=""
    Device.SoftwareModules.ExecutionUnit.1.VendorLogList=""
    Device.SoftwareModules.ExecutionUnit.1.Version="latest"
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.X_PRPL-COM_DNSSDRefList=""
    Device.SoftwareModules.NetworkConfig.
    Device.SoftwareModules.NetworkConfig.DefaultBridge=""
    Device.SoftwareModules.NetworkConfig.DefaultFirewallChain=""

    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4                                                                             IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 RUNNING 0         -      192.168.0.0, 192.168.0.10, 192.168.101.3, 192.168.106.1, 192.168.245.1 -    false        
    root@Filogic-GW:~# lxc-attach 
    lxc-attach: No container name specified
    root@Filogic-GW:~# lxc-attach a6995eb1-777e-52cd-aa7d-cec618548396
    lxc-attach: a6995eb1-777e-52cd-aa7d-cec618548396: confile.c: set_config_unsupported_key: 153 Invalid argument - Unsupported config key "lxc.seccomp"
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# 
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# ping googlep
    ping: bad address 'googlep'
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# ping google.pl
    PING google.pl (142.251.98.94): 56 data bytes
    64 bytes from 142.251.98.94: seq=0 ttl=114 time=8.779 ms
    64 bytes from 142.251.98.94: seq=1 ttl=114 time=18.147 ms
    ^C
    --- google.pl ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 8.779/13.463/18.147 ms
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# wget google.pl
    Connecting to google.pl (142.251.98.94:80)
    Connecting to www.google.pl (142.250.109.94:80)
    Connecting to www.google.com (142.250.130.103:80)
    saving to 'index.html'
    index.html           100% |*********************************************************************************************************************************************************************************************************| 18235  0:00:00 ETA
    'index.html' saved
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# vi index.html 
    root@a6995eb1-777e-52cd-aa7d-cec618548396:/# 
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( RequestedState = "Idle")'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.ExecutionUnit.1.SetRequestedState( RequestedState = "Idle")

    root@Filogic-GW:~# 
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.?'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.?
    Device.SoftwareModules.
    Device.SoftwareModules.DeploymentUnitNumberOfEntries=1
    Device.SoftwareModules.ExecEnvNumberOfEntries=1
    Device.SoftwareModules.ExecutionUnitNumberOfEntries=1
    Device.SoftwareModules.DeploymentUnit.1.
    Device.SoftwareModules.DeploymentUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.DUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.DeploymentUnit.1.Description="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.ExecutionEnvRef="Device.SoftwareModules.ExecEnv.1."
    Device.SoftwareModules.DeploymentUnit.1.ExecutionUnitList="Device.SoftwareModules.ExecutionUnit.1."
    Device.SoftwareModules.DeploymentUnit.1.Installed=2025-11-21T11:34:47Z
    Device.SoftwareModules.DeploymentUnit.1.LastUpdate=1970-01-01T00:00:00Z
    Device.SoftwareModules.DeploymentUnit.1.ModuleVersion=""
    Device.SoftwareModules.DeploymentUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.DeploymentUnit.1.Resolved=true
    Device.SoftwareModules.DeploymentUnit.1.Status="Installed"
    Device.SoftwareModules.DeploymentUnit.1.URL="docker://index.docker.io/piotrnakraszewicz/alpine64:latest"
    Device.SoftwareModules.DeploymentUnit.1.UUID="1713d242-80ba-55b4-a115-07bbb1d318ab"
    Device.SoftwareModules.DeploymentUnit.1.Vendor="Unknown"
    Device.SoftwareModules.DeploymentUnit.1.VendorConfigList=""
    Device.SoftwareModules.DeploymentUnit.1.VendorLogList=""
    Device.SoftwareModules.DeploymentUnit.1.Version="latest"
    Device.SoftwareModules.ExecEnv.1.
    Device.SoftwareModules.ExecEnv.1.ActiveExecutionUnits=""
    Device.SoftwareModules.ExecEnv.1.Alias="cpe-generic"
    Device.SoftwareModules.ExecEnv.1.AllocatedCPUPercent=100
    Device.SoftwareModules.ExecEnv.1.AllocatedDiskSpace=5120
    Device.SoftwareModules.ExecEnv.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableDiskSpace=4737
    Device.SoftwareModules.ExecEnv.1.AvailableMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableRoles=""
    Device.SoftwareModules.ExecEnv.1.CreatedAt=2022-04-28T17:42:57Z
    Device.SoftwareModules.ExecEnv.1.CurrentRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.Description=""
    Device.SoftwareModules.ExecEnv.1.Enable=true
    Device.SoftwareModules.ExecEnv.1.InitialExecutionUnitRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.InitialRunLevel=0
    Device.SoftwareModules.ExecEnv.1.Name="generic"
    Device.SoftwareModules.ExecEnv.1.ParentExecEnv=""
    Device.SoftwareModules.ExecEnv.1.ProcessorRefList=""
    Device.SoftwareModules.ExecEnv.1.RestartReason=""
    Device.SoftwareModules.ExecEnv.1.Status="Up"
    Device.SoftwareModules.ExecEnv.1.Type="lxc:4.0.12"
    Device.SoftwareModules.ExecEnv.1.Vendor="Cthulhu"
    Device.SoftwareModules.ExecEnv.1.Version="3.9.0"
    Device.SoftwareModules.ExecutionUnit.1.
    Device.SoftwareModules.ExecutionUnit.1.Alias="cpe-a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.AllocatedCPUPercent=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedDiskSpace=-1
    Device.SoftwareModules.ExecutionUnit.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.AssociatedProcessList=""
    Device.SoftwareModules.ExecutionUnit.1.AutoStart=false
    Device.SoftwareModules.ExecutionUnit.1.AvailableDiskSpace=4737
    Device.SoftwareModules.ExecutionUnit.1.AvailableMemory=-1
    Device.SoftwareModules.ExecutionUnit.1.Description=""
    Device.SoftwareModules.ExecutionUnit.1.DiskSpaceInUse=39
    Device.SoftwareModules.ExecutionUnit.1.EUID="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecEnvLabel="a6995eb1-777e-52cd-aa7d-cec618548396"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionEnvRef="generic"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultCode="NoFault"
    Device.SoftwareModules.ExecutionUnit.1.ExecutionFaultMessage=""
    Device.SoftwareModules.ExecutionUnit.1.MemoryInUse=1768
    Device.SoftwareModules.ExecutionUnit.1.Name="piotrnakraszewicz/alpine64"
    Device.SoftwareModules.ExecutionUnit.1.References=""
    Device.SoftwareModules.ExecutionUnit.1.RunLevel=0
    Device.SoftwareModules.ExecutionUnit.1.Status="Stopping"
    Device.SoftwareModules.ExecutionUnit.1.Vendor=""
    Device.SoftwareModules.ExecutionUnit.1.VendorConfigList=""
    Device.SoftwareModules.ExecutionUnit.1.VendorLogList=""
    Device.SoftwareModules.ExecutionUnit.1.Version="latest"
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.
    Device.SoftwareModules.ExecutionUnit.1.NetworkConfig.X_PRPL-COM_DNSSDRefList=""
    Device.SoftwareModules.NetworkConfig.
    Device.SoftwareModules.NetworkConfig.DefaultBridge=""
    Device.SoftwareModules.NetworkConfig.DefaultFirewallChain=""

    root@Filogic-GW:~# 
    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4                                                                             IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 RUNNING 0         -      192.168.0.1, 192.168.0.10, 192.168.101.3, 192.168.106.1, 192.168.245.1 -    false        
    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4                                                                             IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 RUNNING 0         -      192.168.0.1, 192.168.0.10, 192.168.101.3, 192.168.106.1, 192.168.245.1 -    false        
    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4                                                                             IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 RUNNING 0         -      192.168.0.1, 192.168.0.10, 192.168.101.3, 192.168.106.1, 192.168.245.1 -    false        
    root@Filogic-GW:~# lxc-ls -f
    NAME                                 STATE   AUTOSTART GROUPS IPV4 IPV6 UNPRIVILEGED 
    a6995eb1-777e-52cd-aa7d-cec618548396 STOPPED 0         -      -    -    false        
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.DeploymentUnit.1.Uninstall( RetainData = "false")'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.DeploymentUnit.1.Uninstall( RetainData = "false")

    root@Filogic-GW:~# 
    root@Filogic-GW:~# ba-cli 'Device.SoftwareModules.?'

    root - * - [bus-cli] (0)
    > > Device.SoftwareModules.?
    Device.SoftwareModules.
    Device.SoftwareModules.DeploymentUnitNumberOfEntries=0
    Device.SoftwareModules.ExecEnvNumberOfEntries=1
    Device.SoftwareModules.ExecutionUnitNumberOfEntries=0
    Device.SoftwareModules.ExecEnv.1.
    Device.SoftwareModules.ExecEnv.1.ActiveExecutionUnits=""
    Device.SoftwareModules.ExecEnv.1.Alias="cpe-generic"
    Device.SoftwareModules.ExecEnv.1.AllocatedCPUPercent=100
    Device.SoftwareModules.ExecEnv.1.AllocatedDiskSpace=5120
    Device.SoftwareModules.ExecEnv.1.AllocatedMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableDiskSpace=4761
    Device.SoftwareModules.ExecEnv.1.AvailableMemory=-1
    Device.SoftwareModules.ExecEnv.1.AvailableRoles=""
    Device.SoftwareModules.ExecEnv.1.CreatedAt=2022-04-28T17:42:57Z
    Device.SoftwareModules.ExecEnv.1.CurrentRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.Description=""
    Device.SoftwareModules.ExecEnv.1.Enable=true
    Device.SoftwareModules.ExecEnv.1.InitialExecutionUnitRunLevel=-1
    Device.SoftwareModules.ExecEnv.1.InitialRunLevel=0
    Device.SoftwareModules.ExecEnv.1.Name="generic"
    Device.SoftwareModules.ExecEnv.1.ParentExecEnv=""
    Device.SoftwareModules.ExecEnv.1.ProcessorRefList=""
    Device.SoftwareModules.ExecEnv.1.RestartReason=""
    Device.SoftwareModules.ExecEnv.1.Status="Up"
    Device.SoftwareModules.ExecEnv.1.Type="lxc:4.0.12"
    Device.SoftwareModules.ExecEnv.1.Vendor="Cthulhu"
    Device.SoftwareModules.ExecEnv.1.Version="3.9.0"
    Device.SoftwareModules.NetworkConfig.
    Device.SoftwareModules.NetworkConfig.DefaultBridge=""
    Device.SoftwareModules.NetworkConfig.DefaultFirewallChain=""

    root@Filogic-GW:~# 
    root@Filogic-GW:~# lxc-ls -f
    root@Filogic-GW:~# 
    ```