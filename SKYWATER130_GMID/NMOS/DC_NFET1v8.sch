v {xschem version=3.4.6RC file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 100 -130 100 -90 {lab=VDS}
N 20 -60 60 -60 {lab=VGS}
N 100 -30 100 10 {lab=GND}
N -60 20 -60 40 {lab=GND}
N 100 10 100 30 {lab=GND}
N 200 -120 200 -100 {lab=GND}
N -60 -60 -60 -30 {lab=VGS}
N 200 -200 200 -180 {lab=VDS}
N 100 -60 100 -30 {lab=GND}
N -60 -60 20 -60 {lab=VGS}
N 100 -200 100 -120 {lab=VDS}
N 100 -200 200 -200 {lab=VDS}
C {sky130_fd_pr/nfet_01v8.sym} 80 -60 0 0 {name=M1
W=1
L=0.15
nf=1 
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {vsource.sym} 200 -150 0 0 {name=VD value=3 savecurrent=false}
C {vsource.sym} -60 -10 0 0 {name=VG value=3 savecurrent=false}
C {gnd.sym} -60 40 0 0 {name=l1 lab=GND}
C {gnd.sym} 200 -100 0 0 {name=l2 lab=GND}
C {gnd.sym} 100 30 0 0 {name=l3 lab=GND}
C {lab_pin.sym} -60 -60 0 0 {name=p1 sig_type=std_logic lab=VGS}
C {lab_pin.sym} 100 -200 0 0 {name=p2 sig_type=std_logic lab=VDS}
C {code_shown.sym} -190 -320 0 0 {name=dc_sweep only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.dc VG 0 1 0.01 VD 0 1 0.1
.save @XM1[gm]
.save i(vds)
.save @m.xm1.msky130_fd_pr__nfet_01v8[gds]
.save @m.xm1.msky130_fd_pr__nfet_01v8[cgg]
.save @m.xm1.msky130_fd_pr__nfet_01v8[ft]
.save all
.op
.end"}
