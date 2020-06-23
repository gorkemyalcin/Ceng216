import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
def plotCurve(x1,x2,x3,x4,y1,y2,y3,y4):
    verts = [
    (x1, y1),  # P0
    (x2, y2), # P1
    (x3, y3), # P2
    (x4, y4), # P3
    ]

    codes = [Path.MOVETO,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4,
         ]

    path = Path(verts, codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='none', lw=2)
    ax.add_patch(patch)

    xs, ys = zip(*verts)
    ax.plot(xs, ys, 'x--', lw=2, color='black', ms=10)

    ax.text(verts[0][0]+0.5, verts[0][1]+0.5, 'P0')
    ax.text(verts[1][0]+0.5, verts[1][1]+0.5, 'P1')
    ax.text(verts[2][0]+0.5, verts[2][1]+0.5, 'P2')
    ax.text(verts[3][0]+0.5, verts[3][1]+0.5, 'P3')

    ax.set_xlim(-5, 20)
    ax.set_ylim(-5, 20)
    plt.show()
    
file_name="ceng216_hw02_bezier2svg"
f=open(file_name+".txt","r")
all_lines=f.readlines()
number_of_lines=len(all_lines)

bfile=open("bezier.svg","w+")
bfile=open("bezier.svg","a")
bfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
bfile.write('<!-- Created with Inkscape (http://www.inkscape.org/) -->\n')
bfile.write('\n<svg \n')
bfile.write('\txmlns:dc="http://purl.org/dc/elements/1.1/"\n')
bfile.write('\txmlns:cc="http://creativecommons.org/ns#"\n')
bfile.write('\txmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
bfile.write('\txmlns:svg="http://www.w3.org/2000/svg"\n')
bfile.write('\txmlns="http://www.w3.org/2000/svg"\n')
bfile.write('\txmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n')
bfile.write('\txmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n')
bfile.write('\twidth="210mm"\n')
bfile.write('\theight="297mm"\n')
bfile.write('\tviewBox="0 0 210 297"\n')
bfile.write('\tversion="1.1"\n')
bfile.write('\tid="svg3727"\n')
bfile.write('\tinkscape:version="0.92.3 (2405546, 2018-03-11)"\n')
bfile.write('\tsodipodi:docname="drawing.svg">\n')
bfile.write('  <defs \n')
bfile.write('\t id="defs3721" />\n')
bfile.write('  <sodipodi:namedview\n')
bfile.write('\tid="base"\n')
bfile.write('\tpagecolor="#ffffff"\n')
bfile.write('\tbordercolor="#666666"\n')
bfile.write('\tborderopacity="1.0"\n')
bfile.write('\tinkscape:pageopacity="0.0"\n')
bfile.write('\tinkscape:pageshadow="2"\n')
bfile.write('\tinkscape:zoom="0.35"\n')
bfile.write('\tinkscape:cx="400"\n')
bfile.write('\tinkscape:cy="560"\n')
bfile.write('\tinkscape:document-units="mm"\n')
bfile.write('\tinkscape:current-layer="layer1"\n')
bfile.write('\tshowgrid="false"\n')
bfile.write('\tinkscape:window-width="1920"\n')
bfile.write('\tinkscape:window-height="1001"\n')
bfile.write('\tinkscape:window-x="-9"\n')
bfile.write('\tinkscape:window-y="-9"\n')
bfile.write('\tinkscape:window-maximized="1" />\n')
bfile.write('  <metadata\n')
bfile.write('\tid="metadata3724">\n')
bfile.write('\t<rdf:RDF>\n')
bfile.write('\t  <cc:Work\n')
bfile.write('\t\t rdf:about="">\n')
bfile.write('\t\t<dc:format>image/svg+xml</dc:format>\n')
bfile.write('\t\t<dc:type\n')
bfile.write('\t\t   rdf:resource="http://purl.org/dc/dcmitype/StillImage" />\n')
bfile.write('\t\t<dc:title></dc:title>\n')
bfile.write('\t  </cc:Work>\n')
bfile.write('\t</rdf:RDF>\n')
bfile.write('  </metadata>\n')
bfile.write('  <g\n')
bfile.write('\t inkscape:label="Layer 1"\n')
bfile.write('\t inkscape:groupmode="layer"\n')
bfile.write('\t id="layer1">\n')
for line in all_lines:
    line=line.split(" ")
    if len(line)==8:
        coor=[]
        for i in range(8):
            line[i]=line[i].strip("\n")
            if (line[i][-4:]=="_x1>" or line[i][-4:]=="_x2>" or line[i][-4:]=="_x3>" or line[i][-4:]=="_x4>" or line[i][-4:]=="_y1>" or line[i][-4:]=="_y2>" or line[i][-4:]=="_y3>" or line[i][-4:]=="_y4>") and line[i][0]=="<":
                coor.append(line[i].strip("<>").split("_"))
    x1=int(coor[0][0])
    y1=int(coor[1][0])
    x2=int(coor[2][0])
    y2=int(coor[3][0])
    x3=int(coor[4][0])
    y3=int(coor[5][0])
    x4=int(coor[6][0])
    y4=int(coor[7][0])
    bfile.write('\t<path\n')
    bfile.write('\t   style="fill:none;stroke:#000000;stroke-width:0.26458332px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"\n')
    bfile.write('\t   d="M'+str(x1)+' '+str(y1)+' C '+str(x2)+' '+str(y2)+', '+str(x3)+' '+str(y3)+', '+str(x4)+' '+str(y4)+'" stroke="black" /\n')
    bfile.write('\t   id="path3729"\n')
    bfile.write('\t   inkscape:connector-curvature="0" />"\n')
bfile.write('  </g>\n')
bfile.write("</svg>")
bfile.close()
f.close()


