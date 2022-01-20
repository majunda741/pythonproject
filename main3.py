from majorCode import majorcode
import scrcpy

if __name__ == '__main__':
    d = scrcpy.Client(device="7XBRX19307009255")
    print()
    d.start(threaded=True)
    d.control.swipe(800, 100, 0.1, 100)
    # d.control.touch(1000, 1000, 0, 0)
    # d.control.touch(900, 1000, 2, 0)
    # d.control.touch(800, 1000, 2, 0)
    # d.control.touch(700, 1000, 2, 0)
    # d.control.touch(600, 1000, 2, 1)
    # d.control.touch(500, 1000, 2, 1)
    # d.control.touch(400, 1000, 2, 1)
    # d.control.touch(300, 1000, 2, 1)
    # d.control.touch(200, 1000, 2, 1)
    # d.control.touch(100, 1000, 2, 1)
    # d.control.touch(100, 900, 2, 1)
    # d.control.touch(100, 800, 2, 1)
    # d.control.touch(100, 700, 2, 1)
    # d.control.touch(100, 600, 2, 1)
    # d.control.touch(100, 500, 2, 1)
    # d.control.touch(100, 400, 2, 1)
    # d.control.touch(100, 300, 2, 1)
    # d.control.touch(100, 200, 2, 1)
    # d.control.touch(100, 100, 1, 1)
    # d.stop()

