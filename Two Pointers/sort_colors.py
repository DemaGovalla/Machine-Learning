def sort_colors(colors):

    red = 0
    # print(red)

    white = 0
    # print(white)

    blue = len(colors)-1
    # print(blue)

    while white <= blue:
        if colors[white] == 0: 
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            white += 1
            red +=1
     
        elif colors[white] == 1:
            white += 1

        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]

            blue -=1




    return colors


def main():

    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]
    
    for i in range(len(inputs)):
        print(i + 1, "\tcolors:", inputs[i].copy(), 
              "\n\n\tThe sorted array is:", sort_colors(inputs[i]))
        print("-"*100)
    # print(sorted_colors)

if __name__ == "__main__":
    main()