@echo off
rem ------ Real Code Start --------------------------------------------------------------
rem ------ Code Runnable Start ----------------------------------------------------------

rem ------ Caution:Root User Only -------------------------------------------------------
rem ------ Ask user to run --------------------------------------------------------------
echo "You're losing some Network setting!!" 
set /P ANSWER="Are you sure ? (Y/N)ÅH"
rem ------ Requesting Green light -------------------------------------------------------
if /i {%ANSWER%}=={y} (goto :yes)
if /i {%ANSWER%}=={yes} (goto :yes)
rem ------ Bye --------------------------------------------------------------------------
exit
rem ------ Rock'n role ------------------------------------------------------------------
:yes
rem ------ IPv6 Tunnel Interface --------------------------------------------------------
rem ------ Command to check the setting before run --------------------------------------
rem netsh interface ipv6 show interface
rem netsh interface tcp show global
rem ------ ISATAP Interface Setting -----------------------------------------------------
netsh interface ipv6 isatap set state disabled
rem ------ 6to4 Interface Setting -------------------------------------------------------
netsh interface ipv6 6to4 set state disabled
rem ------ Teredo Interface Setting -----------------------------------------------------
netsh interface teredo set state disabled

rem ------ Autotuninglevel setting ------------------------------------------------------
netsh interface tcp set global autotuninglevel=restricted

rem ------ Disabling SNP Settings -------------------------------------------------------
rem ------ Disabling RSS ----------------------------------------------------------------
netsh int tcp set global rss=disabled
rem ------ Disabling TCP Chimney Offload ------------------------------------------------
netsh int tcp set global chimney=disabled
rem ------ Disabling TCP Network Direct Memory Access -----------------------------------
netsh int tcp set global netdma=disabled

rem ------ It's all done! ---------------------------------------------------------------
exit

rem ------ Code Runnable End ------------------------------------------------------------
rem ------ Real Code End ----------------------------------------------------------------
