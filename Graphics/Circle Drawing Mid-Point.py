import matplotlib.pyplot as plt

def midPointCircleDraw(x_centre, y_centre, r):
    px=[]
    py=[]
    x = r
    y = 0
      
    # Printing the initial point the 
    # axes after translation 
    print("(", x + x_centre, ", ", 
               y + y_centre, ")", 
               sep = "", end = "") 
      
    # When radius is zero only a single 
    # point be printed 
    if (r > 0) :
      
        print("(", x + x_centre, ", ",
                  -y + y_centre, ")", 
                  sep = "", end = "")

        print("(", y + x_centre, ", ", 
                   x + y_centre, ")",
                   sep = "", end = "")

        print("(", -y + x_centre, ", ", 
                    x + y_centre, ")", sep = "") 
      
    # Initialising the value of P 
    P = 1 - r 
  
    while x > y:
      
        y += 1
          
        # Mid-point inside or on the perimeter
        if P <= 0: 
            P = P + 2 * y + 1
              
        # Mid-point outside the perimeter 
        else:         
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        # All the perimeter points have 
        # already been printed 
        if (x < y):
            break
          
        # Printing the generated point its reflection 
        # in the other octants after translation 
        print("(", x + x_centre, ", ", y + y_centre,
                            ")", sep = "", end = "")
        # plt.scatter(x+x_centre, y+y_centre)
        px.append(x+x_centre)
        py.append(y+y_centre)
        print("(", -x + x_centre, ", ", y + y_centre, 
                             ")", sep = "", end = "") 
        # plt.scatter(-x+x_centre,y + y_centre)
        px.append(-x+x_centre)
        py.append(y+y_centre)
        print("(", x + x_centre, ", ", -y + y_centre,
                             ")", sep = "", end = "")
        # plt.scatter(x+x_centre,-y+y_centre)
        px.append(x+x_centre)
        py.append(-y+y_centre)
        print("(", -x + x_centre, ", ", -y + y_centre,
                                        ")", sep = "")
        # plt.scatter(-x+x_centre,-y+y_centre)
        px.append(-x+x_centre)
        py.append(-y+y_centre)
          
        # If the generated point on the line x = y then 
        # the perimeter points have already been printed 
        if x != y:
          
            print("(", y + x_centre, ", ", x + y_centre, 
                                ")", sep = "", end = "")
            px.append(y+x_centre)
            py.append(x+y_centre)
            print("(", -y + x_centre, ", ", x + y_centre,
                                 ")", sep = "", end = "")
            px.append(-y+x_centre)
            py.append(x+y_centre)
            print("(", y + x_centre, ", ", -x + y_centre,
                                 ")", sep = "", end = "") 
            px.append(y+x_centre)
            py.append(-x+y_centre)
            print("(", -y + x_centre, ", ", -x + y_centre, 
                                            ")", sep = "")
            px.append(-y+x_centre)
            py.append(-x+y_centre)
        
    plt.scatter(px, py)
    plt.show()
        
                              
# Driver Code
if __name__ == '__main__':
      
    # To draw a circle of radius 4
    # centred at (0, 0) 
    midPointCircleDraw(30,50, 8)