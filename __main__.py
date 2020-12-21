from src import ColorSwitchGui, ColorSwitchEnvironment

def main():
    env = ColorSwitchEnvironment()
    gui = ColorSwitchGui(env)
    gui.run()

if __name__ == "__main__":
    main()