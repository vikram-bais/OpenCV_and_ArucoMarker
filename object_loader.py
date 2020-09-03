class OBJ:
    def __init__(self,filename,swapyz=False):
        self.vertices=[]
        self.normals=[]
        self.texcoords=[]
        self.faces=[]
        material=None
        for line in open(filename,'r'):
            if line.startswith('#'):
                continue
            values=line.split()
            if not values:
                continue
            if values[0]=='v':
                v=list(map(float,values[1:4]))
                if swapyz:
                    v=v[0],v[2],v[1]
                self.vertices.append(v)
            elif values[0]=='vn':
                v=list(map(float,values[1:4]))
                if swapyz:
                    v=v[0],v[2],v[1]
                self.normals.append(v)
            elif values[0]=='vt':
                v=values[1:4]
                self.texcoords.append(v)

            elif values[0]=='f':
                face=[]
                texcoords=[]
                norms=[]
                for v in values[1:]:
                    w=v.split('/')
                    face.append(int(w[0]))
                    if len(w)>=2 and len(w[1])>0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w)>=3 and len(w[2])>0:
                        norms.append(w[2])
                    else:
                        norms.append(0)
                    self.faces.append((face,norms,texcoords))


