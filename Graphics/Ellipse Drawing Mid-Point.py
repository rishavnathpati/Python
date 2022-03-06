import matplotlib.pyplot as plt
def midptellipse(rx, ry, xc, yc):
    px=[]
    py=[]
    x = 0;
    y = ry;

    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +
                    (0.25 * rx * rx));
    dx = 2 * ry * ry * x;
    dy = 2 * rx * rx * y;

    # For region 1
    while (dx < dy):

        # Print points based on 4-way symmetry
        print("(", x + xc, ",", y + yc, ")");
        px.append(x+xc)
        py.append(y+yc)
        print("(",-x + xc,",", y + yc, ")");
        px.append(-x+xc)
        py.append(y+yc)
        print("(",x + xc,",", -y + yc ,")");
        px.append(x+xc)
        py.append(-y+yc)
        print("(",-x + xc, ",", -y + yc, ")");
        px.append(-x+xc)
        py.append(-y+yc)

        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1;
            dx = dx + (2 * ry * ry);
            d1 = d1 + dx + (ry * ry);
        else:
            x += 1;
            y -= 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            d1 = d1 + dx - dy + (ry * ry);

    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
        ((rx * rx) * ((y - 1) * (y - 1))) -
        (rx * rx * ry * ry));

    # Plotting points of region 2
    while (y >= 0):

        # printing points based on 4-way symmetry
        print("(", x + xc, ",", y + yc, ")");
        px.append(x+xc)
        py.append(y+yc)
        print("(", -x + xc, ",", y + yc, ")");
        px.append(-x+xc)
        py.append(y+yc)
        print("(", x + xc, ",", -y + yc, ")");
        px.append(x+xc)
        py.append(-y+yc)
        print("(", -x + xc, ",", -y + yc, ")");
        px.append(-x+xc)
        py.append(-y+yc)

        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1;
            dy = dy - (2 * rx * rx);
            d2 = d2 + (rx * rx) - dy;

        else:
            y -= 1;
            x += 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            d2 = d2 + dx - dy + (rx * rx);
    # plt.figure(figsize=(10,15))
    # plt.scatter(px,py)
    # plt.show()

midptellipse(4, 7, 0, 0)
