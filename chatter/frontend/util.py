import subprocess

def get_screen_resolution():
    xrandr = subprocess.Popen(['xrandr'],
                              stdout=subprocess.PIPE)
    def star_filter(line):
        if '*' in line:
            return line
    def x_filter(line):
        if 'x' in line:
            return line
    return filter(x_filter,
                 filter(star_filter, 
                        xrandr.communicate()[0].split('\n'))[0].split()
                 )[0].split('x')

