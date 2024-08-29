
import random as rand
import MathLib as m


def flat(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    #Light model 
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def rainbow (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= rand.random()
        g *= rand.random()
        r *= rand.random()
        

    triangleNormal = ([nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def zebra (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs['normals']
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]
    
    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)

    #Light model 
    intensity = m.dotProduct(triangleNormal, dirLight)


    if intensity > 0.90:
        r, g, b =  (0,0,0)
    elif intensity > 0.80:
           r, g, b =  (1,1,1)
    elif intensity > 0.70:
           r, g, b =  (0,0,0)
    elif intensity > 0.60:
           r, g, b =  (1,1,1)
    elif intensity > 0.50:
           r, g, b =  (0,0,0)
    elif intensity > 0.40:
           r, g, b =  (1,1,1)
    elif intensity > 0.30:
           r, g, b =  (0,0,0)
    elif intensity > 0.20:
       r, g, b =  (1,1,1)
    elif intensity > 0.10:
        r, g, b = (0,0,0)
    elif intensity > 0.05:
        r, g, b = (1,1,1)
    elif intensity > 0.06:
        r, g, b = (0,0,0)
    elif intensity > 0.01:
        r, g, b = (1,1,1)

    b *= intensity 
    g *= intensity 
    r *= intensity 

    if b > 1: r =1
    if r > 1: g =1
    if g > 1: b =1
    
    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def degraded (render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs['normals']
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]
    
    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)
    intensity = m.dotProduct(triangleNormal, dirLight)
    
    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.7:
        intensity = 0.6
    elif intensity < 0.9:
        intensity = 0.8
    elif intensity < 0.94:
        intensity = 0.9
    elif intensity <= 1:
        intensity = 1

    
    g += intensity * 0.5
    r += intensity * 0.5
    b += intensity * 0.3

    if b > 1: b=1
    if r > 1: r=1
    if g > 1: g=1
    
    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def gourad(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    nx = nA[0] * u + nB[0] * v + nC[0] * w
    ny = nA[1] * u + nB[1] * v + nC[1] * w
    nz = nA[2] * u + nB[2] * v + nC[2] * w
    
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]

    triangleNormal = (nx, ny, nz)


    intensity = m.dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def light(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    #Texture Shader 
    if render.active_texture:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    #Light model 
    dirLight = [-render.dirLight [0],
                -render.dirLight [1],
                -render.dirLight [2]]
    intensity = m.dotProduct(triangleNormal, dirLight)

    white = [1,1,1]
    b += intensity * white[0]
    g += intensity * white[1]
    r += intensity * white[2]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def vertexShader(vertex, **kwargs):
    # Se lleva a cabo por cada vertice
    
    # Recibimos las matrices
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    viewportMatrix = kwargs["viewportMatrix"]
    
    # Agregamos un componente W al vertice
    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    
    # Transformamos el vertices por todas las matrices en el orden correcto
    vt = viewportMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt
    
    vt = vt.tolist()[0]
    
    # Dividimos x,y,z por w para regresar el vertices a un tama�o de 3
    vt = [vt[0] / vt[3],
          vt[1] / vt[3],
          vt[2] / vt[3]]
    
    return vt


def fragmentShader(**kwargs):
    # Se lleva a cabo por cada pixel individual
    
    # Obtenemos la informacion requerida
    A, B, C = kwargs["verts"]
    u, v, w = kwargs["bCoords"]
    
    
    # Empezamos siempre con color blanco
    r = 1
    g = 1
    b = 1
    
    # Para el proposito de mostrar las coordenadas de textura
    # en accion, las usamos para el color
    r *= u
    g *= v
    b *= w
        
    # Se regresa el color
    return [r,g,b]
