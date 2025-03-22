v {xschem version=3.4.6RC file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 130 -30 170 -30 {lab=VG}
N 210 90 210 110 {lab=GND}
N 310 -170 310 -150 {lab=GND}
N 50 -30 130 -30 {lab=VG}
N 210 -170 210 -90 {lab=GND}
N 210 -170 310 -170 {lab=GND}
N 200 -40 230 -40 {lab=GND}
N 230 -70 230 -40 {lab=GND}
N 210 -70 230 -70 {lab=GND}
N 210 0 210 30 {lab=VD}
N 50 -30 50 0 {lab=VG}
N 50 60 50 100 {lab=GND}
N 50 100 210 100 {lab=GND}
N 310 -150 310 -80 {lab=GND}
N 210 -90 210 -60 {lab=GND}
C {vsource.sym} 50 30 0 0 {name=VSG value=3 savecurrent=false}
C {gnd.sym} 310 -80 0 0 {name=l2 lab=GND}
C {gnd.sym} 210 110 0 0 {name=l3 lab=GND}
C {lab_pin.sym} 50 -30 0 0 {name=p1 sig_type=std_logic lab=VG}
C {code_shown.sym} -80 -290 0 0 {name=dc_sweep only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.dc VG 0 1 0.01 VD 0 1 0.1
.save @XM1[gm]
.save i(vds)
.save @m.xm1.msky130_fd_pr__nfet_01v8[gds]
.save @m.xm1.msky130_fd_pr__nfet_01v8[cgg]
.save @m.xm1.msky130_fd_pr__nfet_01v8[ft]
.save all
.op
.end"}
C {sky130_fd_pr/pfet3_01v8.sym} 190 -30 0 0 {name=M2
W=1
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {vsource.sym} 210 60 0 0 {name=VDg value=3 savecurrent=false}
C {lab_pin.sym} 210 10 0 0 {name=p3 sig_type=std_logic lab=VD}
