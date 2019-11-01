import argparse
import localsystem as locsys

def get_args():
    """ Create CLI Commands """

    about = """localhost is a python based automation commandline tools that make system task easy"""
    parser = argparse.ArgumentParser(description=about, prog="localhost")

#sample argument
    parser.add_argument(
            "-v",
            "--version",
            help="""Please Check the Version.""",
            )

#Main Function
def main ():
    """
    Main logic of script
    """
    version=locsys.getversion()
    print("version is "+version)




if __name__ == "__main__":
    main()