def copy(source,target,targX,targY):
  targetX=targX
  for sourceX in range(0,getWidth(source)):
    targetY=targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY+1
    targetX=targetX+1
  show(target)
  show(source)
  return(target)
    
def copyHorse():
  file=pickAFile()
  src=makePicture(file)
  canvas=makeEmptyPicture(1000,1000)
  targetX=0
  for sourceX in range(0,getWidth(src)):
   targetY=0
   for sourceY in range(0,getHeight(src)):
      color=getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY=targetY+1
   targetX=targetX+1
  show(src)
  show(canvas)
  return canvas
#target=makeEmptyPicture(500,500)
#file=pickAFile()
#source=makePicture(file)
