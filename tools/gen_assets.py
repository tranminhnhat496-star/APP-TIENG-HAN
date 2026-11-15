import os
O='/mnt/user-data/outputs/Korean_Vocab_Farm_V3'
K='#5A3A22';D='#3A2E22'
def w(p,body,vb='0 0 128 128',css=''):
    f=f'{O}/assets/{p}.svg';os.makedirs(os.path.dirname(f),exist_ok=True)
    st=f'<style>*{{transform-box:fill-box}}{css}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>' if css else ''
    open(f,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{st}{body}</svg>')
def G(b,sw=4):return f'<g stroke="{K}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round">{b}</g>'
def E(x,y,rx,ry,f,x2=''):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{f}" {x2}/>'
def C(x,y,r,f,x2=''):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" {x2}/>'
def P(d,f='none',x2=''):return f'<path d="{d}" fill="{f}" {x2}/>'
def R(x,y,wd,h,r,f,x2=''):return f'<rect x="{x}" y="{y}" width="{wd}" height="{h}" rx="{r}" fill="{f}" {x2}/>'
NS='stroke="none"'
def eye(x,y):return C(x,y,5.5,D,NS)+C(x+1.8,y-2,1.9,'#fff',NS)
def cheeks(a,b,y):return E(a,y,7,5,'#FF9A76',NS)+E(b,y,7,5,'#FF9A76',NS)
def face(a=50,b=78,y=64):return eye(a,y)+eye(b,y)+cheeks(a-10,b+10,y+11)
# ---------- mascot ----------
Y,OR='#FFD34D','#FF8A3D'
def chick(s):
    anim={'idle':'bob 2.4s ease-in-out infinite','hello':'bob 1.6s ease-in-out infinite','happy':'hop .55s ease-in-out infinite','sad':'sag 2.4s ease-in-out infinite','sleep':'br 3s ease-in-out infinite','jump':'jmp .9s ease-in-out infinite'}[s]
    arcs=P('M44 66q6-9 12 0M72 66q6-9 12 0','none',f'stroke="{K}"')
    eyes={'idle':eye(50,64)+eye(78,64),'hello':eye(50,64)+eye(78,64),'happy':arcs,'jump':arcs,
     'sad':eye(50,66)+eye(78,66)+P('M42 54l14 6M86 54l-14 6','none',f'stroke="{K}"')+P('M50 76q-5 8 0 10q5-2 0-10','#8FD3F4','stroke="#4A9FD0" stroke-width="2" style="animation:tr 1.6s linear infinite"'),
     'sleep':P('M44 64q6 6 12 0M72 64q6 6 12 0','none',f'stroke="{K}"')}[s]
    beak=P('M56 75h16q-2 13-8 13t-8-13z','#E5533D',f'stroke="{K}"')+E(64,84,4,3,'#FF9A9A',NS) if s in('happy','jump') else P('M58 76l6 7 6-7z' if s!='sad' else 'M59 79l5 5 5-5z',OR)
    up=s in('jump',)
    lw=f'<g style="transform-origin:90% 90%;animation:{"wv .5s ease-in-out infinite alternate" if s=="hello" else "none"}">'
    wings=E(26,80 if not up else 62,10,15,Y,'transform="rotate(-18 26 80)"' if not up else 'transform="rotate(35 26 62)"')+(lw+E(102,80 if s!='hello' else 58,10,15,Y,'transform="rotate(18 102 80)"' if s!='hello' else 'transform="rotate(-35 102 58)"')+'</g>' if s!='jump' else E(102,62,10,15,Y,'transform="rotate(-35 102 62)"'))
    ex=''
    star=lambda x,y,sc=1:P(f'M{x} {y}l3 8 8 3-8 3-3 8-3-8-8-3 8-3z','#FFC83D',f'stroke="none" transform="scale({sc})" style="animation:tw 1s ease-in-out infinite"')
    if s in('happy','jump'):ex=star(102,18)+star(10,30)+star(100,96)
    if s=='sleep':ex=''.join(f'<text x="{x}" y="{y}" font-family="sans-serif" font-weight="800" font-size="{z}" fill="#6B7FD7" style="animation:zz 2.4s ease-in {d}s infinite">Z</text>' for x,y,z,d in((92,38,18,0),(104,24,13,.8)))
    body=G(P('M58 32q-4-12 2-14M64 31q0-14 6-16M70 33q4-10 10-8','none')+E(52,112,0.1,0.1,'none')+P('M52 108v9M44 117h16M76 108v9M68 117h16','none',f'stroke="{OR}"')+E(64,72,40,38,Y)+E(64,88,24,19,'#FFF0A8',NS)+wings)+eyes+cheeks(40,88,76)+G(beak)
    body='<g style="animation:'+anim+';transform-origin:50% 100%">'+body+'</g>'
    css='@keyframes bob{50%{transform:translateY(-3px)}}@keyframes hop{50%{transform:translateY(-12px) scaleY(1.05)}}@keyframes sag{50%{transform:scaleY(.97)}}@keyframes br{50%{transform:scale(1.03,.98)}}@keyframes jmp{0%,100%{transform:translateY(0) scale(1.08,.9)}45%{transform:translateY(-18px) scale(.95,1.08)}}@keyframes wv{to{transform:rotate(-30deg)}}@keyframes tw{50%{opacity:.2}}@keyframes tr{to{transform:translateY(22px);opacity:0}}@keyframes zz{0%{opacity:0;transform:translate(0,8px)}30%{opacity:1}100%{opacity:0;transform:translate(6px,-14px)}}'
    w('mascot/'+s,body+ex,css=css)
for s in('idle','hello','happy','sad','sleep','jump'):chick(s)
# ---------- bosses ----------
def eyeA(x,y,l=1):return E(x,y,6.5,7.5,'#fff')+C(x+1*l,y+1,3,D,NS)
def brow(a,b,c,d):return P(f'M{a} {b}L{c} {d}','none',f'stroke="{D}" stroke-width="5"')
fang=lambda x,y:P(f'M{x} {y}l4 9 4-9z','#fff')
w('bosses/dokkaebi',G(f'<g transform="translate(-12 6) rotate(22 104 80)">'+R(97,34,16,70,8,'#B07A44')+''.join(C(105,y,3,'#E8D5A8',NS) for y in(46,62,78))+'</g>'
 +E(44,118,13,7,'#C93E2B')+E(80,118,13,7,'#C93E2B')+E(62,82,38,36,'#E8503A')+P('M32 100q30 22 60 0v10q-30 14-60 0z','#FFC83D')
 +P('M36 52l-8-24 20 14zM88 52l8-24-20 14z','#FFF0C2')+E(26,94,9,12,'#E8503A')+C(90,102,10,'#E8503A')
 +eyeA(48,72)+eyeA(76,72,-1)+brow(36,62,56,70)+brow(88,62,68,70)+P('M42 90q20 16 40 0q-20 6-40 0z','#3A1A1A')+fang(49,92)+fang(67,92))
 ,css='g{animation:b 1.8s ease-in-out infinite}@keyframes b{50%{transform:translateY(-3px)}}')
tl=lambda d,c:P(d,'none',f'stroke="{K}" stroke-width="17"')+P(d,'none',f'stroke="{c}" stroke-width="9"')
w('bosses/yong',tl('M92 104q28 2 24-20q-2-9-10-4','#2BB5A3')+G(E(64,96,34,24,'#2BB5A3')+P('M48 98h32M50 108h28','none','stroke="#7FE0D1"')+P('M36 54l-16-6 8 14zM92 54l16-6-8 14z','#FF7A4D')
 +P('M44 38l-12-20 14 8zM84 38l12-20-14 8z','#FFF0C2')+E(64,58,30,26,'#2BB5A3')+E(64,72,19,12,'#7FE0D1')+C(58,71,2,D,NS)+C(70,71,2,D,NS)
 +eyeA(50,52)+eyeA(78,52,-1)+brow(38,43,58,51)+brow(90,43,70,51)+P('M46 76q-24-2-32 14M82 76q24-2 32 14','none',f'stroke="{D}" stroke-width="3"')+fang(55,79)+fang(69,79))
 ,css='@keyframes s{50%{transform:rotate(3deg)}}g>g{animation:s 2s ease-in-out infinite}')
w('bosses/gwisin',E(64,70,52,48,'#8E7CD8','stroke="none" opacity=".25"')+G(P('M32 114V62a32 32 0 0 1 64 0v52l-10-9-11 9-11-9-11 9-11-9z','#E4D9FF')+P('M32 62a32 32 0 0 1 64 0q-14-14-32-6q-18-8-32 6z','#2A2140')+P('M32 60q-6 30-2 52M96 60q6 30 2 52','none','stroke="#2A2140" stroke-width="7"'))
 +E(52,72,7,10,'#2A2140',NS)+E(76,72,7,10,'#2A2140',NS)+C(52,75,2.6,'#FFE45E',NS)+C(76,75,2.6,'#FFE45E',NS)+E(64,95,8,10,'#2A2140',NS)
 +G(E(26,96,8,14,'#E4D9FF','transform="rotate(14 26 96)"')+E(102,96,8,14,'#E4D9FF','transform="rotate(-14 102 96)"')),
 css='@keyframes f{50%{transform:translateY(-6px)}}svg>g{animation:f 2.2s ease-in-out infinite}')
w('bosses/gangsi',G(R(12,74,34,13,6,'#3D5A80')+R(82,74,34,13,6,'#3D5A80')+E(14,81,8,9,'#A8D8C0')+E(114,81,8,9,'#A8D8C0')+P('M38 70h52l6 44h-64z','#3D5A80')+P('M64 70v44','none','stroke="#FFC83D"')
 +R(38,112,22,9,4,'#2A2A3A')+R(68,112,22,9,4,'#2A2A3A')+E(64,50,24,22,'#A8D8C0')+P('M36 36h56l-7-20h-42z','#2A2A3A')+P('M42 28h44','none','stroke="#FFC83D"')
 +R(55,34,18,24,2,'#FFE9A0')+P('M60 41h8M60 48h8M64 52v4','none','stroke="#D9503F" stroke-width="3"'))
 +eyeA(48,62)+eyeA(80,62,-1)+P('M54 70q10 7 20 0','#3A1A1A',f'stroke="{K}" stroke-width="3"')+fang(56,70)+fang(66,70),
 css='@keyframes h{50%{transform:translateY(-8px)}}svg>g{animation:h 1s ease-in-out infinite}')
w('bosses/gongnyong',G(tl('M90 104q30 2 26-22','#F29E4C')[0:0]+E(64,100,32,24,'#F29E4C')+E(64,106,18,14,'#FFE0A8',NS)+E(30,98,8,11,'#F29E4C')+E(98,98,8,11,'#F29E4C')+E(48,121,12,6,'#E0883A')+E(80,121,12,6,'#E0883A')
 +P('M40 34l4-16 10 12zM58 28l6-18 6 18zM74 30l10-12 4 16z','#E0533C')+C(64,54,30,'#F29E4C')+E(64,70,20,14,'#FFC27A')+C(57,67,2,D,NS)+C(71,67,2,D,NS)
 +eyeA(50,50)+eyeA(78,50,-1)+brow(38,42,58,50)+brow(90,42,70,50)+P('M50 76q14 12 28 0z','#3A1A1A')+fang(54,76)+fang(66,76))
 .replace('<g','<path d="M92 106q30 2 26-22" fill="none" stroke="%s" stroke-width="17" stroke-linecap="round"/><path d="M92 106q30 2 26-22" fill="none" stroke="#F29E4C" stroke-width="9" stroke-linecap="round"/><g'%K,1),
 css='@keyframes t{50%{transform:rotate(3deg)}}svg>g{animation:t 1.6s ease-in-out infinite;transform-origin:50% 100%}')
# ---------- pets ----------
def pet(n,body,head,extra_back='',extra_front=''):
    w('pets/'+n,G(extra_back+body+head)+extra_front+face(50,78,60),css='@keyframes b{50%{transform:translateY(-2px)}}svg>g{animation:b 2s ease-in-out infinite}')
ft=lambda c:E(46,116,10,6,c)+E(82,116,10,6,c)
pet('hen',ft(OR)+E(64,88,34,28,'#FFF')+E(34,92,9,14,'#F2EEE4','transform="rotate(14 34 92)"'),P('M52 34q-2-12 6-10q4-10 10-2q8-6 8 10z','#E5533D')+C(64,56,24,'#FFF')+P('M58 66l6 8 6-8z',OR)+P('M64 76q-4 8 0 10q4-2 0-10','#E5533D'))
pet('dog',ft('#C28A52')+E(64,92,30,24,'#D9A066'),E(28,52,10,18,'#A96E3A','transform="rotate(12 28 52)"')+E(100,52,10,18,'#A96E3A','transform="rotate(-12 100 52)"')+C(64,58,26,'#D9A066')+E(64,72,14,10,'#FFF0D6')+E(64,67,5,3.5,D,NS)+P('M60 78q4 6 8 0','#FF8FA0'))
pet('pig',ft('#F58BA1')+E(64,92,32,25,'#FFB3C1'),P('M42 38l-4-14 16 6zM86 38l4-14-16 6z','#F58BA1')+C(64,58,26,'#FFB3C1')+E(64,72,12,9,'#F58BA1')+C(60,72,2,D,NS)+C(68,72,2,D,NS))
pet('cow',ft('#B8B8B8')+E(64,92,34,25,'#FFF')+E(46,96,9,7,'#3A2E22',NS),P('M42 40q-6-10-12-6M86 40q6-10 12-6','none')+E(30,54,9,6,'#FFF','transform="rotate(-20 30 54)"')+E(98,54,9,6,'#FFF','transform="rotate(20 98 54)"')+C(64,58,26,'#FFF')+E(78,46,10,8,'#3A2E22',NS)+E(64,74,17,11,'#FFB3C1')+C(58,74,2.5,D,NS)+C(70,74,2.5,D,NS))
pet('sheep',ft('#5A4A42')+''.join(C(x,y,r,'#FFF') for x,y,r in((40,88,17),(88,88,17),(64,98,19),(50,74,16),(78,74,16))),E(28,60,9,6,'#5A4A42')+E(100,60,9,6,'#5A4A42')+''.join(C(x,y,r,'#FFF') for x,y,r in((46,38,12),(64,32,13),(82,38,12)))+E(64,60,22,22,'#5A4A42'))
pet('horse',ft('#7A4A24')+E(64,92,30,24,'#A66A3C'),P('M46 40l-2-18 12 10zM82 40l2-18-12 10z','#A66A3C')+P('M56 30q-6 20 0 34','none',f'stroke="{D}" stroke-width="8"')+E(64,58,24,26,'#A66A3C')+E(64,76,15,11,'#D9A066')+C(59,77,2,D,NS)+C(69,77,2,D,NS))
# ---------- decor / buildings (reusable inner svg) ----------
def tree(c='#4FB35A',c2='#3E9A4B'):return G(R(56,80,16,36,4,'#8B5E3C')+C(64,60,34,c)+C(44,72,18,c2)+C(86,70,18,c2)+C(64,40,18,c))
def house():return G(R(22,60,84,56,4,'#C99A62')+P('M12 64L64 20l52 44z','#C0452F')+R(52,80,24,36,3,'#8B5E3C')+R(28,74,18,18,2,'#BFE8F7')+R(84,74,18,18,2,'#BFE8F7')+R(88,28,12,22,2,'#8B5E3C')+P('M52 98h24','none','stroke="#6B4423" stroke-width="2"'))
def barn():return G(R(18,56,92,60,3,'#D9503F')+P('M10 60L64 16l54 44z','#B03A2E')+R(44,70,40,46,2,'#F5E6C8')+P('M44 70l40 46M84 70l-40 46','none','stroke="#D9503F" stroke-width="3"')+R(54,34,20,12,2,'#F5E6C8'))
def coop():return G(R(26,66,76,50,4,'#D9A066')+P('M18 70L64 36l46 34z','#C0452F')+E(64,96,12,14,'#3A2E22')+R(40,104,48,5,2,'#8B5E3C'))
def windmill():return G(P('M44 116L52 50h24l8 66z','#F5E6C8')+P('M48 50l16-18 16 18z','#C0452F')+R(56,92,16,24,3,'#8B5E3C'))+'<g style="transform-origin:50% 50%;animation:sp 6s linear infinite" stroke="'+K+'" stroke-width="4" stroke-linejoin="round"><path d="M64 44L50 10l14 6zM64 44l34 -14-6 14zM64 44l14 34-14-6zM64 44L30 58l6-14z" fill="#FFF8E1"/></g>'
def well():return G(R(34,70,60,42,5,'#B9B0A0')+P('M30 70L64 40l34 30z','#C0452F')+R(34,70,6,0,0,'none')+P('M40 70v-26M88 70v-26','none','stroke="#8B5E3C" stroke-width="5"')+E(64,98,18,8,'#5BB6E6',NS))
for n,f in(('house',house),('barn',barn),('coop',coop),('windmill',windmill),('well',well)):
    w('buildings/'+n,f(),css='@keyframes sp{to{transform:rotate(360deg)}}')
w('buildings/mailbox',G(R(58,60,12,56,3,'#8B5E3C')+R(36,32,56,34,12,'#3D7EC9')+R(78,22,6,22,1,'#E5533D')))
w('decor/tree',tree());w('decor/sakura',tree('#FFB7D0','#F58BB0'));w('decor/maple',tree('#F08A3C','#D9503F'))
w('decor/pumpkin',G(E(64,80,40,32,'#FF9A3D')+E(44,80,16,30,'#F58A28',NS)+E(84,80,16,30,'#F58A28',NS)+P('M64 50q2-14 12-16','none','stroke="#4E9C3F" stroke-width="7"')+P('M64 52v56','none','stroke="#D9751F" stroke-width="3"')))
w('decor/tractor',G(R(60,36,40,40,6,'#E5533D')+R(14,60,78,30,8,'#E5533D')+R(70,42,22,18,3,'#BFE8F7')+C(40,96,22,'#3A2E22')+C(40,96,9,'#FFC83D')+C(100,100,14,'#3A2E22')+C(100,100,6,'#FFC83D')))
w('decor/butterflies',G(P('M60 60q-30-30-34 0q2 26 34 12zM68 60q30-30 34 0q-2 26-34 12z','#FFB86B')+P('M60 76q-22 4-18 22q18 2 18-22zM68 76q22 4 18 22q-18 2-18-22z','#FF7A9C')+R(61,50,6,40,3,D)),css='path{animation:fl .5s ease-in-out infinite alternate;transform-origin:50% 50%}@keyframes fl{to{transform:scaleX(.8)}}')
w('decor/watermelon',G(P('M10 60a54 54 0 0 0 108 0z','#E5533D')+P('M10 60a54 54 0 0 0 108 0','none','stroke="#3E9A4B" stroke-width="9"')+''.join(E(x,y,3,5,D,NS) for x,y in((44,76),(64,86),(84,76),(64,70)))))
w('decor/windchime',G(P('M30 28h68','none')+R(36,24,56,10,4,'#C99A62')+''.join(P(f'M{x} 34v{h}','none','stroke="#7FD4E0" stroke-width="5"') for x,h in((44,40),(58,56),(72,48),(86,64)))+C(64,100,6,'#FFC83D')))
w('decor/moon',G(C(64,64,46,'#FFF3B0')+C(48,50,8,'#F2DD7A',NS)+C(80,78,10,'#F2DD7A',NS)+C(74,44,5,'#F2DD7A',NS)),css='@keyframes g{50%{opacity:.8}}circle:first-child{animation:g 3s infinite}')
w('decor/snowman',G(C(64,92,28,'#fff')+C(64,52,20,'#fff')+P('M62 52l16 4-16 4z',OR)+C(57,46,2.5,D,NS)+C(71,46,2.5,D,NS)+R(46,28,36,8,2,'#3D7EC9')+C(64,88,3,D,NS)+C(64,100,3,D,NS)))
w('decor/sweetpotato',G(P('M20 84q4-30 40-30q52 4 52 24q-4 22-44 22q-40 0-48-16z','#B9534A')+P('M44 70q20-6 48 4','none','stroke="#D98B7E" stroke-width="3"')+P('M108 66q10-6 8-14','none','stroke="#8B5E3C"')))
# ---------- crops ----------
def mound():return E(64,110,38,12,'#6B4423')+P('M30 110q10-18 34-18t34 18z','#8B5E3C',f'stroke="{K}" stroke-width="4"')
lf=lambda x,y,a,c='#7BC043',s=1:E(x,y,10*s,5*s,c,f'transform="rotate({a} {x} {y})"')
CR={'carrot':('#5FB84A','#fff',lambda:P('M54 78h20l-10 36z','#FF8A3D')+P('M60 88h8M62 98h4','none','stroke="#D9751F" stroke-width="2"')),
'tomato':('#4FA34A','#FFD84D',lambda:''.join(C(x,y,10,'#E5533D')+P(f'M{x-5} {y-9}l5 4 5-4','none','stroke="#3E9A4B"') for x,y in((46,84),(82,78),(64,98)))),
'corn':('#7BC043','#FFD84D',lambda:E(64,72,11,24,'#FFD84D')+P('M64 48v48','none','stroke="#E0B020" stroke-width="2"')+P('M52 96q-4-30 12-46M76 96q4-30-12-46','#7BC043')),
'strawberry':('#4FA34A','#fff',lambda:''.join(P(f'M{x-10} {y-8}q10-6 20 0q-2 16-10 18q-8-2-10-18z','#E5533D')+P(f'M{x-6} {y-9}l6 5 6-5','none','stroke="#3E9A4B"') for x,y in((46,86),(82,82),(64,100)))),
'eggplant':('#5FB84A','#C9A0F0',lambda:''.join(E(x,y,9,17,'#7B3FA8','transform="rotate(%d %d %d)"'%(a,x,y))+P(f'M{x-6} {y-15}h12','none','stroke="#3E9A4B" stroke-width="5"') for x,y,a in((48,86,12),(80,84,-12)))),
'potato':('#6BB04A','#fff',lambda:E(50,106,13,9,'#C99A62')+E(78,106,15,10,'#B8864F')+C(64,100,9,'#D9AA70'))}
for n,(lc,fc,fr) in CR.items():
    st=[E(64,104,5,7,'#C99A62','transform="rotate(20 64 104)"')+mound()[:0],
        P('M64 96v-16','none','stroke="#4E9C3F" stroke-width="4"')+lf(54,80,-30,lc)+lf(74,80,30,lc),
        P('M64 96v-36','none','stroke="#4E9C3F" stroke-width="4"')+lf(52,82,-30,lc)+lf(76,82,30,lc)+lf(52,66,-40,lc,.9)+lf(76,66,40,lc,.9)+lf(64,56,-90,lc,.8),
        P('M64 96v-52','none','stroke="#4E9C3F" stroke-width="4"')+lf(48,84,-30,lc,1.2)+lf(80,84,30,lc,1.2)+lf(50,66,-40,lc,1.1)+lf(78,66,40,lc,1.1)+lf(64,42,-90,lc,.9)+C(56,52,4,fc)+C(74,56,4,fc)+C(64,36,4,fc),
        lf(46,70,-30,lc,1.2)+lf(82,70,30,lc,1.2)+lf(64,38,-90,lc,.9)+fr()]
    for i,s in enumerate(st):w(f'crops/{n}_{i}',mound()+G(s,3.5))
w('crops/wilt',mound()+G(P('M64 100q-2-14 8-26','none','stroke="#8A6A3A" stroke-width="4"')+E(76,70,10,5,'#B08A4A','transform="rotate(70 76 70)"')+E(52,90,9,4,'#B08A4A','transform="rotate(-40 52 90)"'),3.5))
w('crops/pest',mound()+G(P('M64 96v-30','none','stroke="#4E9C3F" stroke-width="4"')+lf(52,78,-30)+lf(76,78,30)+E(64,58,9,7,'#E5533D')+C(60,56,2,D,NS)+C(68,56,2,D,NS)+P('M60 50l-3-5M68 50l3-5','none',f'stroke="{D}" stroke-width="2"'),3.5))
# ---------- icons (64) ----------
def ic(n,b):w('icons/'+n,G(b,3.5),'0 0 64 64')
ic('learn',P('M32 54V34','none','stroke="#4E9C3F" stroke-width="5"')+P('M32 38q-18 2-20-16q18-2 20 16z','#7BC043')+P('M32 34q18 2 20-16-18-2-20 16z','#5FB84A')+R(14,54,36,6,3,'#8B5E3C'))
ic('book',R(10,12,44,42,5,'#3D7EC9')+R(16,18,32,30,2,'#FFF8E1')+P('M22 26h20M22 34h20M22 42h12','none','stroke="#C99A62" stroke-width="3"'))
ic('shop',P('M8 22l6-12h36l6 12z','#E5533D')+R(12,22,40,32,2,'#FFF8E1')+P('M8 22q6 8 12 0q6 8 12 0q6 8 12 0q6 8 12 0','#FF9A76')+R(26,34,12,20,2,'#C99A62'))
ic('trophy',P('M18 8h28v16q0 14-14 16-14-2-14-16z','#FFC83D')+P('M18 12q-10 0-8 10 2 8 10 8M46 12q10 0 8 10-2 8-10 8','none')+R(28,40,8,8,1,'#E0A800')+R(18,48,28,8,3,'#8B5E3C'))
ic('bell',P('M32 8q-16 0-16 20v8l-5 8h42l-5-8v-8q0-20-16-20z','#FFC83D')+C(32,52,5,'#E0A800')+P('M32 4v4','none'))
ic('save',R(10,10,44,44,6,'#3D7EC9')+R(18,10,28,16,2,'#FFF8E1')+R(18,34,28,20,3,'#C9D8F0'))
ic('speaker',P('M10 24h10l14-12v40L20 40H10z','#FFC83D')+P('M42 22q8 10 0 20M48 14q14 18 0 36','none','stroke="#3D7EC9"'))
hp='M32 54L10 30q-6-14 8-18 10-2 14 8 4-10 14-8 14 4 8 18z'
ic('heart',P(hp,'#E5533D'));ic('heart_off',P(hp,'#C9C2B4'))
ic('coin',C(32,32,22,'#FFC83D')+C(32,32,14,'#FFE07A','stroke="#E0A800" stroke-width="3"')+P('M32 24v16M27 29h10','none','stroke="#E0A800" stroke-width="4"'))
ic('star',P('M32 6l8 18 20 2-15 13 5 19-18-10-18 10 5-19L4 26l20-2z','#FFC83D'))
ic('unknown',E(32,34,20,24,'#E4D9C0')+P('M26 26q0-8 8-8t6 8q-2 6-8 8v4','none','stroke="#8B7B5E" stroke-width="5"')+C(32,50,2,'#8B7B5E'))
ic('medal',P('M18 6l8 20h12l8-20','#E5533D')+C(32,38,18,'#FFC83D')+P('M32 28l3 7 8 1-6 5 2 8-7-4-7 4 2-8-6-5 8-1z','#FFF3B0','stroke-width="2"'))
ic('medal_off',P('M18 6l8 20h12l8-20','#C9C2B4')+C(32,38,18,'#E4DED0'))
ic('chest',R(8,26,48,28,4,'#C99A62')+P('M8 30q0-18 24-18t24 18z','#B07A44')+R(26,30,12,12,2,'#FFC83D')+P('M8 38h48','none','stroke="#8B5E3C" stroke-width="3"'))
w('icons/bubble',G(P('M8 8h64a6 6 0 0 1 6 6v28a6 6 0 0 1-6 6H44l-10 12v-12H8a6 6 0 0 1-6-6V14a6 6 0 0 1 6-6z','#FFFDF6')),'0 0 80 72')
# ---------- fx / scene ----------
w('fx/slash',P('M6 6Q70 20 122 122Q60 50 6 6z','#fff','stroke="#E5533D" stroke-width="5"'),css='path{animation:s .4s ease-out}@keyframes s{from{opacity:0;transform:scale(.4)}}')
w('fx/claw',''.join(P(f'M{x} 10q-14 50 6 108q6-60-6-108z','#E5533D','stroke="#fff" stroke-width="3"') for x in(30,64,98)))
w('fx/burst',P('M64 4l12 34 36-10-20 30 28 22-36 0-4 36-16-32-30 20 10-34-30-14 34-8z','#FFC83D','stroke="#fff" stroke-width="4"'))
w('fx/rays',''.join(P(f'M200 200L{200+400*__import__("math").cos(a*__import__("math").pi/9):.0f} {200+400*__import__("math").sin(a*__import__("math").pi/9):.0f}L{200+400*__import__("math").cos((a+.5)*__import__("math").pi/9):.0f} {200+400*__import__("math").sin((a+.5)*__import__("math").pi/9):.0f}z','#FFE9A0','opacity=".55"') for a in range(18)),'0 0 400 400')
w('scene/grass_tile',R(0,0,64,64,0,'#7BC043')+R(0,0,64,32,0,'#85C94C')+''.join(P(f'M{x} {y}l2-8 2 8M{x+4} {y}l3-6 1 6','none','stroke="#4E9C3F" stroke-width="2" stroke-linecap="round"') for x,y in((8,20),(40,12),(24,50),(52,44),(10,58))),'0 0 64 64')
w('scene/soil_tile',R(0,0,64,64,0,'#8B5E3C')+''.join(P(f'M0 {y}q16-6 32 0t32 0','none','stroke="#6B4423" stroke-width="4"') for y in(12,32,52)),'0 0 64 64')
w('scene/path_tile',R(0,0,96,40,0,'none')+''.join(E(x,y,rx,12,'#D8D2C4','stroke="#A89F8C" stroke-width="3"') for x,y,rx in((16,12,15),(46,22,16),(78,12,14),(30,32,13),(64,34,13),(92,30,10))),'0 0 96 40')
w('scene/fence_tile',R(0,16,48,6,2,'#C99A62','stroke="#8B5E3C" stroke-width="3"')+R(0,28,48,6,2,'#C99A62','stroke="#8B5E3C" stroke-width="3"')+R(18,6,12,34,3,'#D9A66E','stroke="#8B5E3C" stroke-width="3"'),'0 0 48 44')
fl=lambda x,c:P(f'M{x} 40v-14','none','stroke="#4E9C3F" stroke-width="3"')+''.join(C(x+dx,24+dy,4,c) for dx,dy in((0,-5),(5,0),(0,5),(-5,0)))+C(x,24,3,'#FFC83D')
w('scene/meadow',''.join(fl(x,c) for x,c in((14,'#fff'),(52,'#FF9AB8'),(94,'#FFD84D'),(132,'#fff'))),'0 0 160 44')
def cloud(x,y,s=1):return f'<g transform="translate({x} {y}) scale({s})" fill="#fff" opacity=".9" style="animation:dr 40s linear infinite alternate">'+C(0,0,14,'#fff')+C(16,-6,18,'#fff')+C(34,0,14,'#fff')+'</g>'
scene=(f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD3F4"/><stop offset="1" stop-color="#D6F0FA"/></linearGradient></defs><rect width="800" height="300" fill="url(#sk)"/>'
 +cloud(120,50)+cloud(520,36,1.2)+'<path d="M0 170q150-80 300-20t300-30q120-30 200 20v160H0z" fill="#9BD66E"/><path d="M0 200q200-50 400-10t400-20v130H0z" fill="#7BC043"/>'
 +'<g transform="translate(70 70) scale(1.5)">'+house()+'</g><g transform="translate(560 84) scale(1.3)">'+barn()+'</g><g transform="translate(676 90) scale(.95)">'+windmill()+'</g>'
 +'<g transform="translate(250 130) scale(1.1)">'+tree()+'</g><g transform="translate(490 150) scale(.9)">'+tree('#5FC06A','#46A653')+'</g>'
 +'<ellipse cx="330" cy="236" rx="90" ry="28" fill="#5BB6E6" stroke="#3D8FC0" stroke-width="5"/><ellipse cx="316" cy="232" rx="30" ry="6" fill="#fff" opacity=".4"/><ellipse cx="360" cy="240" rx="10" ry="5" fill="#4FA34A"/>'
 +'<ellipse cx="330" cy="236" rx="60" ry="16" fill="none" stroke="#fff" stroke-width="2" opacity=".5" style="animation:rp 3s ease-out infinite"/>'
 +'<path d="M120 300q40-40 100-50" fill="none" stroke="#D8D2C4" stroke-width="22" stroke-linecap="round" stroke-dasharray="16 8"/>'
 +'<g transform="translate(14 268)">'+''.join(f'<g transform="translate({i*48} 0) scale(1)">'+R(0,16,48,6,2,'#C99A62','stroke="#8B5E3C" stroke-width="3"')+R(18,6,12,34,3,'#D9A66E','stroke="#8B5E3C" stroke-width="3"')+'</g>' for i in range(16))+'</g>')
w('scene/farm_top',scene,'0 0 800 320','@keyframes dr{to{transform:translateX(40px)}}@keyframes rp{from{transform:scale(.6);opacity:.8}to{transform:scale(1.15);opacity:0}}ellipse[style]{transform-origin:50% 50%}')
print('assets ok',sum(len(f) for _,_,f in os.walk(O+'/assets')))
