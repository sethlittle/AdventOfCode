# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

# SOLUTION
def getWrappingPaperNeeded(dimensions):
    dimensions = dimensions.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face.
# Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.
# For example:
#     A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#     A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# How many total feet of ribbon should they order?

# SOLUTION
def getRibbonNeeded(dimensions):
    dimensions = dimensions.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    return min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h

# SOLUTION
def getWrappingPaperAndRibbonNeeded(dimensions):
    return getWrappingPaperNeeded(dimensions) + getRibbonNeeded(dimensions)

# TESTS
def test():
    assert getWrappingPaperNeeded('2x3x4') == 58
    assert getWrappingPaperNeeded('1x1x10') == 43
    assert getRibbonNeeded('2x3x4') == 34
    assert getRibbonNeeded('1x1x10') == 14
    assert getWrappingPaperAndRibbonNeeded('2x3x4') == 92
    assert getWrappingPaperAndRibbonNeeded('1x1x10') == 57

# MAIN
def main():
    test()
    input = open('inputFile.txt', 'r')
    lines = input.readlines()
    wrappingPaperNeeded = 0
    ribbonNeeded = 0
    for line in lines:
        wrappingPaperNeeded += getWrappingPaperNeeded(line.strip())
        ribbonNeeded += getRibbonNeeded(line.strip())
    print('Wrapping paper needed: ' + str(wrappingPaperNeeded))
    print('Ribbon needed: ' + str(ribbonNeeded))
    print('Wrapping paper and ribbon needed: ' + str(wrappingPaperNeeded + ribbonNeeded))

if __name__ == '__main__':
    main()

# SOLUTION
# Wrapping paper needed: 1598415
# Ribbon needed: 3812909
# Wrapping paper and ribbon needed: 5411324

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/2