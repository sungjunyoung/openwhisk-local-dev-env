import argparse

def parse_args():
    desc = "deploy openwhisk function."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--name', type=str, required=True,
                        help='function name')
    return parser.parse_args()


def main():
    args = parse_args()
    print(args)


if __name__ == '__main__':
    main()
