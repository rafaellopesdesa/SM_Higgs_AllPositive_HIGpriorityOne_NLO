# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 10.0 for Mac OS X x86 (64-bit) (December 4, 2014)
# Date: Sun 28 Aug 2016 17:44:52


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_146_26,(0,0,1):C.R2GC_146_27,(0,1,0):C.R2GC_149_28,(0,1,1):C.R2GC_149_29,(0,2,0):C.R2GC_149_28,(0,2,1):C.R2GC_149_29,(0,3,0):C.R2GC_146_26,(0,3,1):C.R2GC_146_27,(0,4,0):C.R2GC_146_26,(0,4,1):C.R2GC_146_27,(0,5,0):C.R2GC_149_28,(0,5,1):C.R2GC_149_29})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_110_5,(2,0,1):C.R2GC_110_6,(0,0,0):C.R2GC_110_5,(0,0,1):C.R2GC_110_6,(4,0,0):C.R2GC_108_1,(4,0,1):C.R2GC_108_2,(3,0,0):C.R2GC_108_1,(3,0,1):C.R2GC_108_2,(8,0,0):C.R2GC_109_3,(8,0,1):C.R2GC_109_4,(7,0,0):C.R2GC_114_12,(7,0,1):C.R2GC_155_34,(5,0,0):C.R2GC_108_1,(5,0,1):C.R2GC_108_2,(1,0,0):C.R2GC_108_1,(1,0,1):C.R2GC_108_2,(6,0,0):C.R2GC_113_10,(6,0,1):C.R2GC_156_35,(11,0,0):C.R2GC_112_8,(11,0,1):C.R2GC_112_9,(10,0,0):C.R2GC_112_8,(10,0,1):C.R2GC_112_9,(9,0,1):C.R2GC_111_7,(2,1,0):C.R2GC_110_5,(2,1,1):C.R2GC_110_6,(0,1,0):C.R2GC_110_5,(0,1,1):C.R2GC_110_6,(6,1,0):C.R2GC_152_30,(6,1,1):C.R2GC_152_31,(4,1,0):C.R2GC_108_1,(4,1,1):C.R2GC_108_2,(3,1,0):C.R2GC_108_1,(3,1,1):C.R2GC_108_2,(8,1,0):C.R2GC_109_3,(8,1,1):C.R2GC_157_36,(7,1,0):C.R2GC_114_12,(7,1,1):C.R2GC_114_13,(5,1,0):C.R2GC_108_1,(5,1,1):C.R2GC_108_2,(1,1,0):C.R2GC_108_1,(1,1,1):C.R2GC_108_2,(11,1,0):C.R2GC_112_8,(11,1,1):C.R2GC_112_9,(10,1,0):C.R2GC_112_8,(10,1,1):C.R2GC_112_9,(9,1,1):C.R2GC_111_7,(2,2,0):C.R2GC_110_5,(2,2,1):C.R2GC_110_6,(0,2,0):C.R2GC_110_5,(0,2,1):C.R2GC_110_6,(4,2,0):C.R2GC_108_1,(4,2,1):C.R2GC_108_2,(3,2,0):C.R2GC_108_1,(3,2,1):C.R2GC_108_2,(8,2,0):C.R2GC_109_3,(8,2,1):C.R2GC_154_33,(6,2,0):C.R2GC_113_10,(6,2,1):C.R2GC_113_11,(7,2,0):C.R2GC_153_32,(7,2,1):C.R2GC_110_6,(5,2,0):C.R2GC_108_1,(5,2,1):C.R2GC_108_2,(1,2,0):C.R2GC_108_1,(1,2,1):C.R2GC_108_2,(11,2,0):C.R2GC_112_8,(11,2,1):C.R2GC_112_9,(10,2,0):C.R2GC_112_8,(10,2,1):C.R2GC_112_9,(9,2,1):C.R2GC_111_7})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_143_22})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_165_40})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_118_17})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_118_17})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_118_17})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_115_14})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_115_14})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_115_14})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_18})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_163_38,(0,1,0):C.R2GC_164_39})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_38,(0,1,0):C.R2GC_164_39})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_163_38,(0,1,0):C.R2GC_164_39})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_141_20,(0,1,0):C.R2GC_142_21})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_141_20,(0,1,0):C.R2GC_142_21})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_141_20,(0,1,0):C.R2GC_142_21})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_161_37,(0,2,0):C.R2GC_161_37,(0,1,0):C.R2GC_117_16,(0,3,0):C.R2GC_117_16})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_140_19,(0,2,0):C.R2GC_140_19,(0,1,0):C.R2GC_117_16,(0,3,0):C.R2GC_117_16})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_145_25,(0,1,0):C.R2GC_84_41,(0,1,3):C.R2GC_84_42,(0,2,1):C.R2GC_144_23,(0,2,2):C.R2GC_144_24})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_85_43,(0,0,1):C.R2GC_85_44})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_96_59,(0,1,0):C.R2GC_96_59,(0,2,0):C.R2GC_96_59})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_89_51,(0,0,1):C.R2GC_89_52,(0,1,0):C.R2GC_89_51,(0,1,1):C.R2GC_89_52,(0,2,0):C.R2GC_89_51,(0,2,1):C.R2GC_89_52})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_92_57,(0,0,1):C.R2GC_92_58,(0,1,0):C.R2GC_92_57,(0,1,1):C.R2GC_92_58,(0,2,0):C.R2GC_92_57,(0,2,1):C.R2GC_92_58})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_87_47,(0,0,1):C.R2GC_87_48,(0,1,0):C.R2GC_87_47,(0,1,1):C.R2GC_87_48,(0,2,0):C.R2GC_87_47,(0,2,1):C.R2GC_87_48})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_91_55,(1,0,1):C.R2GC_91_56,(0,1,0):C.R2GC_90_53,(0,1,1):C.R2GC_90_54,(0,2,0):C.R2GC_90_53,(0,2,1):C.R2GC_90_54,(0,3,0):C.R2GC_90_53,(0,3,1):C.R2GC_90_54})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_88_49,(0,0,1):C.R2GC_88_50,(0,1,0):C.R2GC_88_49,(0,1,1):C.R2GC_88_50,(0,2,0):C.R2GC_88_49,(0,2,1):C.R2GC_88_50})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_86_45,(0,0,1):C.R2GC_86_46})

V_44 = CTVertex(name = 'V_44',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_146_45,(0,0,1):C.UVGC_146_46,(0,0,2):C.UVGC_146_47,(0,0,3):C.UVGC_107_7,(0,0,4):C.UVGC_146_48,(0,1,0):C.UVGC_149_53,(0,1,1):C.UVGC_149_54,(0,1,2):C.UVGC_149_55,(0,1,3):C.UVGC_149_56,(0,1,4):C.UVGC_149_57,(0,3,0):C.UVGC_149_53,(0,3,1):C.UVGC_149_54,(0,3,2):C.UVGC_151_60,(0,3,3):C.UVGC_106_5,(0,3,4):C.UVGC_149_57,(0,5,0):C.UVGC_146_45,(0,5,1):C.UVGC_146_46,(0,5,2):C.UVGC_148_51,(0,5,3):C.UVGC_148_52,(0,5,4):C.UVGC_146_48,(0,6,0):C.UVGC_146_45,(0,6,1):C.UVGC_146_46,(0,6,2):C.UVGC_147_49,(0,6,3):C.UVGC_147_50,(0,6,4):C.UVGC_146_48,(0,7,0):C.UVGC_149_53,(0,7,1):C.UVGC_149_54,(0,7,2):C.UVGC_150_58,(0,7,3):C.UVGC_150_59,(0,7,4):C.UVGC_149_57,(0,2,2):C.UVGC_106_4,(0,2,3):C.UVGC_106_5,(0,4,2):C.UVGC_107_6,(0,4,3):C.UVGC_107_7})

V_45 = CTVertex(name = 'V_45',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_109_11,(2,0,4):C.UVGC_109_10,(0,0,3):C.UVGC_109_11,(0,0,4):C.UVGC_109_10,(4,0,3):C.UVGC_108_8,(4,0,4):C.UVGC_108_9,(3,0,3):C.UVGC_108_8,(3,0,4):C.UVGC_108_9,(8,0,3):C.UVGC_109_10,(8,0,4):C.UVGC_109_11,(7,0,0):C.UVGC_155_72,(7,0,2):C.UVGC_155_73,(7,0,3):C.UVGC_155_74,(7,0,4):C.UVGC_155_75,(7,0,5):C.UVGC_155_76,(5,0,3):C.UVGC_108_8,(5,0,4):C.UVGC_108_9,(1,0,3):C.UVGC_108_8,(1,0,4):C.UVGC_108_9,(6,0,0):C.UVGC_155_72,(6,0,2):C.UVGC_155_73,(6,0,3):C.UVGC_156_77,(6,0,4):C.UVGC_156_78,(6,0,5):C.UVGC_155_76,(11,0,3):C.UVGC_112_14,(11,0,4):C.UVGC_112_15,(10,0,3):C.UVGC_112_14,(10,0,4):C.UVGC_112_15,(9,0,3):C.UVGC_111_12,(9,0,4):C.UVGC_111_13,(2,1,3):C.UVGC_109_11,(2,1,4):C.UVGC_109_10,(0,1,3):C.UVGC_109_11,(0,1,4):C.UVGC_109_10,(6,1,0):C.UVGC_152_61,(6,1,3):C.UVGC_152_62,(6,1,4):C.UVGC_152_63,(6,1,5):C.UVGC_152_64,(4,1,3):C.UVGC_108_8,(4,1,4):C.UVGC_108_9,(3,1,3):C.UVGC_108_8,(3,1,4):C.UVGC_108_9,(8,1,0):C.UVGC_157_79,(8,1,2):C.UVGC_157_80,(8,1,3):C.UVGC_157_81,(8,1,4):C.UVGC_157_82,(8,1,5):C.UVGC_157_83,(7,1,1):C.UVGC_113_16,(7,1,3):C.UVGC_114_18,(7,1,4):C.UVGC_114_19,(5,1,3):C.UVGC_108_8,(5,1,4):C.UVGC_108_9,(1,1,3):C.UVGC_108_8,(1,1,4):C.UVGC_108_9,(11,1,3):C.UVGC_112_14,(11,1,4):C.UVGC_112_15,(10,1,3):C.UVGC_112_14,(10,1,4):C.UVGC_112_15,(9,1,3):C.UVGC_111_12,(9,1,4):C.UVGC_111_13,(2,2,3):C.UVGC_109_11,(2,2,4):C.UVGC_109_10,(0,2,3):C.UVGC_109_11,(0,2,4):C.UVGC_109_10,(4,2,3):C.UVGC_108_8,(4,2,4):C.UVGC_108_9,(3,2,3):C.UVGC_108_8,(3,2,4):C.UVGC_108_9,(8,2,0):C.UVGC_154_67,(8,2,2):C.UVGC_154_68,(8,2,3):C.UVGC_154_69,(8,2,4):C.UVGC_154_70,(8,2,5):C.UVGC_154_71,(6,2,1):C.UVGC_113_16,(6,2,3):C.UVGC_113_17,(6,2,4):C.UVGC_111_12,(7,2,0):C.UVGC_152_61,(7,2,3):C.UVGC_153_65,(7,2,4):C.UVGC_153_66,(7,2,5):C.UVGC_152_64,(5,2,3):C.UVGC_108_8,(5,2,4):C.UVGC_108_9,(1,2,3):C.UVGC_108_8,(1,2,4):C.UVGC_108_9,(11,2,3):C.UVGC_112_14,(11,2,4):C.UVGC_112_15,(10,2,3):C.UVGC_112_14,(10,2,4):C.UVGC_112_15,(9,2,3):C.UVGC_111_12,(9,2,4):C.UVGC_111_13})

V_46 = CTVertex(name = 'V_46',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_143_38})

V_47 = CTVertex(name = 'V_47',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_165_92})

V_48 = CTVertex(name = 'V_48',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_118_23,(0,1,0):C.UVGC_105_3,(0,2,0):C.UVGC_105_3})

V_49 = CTVertex(name = 'V_49',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_118_23,(0,1,0):C.UVGC_105_3,(0,2,0):C.UVGC_105_3})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_118_23,(0,1,0):C.UVGC_159_85,(0,2,0):C.UVGC_159_85})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_115_20,(0,1,0):C.UVGC_101_2,(0,2,0):C.UVGC_101_2})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_115_20,(0,1,0):C.UVGC_101_2,(0,2,0):C.UVGC_101_2})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_115_20,(0,1,0):C.UVGC_138_33,(0,2,0):C.UVGC_138_33})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,1):C.UVGC_119_25,(0,1,2):C.UVGC_119_26,(0,1,3):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,4):C.UVGC_119_29,(0,2,0):C.UVGC_119_24,(0,2,1):C.UVGC_119_25,(0,2,2):C.UVGC_119_26,(0,2,3):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,4):C.UVGC_119_29})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,1):C.UVGC_119_25,(0,1,3):C.UVGC_119_26,(0,1,4):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,2):C.UVGC_119_29,(0,2,0):C.UVGC_119_24,(0,2,1):C.UVGC_119_25,(0,2,3):C.UVGC_119_26,(0,2,4):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,2):C.UVGC_119_29})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,1):C.UVGC_119_25,(0,1,2):C.UVGC_119_26,(0,1,3):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,4):C.UVGC_160_86,(0,2,0):C.UVGC_119_24,(0,2,1):C.UVGC_119_25,(0,2,2):C.UVGC_119_26,(0,2,3):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,4):C.UVGC_160_86})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,1):C.UVGC_119_25,(0,1,3):C.UVGC_119_26,(0,1,4):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,2):C.UVGC_119_29,(0,2,0):C.UVGC_119_24,(0,2,1):C.UVGC_119_25,(0,2,3):C.UVGC_119_26,(0,2,4):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,2):C.UVGC_119_29})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,1):C.UVGC_119_25,(0,1,2):C.UVGC_119_26,(0,1,3):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,4):C.UVGC_119_29,(0,2,0):C.UVGC_119_24,(0,2,1):C.UVGC_119_25,(0,2,2):C.UVGC_119_26,(0,2,3):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,4):C.UVGC_119_29})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_116_21,(0,1,0):C.UVGC_119_24,(0,1,2):C.UVGC_119_25,(0,1,3):C.UVGC_119_26,(0,1,4):C.UVGC_119_27,(0,1,5):C.UVGC_119_28,(0,1,1):C.UVGC_139_34,(0,2,0):C.UVGC_119_24,(0,2,2):C.UVGC_119_25,(0,2,3):C.UVGC_119_26,(0,2,4):C.UVGC_119_27,(0,2,5):C.UVGC_119_28,(0,2,1):C.UVGC_139_34})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_135_30,(0,0,1):C.UVGC_135_31})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_135_30,(0,0,1):C.UVGC_135_31})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_162_88,(0,0,2):C.UVGC_162_89,(0,0,1):C.UVGC_135_31})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_135_30,(0,0,1):C.UVGC_135_31})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_135_30,(0,0,1):C.UVGC_135_31})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_162_88,(0,0,2):C.UVGC_162_89,(0,0,1):C.UVGC_135_31})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_163_90,(0,1,0):C.UVGC_164_91})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_141_36,(0,1,0):C.UVGC_142_37})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_117_22,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_117_22,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_161_87,(0,2,0):C.UVGC_161_87,(0,1,0):C.UVGC_158_84,(0,3,0):C.UVGC_158_84})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_117_22,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_117_22,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_140_35,(0,2,0):C.UVGC_140_35,(0,1,0):C.UVGC_137_32,(0,3,0):C.UVGC_137_32})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_145_41,(0,0,1):C.UVGC_145_42,(0,0,2):C.UVGC_145_43,(0,0,3):C.UVGC_145_44,(0,1,0):C.UVGC_144_39,(0,1,3):C.UVGC_144_40})

