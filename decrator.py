def name(bajarangi):
    def ram():
        print("sri")
        bajarangi()
        print("today")
    return ram
@name
def bajarangi():
    print("tomarroe")
bajarangi()