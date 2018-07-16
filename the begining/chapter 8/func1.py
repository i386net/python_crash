# func declaration from if
color = input('Enter color: ')

if color == 'red':
    def color_declaration(color):
        print('User selected %s color. That is cool' % color)
        return '%s ' % (color.upper()*4)
else:
    def color_declaration(color):
        print('User selected the wrong color! What a fool!')
        return color

make_up_color = color_declaration(color)
print(make_up_color)