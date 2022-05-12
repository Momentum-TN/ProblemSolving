'''
Draws a window with two n*n-sized panes

e.g:
- n = 3:
---------
|...|...|
|...|...|
|...|...|
|---+---|
|...|...|
|...|...|
|...|...|
---------

- n = 5:
-------------
|.....|.....|
|.....|.....|
|.....|.....|
|.....|.....|
|.....|.....|
|-----+-----|
|.....|.....|
|.....|.....|
|.....|.....|
|.....|.....|
|.....|.....|
-------------
'''
def window():
    # pane length
    n = int(input())

    # window head and footer
    top = "-" * (n*2+3)
    
    # construct window pane lines (window upper half)
    for i in range(n):
        dots=""
        for j in range(n):
            dots+="."
        lines += "|" + dots +"|" + dots + "|\n"
    
    # add middle separator
    middle = "|" + "-" * n + "+" + "-" * n + "|\n"
    
    # combine components
    window += top+ "\n" + lines + middle + lines + top
    
    print(window)

if __name__ == '__main__':
    window()
